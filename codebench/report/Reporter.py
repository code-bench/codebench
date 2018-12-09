class Reporter:
    """
    report benchmark results
    """

    def __init__(self):
        self.results = dict()

    def add_result(self, commit, result):
        """
        Add result of runner to Reporter
        :param commit: commit hash code
        :param result: a dict object
        """
        self.results[commit] = result

    def generate_report(self):
        raise NotImplementedError
