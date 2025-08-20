# How to Connect GitHub and VS Code 🚀

This guide will walk you through connecting GitHub with VS Code to work efficiently with this LeetCode Problems repository and any other GitHub repositories.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Method 1: Using GitHub CLI (Recommended)](#method-1-using-github-cli-recommended)
- [Method 2: Using Personal Access Token](#method-2-using-personal-access-token)
- [Method 3: Using SSH Keys](#method-3-using-ssh-keys)
- [Cloning and Opening Repositories](#cloning-and-opening-repositories)
- [Essential VS Code Extensions](#essential-vs-code-extensions)
- [Working with Git in VS Code](#working-with-git-in-vs-code)
- [Troubleshooting](#troubleshooting)

## Prerequisites

1. **Install VS Code**: Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. **Install Git**: Download from [git-scm.com](https://git-scm.com/)
3. **GitHub Account**: Create one at [github.com](https://github.com/)

## Method 1: Using GitHub CLI (Recommended)

The GitHub CLI is the easiest way to authenticate and work with GitHub repositories.

### Step 1: Install GitHub CLI
- **Windows**: Download from [cli.github.com](https://cli.github.com/) or use `winget install GitHub.cli`
- **macOS**: `brew install gh`
- **Linux**: Follow instructions at [cli.github.com](https://cli.github.com/)

### Step 2: Authenticate
```bash
gh auth login
```
Follow the prompts to:
1. Choose "GitHub.com"
2. Select your preferred protocol (HTTPS recommended)
3. Authenticate via web browser

### Step 3: Verify Authentication
```bash
gh auth status
```

## Method 2: Using Personal Access Token

### Step 1: Create Personal Access Token
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `workflow`, `write:packages`, `delete:packages`
4. Copy the generated token (save it securely!)

### Step 2: Configure VS Code
1. Open VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type "Git: Clone" and select it
4. Enter repository URL: `https://github.com/username/repository-name.git`
5. When prompted for credentials:
   - Username: Your GitHub username
   - Password: Your personal access token (not your account password)

## Method 3: Using SSH Keys

### Step 1: Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

### Step 2: Add SSH Key to SSH Agent
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Step 3: Add SSH Key to GitHub
1. Copy your public key: `cat ~/.ssh/id_ed25519.pub`
2. Go to GitHub → Settings → SSH and GPG keys → New SSH key
3. Paste your public key and save

### Step 4: Test SSH Connection
```bash
ssh -T git@github.com
```

## Cloning and Opening Repositories

### Using VS Code Command Palette
1. Press `Ctrl+Shift+P` (or `Cmd+Shift+P`)
2. Type "Git: Clone"
3. Enter repository URL:
   - HTTPS: `https://github.com/Aravind-droid1/Leetcode-Problems.git`
   - SSH: `git@github.com:Aravind-droid1/Leetcode-Problems.git`
4. Select folder location
5. Choose "Open" when prompted

### Using Terminal in VS Code
```bash
# Navigate to desired directory
cd /path/to/your/projects

# Clone repository
git clone https://github.com/Aravind-droid1/Leetcode-Problems.git

# Open in VS Code
code Leetcode-Problems
```

## Essential VS Code Extensions

Install these extensions for better GitHub integration:

### Core Git & GitHub Extensions
- **GitHub Pull Requests and Issues** - Official GitHub extension
- **GitLens** - Enhanced Git capabilities
- **Git Graph** - Visual git repository viewer

### Python Development (for this repository)
- **Python** - Official Python extension
- **Pylance** - Advanced Python language support
- **Python Debugger** - Debugging support

### Code Quality & Formatting
- **Black Formatter** - Python code formatting
- **Flake8** - Python linting
- **autoDocstring** - Generate Python docstrings

### Installation Commands
```bash
# Install extensions via CLI
code --install-extension GitHub.vscode-pull-request-github
code --install-extension eamodio.gitlens
code --install-extension mhutchie.git-graph
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.debugpy
```

## Working with Git in VS Code

### Basic Workflow
1. **Make Changes**: Edit your Python files
2. **Stage Changes**: Click `+` next to files in Source Control panel
3. **Commit**: Enter commit message and press `Ctrl+Enter`
4. **Push**: Click sync icon or use `Ctrl+Shift+P` → "Git: Push"

### Source Control Panel
- Press `Ctrl+Shift+G` to open Source Control
- View changes, stage files, commit, and push
- See commit history and branch information

### Terminal Commands
```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Add solution for Two Sum problem"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Create new branch
git checkout -b feature/new-solution

# Switch branches
git checkout main
```

## Working with LeetCode Problems

### Recommended File Organization
```
Leetcode-Problems/
├── README.md
├── Easy/
│   ├── two_sum.py
│   ├── valid_palindrome.py
│   └── ...
├── Medium/
│   ├── add_two_numbers.py
│   └── ...
├── Hard/
│   └── ...
└── Utils/
    ├── test_cases.py
    └── helper_functions.py
```

### Best Practices for This Repository
1. **Consistent Naming**: Use snake_case for Python files
2. **Comments**: Include problem number and description
3. **Test Cases**: Add test cases in your solutions
4. **Documentation**: Comment your approach and time complexity

### Example Solution Format
```python
# 1. Two Sum
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        hash_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        
        return []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # Expected: [1, 2]
```

## Troubleshooting

### Common Issues and Solutions

#### Authentication Problems
```bash
# Clear stored credentials
git config --global --unset user.name
git config --global --unset user.email

# Set new credentials
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

#### Push/Pull Issues
```bash
# If remote branch doesn't exist
git push -u origin main

# If you get "non-fast-forward" error
git pull origin main --rebase

# Reset authentication (if using HTTPS)
git config --global credential.helper manager-core
```

#### VS Code Not Detecting Git
1. Check if Git is in your PATH: `git --version`
2. In VS Code settings, set Git path: `"git.path": "/usr/bin/git"`
3. Restart VS Code

#### Extension Issues
```bash
# Reset VS Code extensions
code --disable-extensions
code --enable-extensions
```

### Getting Help
- **VS Code Docs**: [code.visualstudio.com/docs](https://code.visualstudio.com/docs)
- **GitHub Docs**: [docs.github.com](https://docs.github.com/)
- **Git Docs**: [git-scm.com/doc](https://git-scm.com/doc)

## Additional Tips

### Keyboard Shortcuts
- `Ctrl+Shift+G`: Open Source Control
- `Ctrl+Shift+P`: Command Palette
- `Ctrl+``: Open Terminal
- `F5`: Start Debugging
- `Ctrl+Shift+F`: Search across files

### VS Code Settings for Python Development
Add to your VS Code settings.json:
```json
{
    "python.defaultInterpreterPath": "python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "git.autofetch": true
}
```

### GitHub Features in VS Code
- View and create pull requests directly in VS Code
- Browse GitHub issues
- See GitHub repository information
- Compare branches and commits
- Manage GitHub Copilot (if subscribed)

---

Happy coding! 🎉 Now you're ready to efficiently work with GitHub repositories in VS Code.