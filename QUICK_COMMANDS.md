# 🚀 Quick Commands Reference

## Essential Commands

### Run the Application
```bash
# Windows
START_APP.bat

# Linux/Mac
chmod +x start_app.sh
./start_app.sh

# Or directly
streamlit run src/app.py
```

### Train the Model
```bash
python src/model_training.py
```

### Test the System
```bash
python test_app.py
```

---

## Git Commands for GitHub Upload

### First Time Setup
```bash
# Navigate to project folder
cd "C:\Users\Victus\Downloads\New folder"

# Initialize git
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit - Smart Irrigation AI System v3.0"

# Add remote repository (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/smart-irrigation-ai.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Regular Updates
```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main
```

### Pull Latest Changes
```bash
git pull origin main
```

---

## Python Environment

### Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Update Dependencies
```bash
pip freeze > requirements.txt
```

---

## Streamlit Commands

### Run with Custom Port
```bash
streamlit run src/app.py --server.port 8502
```

### Run with Custom Address
```bash
streamlit run src/app.py --server.address 0.0.0.0
```

### Clear Cache
```bash
streamlit cache clear
```

---

## Useful Shortcuts

### Stop Streamlit Server
- Press `Ctrl + C` in terminal

### Reload App
- Press `R` in browser
- Or `Ctrl + R` / `Cmd + R`

### Clear Cache and Reload
- Press `C` in browser

---

## File Operations

### Check File Sizes
```bash
# Windows
dir /s

# Linux/Mac
du -sh *
```

### Find Large Files
```bash
# Windows PowerShell
Get-ChildItem -Recurse | Sort-Object Length -Descending | Select-Object -First 10

# Linux/Mac
find . -type f -exec du -h {} + | sort -rh | head -n 10
```

---

## GitHub Operations

### Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/smart-irrigation-ai.git
```

### Create New Branch
```bash
git checkout -b feature/new-feature
```

### Switch Branch
```bash
git checkout main
```

### Merge Branch
```bash
git checkout main
git merge feature/new-feature
```

### Delete Branch
```bash
git branch -d feature/new-feature
```

---

## Troubleshooting Commands

### Check Python Version
```bash
python --version
```

### Check Pip Version
```bash
pip --version
```

### Check Git Version
```bash
git --version
```

### Check Streamlit Version
```bash
streamlit --version
```

### List Installed Packages
```bash
pip list
```

### Check for Outdated Packages
```bash
pip list --outdated
```

---

## Quick Fixes

### Port Already in Use
```bash
# Find process using port 8501
# Windows
netstat -ano | findstr :8501

# Linux/Mac
lsof -i :8501

# Kill process (replace PID)
# Windows
taskkill /PID <PID> /F

# Linux/Mac
kill -9 <PID>
```

### Module Not Found Error
```bash
pip install <module-name>
```

### Permission Denied (Linux/Mac)
```bash
chmod +x start_app.sh
```

---

## Deployment Commands

### Streamlit Cloud
```bash
# Just push to GitHub, then:
# 1. Go to share.streamlit.io
# 2. Connect GitHub repository
# 3. Deploy!
```

### Heroku
```bash
# Install Heroku CLI
# Then:
heroku login
heroku create smart-irrigation-ai
git push heroku main
```

### Docker
```bash
# Build image
docker build -t smart-irrigation-ai .

# Run container
docker run -p 8501:8501 smart-irrigation-ai
```

---

## Maintenance Commands

### Update All Packages
```bash
pip install --upgrade -r requirements.txt
```

### Clean Python Cache
```bash
# Windows
del /s /q __pycache__
del /s /q *.pyc

# Linux/Mac
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name '*.pyc' -delete
```

### Backup Project
```bash
# Create zip
# Windows
tar -a -c -f backup.zip *

# Linux/Mac
tar -czf backup.tar.gz *
```

---

## Documentation Commands

### Generate Requirements
```bash
pip freeze > requirements.txt
```

### Count Lines of Code
```bash
# Windows PowerShell
(Get-Content src/*.py | Measure-Object -Line).Lines

# Linux/Mac
find src -name '*.py' | xargs wc -l
```

### Generate Documentation
```bash
# Using pdoc
pip install pdoc3
pdoc --html --output-dir docs src/
```

---

## Testing Commands

### Run All Tests
```bash
python -m pytest
```

### Run Specific Test
```bash
python test_app.py
```

### Check Code Style
```bash
# Install flake8
pip install flake8

# Run check
flake8 src/
```

### Format Code
```bash
# Install black
pip install black

# Format
black src/
```

---

## Performance Commands

### Profile Code
```bash
python -m cProfile -o profile.stats src/app.py
```

### Memory Usage
```bash
# Install memory_profiler
pip install memory_profiler

# Run
python -m memory_profiler src/app.py
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Run app | `streamlit run src/app.py` |
| Train model | `python src/model_training.py` |
| Test system | `python test_app.py` |
| Git commit | `git add . && git commit -m "message"` |
| Git push | `git push origin main` |
| Install deps | `pip install -r requirements.txt` |
| Activate venv | `venv\Scripts\activate` (Windows) |
| Deactivate venv | `deactivate` |

---

**Keep this file handy for quick reference! 📚**

*Made with ❤️ by Code Craft India*
