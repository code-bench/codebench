import subprocess

from codebench.performance.Runner import Runner
from codebench.report.Factory import reporter_factory
from codebench.settings.Setting import get_setting
from codebench.GitHandler import GitHandler


def reset_git_head(git_handler):
    git_handler.reset_head()


def main():
    setting = get_setting()

    # run the preparation script
    if setting.BEFORE_ALL:
        # a blocking call to get prepared for benchmarking
        subprocess.call(setting.BEFORE_ALL)

    start_script = setting.SCRIPT

    git_handler = GitHandler(setting.GIT_FOLDER)

    reporters = reporter_factory(setting.REPORT_TYPES)

    # run benchmark on given commits or head
    if setting.COMMITS:
        commits = setting.COMMITS
    else:
        commits = ['head']

    if setting.BASELINE:
        commits.append(setting.BASELINE)

    for commit in commits:
        try:
            git_handler.checkout(commit)
            if setting.BEFORE_EACH:
                subprocess.call(setting.BEFORE_EACH)
            r = Runner(start_script)
            r.run()
            for reporter in reporters:
                reporter.add_result(commit, r.summary)
            if setting.AFTER_EACH:
                subprocess.call(setting.AFTER_EACH)
        except Exception as e:
            reset_git_head(git_handler)
            raise e

    for reporter in reporters:
        reporter.generate_report()
    reset_git_head(git_handler)

    if setting.AFTER_ALL:
        subprocess.call(setting.AFTER_ALL)
