import subprocess

import psutil


def get_resource_info(proc):
    """
    get resource info of the given process

    :param proc: a psutil.Process instance
    :return: resource info (cpu percent, memory percent, etc.)

    cpu_percent is a float representing the current
    system-wide CPU utilization as a percentage
    >>> proc.cpu_percent()
    98.0

    memory_percent compares process memory to total physical system memory
    and calculate process memory utilization as a percentage
    >>> proc.memory_percent()
    0.05736351013183594

    cpu_times returns a (user, system, children_user, children_system) named
    tuple representing the accumulated process time, in seconds
    >>> proc.cpu_times()
    pcputimes(user=0.07006404, system=0.027061132,
              children_user=0.0, children_system=0.0)
    """
    if proc is None:
        return
    try:
        """
        Utility context manager which considerably speeds up the retrieval of
        multiple process information at the same time.
        """
        cpu_percent = proc.cpu_percent(interval=1)
        with proc.oneshot():
            # execute internal routine once collecting multiple info
            memory_percent = proc.memory_percent()
            # use cached value
            cpu_times = sum(proc.cpu_times())
            print('cpu percent:', cpu_percent)
            print('memory percent:', memory_percent)
            print('cpu times:', cpu_times)
        result = dict()
        result['cpu_percent'] = cpu_percent
        result['memory_percent'] = memory_percent
        result['cpu_times'] = cpu_times
        return result
    except (psutil.NoSuchProcess, psutil.ZombieProcess):
        return


class Runner:
    def __init__(self, program):
        self.program = program
        self.cpu_usage = None
        self.cpu_times = None
        self.memory_usage = None

    def run(self):
        # a non-blocking call to start benchmarking
        proc = subprocess.Popen(self.program)
        try:
            p = psutil.Process(proc.pid)
        except psutil.NoSuchProcess:
            print('no such process, maybe the process is finished')
            return

        cpu_usage_cnt = 0
        cpu_usage_tot = 0
        memory_usage_cnt = 0
        memory_usage_tot = 0

        while proc.poll() is None:
            result = get_resource_info(p)

            if result is None:
                continue

            cpu_times = result['cpu_times']
            cpu_usage_tot += result['cpu_percent']
            cpu_usage_cnt += 1
            memory_usage_tot += result['memory_percent']
            memory_usage_cnt += 1

        if cpu_usage_tot != 0:
            self.cpu_usage = cpu_usage_tot / cpu_usage_cnt
        if memory_usage_tot != 0:
            self.memory_usage = memory_usage_tot / memory_usage_cnt
        self.cpu_times = cpu_times
