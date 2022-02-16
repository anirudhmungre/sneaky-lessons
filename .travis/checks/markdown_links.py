# -*- coding: utf-8 -*-
"""Check Markdown Links.

This module will run on all files to try markdown links.

"""

# Add Native Libraries
from pathlib import Path
import subprocess
import shlex


def check_markdown_links():
    """Function will check all markdown files to see if there are any broken links.

    Args:
        None

    Returns:
       Will pass silently if no broken links are found.
       Will raise an Exception if a broken links is found

    """

    markdown_link_path = Path("./node_modules/.bin/md-report")

    if not markdown_link_path.exists():
        raise Exception(
            "markdown-link-reporter is not found. Might need to do a npm install or yarn install"
        )

    # Running markdown link reporter
    run_md_report = subprocess.run(
        shlex.split(f"{markdown_link_path}"), stdout=subprocess.PIPE
    )

    if run_md_report.returncode == 1:
        raise Exception(f'{run_md_report.stdout.decode("utf-8")}')
