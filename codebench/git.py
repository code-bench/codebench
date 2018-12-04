from git import Repo


class GitHandler:
    def __init__(self, path='./'):
        self.repo = Repo(path)
        self.head = self.repo.head.reference

    def _clean(self):
        """
        reset the index and working tree to match the pointed-to commit
        """
        self.repo.head.reset(index=True, working_tree=True)

    def checkout(self, commit):
        self.repo.head.reference = commit
        self._clean()

    def reset_head(self):
        self.repo.head.reference = self.head
        self._clean()
