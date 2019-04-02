=========================
keycloak-python-installer
=========================


A keycloak installer written in python.


Description
===========

This software allow it users to :
* Download a given version of keycloak.


Running:
========

* Make sure all dependencies are installed
    - pip3 install wget
    - pip3 install semver
    - /Applications/Python\ 3.7/Install\ Certificates.command

* Build binary distribution
    - python3 build bdist

* Run the script with some parameters to download a specific keycloak version
    - $python3 build/lib/keycloak_python_installer/skeleton.py 5.0.0 zip

* Additionals informations
    - The script only accept zip|tar.gz

Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
