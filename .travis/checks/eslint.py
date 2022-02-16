# -*- coding: utf-8 -*-
"""Javascript Linter.

This module will run on changed files to check for JavaScript linting.

"""

# Add Native Libraries
from pathlib import Path
import subprocess
import shlex


def check_eslint(javascript_files_changed):
    """Function will check changed Javascript files to see if there an linter errors/warnings.

    Args:
        javascript_files_changed: git diff will grab any javascript files that was changed for the branch the user has changed.

    Returns:
       Will pass silently if no broken links are found.
       Will raise an Exception if a linting error/warning is found

    """

    eslint_path = Path("./node_modules/.bin/eslint")

    if not eslint_path.exists():
        raise Exception(
            "eslint is not found. Might need to do a npm install or yarn install"
        )

    for file_changed in javascript_files_changed:
        # Running eslint
        eslint_report = subprocess.run(
            shlex.split(f"{eslint_path} -c .eslintrc.json {file_changed}"),
            stdout=subprocess.PIPE,
        )

        if eslint_report.returncode == 1:
            raise Exception(f'{eslint_report.stdout.decode("utf-8")}')
