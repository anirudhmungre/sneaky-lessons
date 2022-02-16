# Checker Script

This script will allow you to check for production related things

## Installation

```
pip install -e .
```

## Usage

* Help menu


```
checker --help

Usage: checker [OPTIONS]

Options:
  -i, --ipath TEXT  Activities Input Path
  --help            Show this message and exit.
```

* Validate that readme files exist in a day folder


```
cd 01-Lesson-Plans/03-Python/1
checker
```

* Validate that readme files exist using a path


```
unsolve -i 03-Python/1/Activities
```
