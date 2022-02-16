# 2.3 Scripting Practice in VBA

## Overview

Today’s lesson is the conclusion of our in-depth week on VBA scripting, formatting, and loops.
During the second half of class, students will work on a short project.

## Class Objectives

By the end of this lesson, the students will be able to: 

* Format spreadsheets by using VBA code.
* Loop through a table by using VBA code and check for changes in values.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. If so, we have provided notes within the lesson plan that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Be on the lookout for a **3-Hour Adjustment** note at the top of activities in this lesson plan. If this class is being taught on a weekday, please follow the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class as well.

  * Shortening these activities could potentially prevent students from finishing them, so please remind them to use office hours to clear up any questions.

* In preparation for 3.1, TAs should use today to confirm each student's Python environment. The installation for Python will generally lead to a few issues, especially for Windows users. To help minimize issues, students will be given the installation guide at the beginning of class. Ask that they confirm their install with a TA during the break or today’s office hours. A common issue is the lack of PATH variable set for Anaconda.

* Students will spend much of today's class working in groups on a small-scale project that covers everything that they have learned so far. While this activity may be challenging, it will be a good indicator of how well the students will be able to handle this week's homework.

* Coding can be stressful, and many of your students may be feeling the pressure of learning so much in such a short amount of time. Keep them confident and motivated. Make jokes, and try to keep them smiling. Assure them that perseverance is a critical facet of programming. Any code will function eventually, as long as you keep at it.

* This lesson marks the first time we will be offering students a significant portion of the class time to complete a small-scale project. Be sure to set concrete stopping points where you bring everyone in the class back together to go over individual parts of the code. This ensures no student or group is left behind if they are struggling.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-02-vba-scripting) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Lastly, as a reminder, these slideshows are for **instructor use only**; when distributing slides to students, please first export the slides to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

## 1. Welcome & Star Counter

| Activity Time:       0:35 |  Elapsed Time:      0:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Students and Pep Talk (0:15)</strong></summary>

* Welcome your class to their final day of VBA.

* Before you begin class, send out [Conda_Installation.md](../../../00-Prework/Conda_Installation.md) to make sure their Python environment is installed before the start of the next class.

  * To verify the installation of the Python environments, students can type into their terminal or git-bash:

  ```sh
  conda list | grep jupyter
  # Or to search a specific environment by name,
  # first list all defined virtual environments:
  conda env list
  # Then use the name of an environment as the argument to the -n parameter:
  conda list -n PythonData | grep jupyter
  ```

  * Ask students to find a TA before they leave for the day and to verify that their Python environment is ready for the next class.

  * Ask students to seek out a TA during the break or office hours if they have any installation issues.

  * Assure students that there will be enough time to work through this during the break, so they don't worry about it during the VBA activities.

* Students have probably noticed that this unit has been more challenging than the previous one. They may even be feeling a little stressed out or frustrated. Let them know that everything is going to be okay. For many of them, this week marks their first foray into programming, and no one expects perfection on the first go. Reassure them that as long as they put in the hours to practice and don’t give up hope, they will come out of this week with a strong understanding of basic programming.

* Open the [slideshow](https://docs.google.com/presentation/d/1s1B-vc1c0XmWl0jDrU55LapwJMJrrIViGTxDhrtu_FM/edit?usp=sharing), and go through the slides. Along the way, explain the following:

  * Tell students that programming takes time to learn, and trying to learn everything at the last minute is tough. 

  * Explain that it’s important that students study correctly, and if something takes too long, they should ask for help.

  * Have students try to explain what a `for` loop does. Use the slides to provide a visualization of how a `for` loop works.

  * Have students try to explain what a nested `for` loop does. Use the slides to provide a visualization of how a nested `for` loop works.

  * Finally, answer any questions that students may have.

</details>

<details>
  <summary><strong>✏️ 1.2 Students Do: Star Counter (0:15)</strong></summary>

* Start today's class off with a short warm-up and review of what we covered during our last two meetings.

* We'll be sending students an Excel spreadsheet containing 50 rows of "review data" for Spanish and French online language courses. Using their knowledge of VBA, students will determine the total number of stars that each user gave their respective program; they will then find the total number of stars both programs received.

* The following GIF captures the resulting spreadsheet: 

![StarCounter Gif](Images/StarCounter.gif)

* **Files**

  * [Activities/01-Stu_StarsCounter/README.md](Activities/01-Stu_StarsCounter/README.md)
  * [Activities/01-Stu_StarsCounter/Unsolved/star_counter.xlsm](Activities/01-Stu_StarsCounter/Unsolved/star_counter.xlsm)

* **Instructions**

  * Create a VBA script that counts the number of "Full Stars" per row and enters the count into the Total column. Starter code is provided, but feel free to start from scratch if you want an extra challenge :-).

