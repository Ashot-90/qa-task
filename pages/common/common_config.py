import os

config_common = {
    'local': {
        "chrome_driver_path": "./chromedriver",
        "ff_driver_path": "./geckodriver"
    },
    'docker': {
        "chrome_driver_path": "/tmp/chromedriver",
        "ff_driver_path": "/tmp/geckodriver"
    }
}

config_catalog = {
    'uk': {
        "url": "https://www.vinted.co.uk/catalog",
        "search_href": "/women/shoes/heels/high-heels/"
    },
    'de': {
        "url": "https://www.vinted.de/catalog",
        "search_href": "/damen/schuhe/absatzschuhe/high-heels-and-pumps/"
    }
}

config_member = {
    'uk': {
        "url": "https://www.vinted.co.uk/member/64678795"
    },
    'de': {
        "url": "https://www.vinted.de/member/64679137"
    }
}

PORTAL = os.environ['PORTAL']
BROWSER = os.environ['BROWSER']
RESULT_DIR = os.environ['RESULT_DIR']
CATALOG_CONFIG = config_catalog.get(PORTAL.lower())
CATALOG_MEMBER = config_member.get(PORTAL.lower())

try:
    DOCKER_RUN_ENV = os.environ['DOCKER_RUN']
    COMMON_CONFIG = config_common.get('docker')
    DOCKER_RUN = True
except KeyError:
    COMMON_CONFIG = config_common.get('local')
    DOCKER_RUN = False
