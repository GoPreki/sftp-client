#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="sftp-client",
    version="1.0.0",
    author="Preki",
    author_email="ramos@gopreki.com",
    packages=['sftp_client'],
    url='https://gopreki.com',
    download_url="https://github.com/GoPreki/sftp-client",
    license="MIT",
    description="Python library for Preki sftp connection",
    long_description="Python library for Preki sftp connection",
    install_requires=["paramiko"],
)