* **Bonus**

  * Instead of hard-coding the last number of the loop, use VBA to determine the last row automatically (so, do not use `for i = 2 to 51`)

  * Create two charts:

    *  Create a bar chart to check if there is a relationship between program type and rating 

    * Create a line graph to check if there is a relationship between review date and rating

* **Hints**

  * You will need to use a nested `for` loop.

  * You will need to create a variable to hold the number of stars and you will need to continually reset this variable at the start of each row.

</details>

<details>
  <summary><strong>⭐ 1.3 Review: Star Counter (0:05)</strong></summary>

* Open up [01-Stu_StarsCounter/StarCounter_Solved_WithVBA](Activities/01-Stu_StarsCounter/Solved/star_counter_with_VBA.xlsm), go through the code with your class, and check for any questions.

* In your discussion of the basic solution, be sure to point out the following:

  * The code loops through Rows 2 to 51 in our first loop.

  * For each row in the first loop, the code then loops through Columns 4 to 8 for that row within the second loop.

  * Every time we find a "Full-Star" value within a column, we add one to our `StarCounter`.

  * The value of `StarCounter` is placed within a new cell after the conclusion of the second loop, and then we move on to the next value in the first loop.

  ```vb
  Sub StarCounter()

    ' Create a variable to hold the StarCounter. We will repeatedly use this.
    dim StarCounter as Integer

    ' Loop through each row
    for i = 2 to 51

      ' Initially set the StarCounter to be 0 for each row
      StarCounter = 0

      ' While in each row, loop through each star column
      for j = 4 to 8

        ' If a column contains the word "Full-Star"...
        if (Cells(i, j).value = "Full-Star") then

          ' Add 1 to the StarCounter
          StarCounter = StarCounter + 1

        end if

      Next j

      ' Once we've iterated through each column in row i, print the value in the total column.
    Cells(i, 9).value = StarCounter

    Next i

  End Sub
  ```

* Data Source: Dataset generated by Trilogy Education Services, LLC.


</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+%26+Star+Counter&lessonpageTitle=Scripting+Practice+in+VBA&lessonpageNumber=2.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F02-VBA-Scripting%2F3%2FLessonPlan.md)</sub>

- - -

## 2. VBA Grade Book

| Activity Time:       0:25 |  Elapsed Time:      1:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: VBA Formatting (0:05)</strong></summary>

* Not only can we use VBA to change the values within cells, but we can also easily code in formatting with a variety of functions.

* The following image captures four unformatted columns:

  ![Without Formatting](Images/WithoutFormatting-VBA.png)

* Open [02-Ins_Formatter/formatter.xlsm](Activities/02-Ins_Formatter/Solved/formatter.xlsm) in Excel, and explain to students how we can use VBA to fill each of these cells with their respective colors.

  * Within the VBA editor, write the following code:

  ```vba
  Sub formatter()

    ' Set the Font color to Red
    Range("A1").Font.ColorIndex = 3

    ' Set the Cell Colors to Red
    Range("A2:A5").Interior.ColorIndex = 3

  ```

