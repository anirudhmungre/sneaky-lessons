# -*- coding: utf-8 -*-
"""Check Changed Files.

This module will run linters on any files that changed in the commit.

"""

# Add Native Libraries
import shlex
from pathlib import Path
import subprocess
from checks.markdown_links import check_markdown_links
from checks.cspell import check_cspell
from checks.eslint import check_eslint
from checks.pycodestyle import check_pycodestyle

# Declare Lists to hold changes changed
markdown_files_changed = []
python_files_changed = []
javascript_files_changed = []

# Main Git CMD to find the changes changed
git_diff = shlex.split("git diff --diff-filter=d --name-only master")

# Running Git CMD to get the files changed
# Removing formatting on the end of the string with rstrip
# Spliting string to list with split based on \n
all_files_changed = (
    subprocess.check_output(git_diff, encoding="utf-8").rstrip().split("\n")
)

# Sorting the list of all files changed into list based on extension
for file_changed in all_files_changed:

    if file_changed.endswith(".md"):
        markdown_files_changed.append(file_changed)
    if file_changed.endswith(".py"):
        python_files_changed.append(file_changed)
    if file_changed.endswith(".js"):
        javascript_files_changed.append(file_changed)

try:
    check_markdown_links()
except Exception as e:
    print(e)

try:
    check_cspell(all_files_changed)
except Exception as e:
    print(e)

try:
    check_eslint(javascript_files_changed)
except Exception as e:
    print(e)

try:
    check_pycodestyle(python_files_changed)
except Exception as e:
    print(e)
