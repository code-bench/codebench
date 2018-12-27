import yaml


class ConfParseError(ValueError):
    pass


def parse_config_args(file=None):
    """
    This function parses configurations from yaml file
    :param file: address of configuration file
    :return a dict consisting of arguments
    """
    if file is None:
        file = '.codebench.yml'
    try:
        with open(file, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)
        raise ConfParseError