* Check if your students can guess what this code will do.

  * “The text in cell A1 will be colored red.”

  * “The interiors of cells A2 to A5 will be filled with red as well.”

  * The following GIF demonstrates the result of our code:

  ![Paint the Cells Red](Images/PaintTheCellsRed.gif)

  * Your students may be wondering about the value "3" and how it corresponds to the color red. The answer is that Excel has divided its palette into 56 colors and assigned each color a numeric value. Your students can find a helpful chart for these values by following [this link](http://dmcritchie.mvps.org/excel/colors.htm).

* Now that your students have a guide to the colors, have them help you create the code that will color Columns B, C, and D.

  * The following GIF captures the result of our code:

  ![Paint the Cell Rainbow](Images/PaintTheCellRainbow.gif)

  * Point out how the code is mostly the same as when we painted the cells red; the only values that change are the cells referenced and the numeric color values.

* Check if your students have any questions regarding VBA formatting before moving on to the next activity.

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: VBA Grade Book (0:15)</strong></summary>

* Now, your students will create an Excel application that checks a fictional student's grade and performs actions based on the grade.

* The following GIF captures this application in action:

  ![Grade Book](Images/GradeBook.gif)

* Once you have guided students through an example of how this application will function, send out the starter file and instructions.

* **Files**

  * [Activities/03-Stu_Gradebook-Conditionals/README.md](Activities/03-Stu_Gradebook-Conditionals/README.md)
  * [Activities/03-Stu_Gradebook-Conditionals/Unsolved/grader.xlsm](Activities/03-Stu_Gradebook-Conditionals/Unsolved/grader.xlsm)

* **Instructions**

  * Using `grader.xlsm` as a starting point, create a grade calculator using **conditionals**. This calculator will convert a student's numeric grade into a letter grade and then style the resulting cell accordingly.

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

* **Bonus**

  * Create a second button that resets the grades to the original state and then establishes the previous grade in a row labeled "Last Grade."

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Grade Book (0:05)</strong></summary>

* Open  [03-Stu_Gradebook-Conditionals/graderSolved.xlsm](Activities/03-Stu_Gradebook-Conditionals/Solved/grader.xlsm), go through the code with your class, and check for any questions.

* While discussing the solution, be sure to cover the following points:

  * Point out how you are modifying the formatting and value of Cells B2 and C2 based on the value stored within A2. When the value of A2 changes, so does the formatting and value of Cells B2 and C2.

  * Due to the number of possible inputs, our code includes plenty of conditionals to account for every possible letter grade, for example:

```vb
Sub GradeBook()

  ' Check if the student's grade is greater than or equal to 90...
  If Cells(2, 2).Value >= 90 Then

      ' Establish that the grade is Passing
      Cells(2, 3).Value = "Pass"

      ' Color the Passing grade green
      Cells(2, 3).Interior.ColorIndex = 4

      ' Set the letter grade to "A"
      Cells(2, 4).Value = "A"

  ' Check if the student's grade is greater than or equal to 80...
  ElseIf Cells(2, 2).Value >= 80 Then

      ' Establish that the grade is Passing
      Cells(2, 3).Value = "Pass"

      ' Color the Passing grade green
      Cells(2, 3).Interior.ColorIndex = 4

      ' Set the letter grade to "B"
      Cells(2, 4).Value = "B"
```

  * For the bonus, the code needs to collect the previous values of A2, B2, and C2 before moving the values into three new cells and then clearing the information stored in Row 2.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+VBA+Grade+Book&lessonpageTitle=Scripting+Practice+in+VBA&lessonpageNumber=2.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F02-VBA-Scripting%2F3%2FLessonPlan.md)</sub>

- - -

## 3. Checkerboard - Coding Logic

| Activity Time:       0:20 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>👥 3.1 Partners Do: Checkerboard (0:15)</summary></strong>

* Emphasize to students that this next activity is designed to help them understand coding logic; the VBA formatting involved is secondary to the underlying logic.

