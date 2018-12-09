import argparse
import re
import unittest

from codebench.parsing.DefaultArgParser import CustomFormatter


def _get_arg(parser, arg):
    actions = parser.__dict__['_action_groups'][0].__dict__['_actions']
    args = [item for item in actions
            if arg in item.option_strings]
    return args[0]


class CustomFormatterTest(unittest.TestCase):

    def setUp(self):
        arg_parser = argparse.ArgumentParser(formatter_class=CustomFormatter)
        arg_parser.add_argument('-a',
                                '--all',
                                nargs='?',
                                const=True,
                                metavar='BOOL')
        arg_parser.add_argument('TARGETS',
                                nargs='*')
        self.output = arg_parser.format_help()

    def test_metavar_in_usage(self):
        match = re.search(r'usage:.+(-a \[BOOL\]).+\n\n',
                          self.output,
                          flags=re.DOTALL)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), '-a [BOOL]')

    def test_metavar_not_in_optional_args_sections(self):
        match = re.search('optional arguments:.+(-a, --all).*',
                          self.output,
                          flags=re.DOTALL)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), '-a, --all')
