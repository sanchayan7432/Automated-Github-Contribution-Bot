import schedule
import time
from commit_manager import CommitManager
from config import DAILY_COMMIT_TIME


class CommitScheduler:

    def __init__(self):
        self.manager = CommitManager()

    def run_daily_commit(self):
        self.manager.make_commit()

    def start(self):

        schedule.every().day.at(DAILY_COMMIT_TIME).do(self.run_daily_commit)

        print("⏳ Scheduler running...")

        while True:
            schedule.run_pending()
            time.sleep(30)