* Students must create an 8-by-8 checkerboard pattern using only VBA scripts. This means creating a script that formats cells based on whether they are even or odd. Open [04-Stu_Checkerboard-CodingLogic/checkerboard_solved.xlsm](Activities/04-Stu_Checkerboard-CodingLogic/Solved/checkerboard.xlsm), and demonstrate the solution.

  * The following GIF captures the demonstration of the solution.

  ![CheckerBoard](Images/CheckerBoard.gif)

* **Instructions**

  * Using VBA scripts, create an 8-by-8 grid with alternating red and black squares.

* **Hints**

  * You will need to use nested `for` loops, conditionals, the `MOD()` function, and formatting to create the board.

  * This is a tricky problem! Try to pseudocode a plan first.

    * Unlike previous activities, this one can be solved in many different ways. While some methods may be more efficient, simply finding a solution to the problem is a great start!

</details>

<details>
  <summary><strong>⭐ 3.2 Review: Checkerboard (0:05)</strong></summary>

* Open the [04-Stu_Checkerboard-CodingLogic/checkerboard_solved.xlsm](Activities/04-Stu_Checkerboard-CodingLogic/Solved/checkerboard.xlsm), review the code with your class, and check for any questions.

* While discussing this activity's solution, note that this is not the “correct” or “optimal” way to solve this problem. Check in with students as you go, and ask if they did anything differently.

* Be sure to cover the following points:

  * This solution uses two `for` loops, a variable, and an `if-else` conditional.

  * With each iteration of our loops, the variable goes up by one.

  * If the variable is even, the cell is formatted to be black. Otherwise, it is formatted to be red.

```vb
Sub CheckerBoard()

  ' Setup a counter to track cell number
  Dim cellnumber as Integer
  Dim i, j As Integer
  cellnumber = 1

  ' Loop through each row of the board
  For i = 1 to 8

    ' Loop through each column of the board
    For j = 1 to 8

      ' If we are on a cell that is divisible by 2 then color it black
      If (cellnumber Mod 2 = 0) then

        Cells(i, j).Interior.ColorIndex = 1

      ' Otherwise color it red
      Else

        Cells(i, j).Interior.ColorIndex = 3

      End if

      ' Add one to our cell number each time
      cellnumber = cellnumber + 1

    Next j

    ' Whenever we start on a new row, we also add one to the cell number (to create the alternation)
    cellnumber = cellnumber + 1

  Next i

End Sub
```

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Checkerboard+-+Coding+Logic&lessonpageTitle=Scripting+Practice+in+VBA&lessonpageNumber=2.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F02-VBA-Scripting%2F3%2FLessonPlan.md)</sub>

- - -

## 4. Card Checker - Cell Comparison

| Activity Time:       0:35 |  Elapsed Time:      1:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Looking to the Next Cell (0:05)</strong></summary>

* When looping through rows and/or columns, it can be necessary to check for changes and then run some alternative code based on those changes.

  * For example, you might want to count how many cells in a column contain a specific value. One way to do this is to loop through the cells, comparing each cell to the one below it, and add 1 to a counter if both cells match.

* Open up [05-Ins_NextCells/NextCells.xlsx](Activities/05-Ins_NextCells/Solved/next_cells.xlsx), and copy the code from [05-Ins_NextCells/NextCells.vbs](Activities/05-Ins_NextCells/Solved/next_cells.vbs) into the VBA editor.

* The following image captures the contents of the Excel file. 

![CheckingCells](Images/CheckingCells.png)

* Go through the code with your students.

  * Point out how we are looping through the rows in the first column and printing a message to the screen whenever the value changes from one row to the next.

  * Feel free to change the column variable to 2 and then 3 to show students how this code is checking for changes against the previous value (Texas versus New York, New York versus Nebraska, Nebraska versus Texas)

* Check for any questions before moving on to the next activity.

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Card Checker - Cell Comparison (0:20)</strong></summary>

* This activity is designed to solidify how important it is to check for changes in cell values and perform calculations whenever those changes occur.

