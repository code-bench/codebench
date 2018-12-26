import yaml


def parse_config_args(file=None):
    """
    This function parses configurations from yaml file
    :param file: address of configuration file
    :return a dict consisting of arguments
    """
    if file is None:
        file = '.codebench.yml'
    args = {}
    try:
        with open(file, 'r') as f:
            args = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)
    return args
