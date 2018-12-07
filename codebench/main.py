import subprocess

from codebench.parsing.DefaultArgParser import default_arg_parser
from codebench.performance.Runner import Runner
from codebench.report.Factory import reporter_factory
from codebench.git import GitHandler


def main():
    args = default_arg_parser().parse_args()

    # run the preparation script
    if args.before is not None:
        # a blocking call to get prepared for benchmarking
        subprocess.call(args.before)

    start_script = args.start

    git_handler = GitHandler(args.git_folder)

    reporter = reporter_factory(args.report_type)

    # run benchmark on given commits or head
    if args.commits:
        commits = args.commits
    else:
        commits = ['head']

    for commit in commits:
        git_handler.checkout(commit)
        r = Runner(start_script)
        r.run()
        reporter.add_result(commit, r.summary)

    if args.baseline:
        # run benchmark using baseline commit
        git_handler.checkout(args.baseline)
        r = Runner(start_script)
        r.run()
        reporter.add_result('baseline', r.summary)

    reporter.generate_report()
    # reset back to head
    git_handler.reset_head()
