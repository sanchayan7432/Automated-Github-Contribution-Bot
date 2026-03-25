import os
from dotenv import load_dotenv

load_dotenv()

# Target repository path
REPO_PATH = os.getenv("REPO_PATH", "D:\\NATURE-YouTube-video-Downloader")

# Branch name
BRANCH = "main"

# Commit settings
COMMIT_MESSAGE = "🤖 Automated daily contribution"
FILE_TO_UPDATE = "activity.log"

# Scheduler settings
FIRST_COMMIT_DELAY = 60
DAILY_COMMIT_TIME = "12:00"