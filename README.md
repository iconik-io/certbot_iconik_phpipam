# iconik Phpipam DNS Authenticator for Certbot

This allows automatic completion of `Certbot's <https://github.com/certbot/certbot>`_
DNS01 challange for domains managed via `Phpipam <https://phpipam.net/>`_ DNS.

## iconik phpipam customization

:warning:

This plugin is built for the internal use at iconik. Our phpipam
instance has a custom field on each address called `acme_challenge`
which gets propagated to our DNS as an entry called
`_acme-challenge.$HOSTNAME` and this plugin simply updates this
field. If your phpipam setup doesn't have anything similar this plugin
is likely going to be of limited use to you.

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
iconik_phpipam_username = admin
iconik_phpipam_password = password
iconik_phpipam_endpoint = https://phpipam
iconik_phpipam_appid = app_id
iconik_phpipam_verify = True
```

For safety reasons the file must not be world readable. You can solve this by
running:

```
$ chmod 600 credentials.ini
```

Then you can run `certbot` using:

```
$ sudo certbot certonly \
    --authenticator iconik-phpipam \
    --iconik-phpipam-credentials credentials.ini \
    -d domain.com
```

## Attribution

This plugin is based on https://github.com/runfalk/certbot-loopia by Andreas Runfalk

## Changelog

### Version 0.1.0

Released 2021-09-21

* Initial Release