* Students will use a VBA script to create a summary table based on a series of values stored in an Excel spreadsheet, as captured in the following GIF:

![CreditCardChecker](Images/CreditCardChecker.gif)

* Once you have demonstrated to students what they will be working to accomplish, send out the data file and instructions for this activity.

* **Files**

  * [Activities/06-Stu_CreditCardChecker-CellComparison/README.md](Activities/06-Stu_CreditCardChecker-CellComparison/README.md)
  * [Activities/06-Stu_CreditCardChecker-CellComparison/Unsolved/credit_charges.xlsm](Activities/06-Stu_CreditCardChecker-CellComparison/Unsolved/credit_charges.xlsm)

* **Instructions**

  * Create a VBA script that will process the credit card purchases by identifying each of the unique brands listed.

  * For the _basic_ assignment, create a single pop-up message for each of the credit card brands listed by looping through the list.

  * For the _advanced_ assignment, add up the total value of credit card purchases for each brand, and put the information in the summary table.

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Card Checker (0:10)</strong></summary>

* Open up [06-Stu_CreditCardChecker-CellComparison/Solved/credit_charges.xlsm](Activities/06-Stu_CreditCardChecker-CellComparison/Solved/credit_charges.xlsm), review the code with your class, and check for any questions.

* Cover the following key points in your review of this activity:

  * The code loops through all of the rows containing credit card purchases.

  * The code then checks for instances when the contents of a cell in Column A do not match the contents of the cell in the following row.

  * Whenever the contents of the two cells do not match, we print the contents of the first cell to a message box before continuing.

  ```vb
  Sub credit_card()

    ' Set an initial variable for holding the brand name
    Dim Brand_Name As String

    ' Loop through all credit card purchases
    For i = 2 To 101

      ' Check if we are still within the same credit card brand, if we are not...
      If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

        ' Message Box the unique Bank Name
        MsgBox(Cells(i, 1).Value)

      End If

    Next i

  End Sub
  ``

* Cover the following key points for the advanced solution:

  * The code is very similar to the basic solution. The main difference is that it is now adding to the `Brand_Total` variable whenever a different value in Column A is _not_ found.

  * Whenever a change _is_ found, the application will add the value of the final row of the brand to the total before placing the `Brand_Name` and `Brand_Total` into a summary table.

  * The `Summary_Table_Row` variable keeps track of the row where we should print the next line of data so that there is no overwriting.

  ```vb
  Sub credit_card()

    ' Set an initial variable for holding the brand name
    Dim Brand_Name As String

    ' Set an initial variable for holding the total per credit card brand
    Dim Brand_Total As Double
    Brand_Total = 0

    ' Keep track of the location for each credit card brand in the summary table
    Dim Summary_Table_Row As Integer
    Summary_Table_Row = 2

    ' Loop through all credit card purchases
    For i = 2 To 101

      ' Check if we are still within the same credit card brand, if it is not...
      If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

        ' Set the Brand name
        Brand_Name = Cells(i, 1).Value

        ' Add to the Brand Total
        Brand_Total = Brand_Total + Cells(i, 3).Value

        ' Print the Credit Card Brand in the Summary Table
        Range("G" & Summary_Table_Row).Value = Brand_Name

        ' Print the Brand Amount to the Summary Table
        Range("H" & Summary_Table_Row).Value = Brand_Total

        ' Add one to the summary table row
        Summary_Table_Row = Summary_Table_Row + 1
      
        ' Reset the Brand Total
        Brand_Total = 0

      ' If the cell immediately following a row is the same brand...
      Else

        ' Add to the Brand Total
        Brand_Total = Brand_Total + Cells(i, 3).Value

      End If

    Next i

  End Sub
  ```
* Data Source: Dataset generated by Trilogy Education Services, LLC.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Card+Checker+-+Cell+Comparison&lessonpageTitle=Scripting+Practice+in+VBA&lessonpageNumber=2.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F02-VBA-Scripting%2F3%2FLessonPlan.md)</sub>

- - -

## Break (0:40)

| Activity Time:       0:40 |  Elapsed Time:      2:35  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Reduce break time from 40 minutes to 15 minutes.

- - -

## 5. U.S. Census

| Activity Time:       1:15 |  Elapsed Time:      3:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: U.S. Census Setup (0:05)</strong></summary>

* For the rest of class, students will work in small groups to create a VBA script that takes an Excel workbook with multiple sheets of U.S. Census data, formats each sheet to improve readability, and then combines all of the data into a single table.

* Let students know that we’ll use Census data throughout the course. Later on, students will learn how to access the data themselves, but for this exercise, we will use precollected data from the Census API.

* Students should place one person from their group in charge of writing the code. This arrangement promotes collaboration and ensures that students work at the same general pace.

* Let students know that this activity will be divided into parts, and we will review each part as a class before moving on.

</details>

<details>
  <summary><strong>✏️ 5.2 Groups Do: U.S. Census - Part 1 (0:25)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Groups Do** activity, and continue to the Review activity.

* Open up and share the [unsolved](Activities/07-Stu_Census_Pt1/Unsolved/census_data_2016-2019_pt1.xlsm) version of the data. Provide students with a brief description of the workbook, which is captured in the following image:

![Census Part 1 Unsolved](Images/Census_pt1_unsolved.png)

  * This data is not ideally formatted for analysis. For example, the year is contained in the sheet names instead of cells, and the “Place” column contains both the county and state. So, in this activity, the students will create a VBA script to parse the data into a more usable format. 

* Open the solution file [Activities/07-Stu_Census_Pt1/Solved/census_data_2016-2019_pt1.xlsm](Activities/07-Stu_Census_Pt1/Solved/census_data_2016-2019_pt1.xlsm) and show students what they are working towards. Share the following image with the students to use as a reference.

![Census Part 1 Solved](Images/Census_pt1_solved.png)

  * It’s recommended that students first write the code to format a single sheet; then, once they’ve successfully formatted one sheet, modify the code to loop through and format the other worksheets in the workbook.   

* After answering any questions from students, send out the following files and instructions.

* **Files**

  * [Activities/07-Stu_Census_Pt1/README.md](Activities/07-Stu_Census_Pt1/README.md)
  * [Activities/07-Stu_Census_Pt1/Unsolvedcensus_data_2016-2019_pt1.xlsm](Activities/07-Stu_Census_Pt1/Unsolved/census_data_2016-2019_pt1.xlsm)

* **Instructions**

 1. Extract the number before the phrase "\_census_data" to figure out the year.

 2. Add the year to the first column of each spreadsheet.

 3. Split the "Place" column into "County" and "State".

 4. Convert the household and per capita income columns to currency values for all cells.

* **Hints**

  * We will need to use a [For Each loop](https://docs.microsoft.com/en-us/dotnet/visual-basic/language-reference/statements/for-each-next-statement); in Excel, we can use `For Each` to loop over each worksheet in the workbook, no matter how many there are. The syntax to loop over all worksheets is provided below:

  ```vb
    For Each ws In Worksheets
      ' do stuff with the worksheet (ws) '
    Next ws

  ```

  * Get the formatting right on one sheet before creating a loop that formats each sheet within your workbook.

  * If you’d like a helpful resource about looping through all worksheets in a workbook, check out this [documentation](https://support.microsoft.com/en-us/help/142126/macro-to-loop-through-all-worksheets-in-a-workbook).

</details>

<details>
  <summary><strong>⭐ 5.3 Review: U.S. Census - Part 1 (0:10)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend 20 minutes on this activity.

  * Use this review section as guidance for talking points as you live-code with the students.

  * Be sure to take your time and answer all student questions along the way.

* Open up [07-Stu_Census_Pt1/census_data_2016-2019_pt1.xlsm](Activities/07-Stu_Census_Pt1/Solved/census_data_2016-2019_pt1.xlsm), review the code with your class, and check for any questions.

* Cover the following key points:

  * To loop through all worksheets using VBA, we use a `For Each` loop that loops through the built-in array of `Worksheets`.

```vb
Sub Census_pt1()

    ' --------------------------------------------
    ' LOOP THROUGH ALL SHEETS
    ' --------------------------------------------
    For Each ws In Worksheets
