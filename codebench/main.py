import subprocess

from codebench.parsing.DefaultArgParser import default_arg_parser
from codebench.performance.TimeUtilities import (
    get_time,
    get_time_difference,
)
from codebench.git import GitHandler


def run_benchmark(benchmark):
    start_time = get_time()
    # execute the benchmark program
    subprocess.call(benchmark)
    end_time = get_time()
    time_diff = get_time_difference(start_time, end_time)
    print('time difference =', time_diff)


def main():
    args = default_arg_parser().parse_args()

    # run the preparation script
    if args.before is not None:
        subprocess.call(args.before)

    start_script = args.start
    run_benchmark(start_script)

    if args.baseline:
        git_handler = GitHandler(args.git_folder)
        # run benchmark using baseline commit
        git_handler.checkout(args.baseline)
        run_benchmark(start_script)
        # reset back to head
        git_handler.reset_head()
