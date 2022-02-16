import os
import pandas as pd
import glob

LESSONS_PATH = "../../../01-Lesson-Plans"
OUTPUT_PATH = "overview_objectives_data.csv"


def main(lessons_path, output_path=None):

    target_path = os.path.join(lessons_path, "*/*/LessonPlan.md")
    files = glob.glob(target_path)

    data = [extract_data(f) for f in files]

    df = pd.DataFrame(data)
    df = df.set_index("lesson")

    if output_path:
        df.to_csv(output_path)


def extract_data(filename):

    with open(filename, encoding='utf-8') as fin:
        markdown = fin.read()

    outputs = {}
    outputs["lesson"] = filename

    searches = {
        "overview": "## Overview",
        "objectives": "## Class Objectives",
        "priorities": "## Instructor Priorities",
    }

    for key, query in searches.items():

        try:
            overview_index = markdown.index(query) + len(query)
            remaining_text = markdown[overview_index:]
            end_boundary = overview_index + remaining_text.index("##")
            outputs[key] = markdown[overview_index:end_boundary].strip("\n")
        except ValueError:
            pass

    return outputs


if __name__ == "__main__":

    main(LESSONS_PATH, OUTPUT_PATH)
