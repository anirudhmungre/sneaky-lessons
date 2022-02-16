# 1.2: Data Fundamentals in Excel

## Overview

In this class, students will be introduced to advanced features in Microsoft Excel, including pivot tables, lookups, and conditional formatting.

## Class Objectives

By the end of this lesson, the students will be able to: 

* Demonstrate basic Excel navigation and functionality.
* Explain the value and use of pivot tables.
* Use VLOOKUPs and HLOOKUPs.
* Implement conditional formatting based on logical rules.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Welcome to Day 2! Hope your first day was fun. Today's session marks the first "real" class. As will be the case throughout this program, you will guide students through a series of increasingly complex exercises.

* Today's class is entirely focused on Microsoft Excel. Admittedly, Microsoft Excel isn't the most exciting subject to teach. However, it is critically important that your students, as future analysts, master even the tools used less commonly by everyday users. You might be surprised by the number of your students who will struggle with creating advanced conditionals even in Microsoft Excel.

* Spend time before class practicing your workflow. Opening and navigating through multiple spreadsheets can easily become cumbersome. Make sure that you are well aware of the layout and key takeaways for all activities before class. There's a "magic" feeling in a class when things flow seamlessly, but that magic requires active preparation on your part.

* As you talk through today's exercises, find ways to comment on the benefits and limitations of Microsoft Excel versus the course’s future topics. Excel has capabilities that will prepare students to use Python, JavaScript, and SQL.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

* Please refer to our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-01-excel) for answers to questions that are frequently asked by students of this program. If you have any recommendations for additional questions and answers, feel free to log an issue or a pull request with your desired additions.

* Remember that today's slideshow includes information that you’ll need to share with your class. Specifically, two slides will require you to send links to your student-facing repository and class recordings.

* Finally, as a reminder, these slideshows are for **instructor use only**. When distributing slides to students, please first export the slides to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

## 1. Instructor Presentation

| Activity Time:       0:35 |  Elapsed Time:      0:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Fundamentals of Data in Excel Slideshow (0:05)</strong></summary>

