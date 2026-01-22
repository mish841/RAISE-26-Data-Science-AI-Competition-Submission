"""
Quick setup script for Google Colab to connect with this repository.
Copy and paste this into a Colab cell to get started.
"""

# Replace with your GitHub username
GITHUB_USERNAME = "YOUR_USERNAME"
REPO_NAME = "RAISE-26-Data-Science-AI-Competition-Submission"

# Clone repository
import os
if not os.path.exists(REPO_NAME):
    print(f"Cloning repository: {REPO_NAME}")
    os.system(f"git clone https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git")
else:
    print(f"Repository {REPO_NAME} already exists")

# Navigate to repository
os.chdir(REPO_NAME)
print(f"Current directory: {os.getcwd()}")

# Pull latest changes
print("Pulling latest changes...")
os.system("git pull origin main")

print("Setup complete! You can now work with your notebooks.")
