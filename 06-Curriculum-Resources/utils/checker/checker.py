import sys
import click
from pathlib import Path


@click.command()
@click.option('--ipath', '-i', default=".", help="Input Path")
def cli(ipath):
    # Create Path
    activities_path = Path(ipath)

    # Add folder names to the path if needed
    if activities_path.name != "Activities":
        activities_path = activities_path / "Activities"

    # Error Checking
    if not activities_path.exists():
        print("ERROR: Activities folder not in path")
        sys.exit(3)

    passed = True
    for activity in activities_path.iterdir():
        readme = activity / "README.md"
        if not readme.is_file():
            print(f"README not found in {activity}")
            passed = False

    if not passed:
        sys.exit(3)
    else:
        print("Every activity has a README.md file!")


if __name__ == '__main__':
    cli()
