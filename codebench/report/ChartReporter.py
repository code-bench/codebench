from pyecharts import Bar

from codebench.report.Reporter import Reporter


class ChartReporter(Reporter):
    """
    generate charts based on results
    """
    def generate_report(self):
        x_values = []
        cpu_usage = []
        for commit, result in self.results.items():
            x_values.append(commit)
            cpu_usage.append(result.get('cpu_usage'))
        bar = Bar("Benchmark Performances",
                  "benchmark performance comparison among commits")
        bar.add("cpu_usage", x_values, cpu_usage,
                mark_line=["average"], mark_point=["max", "min"])
        bar.render()
