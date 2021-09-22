import logging
import itertools
import re
import zope.interface

from certbot.plugins.dns_common import DNSAuthenticator
from certbot.interfaces import IAuthenticator, IPluginFactory
from datetime import datetime, timedelta
from time import sleep

import phpypam


logger = logging.getLogger(__name__)


def as_bool(obj):
    if isinstance(obj, str):
        obj = obj.strip().lower()
        if obj in ['True', 'true', 'yes', 'on', 'y', 't', '1']:
            return True
        elif obj in ['False', 'false', 'no', 'off', 'n', 'f', '0']:
            return False
        else:
            raise ValueError("String is not true/false: %r" % obj)
    return bool(obj)


@zope.interface.implementer(IAuthenticator)
@zope.interface.provider(IPluginFactory)
class PhpipamAuthenticator(DNSAuthenticator):
    """
    Phpipam DNS ACME authenticator.

    This Authenticator uses the Phpipam REST API to fulfill a dns-01 challenge.
    """

    #: Short description of plugin
    description = __doc__.strip().split("\n", 1)[0]

    #: TTL for the validation TXT record
    ttl = 30

    def __init__(self, *args, **kwargs):
        super(PhpipamAuthenticator, self).__init__(*args, **kwargs)
        self._client = None
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add, default_propagation_seconds=90):
        super(PhpipamAuthenticator, cls).add_parser_arguments(
            add, default_propagation_seconds)
        add("credentials", help="Phpipam credentials INI file.")


    def more_info(self):
        """
        More in-depth description of the plugin.
        """

        return "\n".join(line[4:] for line in __doc__.strip().split("\n"))

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            "credentials",
            "Phpipam credentials INI file",
            {
                "endpoint": "Api endpoint",
                "username": "API username for Phpipam account",
                "password": "API password for Phpipam account",
                "appid": "API app id for Phpipam account"
            }
        )

    def _get_phpipam_client(self):
        verify = self.credentials.conf("verify")

        # Default verify to True
        if verify is None:
            verify = True

        return PhpipamClient(
            self.credentials.conf("endpoint"),
            self.credentials.conf("username"),
            self.credentials.conf("password"),
            self.credentials.conf("appid"),
            as_bool(verify)
        )

    def _perform(self, domain, validation_name, validation):
        phpipam = self._get_phpipam_client()
        phpipam.add_txt_record(validation_name, validation, ttl=self.ttl)

    def _cleanup(self, domain, validation_name, validation):
        phpipam = self._get_phpipam_client()
        phpipam.remove_record(validation_name)


class PhpipamClient:
    """
    Encapsulates the communication with phpipam
    """

    def __init__(self, endpoint, username, password, appid, verify):
        self._client = phpypam.api(
            url=endpoint,
            app_id=appid,
            username=username,
            password=password,
            ssl_verify=verify
        )

    def get_hostname(self, name):
        if name.startswith('_acme-challenge.'):
            return name[16:]
        return name


    def lookup_rr(self, name):
        hostname = self.get_hostname(name)
        addresses = self._client.get_entity(controller='addresses', controller_path=f"search_hostname/{hostname}")
        if not addresses:
            raise Exception(f"Could not find phpipam entry for {name}")

        return addresses[0]

    def remove_record(self, name):
        rr = self.lookup_rr(name)
        if rr:
            self._client.update_entity(controller='addresses', controller_path=rr['id'], data={'custom_acme_challenge': ''})

    def add_txt_record(self, validation_name, validation, ttl=30):
        rr = self.lookup_rr(validation_name)
        self._client.update_entity(controller='addresses', controller_path=rr['id'], data={'custom_acme_challenge': validation})
