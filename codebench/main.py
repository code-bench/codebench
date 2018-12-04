import subprocess

from codebench.parsing.DefaultArgParser import default_arg_parser
from codebench.performance.TimeUtilities import (
    get_time,
    get_time_difference,
)


def main():
    args = default_arg_parser().parse_args()

    # run the preparation script
    if args.before is not None:
        subprocess.call(args.before)

    start_time = get_time()
    # execute the benchmark program
    subprocess.call(args.start)
    end_time = get_time()
    time_diff = get_time_difference(start_time, end_time)
    print('time difference =', time_diff)
