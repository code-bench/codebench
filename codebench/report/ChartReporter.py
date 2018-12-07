from pyecharts import Bar

from codebench.report.Reporter import Reporter


class ChartReporter(Reporter):
    """
    generate charts based on results
    """
    def generate_report(self):
        x_values = []
        cpu_usage = []
        memory_usage = []
        cpu_times = []
        for commit, result in self.results.items():
            x_values.append(commit[:6] if len(commit) > 10 else commit)
            cpu_usage.append(round(result.get('cpu_usage'), 2))
            memory_usage.append(round(result.get('memory_usage'), 2))
            cpu_times.append(round(result.get('cpu_times'), 2))
        bar = Bar('Benchmark Performances',
                  'benchmark performance comparison among commits')
        bar.add('cpu_usage', x_values, cpu_usage)
        bar.add('memory_usage', x_values, memory_usage)
        bar.add('elapsed_time', x_values, cpu_times)
        bar.render()
