#!/usr/bin/env bash

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEST_DIR="$PROJECT_ROOT/tests"
OUTPUT_DIR="$TEST_DIR/outputs"

mkdir -p "$OUTPUT_DIR"

PLANNER="$PROJECT_ROOT/planner.py"

if [[ ! -f "$PLANNER" ]]; then
    echo "Error: planner.py not found."
    exit 1
fi

echo "===================================="
echo " Running Course Planner Test Suite"
echo "===================================="

for input in "$TEST_DIR"/*.txt; do

    filename=$(basename "$input")

    # Skip expected output files if you add them later
    [[ "$filename" == expected* ]] && continue

    base="${filename%.txt}"

    output="$OUTPUT_DIR/${base}_output.txt"

    echo
    echo "Running $filename"

    python3 "$PLANNER" \
        "$input" \
        -o "$output"

done

echo
echo "===================================="
echo " All tests completed successfully."
echo " Outputs written to:"
echo "   $OUTPUT_DIR"
echo "===================================="