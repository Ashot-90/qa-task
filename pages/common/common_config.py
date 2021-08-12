import os

config_common_local = {
    "chrome_driver_path": "./chromedriver",
    "ff_driver_path": "./geckodriver"
}

config_common_docker = {
    "chrome_driver_path": "/tmp/chromedriver",
    "ff_driver_path": "/tmp/geckodriver"
}

catalog_config_uk = {
    "url": "https://www.vinted.co.uk/catalog",
    "search_href": "/women/shoes/heels/high-heels/"
}

catalog_config_de = {
    "url": "https://www.vinted.de/catalog",
    "search_href": "/damen/schuhe/absatzschuhe/high-heels-and-pumps/"
}

member_config_uk = {
    "url": "https://www.vinted.co.uk/member/64678795"
}

member_config_de = {
    "url": "https://www.vinted.de/member/64679137"
}

PORTAL = os.environ['PORTAL']
BROWSER = os.environ['BROWSER']
RESULT_DIR = os.environ['RESULT_DIR']

if PORTAL == 'DE':
    CATALOG_CONFIG = catalog_config_de
    CATALOG_MEMBER = member_config_de
elif PORTAL == 'UK':
    CATALOG_CONFIG = catalog_config_uk
    CATALOG_MEMBER = member_config_uk

try:
    DOCKER_RUN_ENV = os.environ['DOCKER_RUN']
    COMMON_CONFIG = config_common_docker
    DOCKER_RUN = True
except KeyError:
    COMMON_CONFIG = config_common_local
    DOCKER_RUN = False
