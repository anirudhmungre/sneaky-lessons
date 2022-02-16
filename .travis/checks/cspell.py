# -*- coding: utf-8 -*-
"""Check Spelling.

This module will run on changed files to check for spelling.

"""

# Add Native Libraries
from pathlib import Path
import subprocess
import shlex


def check_cspell(all_files_changed):
    """Function will check changed files to see if there an spelling errors.

    Args:
        all_files_changed: git diff will grab any files that was changed for the branch the user has changed.

    Returns:
       Will pass silently if no broken links are found.
       Will raise an Exception if a spelling error is found

    """

    cspell_path = Path("./node_modules/.bin/cspell")

    if not cspell_path.exists():
        raise Exception(
            "Cspell is not found. Might need to do a npm install or yarn install"
        )

    for file_changed in all_files_changed:
        # Running cspell
        cspell_report = subprocess.run(
            shlex.split(f"{cspell_path} -u {file_changed}"), stdout=subprocess.PIPE
        )

        if cspell_report.returncode == 1:
            raise Exception(f' \n\n {cspell_report.stdout.decode("utf-8")}')
