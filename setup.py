from setuptools import setup


try:
    long_desc = open("README.md").read()
except:
    print("Skipping README.md for long description as it was not found")
    long_desc = None

setup(
    name="certbot-iconik-phpipam",
    version="0.1.0",
    description="phpipam DNS authentication plugin for Certbot (iconik internal)",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Mattias Amnefelt",
    author_email="mattiasa@iconik.io",
    url="https://www.github.com/iconik-io/certbot-iconik-ipam",
    py_modules=["certbot_iconik_phpipam"],
    install_requires=[
        "acme>=1.4.0",
        "certbot>=1.4.0",
        "phpypam>=1.0.0"
    ],
    entry_points={
        "certbot.plugins": [
            "iconik-phpipam = certbot_iconik_phpipam:PhpipamAuthenticator",
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
)
