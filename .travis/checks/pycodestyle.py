# -*- coding: utf-8 -*-
"""Check Python.

This module will run on changed files to check for Python linting.

"""

# Add Native Libraries
import subprocess
import shlex


def check_pycodestyle(python_files_changed):
    """Function will check changed python files to see if there an linter errors/warnings.

    Args:
        python_files_changed: git diff will grab any python files that was changed for the branch the user has changed.

    Returns:
       Will pass silently if no broken links are found.
       Will raise an Exception if a linting error/warning is found

    """

    for file_changed in python_files_changed:
        # Running pycodestyle
        pycodestyle_report = subprocess.run(
            shlex.split(f"pycodestyle --show-source {file_changed}"),
            stdout=subprocess.PIPE,
        )

        if pycodestyle_report.returncode == 1:
            raise Exception(f'{pycodestyle_report.stdout.decode("utf-8")}')
