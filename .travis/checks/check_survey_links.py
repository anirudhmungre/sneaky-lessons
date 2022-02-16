# -*- coding: utf-8 -*-
"""Check Survey Links.

This module will check surveygizmo survey links to ensure that
each link number matches the lesson plan number. These numbers
can get out-of-sync if units are moved during content development.

Arguments:
    This script can accept a complete LessonPlan.md filepath, or
    it can accept a `--all-lessonplans` flag to search all lesson plan files.
"""

import re
import os
import sys
from pathlib import Path
from argparse import ArgumentParser

unit_number_pattern = r"(?:^##?\s)(\d{1,2}\.\d{1})"
regex_unit_number = re.compile(unit_number_pattern)

feedback_links_pattern = r"(surveygizmo.com/.*section=)(\d{1,2}\.\d{1})"
regex_survey_numbers = re.compile(feedback_links_pattern)


class SurveyException(Exception):
    pass


def get_all_lessonplan_paths():
    """Get all lesson plan paths."""

    return Path().glob("01-Lesson-Plans/**/[1,2,3,4]/LessonPlan.md")


def check_section_numbers(text, filepath):
    """Check Survey Section Numbers.

    Args:
        text (str): LessonPlan.md text.

    Returns:
        None: Exits with error if check fails.

    """

    # Grab the unit number and survey link numbers
    unit_number = regex_unit_number.match(text).group(1)
    survey_numbers = regex_survey_numbers.findall(text)

    # Make sure there are 5 total links
    if len(survey_numbers) != 5:
        raise SurveyException(
            {"message": "There should be 5 survey links", "filepath": filepath}
        )

    # Make sure each link matches the unit number
    for _, survey_number in survey_numbers:
        if survey_number != unit_number:
            raise SurveyException(
                {
                    "message": f"Expected {unit_number} and got {survey_number}",
                    "filepath": filepath,
                }
            )


if __name__ == "__main__":

    parser = ArgumentParser(description=__doc__)

    parser.add_argument(
        "filepath", nargs="?", default=os.getcwd(), help="Path to LessonPlan.md"
    )

    parser.add_argument(
        "--all-lessonplans",
        action="store_true",
        default=False,
        help="Check all LessonPlan.md files",
    )

    args = parser.parse_args()

    try:
        if args.all_lessonplans:

            lessonplan_paths = get_all_lessonplan_paths()

            for filepath in lessonplan_paths:
                with open(filepath) as lp:
                    text = lp.read()
                    check_section_numbers(text, filepath)
        else:
            with open(args.filepath) as LP:
                text = LP.read()
                check_section_numbers(text, args.filepath)
    except SurveyException as e:
        details = e.args[0]
        print(details["message"])
        print(f"Filepath: {details['filepath']}")
    except Exception as e:
        print(e)
        parser.print_help(sys.stderr)
        sys.exit(1)
