import subprocess

import psutil

from codebench.performance.TimeUtilities import (
    get_time,
    get_time_difference,
)


def get_cpu_info(proc):
    """
    get cpu info of the given process
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


class Reporter:
    def __init__(self, program):
        self.program = program

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
        while proc.poll() is None:
            get_cpu_info(p)
            print('pid=', proc.pid)
        self._after()
