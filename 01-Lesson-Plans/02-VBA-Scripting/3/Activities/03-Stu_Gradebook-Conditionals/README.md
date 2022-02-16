# VBA Grade Book

In this activity, you will create a macro that will check a student’s numerical grade, assign them a letter grade, and apply different formatting changes to a cell depending on the value of the student’s grade. 

## Instructions

With `grader.xlsm` as your starting point, create a grade calculator using **conditionals**. This calculator will convert a student's numeric grade into a letter grade and then style the resulting cell accordingly.

Once complete, your script should perform the following:

* If the score is 90 or higher:
  * Add an "A" in the letter grade cell.
  * Fill the Pass/Warning/Fail cell with the color green.
  * Add the text “Pass” to the Pass/Warning/Fail cell.

* If the score is between 80 and 89: 
  * Add a "B" in the letter grade cell.
  * Fill the Pass/Warning/Fail cell with the color green. 
  * Add the text “Pass” to the Pass/Warning/Fail cell.
  * Note that the number range is inclusive, so a score up to 89.9 will stay in the "B" grade range and not be rounded up.

* If the score is between 70 and 79 (inclusive): 
  * Add a "C" in the letter grade cell. 
  * Fill the Pass/Warning/Fail cell with the color yellow.
  * Add the text "Warning" to the Pass/Warning/Fail cell.

* Finally, if the score is below 70:
  * Add an “F” in the letter grade cell. 
  * Fill the Pass/Warning/Fail cell with the color red. 
  * Add the text “Fail” to the Pass/Warning/Fail cell.

## Bonus

Create a second button that resets the grades to the original state and then establishes the previous grade in a row labeled "Last Grade."

—

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
