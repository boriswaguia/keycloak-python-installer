#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import wget

from keycloak_python_installer.skeleton import download
from keycloak_python_installer.skeleton import build_download_url

def test_build_download_url_with_no_version_should_raise_exception():
        with pytest.raises(ValueError):
                build_download_url(None, 'zip')

def test_build_download_url_with_invalid_version_should_raise_valueerror():
        with pytest.raises(ValueError):
                build_download_url('ab','zip')

def test_build_download_url_with_no_format_should_raise_valueerror():
        with pytest.raises(ValueError):
                build_download_url('5.0.0', None)

def test_build_download_url_with_invalid_format_should_raise_valueerror():
        with pytest.raises(ValueError):
                build_download_url('5.0.0','123')


def test_build_download_url_should_be_valid():
        keycloak_version = '5.0.0'
        keycloak_download_format = 'zip'
        assert build_download_url(keycloak_version, keycloak_download_format) == 'https://downloads.jboss.org/keycloak/5.0.0/keycloak-5.0.0.zip'


def test_download_with_valid_format_should_return_True(mocker):
        keycloak_version = '5.0.0'
        mocker.patch('wget.download')
        downloaded = download(keycloak_version)
        wget.download.assert_called_once_with('https://downloads.jboss.org/keycloak/5.0.0/keycloak-5.0.0.zip')
        assert downloaded == True
