"""
CS430 - Intelligent Course Planner

Reads course data from ./input.txt, validates the input,
runs the optimization algorithm,
and writes the results to output.txt
"""
import argparse
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import List

LOGGER = logging.getLogger(__name__)

@dataclass
class Course:
    name: str
    hours: int
    benefit: int

@dataclass
class PlannerResult:
    selected_courses: List[Course]
    total_hours: int
    total_benefit: int

class InputFormatError(Exception):
    """Raised when the input file format is invalid."""

def read_input(file_path: Path) -> List[Course]:
    """Reads the input file.

    Expected format:
        CourseName Hours Benefit

    Example:
        CS330 5 2
        CS331 8 4
        CS450 10 5
    """

    if not file_path.exists():
        raise FileNotFoundError(f"Input file '{file_path}' was not found.")

    courses: List[Course] = []


    with file_path.open("r", encoding="utf-8") as infile:
        for line_number, raw_line in enumerate(infile, start=1):
            line = raw_line.strip()
            # Skip blank lines
            if not line:
                continue
            tokens = line.split()
            if len(tokens) != 3:
                raise InputFormatError(
                    f"Line {line_number}: expected 3 fields "
                    f"(course hours benefit)."
                )
            name, hours_str, benefit_str = tokens
            try:
                hours = int(hours_str)
                benefit = int(benefit_str)
            except ValueError:
                raise InputFormatError(
                    f"Line {line_number}: hours and benefit must be integers."
                )

            if hours <= 0:
                raise InputFormatError(
                    f"Line {line_number}: hours must be positive."
                )

            if benefit < 0:
                raise InputFormatError(
                    f"Line {line_number}: benefit cannot be negative."
                )

            course = Course(name, hours, benefit)
            courses.append(course)
    LOGGER.info("Successfully read %d courses.", len(courses))
    for c in courses:
        LOGGER.info(
            "Course=%s Hours=%d Benefit=%d",
            c.name,
            c.hours,
            c.benefit,
        )

    return courses

def optimize_courses(
        courses: List[Course],
        max_hours: int,
) -> PlannerResult:
    """
    Placeholder optimization algorithm.
    0/1 Knapsack is probably the way to go here? - Noah
    """
    # TODO: Replace this with the actual optimization algorithm.

    LOGGER.info("Running placeholder optimization...")

    return PlannerResult(
        selected_courses=[],
        total_hours=0,
        total_benefit=0,
    )


def write_output(
    file_path: Path,
    result: PlannerResult,
) -> None:
    with file_path.open("w", encoding="utf-8") as outfile:
        outfile.write("Selected Courses\n")
        outfile.write("----------------\n")
        if not result.selected_courses:
            outfile.write("None\n")
        else:
            for course in result.selected_courses:
                outfile.write(
                    f"{course.name} "
                    f"(Hours={course.hours}, Benefit={course.benefit})\n"
                )

        outfile.write("\n")
        outfile.write(f"Total Hours: {result.total_hours}\n")
        outfile.write(f"Total Benefit: {result.total_benefit}\n")

    LOGGER.info("Results written to %s", file_path)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="CS430 Intelligent Course Planner"
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        default="input.txt",
        help="Input file containing course data.",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="output.txt",
        help="Output file (default: output.txt).",
    )

    parser.add_argument(
        "-H",
        "--hours",
        type=int,
        help="Maximum available study hours.",
    )

    return parser.parse_args()

def main() -> None:
    args = parse_args()

    # If H wasn't provided on the command line, ask interactively.
    if args.hours is None:
        try:
            max_hours = int(input("Enter maximum study hours (H): "))
        except ValueError:
            print("Maximum study hours must be an integer.")
            return
    else:
        max_hours = args.hours

    if max_hours <= 0:
        print("Maximum study hours must be positive.")
        return

    input_path = Path(args.input_file)
    output_path = Path(args.output)

    try:
        courses = read_input(input_path)

        result = optimize_courses(
            courses,
            max_hours,
        )

        write_output(
            output_path,
            result,
        )

        print("Program completed successfully.")

    except FileNotFoundError as ex:
        print(ex)

    except InputFormatError as ex:
        print(f"Input Error: {ex}")

    except Exception as ex:
        print(f"Unexpected Error: {ex}")

if __name__ == "__main__":
    main()