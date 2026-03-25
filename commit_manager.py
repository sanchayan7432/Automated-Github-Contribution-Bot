from git_utils import GitManager


class CommitManager:

    def __init__(self):
        self.git = GitManager()

    def make_commit(self):
        print("🚀 Creating automated commit...")
        self.git.commit_and_push()