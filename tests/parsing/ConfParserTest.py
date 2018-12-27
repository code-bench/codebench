import unittest
from unittest import mock

from codebench.parsing.ConfParser import parse_config_args


class ConfParserTest(unittest.TestCase):

    def test_default_file(self):
        m = mock.mock_open()
        with mock.patch('codebench.parsing.ConfParser.open', m):
            parse_config_args(None)
            m.assert_called_once_with('.codebench.yml', 'r')
