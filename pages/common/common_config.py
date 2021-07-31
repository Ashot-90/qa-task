import os
from pages.catalog import catalog_config
from pages.member import member_config

config_common_local = {
    "chrome_driver_path": "./chromedriver",
    "ff_driver_path": "./geckodriver"
}

config_common_docker = {
    "chrome_driver_path": "/tmp/chromedriver",
    "ff_driver_path": "/tmp/geckodriver"
}

PORTAL = os.environ['PORTAL']
BROWSER = os.environ['BROWSER']
RESULT_DIR = os.environ['RESULT_DIR']

if PORTAL == 'DE':
    CATALOG_CONFIG = catalog_config.config_de
    CATALOG_MEMBER = member_config.config_de
elif PORTAL == 'UK':
    CATALOG_CONFIG = catalog_config.config_uk
    CATALOG_MEMBER = member_config.config_uk

try:
    DOCKER_RUN_ENV = os.environ['DOCKER_RUN']
    COMMON_CONFIG = config_common_docker
    DOCKER_RUN = True
except KeyError:
    COMMON_CONFIG = config_common_local
    DOCKER_RUN = False
