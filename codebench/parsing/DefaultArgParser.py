import argparse
import os


class PathArg(str):
    """
    Uni(xi)fying OS-native directory separators in path arguments.

    Removing the pain from interactively using coala in a Windows cmdline,
    because backslashes are interpreted as escaping syntax and therefore
    removed when arguments are turned into coala settings

    >>> import os
    >>> PathArg(os.path.join('path', 'with', 'separators'))
    'path/with/separators'
    """

    def __new__(cls, path):
        return str.__new__(cls, path.replace(os.path.sep, '/'))


def default_arg_parser():
    """
    This function creates an ArgParser to parse command line arguments.
    """
    description = """
Automated code benchmark solution.
Empower developers with tools to trace and analyze project performances.
"""

    arg_parser = argparse.ArgumentParser(description=description)

    before_group = arg_parser.add_argument_group('Before')

    before_group.add_argument(
        '-b', '--before', type=PathArg, nargs=1, metavar='FILE',
        help='file to be run before benchmarking')

    start_group = arg_parser.add_argument_group('Start')

    start_group.add_argument(
        '-s', '--start', type=PathArg, nargs=1, metavar='FILE',
        required=True, help='benchmark script to be run')

    baseline_group = arg_parser.add_argument_group('Baseline')

    baseline_group.add_argument(
        '-l', '--baseline', type=str, nargs=1,
        help='Commit hash for the baseline')

    return arg_parser
