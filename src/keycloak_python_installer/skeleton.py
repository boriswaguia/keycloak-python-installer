import wget
import sys
from semver import parse

keycloak_url = "https://downloads.jboss.org/keycloak/{0}/keycloak-{1}.{2}"


def __validate__(keycloak_version, keycloak_format):
    if keycloak_version is None:
        raise ValueError('keycloak_version is required')
    if keycloak_format is None:
        raise ValueError('keycloak_format is required')
    if str(keycloak_format) != 'zip' and str(keycloak_format) != 'tar.gz':
        raise ValueError('keycloak_format is invalid valid. Should be one of .zip or .tar.gz')
    
    parse(keycloak_version)#validate version is formatted as semver.

def build_download_url(keycloak_version, keycloak_format):
    __validate__(keycloak_version, keycloak_format)
    formated_url = str(keycloak_url).format(keycloak_version, keycloak_version, keycloak_format)
    return formated_url

def download(version=None, format_='zip'):
    formatted_url = build_download_url(version, format_)
    filename = wget.download(formatted_url)
    print('File downloaded at %s'%filename)
    return True

def run():
    download(sys.argv[1],sys.argv[2])
if __name__ == "__main__":
    run()