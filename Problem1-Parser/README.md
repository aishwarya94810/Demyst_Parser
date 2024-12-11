# Fixed Width File Parser

This project contains scripts to read a specification from a JSON file, generate a fixed width file, parse the fixed width file, and convert it to a CSV file. The provided specification includes column names, field offsets, and encoding details.

## Project Structure

/project-directory


## Prerequisites

- Python 3.x
- Docker (optional, for containerized execution)

## Files

### `spec.json`

A JSON file containing the specification for the fixed width file, including column names, field offsets, and encoding details.


The Parser.py Python script that performs the following tasks:

1. Reads the specification from spec.json.
2. Generates a fixed width file if it does not exist.
3. Parses the fixed width file.
4. Writes the parsed data to a CSV file.