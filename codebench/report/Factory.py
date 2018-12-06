from codebench.report.ChartReporter import ChartReporter


def reporter_factory(name):
    if name == 'chart' or name is None:
        return ChartReporter()
    else:
        raise ValueError("reporter type is invalid!"
                         "available type includes 'chart'.")
