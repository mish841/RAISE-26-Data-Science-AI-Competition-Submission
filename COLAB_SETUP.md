# Linking Google Colab to This Repository

This guide explains how to connect your Google Colab notebooks to this GitHub repository.

## Method 1: Using Colab's Built-in GitHub Integration (Easiest)

### Saving from Colab to GitHub:
1. In your Colab notebook, go to **File → Save a copy in GitHub**
2. Select your repository: `RAISE-26-Data-Science-AI-Competition-Submission`
3. Choose the branch (usually `main` or `master`)
4. Add a commit message
5. Click **OK**

### Loading from GitHub to Colab:
1. In Colab, go to **File → Open notebook**
2. Click the **GitHub** tab
3. Enter your repository URL: `https://github.com/YOUR_USERNAME/RAISE-26-Data-Science-AI-Competition-Submission`
4. Select the notebook you want to open

**Note:** You'll need to authenticate with GitHub the first time.

---

## Method 2: Clone Repository in Colab (Best for Active Development)

This method allows you to work directly with git commands in Colab.

### Step 1: Clone the repository in Colab

Add this cell at the beginning of your Colab notebook:

```python
# Clone the repository
!git clone https://github.com/YOUR_USERNAME/RAISE-26-Data-Science-AI-Competition-Submission.git

# Navigate to the repository directory
import os
os.chdir('RAISE-26-Data-Science-AI-Competition-Submission')
```

### Step 2: Set up Git credentials (one-time setup)

```python
# Configure git (replace with your details)
!git config --global user.name "Your Name"
!git config --global user.email "your.email@example.com"
```

### Step 3: Authenticate with GitHub

For private repositories, you'll need to use a Personal Access Token:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with `repo` permissions
3. Use it when prompted for password, or set it up:

```python
# Option A: Use token in clone URL (for private repos)
!git clone https://YOUR_TOKEN@github.com/YOUR_USERNAME/RAISE-26-Data-Science-AI-Competition-Submission.git

# Option B: Store credentials (less secure)
import getpass
import os
os.environ['GIT_ASKPASS'] = 'echo'
!git config --global credential.helper store
```

### Step 4: Work with your notebooks

```python
# Save your notebook
# Then commit and push changes
!git add .
!git commit -m "Update notebook"
!git push origin main
```

### Step 5: Pull latest changes

```python
# Pull latest changes from GitHub
!git pull origin main
```

---

## Method 3: Manual Sync (Simple but Manual)

1. **Download from Colab:**
   - In Colab: **File → Download → Download .ipynb**

2. **Upload to GitHub:**
   - Add the downloaded `.ipynb` file to your local repository
   - Commit and push:
     ```bash
     git add *.ipynb
     git commit -m "Add Colab notebook"
     git push origin main
     ```

3. **Load back to Colab:**
   - Upload the file: **File → Upload notebook**
   - Or use Method 1 to open from GitHub

---

## Recommended Workflow

For active development, we recommend **Method 2**:

1. Clone the repo once at the start of your Colab session
2. Work on your notebooks
3. Commit and push changes regularly
4. Pull before starting new work to get latest changes

### Example Colab Setup Cell:

```python
# ============================================
# Repository Setup
# ============================================
import os

# Clone repository (if not already cloned)
if not os.path.exists('RAISE-26-Data-Science-AI-Competition-Submission'):
    !git clone https://github.com/YOUR_USERNAME/RAISE-26-Data-Science-AI-Competition-Submission.git

# Navigate to repository
os.chdir('RAISE-26-Data-Science-AI-Competition-Submission')

# Pull latest changes
!git pull origin main

# Verify location
print(f"Current directory: {os.getcwd()}")
```

---

## Troubleshooting

### Authentication Issues:
- Use Personal Access Tokens instead of passwords
- For public repos, authentication may not be required for read access

### Permission Denied:
- Make sure your GitHub token has `repo` permissions
- Check that you have write access to the repository

### Notebook Conflicts:
- Always pull before starting work
- Resolve merge conflicts if multiple people are working

---

## Next Steps

1. Replace `YOUR_USERNAME` with your actual GitHub username in the commands above
2. Choose the method that works best for your workflow
3. Set up authentication if using a private repository
4. Start working on your notebooks!
