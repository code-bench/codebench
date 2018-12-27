from codebench.parsing.DefaultArgParser import default_arg_parser


def parse_cli_args():
    """
    This function parses configurations from command line interface
    :return: an instance of argparse.Namespace
    """
    return default_arg_parser().parse_args()
