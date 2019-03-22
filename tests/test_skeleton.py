#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from keycloak_python_installer.skeleton import fib

__author__ = "Boris Waguia"
__copyright__ = "Boris Waguia"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
