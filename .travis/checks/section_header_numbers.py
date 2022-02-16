import re
import os
import sys
from pathlib import Path
from argparse import ArgumentParser


pattern = r"^\s*##+\s?(?P<number>\d+)(\.|:)?\s"
regex = re.compile(pattern)


def get_all_lessonplan_paths():
    """Get all lesson plan paths."""

    return Path().glob("01-Lesson-Plans/**/[1,2,3,4]/LessonPlan.md")


def get_section_numbers(text):
    # Parses LP for section numbers.
    section_numbers = []
    for line in text.split("\n"):
        match = regex.match(line)
        if match:
            section_numbers.append(int(match.group("number")))
    return section_numbers


class HeaderNumbersException(Exception):
    pass


def check_headers(numbers, filepath):

    if not numbers:
        raise HeaderNumbersException(
            {"message": "No header numbers found", "filepath": filepath}
        )

    if len(numbers) != len(set(numbers)):
        raise HeaderNumbersException(
            {"message": f"Duplicate header numbers: {numbers}", "filepath": filepath}
        )

    if sorted(numbers) != numbers:
        raise HeaderNumbersException(
            {"message": f"Header numbers not in order: {numbers}", "filepath": filepath}
        )

    if sorted(numbers) != list(range(min(numbers), max(numbers) + 1)):
        raise HeaderNumbersException(
            {
                "message": f"Nonconsecutive Header numbers: {numbers}",
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
                    section_numbers = get_section_numbers(text)
                    check_headers(section_numbers, filepath)
        else:
            with open(args.filepath) as LP:
                text = LP.read()
                section_numbers = get_section_numbers(text)
                check_headers(section_numbers, args.filepath)
    except HeaderNumbersException as e:
        details = e.args[0]
        print(details["message"])
        print(f"Filepath: {details['filepath']}")
    except Exception as e:
        print(e)
        parser.print_help(sys.stderr)
        sys.exit(1)
