import argparse
import os

class CustomFormatter(argparse.RawDescriptionHelpFormatter):
    """
    A Custom Formatter that will keep the metavars in the usage but remove them
    in the more detailed arguments section.
    """

    def _format_action_invocation(self, action):
        if not action.option_strings:
            # For arguments that don't have options strings
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            # Option string arguments (like "-f, --files")
            parts = action.option_strings
            return ', '.join(parts)


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


def default_arg_parser(formatter_class=None):
    """
    This function creates an ArgParser to parse command line arguments.

    :param formatter_class: Formatting the arg_parser output into a specific
                            form. For example: In the manpage format.
    """
    formatter_class = (CustomFormatter if formatter_class is None
                       else formatter_class)

    description = """
Automated code benchmark solution.
Empower developers with tools to trace and analyze project performances.
"""

    arg_parser = argparse.ArgumentParser(
        formatter_class = formatter_class,
        description=description)

    before_group = arg_parser.add_argument_group('Before')

    before_group.add_argument(
        '-b', '--before_all', type=PathArg, nargs=1,
        help='script that to be run before all')

    before_group.add_argument(
        '-e', '--before_each', type=PathArg, nargs=1,
        help='script that to be run before each benchmark')

    start_group = arg_parser.add_argument_group('Script')

    start_group.add_argument(
        '-s', '--script', type=PathArg, nargs=1,
        required=True, help='benchmark script to be run')

    after_group = arg_parser.add_argument_group('After')

    after_group.add_argument(
        '-a', '--after_all', type=PathArg, nargs=1,
        help='script that to be run after all')

    after_group.add_argument(
        '-f', '--after_each', type=PathArg, nargs=1,
        help='script that to be run after each benchmark')

    commits_group = arg_parser.add_argument_group('Commits')

    commits_group.add_argument(
        '-g', '--git_folder', type=PathArg,
        help='project git directory')

    commits_group.add_argument(
        '-l', '--baseline', type=str,
        help='baseline commit hash')

    commits_group.add_argument(
        '-c', '--commits', type=str, nargs='+',
        help='one or more commits to be benchmarked')

    report_group = arg_parser.add_argument_group('Report')

    report_group.add_argument(
        '-t', '--report_type', type=str,
        choices=['chart'],
        help='report type')

    return arg_parser