```

  * To collect the year, the code looks at the name of the current worksheet, `ws.Name`, and then splits the name where underscores are used. The code can then place the extracted year by referencing `CensusYear(0)`, since the year is stored at index 0 in the `CensusYear` array.  Note that the code will cause an error if the array is named `Year`, which is why we use a more specific variable name.

```vb
        ' Create a Variable to Hold File Name, Last Row, and Year
        Dim WorksheetName As String

        ' Determine the Last Row
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

        ' Grabbed the WorksheetName
        WorksheetName = ws.Name
        'MsgBox WorksheetName

        ' Split the WorksheetName
        CensusYear = Split(WorksheetName, "_")
        'MsgBox CensusYear(0)

        ' Add a Column for the Year
        ws.Range("A1").EntireColumn.Insert

        ' Add the word Year to the First Column Header
        ws.Cells(1, 1).Value = "Year"

        ' Add the Year to all rows
        ws.Range("A2:A" & LastRow) = CensusYear(0)
```

  * To collect the place and split it into two columns for county and state, the code adds a new “State” column after "Place" and then renames the headers. Next, it loops through the "Place" column and splits the contents at the comma; then, it places the County value at index 0 into the "County" cell and the State value at index 1 into the "State" cell.

```vb
        ' --------------------------------------------
        ' SPLIT COUNTY AND STATE
        ' --------------------------------------------

        ' Add the State Column after County
        ws.Range("C1").EntireColumn.Insert
        
        ' Rename Place to County
        ws.Cells(1, 2).Value = "County"
        
        ' Label State Column
        ws.Cells(1, 3).Value = "State"

        ' Split County and State and store values in appropriate
        ' column by looping through and renaming each
        For i = 2 To LastRow
            CountyState = ws.Cells(i, 2).Value
            CSSplit = Split(CountyState, ", ")
            'MsgBox CSSplit(1)
            ws.Cells(i, 2).Value = CSSplit(0)
            ws.Cells(i, 3).Value = CSSplit(1)
            ' MsgBox Cells(i, 2)
            ' MsgBox CSSplit(0)

        Next i
