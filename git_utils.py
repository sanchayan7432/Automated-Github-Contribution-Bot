from git import Repo
import os
from datetime import datetime
from config import REPO_PATH, FILE_TO_UPDATE, COMMIT_MESSAGE


class GitManager:

    def __init__(self):
        if not os.path.exists(REPO_PATH):
            raise Exception("Repository path not found")

        self.repo = Repo(REPO_PATH)

    def update_file(self):
        file_path = os.path.join(REPO_PATH, FILE_TO_UPDATE)

        with open(file_path, "a") as f:
            f.write(f"Commit at {datetime.now()}\n")

    def commit_and_push(self):

        self.update_file()

        self.repo.git.add(all=True)

        if self.repo.is_dirty():
            self.repo.index.commit(COMMIT_MESSAGE)

            origin = self.repo.remote(name="origin")
            origin.push()

            print("✅ Commit pushed successfully")

        else:
            print("⚠ No changes to commit")