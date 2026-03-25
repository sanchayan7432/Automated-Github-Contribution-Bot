# Automated GitHub Contribution Bot

A lightweight Python bot that automates commits to GitHub on a daily schedule.  
This project helps maintain consistent repository activity and keeps your GitHub contribution graph alive.
---

## ✨ Features
```
- ⏱ First commit triggered within 1 minute
- 📅 Daily automated commits thereafter
- 🔗 Seamless Git integration
- ⚙️ Fully configurable via environment variables
- 🪶 Lightweight scheduler for minimal resource usage
```
---

## 🚀 Setup

1. **Clone the repository**
```
git clone https://github.com/sanchayan7432/Automated-Github-Contribution-Bot.git

cd Automated-Github-Contribution-Bot
```
2. Install dependencies
```
pip install -r requirements.txt

- Configure environment variables
```
3. Create a .env file in the project root and add your GitHub credentials and repository details:
```
GITHUB_USER=your-username
GITHUB_REPO=your-repo-name
GITHUB_TOKEN=your-personal-access-token
```

4. Run the bot
```
python main.py
```
---

## ⚡ How It Works
- The bot waits for a short delay before making the first commit.
- Afterward, it runs on a daily schedule, committing changes automatically.
- The commit manager handles Git operations, while the scheduler ensures precise timing.
---

## 📂 Project Structure
```
Automated-GitHub-Contribution-Bot/
├── app.py                # Entry point of the bot
├── schedular.py     # Handles scheduling logic
├── CommitManager.py       # Manages commit creation and pushes
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (GitHub credentials, repo info)
├── config.py
├── git_utils.py
├── setup.sh
└── README.md              # Project documentation
```
---

## 🛠 Customization
- Adjust commit frequency by modifying the scheduler logic.
- Update commit messages in CommitManager.py to personalize contributions.
- Extend functionality to include file edits, random content generation, or custom commit strategies.
---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to add or modify.
---

## 📜 License
This project is licensed under the MIT License.
---

## Author
Sanchayan Ghosh. Email me at sanchayan.ghosh2022@uem.edu.in
