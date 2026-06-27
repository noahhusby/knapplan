<!--suppress HtmlDeprecatedAttribute -->
<div align="center">

# cs430-final-project

<p>
  <b>An intelligent course planner. </b>
  <br/>
  ⚠️ This is part of a <a href="https://github.com/noahhusby/university"><strong>larger collection of projects</strong></a> for university. ⚠️
  <br/><br/>
</p>

[![](https://img.shields.io/github/license/noahhusby/cs430-final-project)](https://github.com/noahhusby/cs430-final-project/blob/main/LICENSE)
</div>

## Contributing Members
- Noah Husby
- Anna Gibes
- Bolin Zhu
  
## Running the Program

To execute the planner using the default input and output files:

```bash
python3 planner.py
```

To specify an alternate input file:

```bash
python3 planner.py tests/small.txt
```

To specify the maximum available study hours:

```bash
python3 planner.py tests/small.txt -H 8
```

To specify both an input and output file:

```bash
python3 planner.py tests/small.txt -H 8 -o results.txt
```

## Running the Test Suite

The project includes a Bash script that automatically executes all test cases located in the `tests/` directory.

To run the complete test suite:

```bash
./tests/run_tests.sh
```

The script will:

- Locate every `.txt` file inside the `tests/` directory.
- Execute the planner on each test case.
- Generate an output file for each test.
- Store all generated outputs in `tests/outputs/`.

This provides a simple way to verify the program against multiple input files without manually invoking the planner for each test case.