* You may choose to open up the [slideshow](https://docs.google.com/presentation/d/1fvwswAFXdzbOyjS7t7FsNdOeS3j4VzPiwflIJ1id2sI/edit?usp=sharing), and step through the first few slides to facilitate your welcome to the class. Be sure to cover the following talking points:

  * Explain that before we start today's class, it is important that we look at our class repository and Zoom video feed.

  * Show the students their class git repository on either the Github or GitLab site, depending on your program.

    * Explain that this is where **all** classroom content and homework assignments will be posted.

  * Show the students their Zoom video feed.

    * Explain that this is where all classroom recordings will be uploaded automatically.

  * Explain that we will take a few minutes to review the core concepts from yesterday's class.

  * Ask a student to explain the two aspects of data analytics.

    * Explain that at its core, data analytics is about storytelling and truth-telling.

  * Ask another student to list the steps in the analytics paradigm.

    * Explain that the analytics paradigm includes the following steps:

      1. Decompose the “ask.”

      2. Define strategy and metrics.

      3. Identify the data sources.

      4. Build a data-retrieval plan.

      5. Retrieve the data.

      6. Assemble and clean the data.

      7. Analyze data for trends.

      8. Acknowledge limitations of the analysis.

      9. Make the call or tell the story.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Excel Playground (0:05)</strong></summary>

* You may choose to open up the slideshow, and step through the next few slides to accompany the beginning of this next activity. Be sure to cover the following talking points:

  * Explain that this unit will cover fundamental concepts in programming and statistics. The easiest way to teach these fundamentals is to use a tool that many of us are familiar with, Excel.

  * Explain that we can think of Excel as a type of proto-programming.

  * Explain that all programming languages have **functions** (or methods) that produce an output.

  * Explain that these functions rely on parameters, or **arguments**, as inputs to know how to produce the desired output.

  * Point out that in Excel, we use **formulas** to call functions and provide arguments to calculate new values in a cell.

  * Point out that in Excel, the arguments that we provide to a function are called **variables**.

  * Explain that a formula can contain multiple functions and variables.

  * Explain that a variable in Excel can be a number, a cell, a range of cells, or the output of another function.

  * Explain that in Excel, functions typically expect a number, a cell, a range of cells, or the output of another function.

  * Explain that when an inner function is a variable to an outer function, the inner function is known as a **nested function**.

  * Explain that throughout this course, we will work with multiple programming languages and scripting tools. Although the implementation will vary, the concepts of functions, arguments, and variables will remain the same.

* Now, open the starter file inside [/01-Ins_ExcelPlayground/Solved/Excel_Playground_Starter.xlsx](Activities/01-Ins_ExcelPlayground/Solved/Excel_Playground_Starter.xlsx). The file includes a mock grade book.

* Acknowledge that we’ll start with a simple demo before we begin manipulating the data in basic ways. Specifically:

  * Demonstrate how to calculate the average grade for each student by using the `average` function.

  * Demonstrate how to copy a formula downstream in an Excel column. Either use copy and paste or drag the bottom-right corner of the cell, as in the following GIF:

  ![Images/01-ExcelPlayground.gif](Images/01-ExcelPlayground.gif)

  * Finally, demonstrate how you can pull up the Excel Formula Builder to access a GUI for Excel's off-the-shelf formulas. Use the appropriate formula to calculate values for the cells associated with the average, max, min, and standard deviation of grades, as in the following image:

  ![Images/01-ExcelPlayground_2.png](Images/01-ExcelPlayground_2.png)

* Once complete, TAs should send your completed file to students.

</details>

<details>
  <summary><strong>📣 1.3 Instructor Do: Named Ranges (0:05)</strong></summary>

* You may choose to open up the slideshow, and step through the next few slides to accompany the beginning of this next activity. Be sure to cover the following talking points:

  * Explain that most Excel functions expect more than one value. Therefore, we provide the function with a range of values to calculate the output.

  * Explain that if an Excel workbook is large, it can be difficult to keep track of which values are used as inputs to a function.

  * Explain that we can name a range of cells in Excel to help keep track of the values being used.

* Next, proceed to the example on [02-Ins_NamedRanges/ShoppingTrip.xlsx](Activities/02-Ins_NamedRanges/Solved/ShoppingTrip.xlsx).

  * Open the exercise, and begin to highlight entire columns of existing data (e.g., `A1:A6`, `B1:B6`, etc.). Note the fact that the upper-left corner, before the Formula Bar, has a Name Box. This shows the currently selected cell, or if a named range is selected, the name of the named range. These names can be created by selecting any set of cells and clicking the Name Box to insert a name, as in the following image:

  ![Images/02-NamedRanges.png](Images/02-NamedRanges.png)

  * Demonstrate to students that these named ranges can be used in formulas, like any other Excel selection. Point out that named ranges provide a more readable version of spreadsheet formulas, as in the following image:

  ![Images/02-NamedRanges_1.png](Images/02-NamedRanges_1.png)

* Once complete, TAs should send out the spreadsheet for students to reference.

</details>

<details>
  <summary><strong>📣 1.4 Instructor Do: Color Counter (0:10)</strong></summary>

* You may choose to open up the slideshow, and step through the next few slides to accompany the beginning of this next activity. Be sure to cover the following talking points:

  * Explain that conditionals are used to control the flow of logic.

  * Explain that the most common conditional used in programming is the **if statement**. In Microsoft Excel, we use `if` statements to selectively assign cell values.

  * Explain that conditional statements can be found across all programming languages, and they are fundamental to automating any code.

  * Point out that making a decision may require multiple conditions, just like in real life.

    * For example, you may not want to go to the park unless it’s light out **and** not raining.

  * Explain that in programming, including Excel, we can use **logical operators** such as `AND`, `NOT`, and `OR` to combine logical statements to produce a desired outcome.

* Then, transition into the first demonstration with [03-Ins_ColorCounter/FavoriteColors.xlsx](Activities/03-Ins_ColorCounter/Solved/FavoriteColors.xlsx). Explain to students:

  * In this example, a column of colors is listed.

  * A row of color counters uses conditional statements like `COUNTIF(Colors,"Red")` to count the instances of each color.

  * A second row of "Above Five" counters use a _different_ conditional statement (`IF(C2>5), "TRUE", "FALSE"`) to check if the color count exceeds five for each color.

  * Remind students that in both cases, the cell value is determined by the respective conditional formula, as in the following image:

![Images/03-ColorCounter.png](Images/03-ColorCounter.png)

* Answer any questions, then send the file to students.

</details>

<details>
  <summary><strong>👥 1.5 Partners Do: Review Color Counter (0:10)</strong></summary>

* Have students briefly reflect on the exercise with the person next to them. Once time is up, the students will re-explain the concept and syntax of conditionals in Excel.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Instructor+Presentation&lessonpageTitle=Data+Fundamentals+in+Excel&lessonpageNumber=1.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F01-Excel%2F2%2FLessonPlan.md)</sub>

- - -

## 2. Grade Book

| Activity Time:       0:20 |  Elapsed Time:      0:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 2.1 Students Do: Grade Book (0:15)</strong></summary>

* Next, proceed with the first student exercise of the day. In this example, students are tasked with modifying a more complex grade book to determine the letter grades and pass-or-fail status of a make-believe class. The following image captures the solution for this activity: 

![Grade Book Solved](Images/GradeBook_Solved.png)

