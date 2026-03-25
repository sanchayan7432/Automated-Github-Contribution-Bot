import time
from scheduler import CommitScheduler
from commit_manager import CommitManager
from config import FIRST_COMMIT_DELAY


def main():

    print("🤖 GitHub Contribution Bot Started")

    manager = CommitManager()

    # First commit after startup
    print(f"⏳ First commit in {FIRST_COMMIT_DELAY} seconds...")
    time.sleep(FIRST_COMMIT_DELAY)

    manager.make_commit()

    # Start daily scheduler
    scheduler = CommitScheduler()
    scheduler.start()


if __name__ == "__main__":
    main()