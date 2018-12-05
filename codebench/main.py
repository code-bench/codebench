import subprocess

from codebench.parsing.DefaultArgParser import default_arg_parser
from codebench.performance.Runner import Runner
from codebench.report.ChartReporter import ChartReporter
from codebench.git import GitHandler


def main():
    args = default_arg_parser().parse_args()

    # run the preparation script
    if args.before is not None:
        # a blocking call to get prepared for benchmarking
        subprocess.call(args.before)

    start_script = args.start

    git_handler = GitHandler(args.git_folder)

    chart_reporter = ChartReporter()

    # run benchmark on given commits or head
    if args.commits:
        commits = args.commits
    else:
        commits = ['head']

    for commit in commits:
        git_handler.checkout(commit)
        r = Runner(start_script)
        r.run()
        chart_reporter.add_result(commit, {'cpu_usage': r.cpu_usage})

    if args.baseline:
        # run benchmark using baseline commit
        git_handler.checkout(args.baseline)
        r = Runner(start_script)
        r.run()
        chart_reporter.add_result('baseline', {'cpu_usage': r.cpu_usage})

    chart_reporter.generate_report()
    # reset back to head
    git_handler.reset_head()
