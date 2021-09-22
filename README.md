# iconik Phpipam DNS Authenticator for Certbot

This allows automatic completion of `Certbot's <https://github.com/certbot/certbot>`_
DNS01 challange for domains managed via `Phpipam <https://phpipam.net/>`_ DNS.

## Installing

```
$ sudo pip install git+https://github.com/iconik-io/certbot_iconik_phpipam
```

Note that you should normally install this as ``root``, unless you know what
you are doing.

## Usage

The plugin requires a user with the edit, view and delete permissions for the DNS zone you
are creating a certificate in.

To use the plugin you need to provide a credentials file

`--certbot-iconik-phpipam:credentials` *(required)*
  INI file with ``username`` and ``password`` for your Phpipam user as well as the endpoint
  URL for your phpipam instance. You can also provide the `verify` flag to disable certificate
  verification of the phpipam server. This should of course only be used when you want to generate
  the certificate for your phpipam server itself :)

The credentials file must have the following format:

```
certbot_iconik_phpipam:auth_username = admin
certbot_iconik_phpipam:auth_password = password
certbot_iconik_phpipam:auth_endpoint = https://phpipam/iconik_phpipam
certbot_iconik_phpipam:api_id = app_id
certbot_iconik_phpipam:auth_verify = True
```

For safety reasons the file must not be world readable. You can solve this by
running:

```
$ chmod 600 credentials.ini
```

Then you can run `certbot` using:

```
$ sudo certbot certonly \
    --authenticator certbot-iconik-phpipam:auth \
    --certbot-iconik-phpipam:auth-credentials credentials.ini \
    -d domain.com
```

## Attribution

This plugin is based on https://github.com/runfalk/certbot-loopia by Andreas Runfalk

## Changelog

### Version 0.1.0

Released 2021-09-21

* Initial Release
