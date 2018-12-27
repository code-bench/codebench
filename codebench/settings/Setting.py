from codebench.parsing.CliParser import parse_cli_args
from codebench.parsing.ConfParser import parse_config_args, ConfParseError


class Setting:
    """
    Global setting consisting of configurations
    """

    # Before
    BEFORE_ALL = None
    BEFORE_EACH = None

    # Script
    SCRIPT = None

    # After
    AFTER_ALL = None
    AFTER_EACH = None

    # Commits
    GIT_FOLDER = None
    BASELINE = None
    COMMITS = []

    # Report
    REPORT_TYPES = []


def get_setting_from_cli(args):
    setting = Setting()

    setting.BEFORE_ALL = args.before_all
    setting.BEFORE_EACH = args.before_each

    setting.SCRIPT = args.script

    setting.AFTER_ALL = args.after_all
    setting.AFTER_EACH = args.after_each

    setting.GIT_FOLDER = args.git_folder
    setting.BASELINE = args.baseline
    setting.COMMITS = args.commits

    setting.REPORT_TYPES = args.report_types

    return setting


def get_setting_from_conf(config_file):
    args = parse_config_args(config_file)
    setting = Setting()

    setting.BEFORE_ALL = args.get('before_all')
    setting.BEFORE_EACH = args.get('before_each')

    setting.SCRIPT = args.get('script')

    setting.AFTER_ALL = args.get('after_all')
    setting.AFTER_EACH = args.get('after_each')

    setting.GIT_FOLDER = args.get('git_folder')
    setting.BASELINE = args.get('baseline')
    setting.COMMITS = args.get('commits')

    setting.REPORT_TYPES = args.get('report_types')

    return setting


def get_setting():
    args = parse_cli_args()
    use_cli_args = args.no_config
    if not use_cli_args:
        try:
            setting = get_setting_from_conf(args.config)
        except ConfParseError:
            print('Parsing configurations from config file fails'
                  'try CLI arguments instead...')
            use_cli_args = True
    if use_cli_args:
        setting = get_setting_from_cli(args)
    return setting
