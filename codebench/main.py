import subprocess

from codebench.parsing.DefaultArgParser import default_arg_parser
from codebench.performance.Runner import Runner
from codebench.report.Factory import reporter_factory
from codebench.GitHandler import GitHandler

def reset_git_head(git_handler):
    git_handler.reset_head()


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
        try:
            git_handler.checkout(commit)
            r = Runner(start_script)
            r.run()
            reporter.add_result(commit, r.summary)
        except Exception as e:
            reset_git_head(git_handler)
            raise e

    if args.baseline:
        # run benchmark using baseline commit
        try:
            git_handler.checkout(args.baseline)
            r = Runner(start_script)
            r.run()
            reporter.add_result('baseline', r.summary)
        except Exception as e:
            reset_git_head(git_handler)
            raise e

    reporter.generate_report()
    reset_git_head(git_handler)
