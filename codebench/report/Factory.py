from codebench.report.ChartReporter import ChartReporter


def reporter_factory(names):
    reporters = []
    for name in names:
        if name == 'chart':
            reporters.append(ChartReporter())
        else:
            print('reporter type %s is invalid', name)
    if len(reporters) == 0:
        print('warning: no valid reporter type is specified, '
              'use chart reporter by default')
        reporters.append(ChartReporter())
    return reporters
