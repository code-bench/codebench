import subprocess

import psutil

from codebench.performance.TimeUtilities import (
    get_time,
    get_time_difference,
)


def get_cpu_usage(proc):
    """
    get cpu usage of the given process
    :param proc: a psutil.Process instance
    :return: cpu usage info
    """
    if proc is None:
        return
    try:
        info = proc.cpu_percent(interval=1)
        print('cpu usage:', info)
        return info
    except (psutil.NoSuchProcess, psutil.ZombieProcess):
        return


class Runner:
    def __init__(self, program):
        self.program = program
        self.cpu_usage = None

    def _before(self):
        self.start_time = get_time()

    def _after(self):
        self.end_time = get_time()
        time_diff = get_time_difference(self.start_time, self.end_time)
        print('time difference =', time_diff)

    def run(self):
        self._before()
        # a non-blocking call to start benchmarking
        proc = subprocess.Popen(self.program)
        p = None
        try:
            p = psutil.Process(proc.pid)
        except psutil.NoSuchProcess:
            print('no such process, maybe the process is finished')
        cpu_usage_cnt = 0
        cpu_usage_tot = 0
        while proc.poll() is None:
            res = get_cpu_usage(p)
            if res is not None:
                cpu_usage_tot += res
                cpu_usage_cnt += 1
            print('pid=', proc.pid)
        if cpu_usage_tot != 0:
            self.cpu_usage = cpu_usage_tot / cpu_usage_cnt
        self._after()
