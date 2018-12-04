from codebench.parsing.DefaultArgParser import default_arg_parser


def main():
    args = default_arg_parser().parse_args()
    start_script = args.start
    before_script = args.before
    print(start_script, before_script)
