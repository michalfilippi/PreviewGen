import argparse
import yaml
import logging
from schema import Schema, Optional

from .previewer import previewer_config_schema
from .scanner import scanner_config_schema
from .previewgenerator import run

default_logging_level = logging.INFO

config_schema = Schema({
    'scanner': scanner_config_schema,
    'previewer': previewer_config_schema,
    Optional('logger'): {
        Optional('level'): str
    }
})

logging.basicConfig(level=default_logging_level)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description='Create a preview from given gallery location.')
    parser.add_argument('config_file', metavar='config_file', type=str, help='path to a YAML config file')
    args = parser.parse_args()

    config = {}
    with open(args.config_file, 'r') as conf_in:
        try:
            config = yaml.safe_load(conf_in)
            logger.info(f"Config file \"{args.config_file}\" read successfully.")
            logger.info(config)
        except yaml.YAMLError as exc:
            logger.error(f"Reading config file \"{args.config_file}\" failed.")
            raise exc

    config_schema.validate(config)

    if 'logger' in config and 'level' in config['logger']:
        level = config['logger']['level']
        try:
            logger.setLevel(level)
            logger.debug(f"Loging level set to {logger.level} ({level}).")
        except ValueError as exc:
            logger.error(f"Unknown logging level \"{level}\". Fallback to \"{default_logging_level}\".")
            logger.error(exc)

    run(config['scanner'], config['previewer'])


if __name__ == "__main__":
    main()
