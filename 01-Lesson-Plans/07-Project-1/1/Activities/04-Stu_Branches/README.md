# Working with Branches

This activity gives students further experience diagramming branches, and with creating and merging them on the command line.

## Instructions

### Diagramming

Refer to the series of `git` commands your instructor walked through in lecture. Draw a branch diagram describing the commits on `main` and `data_analysis`.

### Practicing Branch Workflows

Next, get some practice working with branches by following these instructions:

 * Create a new directory, and initialize a Git repo inside it.

 * Create a `hello.py` that simply prints `"Hello, World"`.

 * Add and commit your `hello.py`.

 * Create a new branch, called `helpers`.
 
 * Create a file called `helpers.py`.

 * Inside of `helpers.py`, write a function, called `greet`, that accepts a name and prints: `"Hello, <name>"`. For example, `greet("Jane")` would print: `"Hello, Jane"`.

 * Add and commit your changes.
 
 * Inside of `hello.py`, import `greet` from `helpers.py`, and use it print `"Hello, World"`.

 * Move back to your `main` branch.

 * Merge `main` with your `helpers` branch.

 * Delete your `helpers` branch.

 ---

 © 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