```

  * Finally, to add the currency number format to our income data, the code simply loops through all rows from Row 2 on and the two columns that refer to income&mdash;now the sixth and seventh columns in the sheet&mdash;and applies the "Currency" style.

```vb
        ' --------------------------------------------
        ' CORRECT THE CURRENCY FORMAT
        ' --------------------------------------------

        ' Add the currency
        For i = 2 To LastRow

            ' For columns Household and Per Capita Income only
            For j = 6 To 7

                ws.Cells(i, j).Style = "Currency"

            Next j

        Next i
```

* Send out the code for this part of the activity so that any groups that may have fallen behind can move on to Part 2.

Data Source: [U.S. Census API - ACS 5-Year Estimates 2016-2019](https://www.census.gov/data/developers/data-sets/census-microdata-api.ACS_5-Year_PUMS.html)

</details>

<details>
  <summary><strong>✏️ 5.4 Groups Do: U.S. Census - Part 2 (0:25)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Groups Do** activity, and continue to the Review activity.

* In this second part of the project, students will be combining all the worksheets into one massive table in a new sheet.

  * They will need to loop through each sheet, select each row of data, and move it into the new sheet.

  * The following image captures the resulting spreadsheet:

![Census Part 2](Images/CensusPart2.png)

* Once you’ve described the solved version of the activity, send out the following file and instructions:

* **Files**

  * [08-Stu_Census_Pt2/census_data_2016-2019_pt2.xlsm](Activities/08-Stu_Census_Pt2/Unsolved/census_data_2016-2019_pt2.xlsm)

* **Instructions**

  1. Loop through every worksheet, and select the year contents.

  2. Copy the year contents, and paste them into the `Combined_Data` tab

</details>

<details>
  <summary><strong>⭐ 5.5 Review: U.S. Census - Part 2 (0:10)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend 20 minutes on this activity.

  * Use this review section as guidance for talking points as you live-code with the students.

  * Be sure to take your time and answer all student questions along the way.

* Open up [Activities/08-Stu_Census_Pt2/census_data_2016-2019_pt2.xlsx](Activities/08-Stu_Census_Pt2/Unsolved/census_data_2016-2019_pt2.xlsm) and [08-Stu_Census_Pt2/census_pt2.vbs](Activities/08-Stu_Census_Pt2/Solved/census_pt2.vbs), and combine them into one file. Now, review the combined solution with your class, and check for any questions.

* Cover the following key points for this part of the activity:

  * The code sets a variable for the location of the "Combined_Data" worksheet in the workbook. If this sheet has not been created, the code should return an error.

  * Once again, the code uses a `For Each` loop to move through each worksheet in the workbook.

  * The code finds the final row on each sheet and then collects all the data on the sheet before transplanting it into the combined sheet.

```vb
Sub Census_pt2()

    ' Add a sheet named "Combined Data"
    Sheets.Add.Name = "Combined_Data"
    'move created sheet to be first sheet
    Sheets("Combined_Data").Move Before:=Sheets(1)
    ' Specify the location of the combined sheet
    Set combined_sheet = Worksheets("Combined_Data")

    ' Loop through all sheets
    For Each ws In Worksheets

        ' Find the last row of the combined sheet after each paste
        ' Add 1 to get first empty row
        lastRow = combined_sheet.Cells(Rows.Count, "A").End(xlUp).Row + 1

        ' Find the last row of each worksheet
        ' Subtract one to return the number of rows without header
        lastRowYear = ws.Cells(Rows.Count, "A").End(xlUp).Row - 1

        ' Copy the contents of each year sheet into the combined sheet
        combined_sheet.Range("A" & lastRow & ":K" & ((lastRowYear - 1) + lastRow)).Value = ws.Range("A2:K" & (lastRowYear + 1)).Value

    Next ws

    ' Copy the headers from sheet 1
    combined_sheet.Range("A1:K1").Value = Sheets(2).Range("A1:K1").Value
    
    ' Autofit to display data
    combined_sheet.Columns("A:K").AutoFit

