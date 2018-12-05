import subprocess

from codebench.parsing.DefaultArgParser import default_arg_parser
from codebench.performance.Reporter import Reporter
from codebench.git import GitHandler


def main():
    args = default_arg_parser().parse_args()

    # run the preparation script
    if args.before is not None:
        # a blocking call to get prepared for benchmarking
        subprocess.call(args.before)

    start_script = args.start

    git_handler = GitHandler(args.git_folder)

    # run benchmark on given commits or head
    if args.commits:
        commits = args.commits
    else:
        commits = [None]

    for commit in commits:
        git_handler.checkout(commit)
        r = Reporter(start_script)
        r.run()

    if args.baseline:
        # run benchmark using baseline commit
        git_handler.checkout(args.baseline)
        r = Reporter(start_script)
        r.run()

    # reset back to head
    git_handler.reset_head()