* Introduce students to the solution they will be working toward, [04-Stu_GradeBook/GradeBook_Solved.xlsx](Activities/04-Stu_GradeBook/Solved/GradeBook_Solved.xlsx).

* You may choose to open up the slideshow and step through the next few slides to accompany this next activity.

* **Files:**

  * [README](Activities/04-Stu_GradeBook/README.md)

  * [04-Stu_GradeBook/GradeBook_Unsolved.xlsx](Activities/04-Stu_GradeBook/Unsolved/GradeBook_Unsolved.xlsx)

* Data Source: Data generated by Mockaroo, LLC. (2021) Realistic Data Generator. [https://www.mockaroo.com/](https://mockaroo.com/). Modified by Trilogy Education Services, LLC.

</details>

<details>
  <summary><strong>⭐ 2.2 Review: Grade Book (0:05)</strong></summary>

* Once time is complete, send out [04-Stu_GradeBook/GradeBook_Solved](Activities/04-Stu_GradeBook/Solved/GradeBook_Solved.xlsx), and go over the solved version of this activity with the class. Be sure to answer any questions that students may have.

* Key points to cover in this discussion:

  * The values in the "Pass/Fail" column are determined by a conditional that checks if a student’s "Final Grade" was greater than or equal to 60. If the statement evaluates to false, then the value is "FAIL." If the statement evaluates to true, then the value is "PASS," as in the following image:

  ![Images/04-GradeBook_1.png](Images/04-GradeBook_1.png)

  * The values in the "Letter Grade" column are also determined by a conditional, but this conditional is more complex. Whenever a statement evaluates to false in this formula, another conditional is run to check the "Final Grade." Once a statement is found to be true, the corresponding letter grade is placed in the column, as in the following image:

  ![Images/04-GradeBook_2.png](Images/04-GradeBook_2.png)

  * A recent Excel update added another method to solve a problem like this: the `IFS` function. This function can be used in place of multiple nested `IF` functions. It works in the same manner as the nested functions, but it is less bulky. Use of the `IFS` function is captured in the following image:

  ![Images/04-GradeBook_3.png](Images/04-GradeBook_3.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Gradebook&lessonpageTitle=Data+Fundamentals+in+Excel&lessonpageNumber=1.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F01-Excel%2F2%2FLessonPlan.md)</sub>

- - -

## 3. Measuring the Measures - Central Tendency

| Activity Time:       0:25 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Measures of Central Tendency (0:10)</strong></summary>

* Explain that this week's classes will include an introduction to statistics along with the fundamentals of data visualization using Excel.

* Explain that we’ll start with the basics in this first statistics-related activity. **Measures of central tendency** are some of the most basic concepts in statistics.

* You may choose to open up the slideshow, and step through the next few slides to accompany the beginning of this next activity. Be sure to cover the following talking points:

  * Ask if any students have heard the term "measures of central tendency" or would like to define it for the class.

  * Explain that the **measures of central tendency** are values that describe a dataset. More specifically, the **measures of central tendency** describe the _center_ of a dataset.

  * Point out that the most common measures of central tendency are the **mean**, **median**, and **mode**.

  * Explain that in addition to knowing how to define the measures of central tendency, it is very important to know how to manually calculate the **mean**, **median**, and **mode**. Many employers will ask you to manually calculate these values as part of their proficiency tests during an interview process.

  * Explain that the **mean** of a dataset is also referred to as the _arithmetic_ average of a dataset.

  * Explain that to manually calculate the mean, we sum all numbers in the dataset and divide by the number of elements in the dataset.

  * Explain that the **median** of a dataset is the middle element.

  * Explain that to manually calculate the **median**, we sort the values in the dataset and then select the middle element.

    * For even-length datasets, we will have _two_ elements in the middle of the list. The average of the two elements is the median of such a list.

  * Explain that the **mode** of a dataset is the _most frequently occurring value_.

    * Unlike the **mean** and **median**, which can only be used to describe numerical datasets, the **mode** can be used to describe numerical or _categorical_ datasets.

  * Explain that to manually calculate the **mode**, we would count every element in a dataset. The most frequent element in the dataset is the **mode**.

    * If multiple elements in a dataset share the greatest frequency (that is, there’s a tie), the dataset would have multiple **modes** and, therefore, be considered **multimodal**.

* Now, open the activity file [05-Ins_CentralTendency](Activities/05-Ins_CentralTendency/Solved/CentralTendency.xlsx).

* Introduce the students to the first sheet in the workbook. 

  * Point out that this example consists of a dataset of 30 numbers that range between one and ten. Explain that we have plotted each value and its frequency to better visualize the dataset in Excel, as captured in the following image:

![Example of mean in Excel](Images/05-MeanExample.png)

  * "If any of you are unfamiliar with bar plots, that is fine; we will learn how to make plots like these tomorrow!"

* Explain the steps needed to manually calculate the mean in Excel.

  * Calculate the sum of all values in the dataset using the `SUM` function.

  * Calculate the number of elements in the dataset using the `COUNT` function.

  * Divide the sum of all the values by the number of elements to calculate the mean.

* Point out that in Excel, we have already calculated the mean of a dataset in previous activities using the `AVERAGE` function.

* Introduce the students to the next sheet in the workbook. Point out that this example consists of another 30 numbers that range between one and ten; and once again, we’ve plotted each value and its frequency to visualize the dataset, as captured in the following image:

![Example of median in Excel](Images/05-MedianExample.png)

* Explain the steps to manually calculate the median.

  * Sort the dataset in ascending order.

  * Determine the length of the dataset.

  * Identify the middle element. This is the median value.

* Point out that because our dataset is even in length, the middle of the dataset is between two numbers. Therefore, we must calculate the mean between both numbers, which is five in this case.

* Explain that in Excel, we use the `MEDIAN` function to calculate the median of the dataset for us.

* Introduce the students to the next sheet in the workbook, which includes another 30 numbers between one and ten and a plot of each value’s frequency. In this dataset, the distribution has changed slightly, as captured in the following image:

![Example of a single mode in Excel](Images/05-SingeModeExample.png)

* Explain the steps to manually calculate the mode.

  * Count the occurrences of each value in the dataset.

  * Determine the most frequent value or values in the dataset to find the mode or modes.

* Explain that for this dataset, there is only one element with the highest count. In this case, the number five is the only mode in the data.

* Explain that in Excel, we would use the `MODE` or `MODE.SNGL` function to determine the single mode of the dataset.

* Point out to the students that the `MODE` function is just an abbreviation of the `MODE.SNGL` function.

* Introduce the students to the next sheet in the workbook, which includes another 30 numbers between one and ten and a plot of each value’s frequency. Point out that the difference between this dataset and the previous one is that three numbers share the highest occurrence in the dataset, as captured in the following image:

![Example of a multi-mode in Excel](Images/05-MultiModeExample.png)

* Explain that if we count the occurrences of each element in the dataset, the values two, five, and eight occur four times. Therefore, we would call this dataset _multimodal_.

* Explain that if we were to calculate the mode manually, we would say that two, five, and eight are modes of the dataset.

* Point out that in Excel, the `MODE.SNGL` function will only return the first mode it finds. When a dataset is multimodal, the `MODE.SNGL` function should not be used.

* Explain that instead of `MODE.SNGL`, we use `MODE.MULT` to return all of the modes in a dataset.

* Explain that the behavior of `MODE.MULT` is different from other functions in Excel.

  * "`MODE.MULT` is an array function in Excel. All that means, for now, is that the function will act slightly differently than any of the other functions you will learn in this unit."

  * When you use `MODE.MULT`, you start by typing the function into the cell just like any other Excel function. Then, you select a range of data. 

  * Once the data has been selected, press `Enter` on your keyboard to execute the function; this action fills in all mode values in the array of cells.

* Point out that when we use `MODE.MULT`, it returns all of the modes in the dataset correctly.

* Explain that if we are calculating the mode but are uncertain if the dataset is multimodal, it is better to use the `MODE.MULT` function and select a large array of cells.

  * Any unused cells in Excel array functions will have an "N/A" value, but it is better to have unused cells than to miscalculate the mode.

* Send out the workbook, [05-Ins_CentralTendency](Activities/05-Ins_CentralTendency/Solved/CentralTendency.xlsx), for students to refer to later.

</details>

<details>
  <summary><strong>🎉 3.2 Everyone Do: Measuring the Measures (0:15)</strong></summary>

* Explain that the measures of central tendency can summarize the dataset using single values, so they are a type of **summary statistic**. Whenever we analyze a new dataset, we should calculate all three measures of central tendency.

* Point out to students that depending on the type and size of the dataset, the different measures of central tendency may or may not describe the dataset effectively. Therefore, we should always consider what measures of central tendency will summarize the data well before we use them in a summary table.

* Explain that in this exercise, we will be looking at variety of example datasets; calculating the mean, median, and mode; and determining which measures of central tendency describe the data effectively.

* Send [MeasuringMeasures.xlsx](Activities/06-Evr_MeasuringMeasures-CentralTendency/Solved/MeasuringMeasures.xlsx) to students, and open the workbook to introduce the students to the first example. 

* Explain to the students that this first dataset contains the number of cup holders in 20 vehicles surveyed in a school parking lot. Point out that in this example, we plotted out the distribution of cup-holder results into categories and determined the number of vehicles for each category, as captured in the following image:

![This is the first example](Images/06-MeasuringExample1.png)

* Ask a student to demonstrate or explain how to manually calculate the mean in Excel.

  * Remember that the manual calculation for the mean is the sum of all values divided by the number of values in the dataset.

  * If possible, have the student enter the calculations directly into the projected workbook. Otherwise, enter the formula as the student talks through the answer.

* Ask a different student to demonstrate or explain how to manually calculate the median in Excel.

  * Remember that the manual calculation for the median is finding the center of a sorted dataset.

  * If possible, have the student enter the calculations directly into the projected workbook. Otherwise, enter the formula as the student talks through the answer.

* Ask a third student to demonstrate or explain how to manually calculate the mode in Excel.

  * Remember that the manual calculation for mode determines the most frequently appearing value in a dataset.

  * If possible, have the student enter the calculations directly into the projected workbook. Otherwise, enter the formula as the student talks through the answer.

* Now introduce the students to the next sheet in the workbook for the solution. This sheet plots the three measures of central tendency for the cup-holder dataset. Point out that we calculated the values for mean, median, and mode using the Excel functions, and we plotted their values using colored lines. In this example, all three measures of central tendency are roughly the same value, as captured in the following image:

![This is the first example](Images/06-MeasuringExample1Solved.png)

* Explain that in this instance, all three measures of central tendency effectively describe the center of the data.

* Introduce the students to the next sheet in the workbook, which contains a dataset on the salaries of 10 employees at a small, family-owned car dealership. Point out that in this example, we have already calculated the mean, median, and mode using Excel functions. Additionally, we have already plotted the distribution of salaries and added colored lines for the measures of central tendency, as captured in the following image:

![This is the second example](Images/06-MeasuringExample2.png)

* Ask the students if they notice anything different between the mean of the first example and the mean of the second example.

* Point out that the mean of the dataset in the second example no longer effectively describes the center of the data.

* Explain that when there are extreme values in a dataset, the mean can drift away from the center of the data.

  * In this example, the $100,000 and $200,000 salaries are much higher than the rest of the salaries; these higher salaries would be considered extreme values for this dataset

* Point out to the students that the `MODE.SNGL` function in Excel returned an "#N/A" value. Explain that this means there is no mode for the dataset.

* Ask the students why a dataset might not have a mode.

* Explain to the students that the mode is used to describe the center of a dataset when measurements are repeated or there are finite options for each data point. When there are infinite possible values, there is typically no mode for the dataset.

  * In this example, each employee's salary was a different amount. Therefore, the dataset does not have a mode.

* Point out to the students that the median salary is $24,500, which is right around the center of the dataset.

* Ask the students to take one minute with the people around them and come up with a reason for why the median was able to effectively describe the center of the data, but the mean was not.

* Ask a student to share what their group came up with. Some example answers may be:

  * “The median only considers the _center_ of a sorted dataset”
  * “The mean is affected by very large values”
  * “The median is less sensitive”

* Explain that mean and median values are _usually_ very close when a dataset is large or doesn’t contain extreme values. When the dataset is smaller or contains extreme values, the mean and median _usually_ differ.

* Introduce the students to the next sheet in the workbook. Explain that this third dataset contains the results from an office survey asking employees how many cups of coffee they drink per day. Point out that we have calculated the mean, median, and mode for the dataset, and we’ve plotted the cups of coffee per day to help visualize the data. The mean, median, and mode are represented on the plot by colored lines, as captured in the following image:

![This is the third example](Images/06-MeasuringExample3.png)

* Explain that in this example, we are once again dealing with a dataset with discrete groups. The counts for cups of coffee fall into four groups: 0 cups, 1 cup, 2 cups, or 3 cups.

* Ask the students which measure of central tendency best describes the center of the data, and ask them to provide their reasoning.

* Explain that when numerical data falls into a small number of categories, the data often becomes multimodal.

* Explain that in this example, there are two modes in the data, which represent two distinct groups of employees: one group drinks two cups of coffee per day, and the other group does not drink coffee at all.

* Point out that the mean and median both estimate that the center of the data is around 1.5 cups of coffee per day. However, if we used the mean or median to describe the dataset, we would be misrepresenting the large group of employees who do not drink any coffee.

* Explain that in this example, the measure of central tendency that we choose may be dependent on what question we are trying to answer.

* Ask the students to think of a scenario where we would want to use the mean or median to describe the center of the data.

  * If the reason for collecting this data was to answer the question "How much coffee should we buy for the break room?", then the mean or median would be the best way to describe the center of the data.

* Now, ask the students to provide a scenario where we would want to use the mode to describe the center of the data.

  * If the reason for collecting this data was to answer the question "Is coffee the drink of choice at our company?", then the mode would be the best way to describe the center of the data.

* Introduce the students to the fourth example. Explain that the fourth dataset contains the amount of rainfall per month at an airport over a year from January through December. Point out that we have calculated the mean, median, and mode for the dataset, and that the rainfall per month has been plotted to help visualize the data. The mean, median, and mode are represented by color lines on the plot, as captured in the following image:

![This is the fourth example](Images/06-MeasuringExample4.png)

* Ask the students which measure of central tendency best describes the center of the data, and ask them to provide their reasoning.

  * This dataset contains rainfall measurements, and there are infinite possibilities for the amount of rainfall per month. Therefore, using mode to describe the dataset is not the best measure.

  * The mean or median could be used to describe the center of this dataset because the values are relatively close together.

  * Because there are relatively extreme values in January and April, the median would be the best measure of central tendency.

* Explain that the median is typically the safest measure of central tendency to use when you are uncertain about the origins of the data or what questions you are trying to answer with the data.
 
  *Caution the students that when people ask for the average of the dataset, they are most likely referring to the mean.

* Send out the [workbook](Activities/06-Evr_MeasuringMeasures-CentralTendency/Solved/MeasuringMeasures.xlsx) for students to refer to later.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Measuring+the+Measures+-+Central+Tendency&lessonpageTitle=Data+Fundamentals+in+Excel&lessonpageNumber=1.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F01-Excel%2F2%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

- - -

## 4. Top-Songs Pivot Table

| Activity Time:       0:50 |  Elapsed Time:      2:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Formatting (0:10)</strong></summary>

* Welcome students back from their break. Explain that we will now switch gears back to Excel fundamentals for the rest of the class. We will return to our introduction to statistics during the next class.

* You may choose to open up the slideshow and go through the next few slides to accompany the beginning of this next activity. Be sure to cover the following talking points:

  * Explain that formatting in Excel can be split up into two distinct parts: **data formatting** and **style formatting**.

  * Explain that data formatting changes the way a value is represented in a cell. Data formatting can help provide context for a range of values.

    * For example, a value of 5 could be represented as $5 or 5 o'clock depending on the context.

  * Explain that style formatting changes the way a cell is viewed.

    * Style formatting is commonly used to highlight values of interest in a dataset.

* Send [07-Ins_Formatting/NumberTypes.xlsx](Activities/07-Ins_Formatting/Solved/NumberTypes.xlsx) to students, and review the data with the class.

  * Excel can style the numeric data of a spreadsheet so that it looks a certain way. This can be done by selecting a cell or a range of numeric data, clicking on the "Number" group, and then selecting any of the available numeric styles.

  * It is important to note that we are only altering the look or appearance of the number. In the following image, the data itself is the same as it was before we applied the styling, but we’ve formatted the original value as a currency:

  ![Number Formats](Images/NumberFormats.png)

* We can make in-depth formatting changes to a spreadsheet by altering the styling of the cells on the page. Send [07-Ins_Formatting/ConditionalFormatting.xlsx](Activities/07-Ins_Formatting/Solved/ConditionalFormatting.xlsx) to students, and demonstrate to the class how Excel can automatically format cells based on certain conditions or rules.

  * Each cell within the "Favorite Color" column is being painted a certain color based on the value contained in the cell.

  * The cells in the C2 to H2 range are being painted based on how many times each color appears in the "Favorite Color" column.

  * This kind of formatting could be applied manually, but it would be tedious and need to be redone any time the data changed. Thankfully, Excel includes the option to format cells based on conditionals.

  * Click on the "Conditional Formatting" option within Excel's "Home" tab and select "Manage Rules" from the menu that appears. Now, you can examine the formatting rules for the entire worksheet.

  * **Conditional Formatting** changes the styling of a cell based on certain conditions. As such, this sheet includes rules that style cells based on the values that the cells contain, as captured in the following GIF:

  ![Images/06-Formatting.png](Images/06-Formatting.png)

  * Click through a few of the rules in this spreadsheet to introduce students to some of the options for setting conditional formatting rules.

</details>

<details>
  <summary><strong>📣 4.2 Instructor Do: Pivot Tables (0:10)</strong></summary>

* You may choose to open up the slideshow and go through the next few slides to accompany the beginning of this next activity. Be sure to cover the following talking points:

  * Explain that another powerful tool in the Excel arsenal is the **pivot table**, which allows users to extract summary data from large, detailed, and consistent datasets.

  * Explain that pivot tables summarize data using functions like `SUM`, `COUNT`, and `AVERAGE` on subsets of the data. These subsets can be as general or as specific as we like.

  * Caution students that pivot tables are not designed for deeper analysis. They are designed to provide summary metrics at a glance.

* Open up [09-Ins_PivotTables/PivotTables_Solved.xlsx](Activities/09-Ins_PivotTables/Solved/PivotTables_Solved.xlsx) for this activity.

  * To create a pivot table, select "Pivot Table" within the "Insert" tab, and then hit “OK” in the new window that pops up.

  * A menu will appear, and users will be able to pick and choose what columns from the original sheet should be placed into their pivot table.

  * Place "ACTIVITY" into "Rows," and a column containing all products will appear on the screen, with all duplicate data points placed together.

  * Users can also group rows into subcategories to allow for more specific or generalized tables by adding more fields into the "Rows" section. Add "TYPE" into the "Rows" section, as in the following image:

  ![MultiRows](Images/MultiRows.png)

  * Place "INCOME_AMT" into "Values," and a new column will appear containing the sum of the "INCOME_AMT" column from the original spreadsheet as it relates to the "TYPE" column. In other words, all "Cultural, Ethnic Awareness" values are added together, all "Theater" values are added together, and so on.

  * Users can change what kind of data they would like to analyze within a pivot table by clicking on any of the fields placed within the "Values" section and selecting "Field Value Settings" from the dropdown menu. The following “PivotTable Field” window allows users to calculate maximums, minimums, and averages among other options, as captured in the following image:

  ![ValueSettings](Images/ValueSettings.png)

  * Place "STATE" into "Filters", and a new field named "STATE" will appear above the pivot table. By clicking on this field and selecting a value from the list that appears, users can filter data based on what sales took place in a particular state, as captured in the following image: 

  ![Images/07-PivotTables.png](Images/07-PivotTables.png)

* Users can also sort tables by selecting any individual cell and then right-clicking. Within the pop-up menu that appears, select “Sort”, then choose your desired sorting method.

* Data Source:
  * Exempt Organizations Business Master File Extract (EO BMF), Internal Revenue Service (IRS), [https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf](https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf)
    * [https://www.irs.gov/pub/irs-soi/eo1.csv](https://www.irs.gov/pub/irs-soi/eo1.csv), accessed August 18, 2021.
    * [https://www.irs.gov/pub/irs-soi/eo_info.pdf](https://www.irs.gov/pub/irs-soi/eo_info.pdf), accessed August 31, 2021.
  * Dataset reduced in Pandas. For more information, see exercise [README.md](Activities/09-Ins_PivotTables/README.md)

</details>

<details>
  <summary><strong>✏️ 4.3 Students Do: Top-Songs Pivot Table (0:20)</strong></summary>

* Explain that pivot tables are exceptionally helpful when dealing with large-scale datasets that contain similarities between data points.

* Introduce students to the [solution](Activities/10-Stu_TopSongsPivot/Solved/Top5000Songs_Solved.xlsx) they will be working toward, captured in the following image, then send out the instructions and starter file.

![Images/08-TopPivot.png](Images/08-TopPivot.png)

* You may choose to open up the slideshow and use the next few slides to accompany this next activity.

* **Files:**

  * [README](Activities/10-Stu_TopSongsPivot/README.md)

  * [Top5000Songs_Unsolved.xlsx](Activities/10-Stu_TopSongsPivot/Unsolved/Top5000Songs_Unsolved.xlsx)

* Data Source: The World's Music Charts "All Time Songs" T Sort, Hawtin, S. et al, version 2.8.0044 [https://tsort.info/csv/top5000songs-2-8-0044.csv](https://tsort.info/csv/top5000songs-2-8-0044.csv) from [https://tsort.info/music/songs0.htm](https://tsort.info/music/songs0.htm)

</details>

<details>
  <summary><strong>⭐ 4.4 Review: Top-Songs Pivot Table (0:10)</strong></summary>

* Once time is up, send out the [solution](Activities/10-Stu_TopSongsPivot/Solved/Top5000Songs_Solved.xlsx), and go over the solved version of this activity with the class. Be sure to answer whatever questions students may have.

* Key points to hit upon during this activity's discussion:

  * The "Rows" for the pivot table have Artist as the main category and Song Name as the subcategory, so all songs are stored under their artist's name.

  * To determine how many songs an artist has in the original chart, place "artist" into the "Values" section, then count how many times their name appears. The sum of "final_score" is self-explanatory.

  * To sort the chart based on an artist's overall score, click on the "Sum of Final_Score" column within the pivot table and select "Sort From Largest to Smallest."
  
  * The following image captures the key points for this discussion:

![Top5000Songs](Images/Top5000SongsPivot.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Top+Songs+Pivot+Table&lessonpageTitle=Data+Fundamentals+in+Excel&lessonpageNumber=1.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F01-Excel%2F2%2FLessonPlan.md)</sub>

- - -

## 5. Product Pivot

| Activity Time:       0:35 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Lookups (0:10)</strong></summary>

* You may choose to open up the slideshow, and go over the next few slides to accompany the beginning of this next activity. Be sure to cover the following talking points:

  * Explain that when working with large workbooks that contain multiple tables, it can become challenging to find specific values.

  * Explain that **lookup** functions in Excel are designed to search through ranges and create references automatically.

  * Point out that there are two `lookup` functions: **VLOOKUP** and **HLOOKUP**.

  * Explain that **VLOOKUP** is used to find values in adjacent columns, while **HLOOKUP** is used to find values in adjacent rows.

  * Explain that `lookup` formulas work by:

    * Selecting a range of data to browse through (generally a table)

    * Selecting a value from within that range

    * Selecting the desired information

    * Grabbing the result

* Send [11-Ins_Lookups/Lookups.xlsx](Activities/11-Ins_Lookups/Solved/Lookups.xlsx) to students, and open the file to introduce students to how column B is using a function called `VLOOKUP()` to collect values from the table to the right based on the values in "ID".

  * `VLOOKUP()` takes in four values: a lookup value, the range of a table, the index number for a column within that range, and the match parameter.

  * Make sure students understand that when `VLOOKUP()` searches for a value, it is only looking for matches within the leftmost column of the range that they have selected.

  * Since the formula listed specifies 3 as the column index, it will grab the value stored within the third column of the second table. As such, it is grabbing the value stored within the "Role" column, as captured in the following image:

  ![Images/09-VLookups_1.png](Images/09-VLookups_1.png)

  * The match parameter indicates either an exact match (`FALSE`) or an approximate match (`TRUE`).

* `HLOOKUP()` is almost identical to `VLOOKUP()`, except it searches through ranges horizontally instead of vertically. Therefore, this formula searches through rows instead of columns.

* Data Source: Dataset created by Trilogy Education Services, LLC.

</details>

<details>
  <summary><strong>👥 5.2 Partners Do: Product Pivot (0:15)</strong></summary>

* An independent artist who sells their designs on products in an online store has called on the class to create a table to visualize the cost of their recent orders. Have students use lookups to create a pivot table for the artist, as captured in the following image:

![Images/10-ProductLookups_1.png](Images/10-ProductLookups_1.png)

* Introduce students to the [solution](Activities/12-Stu_ProductPivot/Solved/ProductionPivot_Solved.xlsx) they will be working toward before sending the instructions and starter file below.

* You may choose to open up the slideshow and use the next few slides to accompany this next activity.

* **Files:**

  * [README](Activities/12-Stu_ProductPivot/README.md)

  * [12-Stu_ProductPivot/ProductionPivot_Unsolved.xlsx](Activities/12-Stu_ProductPivot/Unsolved/ProductionPivot_Unsolved.xlsx)

* Data Source: 
  * Product List and prices created by Trilogy Education Services, LLC.
  * Shipping prices based on USPS prices [https://postcalc.usps.com/business/MailServices?country=0&ccode=US&mdt=9%2F1%2F2021&m=6](https://postcalc.usps.com/business/MailServices?country=0&ccode=US&mdt=9%2F1%2F2021&m=6)
  * Orders data generated by Mockaroo, LLC. (2021) Realistic Data Generator. [https://www.mockaroo.com/](https://mockaroo.com/).

</details>

<details>
  <summary><strong>⭐ 5.3 Review: Product Pivot (0:05)</strong></summary>

* Once time is up, send out the solution, [12-Stu_ProductPivot/ProductionPivot_Solved.xlsx](Activities/12-Stu_ProductPivot/Solved/ProductionPivot_Solved.xlsx), and go over the solved version of this activity with the class. Make sure to answer any questions that students may have.

* Key points to cover during this discussion:

  * The `VLOOKUP()` in column D of the "Orders" sheet searches for a matching "Product ID" within the first table of the "Product List" sheet and then grabs the "Price" from within.

  ![Images/10-ProductLookups_2.png](Images/10-ProductLookups_2.png)

  * The `VLOOKUP()` in column E of the "Orders" sheet searches for a matching "Shipping Priority" within the second table of the "Product List" sheet and then grabs the "Price" from within.

  ![Images/ProductionPivot_Shipping](Images/ProductionPivot_Shipping.png)

  * The pivot table is made with a primary row of "Order Number", a secondary row of "Product ID", a primary value of "Sum of Price", and a secondary value of "Sum of Shipping Price"

  ![Images/10-ProductLookups_3.png](Images/10-ProductLookups_3.png)

</details>

<details>
  <summary><strong>📣 5.4 Instructor Do: Final Questions Before Ending Class (0:05)</strong></summary>

* Take a few minutes to ask the students if they have any final questions, and answer any that arise.

  * If students are reluctant to ask questions, use the next slides in the slideshow as prompts. Use the fist-to-five technique (fist meaning not comfortable at all, five fingers meaning they feel like they have mastered the topic) to survey students on their comfort with pivot tables and the measures of central tendency.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Product+Pivot&lessonpageTitle=Data+Fundamentals+in+Excel&lessonpageNumber=1.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F01-Excel%2F2%2FLessonPlan.md)</sub>

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.