End Sub
```

Data Source: [U.S. Census API - ACS 5-Year Estimates 2016-2019](https://www.census.gov/data/developers/data-sets/census-microdata-api.ACS_5-Year_PUMS.html)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Crypto+Kennel&lessonpageTitle=Scripting+Practice+in+VBA&lessonpageNumber=2.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F02-VBA-Scripting%2F3%2FLessonPlan.md)</sub>

- - -

## 6. End Class & Python Install Check

| Activity Time:       0:10 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>🎉 6.1 Python Installation Check (0:10)</strong></summary>

* ⏰ **3-Hour Adjustment**: Reduce time to 5 minutes.

* Before dismissing class, ask students to verify their Python installations:
  * Windows: Click Start, and search or select Anaconda Navigator from the menu.
  * macOS: Click Launchpad, then select Anaconda Navigator, or use Cmd+Space to open Spotlight Search and type “Navigator” to initiate the program.
* If any students cannot open Anaconda Navigator, ask them to stay behind for office hours.

* During office hours, send out the link to the [Anaconda Install Guide](../../../00-Prework/Conda_Installation.md), and have the students run through the Anaconda installation guide.

* Instructional staff should help guide students through the install process during this time.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=6+-+End+Class+%26+Python+Install+Check&lessonpageTitle=Scripting+Practice+in+VBA&lessonpageNumber=2.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F02-VBA-Scripting%2F3%2FLessonPlan.md)</sub>

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
