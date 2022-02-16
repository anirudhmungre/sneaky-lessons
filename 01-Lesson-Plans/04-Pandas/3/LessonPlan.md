# 4.3 Merging and Data Cleaning

## Overview

Today's lesson is split into two parts. The first part will test the Pandas skills of the class by having them identify and fix buggy code so it functions properly. In the second part, the students will use all the tools they have developed this week to understand the concept of programmatically manipulating data.

## Class Objectives

By the end of this lesson, the students will be able to:

* Merge DataFrames and distinguish between inner, outer, left, and right merges.

* Slice data by using the `cut()` method, and create new values based on a series of bins.

* Fix common Python/Pandas bugs in Jupyter Notebook.

* Use Google to explore additional Pandas functionality as needed.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. In this case, we have provided helpful notes within the LP that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Check for a **3-Hour Adjustment** note at the top of activities in this lesson plan. If this class occurs on a weekday, please use the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class.

  * Reducing activity time could potentially prevent the students from finishing, so please remind them to use office hours to clear up any questions that they may have.

* This class will contain minimal lecture time. In fact, most of the day will be taken up with large-scale activities that will test the skill and problem-solving abilities of the students. It is critical that everyone on the instructional team is ready to assist students whenever a bug or question arises.

* Some questions or code blocks will baffle even the most experienced Pandas programmers. Therefore, it may be wise to keep a laptop with solved activity code loaded and ready. This way, whenever a student gets stuck, the instructional team will have a reference ready to help fix the problem.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-04-pandas) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

- - -

# Class Activities

## 1. Welcome and Census Merging

| Activity Time:       0:45 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Class (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1LbIbYi8LHXXGTzatXztB92kMRBR0kYbFR8QLO7orWkQ), and use the first few slides to welcome the class and introduce today's lesson. Cover the following points:

* Welcome the class, and let them know that today we will delve into a few more functions in the Pandas library. We will also learn how to deal with multiple datasets. The end of the lesson will focus more on teaching the students how to teach themselves and fix bugs.

  * Although this concept may sound strange to the class at first, let them know that self-teaching is probably the most important skill in the programmer’s toolkit because languages are never set in stone.

  * New libraries are always being developed, and even core programming languages are regularly updated to include new functions or syntax. As such, proficient programmers must always be ready and willing to teach themselves new skills.

  * If the students seem nervous, reassure them that self-teaching becomes much easier as time goes by. The students may already be practicing this skill without realizing it because the best way to learn new techniques is to make mistakes and look up solutions online.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Merging DataFrames (0:10)</strong></summary>

* Continue stepping through the slideshow, while you cover the following talking points:

* Analysts are often provided data that is split into multiple parts. Of course, working with a bunch of different datasets is less than ideal.

  * Thankfully, Pandas allows its users to easily combine, or **merge**, separate DataFrames on similar values using the `pd.merge()` method.

* Open [01-Ins_Merging](Activities/01-Ins_Merging/Solved/Merging.ipynb) within Jupyter Notebook, share the file with students, and go through the code with the class, discussing it cell by cell.

  * The first chunks of code are used to create two DataFrames that contain information on customers and the purchases they’ve made.

  * Point out that these two DataFrames share the "customer_id" column. This will be very important soon.

  * In the final chunk of code, the `pd.merge()` method is used, and three parameters are passed into it: references to both DataFrames and the value `on="customer_id"`.

  * This code tells the computer to combine the two DataFrames so that whenever the "customer_id" column matches, the rows containing the matching data are joined, as captured in the following image:

    ![Inner Merge.](Images/1-Merging_Inner.png)

  * This is known as an **inner join**. Inner joins are the default means for combining DataFrames using the `pd.merge()` method. They will only return data whose values match. Any rows that do not include matching data will be dropped from the combined DataFrame.

  * The opposite of an inner join is an **outer join**. Outer joins will combine the DataFrames whether or not any of the rows match. Outer joins must be declared as a parameter within the `pd.merge()` method using the syntax `how="outer"`, as captured in the following image:

    ![Outer Merge.](Images/1-Merging_Outer.png)

  * Any rows that do not include matching data will have the values within replaced with `NaN`.

  * There are also **right joins** and **left joins**. These joins will protect the data contained within one DataFrame, like an outer join does, while also dropping the rows with null data from the other DataFrame, as captured in the following image:

    ![Left and Right Merge.](Images/1-Merging_LeftRight.png)

</details>

<details>
  <summary><strong>✏️ 1.3 Students Do: Census Merging (0:20)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* ⏰ **3-Hour Adjustment**: Reduce activity time from 20 minutes to 15 minutes.

* The students will now take a moment to merge the two census datasets they created in the previous class.

* Open and discuss the solved version of [02-Stu_Census](Activities/02-Stu_Census-Merging/Solved/Census.ipynb) within Jupyter Notebook to give students an idea of the application’s end results, which are captured in the following image:

  ![Census Output.](Images/2-Census_Output.png)

* Send the following files and instructions:

* **Files:**

  * [Census.ipynb](Activities/02-Stu_Census-Merging/Unsolved/Census.ipynb)

  * [state_avg.csv](Activities/02-Stu_Census-Merging/Unsolved/Resources/state_avg.csv)

  * [state_totals.csv](Activities/02-Stu_Census-Merging/Unsolved/Resources/state_totals.csv)

* **Instructions:**

  * Read in both of the CSV files, and print out their DataFrames.

  * Perform an inner merge that combines both DataFrames on the "Year" and "State" columns.

  * Create a DataFrame that filters the data to only the 2019 data.

  * Add a new column that calculates the poverty rate.

  * Sort the data by Poverty Rate and Average Per Capita Income by County, highest to lowest, to find the state or territory with the highest poverty rate.

  * Print out the data for the state or territory with the highest poverty rate.

  * **Bonus:** Print out the data for the state or territory with the lowest poverty rate with one line of code.

</details>

<details>
  <summary><strong>⭐ 1.4 Review: Census Merging (0:10)</strong></summary>

* Open [02-Stu_Census](Activities/02-Stu_Census-Merging/Solved/Census.ipynb) in Jupyter Notebook, send out the file, and go through the code with the class, discussing it cell by cell.

* Cover the following key points:

  * Since we are merging on two columns, the columns must be in a list, as captured in the following image:

    ![Census Merge.](Images/2-Census_Merge.png)

  * When creating a new DataFrame with 2019 data only, `pd.DataFrame()` must be used to avoid a warning error when calculating the Poverty Rate in a new column, as captured in the following image:

    ![Census Poverty Rate.](Images/2-Census_Poverty_Rate.png)

  * Once a DataFrame has been sorted, it is possible to use `len(df)-1` inside `.loc[]` to find the final row of a DataFrame and print out the data, as captured in the following image:

    ![Census Poverty Summary.](Images/2-Census_Poverty_Summary.png)

* Data Source: [U.S. Census API - ACS 5-Year Estimates 2016-2019](https://www.census.gov/data/developers/data-sets/census-microdata-api.ACS_5-Year_PUMS.html)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+%26+Cryptocurrency+Merging&lessonpageTitle=Merging+and+Data+Clean+Project&lessonpageNumber=4.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F3%2FLessonPlan.md)</sub>

- - -

## 2. Binning Movies

| Activity Time:       0:40 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Binning Data (0:10)</strong></summary>

* Continue stepping through the slideshow, while you cover the following talking points:

* Not everyone is a “numbers person,” and sometimes a DataFrame has so many values that it becomes extremely difficult to comprehend exactly what is going on. For this reason, Pandas has a built-in **binning** method that allows its users to place values into groups, which enables more vigorous dataset customization.

* Open [03-Ins_Binning](Activities/03-Ins_Binning/Solved/Binning.ipynb) in Jupyter Notebook, share the file, and go through the code with the class, discussing it cell by cell.

* Cover the following points:

  * When using the `pd.cut()` method, three parameters must be passed in. The first is the Series that is going to be cut. The second is a list of cutoff values for the bins that the Series will be sliced into. The third is a list of the names or values that will be given to the bins.

  * Pandas automatically creates the bin ranges from the list of cutoff values. It’s important to note that the first and last cutoff value will be the minimum of the first bin and maximum of the last bin, respectively. The other cutoff values will be shared by adjacent bins. (The default behavior of `pd.cut()` is to include the higher cutoff value in the bin). So, for example, when given the list `[0, 59, 69, 79, 89, 100]` of cutoff values, Pandas will create the following bins: (0, 59], (59, 69], (69, 79], (79, 89], (89, 100]. .

  * The number of labels for the `pd.cut()` method must equal the number of bins. If there are too many or too few, an error will be returned.

  * Binning is so powerful because, after creating and applying these bins, the DataFrame can be grouped according to those values, and a higher-level analysis can be conducted, as in the following image:

    ![Binning Groups.](Images/3-Binning_Groups.png)

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Binning Movies (0:25)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* The students will now put their binning skills to use by creating bins for movies based on their IMDd user vote count. After creating the bins, they will group the DataFrame based on those bins and then perform some analysis on them.

* Open and discuss the solved version of [04-Stu_MovieRatings-Binning](Activities/04-Stu_MovieRatings-Binning/Solved/BinningMovies.ipynb) within Jupyter Notebook to give students an idea of the application’s end results, which are captured in the following image:

  ![Binning Movies - Output.](Images/4-BinningMovies_Output.png)

 * Send the following files and instructions:

* **Files:**

  * [BinningMovies.ipynb](Activities/04-Stu_MovieRatings-Binning/Unsolved/BinningMovies.ipynb)

  * [movie_scores.csv](Activities/04-Stu_MovieRatings-Binning/Unsolved/Resources/movie_scores.csv)

* **Instructions:**

  * Read in the provided CSV file, and print it to the screen.

  * Find the minimum "IMDB user vote count" and maximum "IMDB user vote count".

  * Using the minimum and maximum "votes" as a reference, create 9 bins to slice the data into.

  * Create a new column called "IMDB User Votes Group", and fill it with the values collected through your slicing.

  * Group the DataFrame based on the values within "IMDB User Votes Group."

  * Find out how many rows fall into each group before finding the averages for "RottenTomatoes", "RottenTomatoes_User", "Metacritic", "Metacritic_User", and "IMDB".

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Binning Movies (0:05)</strong></summary>

* Open [04-Stu_MovieRatings-Binning](Activities/04-Stu_MovieRatings-Binning/Solved/BinningMovies.ipynb) in Jupyter Notebook, share the file, and go through the code with the class, discussing it cell by cell.

  * Since the values contained within the "IMDB user vote count" column are so widespread, there are several acceptable ways to split up the data. This particular code uses a variable scale so there are 12 to 19 rows in each group. This creates a graduated scale that starts with 2.5K user vote count ranges for the first two bins, scaling up to a 250K range for the final bin, as captured in the following image:

    ![Binning Movies - Bins.](Images/4-BinningMovies_Bins.png)

  * The bins are added into the DataFrame by simply placing them within a new column. The DataFrame is then grouped on this new column to perform all of the data functions.

* Data Source: FiveThirtyEight (2015). [https://github.com/fivethirtyeight/data/tree/master/fandango](https://github.com/fivethirtyeight/data/tree/master/fandango)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Binning+TED&lessonpageTitle=Merging+and+Data+Clean+Project&lessonpageNumber=4.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F3%2FLessonPlan.md)</sub>

- - -

## 3. Cleaning Crowdfunding

| Activity Time:       0:50 |  Elapsed Time:      2:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Mapping (0:10)</strong></summary>

* Continue stepping through the slideshow, while you cover the following talking points:

* Remind the students how Excel's number formats allow users to easily change the styling of columns. Pandas also includes this functionality with its `df.map()` method, which allows users to style entire columns at once.

* Open [05-Ins_Mapping](Activities/05-Ins_Mapping/Solved/Mapping.ipynb) in Jupyter Notebook, share the file with the students, and go through the code with the class, discussing it cell by cell.

  * `df[<COLUMN>].map(<FORMAT STRING>.format)` enables users to modify the styling of an entire column.

  * The formatting syntax used for mapping is, in a word, confusing. It uses strings containing curly brackets to determine how to style columns, and this can make it difficult to understand at first.

  * A somewhat easy way to understand mapping strings is that it is fairly similar to concatenating strings. Whatever is outside of the curly brackets is added before or after the initial value, which is modified by whatever is contained within the curly brackets.

  * So, to convert values into a typical dollar format, one would use `"${:.2f}"`. This places a dollar sign before the value, which has been rounded to two decimal places.

  * Using `"{:,}"` will split a number up so that it uses comma notation. For example, the value `2000` would become `2,000` using this format string, as captured in the following image:

    ![Mapping Syntax.](Images/5-Mapping_Syntax.png)

  * Format mapping really works only once; it will return errors if the same code is run multiple times without restarting the kernel. Therefore, formatting is usually applied near the end of an application.

  * Note also that it will format `NaN` values, so it is a good idea to run a `.fillna()` or `.dropna()` to avoid formatting null values.

  * Format mapping also can change the data type of a column, as captured in the following image, so all calculations should be handled before modifying the formatting.

    ![Mapping Ruins Data Types.](Images/5-Mapping_DataTypes.png)

* Data Source: Seattle GeoData. Seattle Housing Cost Burden by Race. [https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::housing-cost-burden-by-race/about](https://data-seattlecitygis.opendata.arcgis.com/datasets/SeattleCityGIS::housing-cost-burden-by-race/about)
</details>

<details>
  <summary><strong>👥 3.2 Partners Do: Cleaning Crowdfunding (0:30)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* ⏰ **3-Hour Adjustment**: Skip this **Partners Do** activity, and continue on to the review activity.

* For the remainder of the lesson, the class will practice using Pandas by taking the dataset from their first homework, cleaning it up, and formatting it in far less time than it would take in Excel.

* Open and discuss the solved version of [06-Stu_CleaningCrowdfunding](Activities/06-Stu_CleaningCrowdfunding/Solved/CrowdfundingClean.ipynb) within Jupyter Notebook to give students an idea of their application’s end results.

Send the following files, and find instructions for this activity within the Jupyter notebook:

* **Files:**

  * [CrowdfundingData.csv](Activities/06-Stu_CleaningCrowdfunding/Unsolved/Resources/CrowdfundingData.csv)

  * [CrowdfundingClean.ipynb](Activities/06-Stu_CleaningCrowdfunding/Unsolved/CrowdfundingClean.ipynb)

* **Instructions:**

  * The instructions for this activity are contained within the Jupyter notebook.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Cleaning Crowdfunding (0:10)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 30 minutes on this activity.

  * Use the review section as guidance for talking points while you live-code along with the students.

  * Take your time, and answer all student questions along the way.

* Open [06-Stu_CleaningCrowdfunding](Activities/06-Stu_CleaningCrowdfunding/Solved/CrowdfundingClean.ipynb) within Jupyter Notebook, and go through the code with the class, discussing it cell by cell.

* Data Source: Data generated by Trilogy Education Services, a 2U, Inc. brand, and is intended for educational purposes only.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Cleaning+Kickstarter&lessonpageTitle=Merging+and+Data+Clean+Project&lessonpageNumber=4.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F3%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      2:55  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Reduce break time to 15 minutes.

- - -

## 4. Bug-Fixing Bonanza!

| Activity Time:       1:05 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Introduction to Bug Fixing (0:10)</strong></summary>

* Continue the slideshow using the next few slides for this demonstration.

* Open [07-Ins_IntroToBugfixing](Activities/07-Ins_IntroToBugfixing/Unsolved/IntroToBugfixing_Unsolved.ipynb) within Jupyter Notebook, and also send the code out to the class. Make sure to send [veterans.csv](Activities/07-Ins_IntroToBugfixing//Unsolved/Resources/veterans.csv) out to the class, as well.

Cover the following key points as you go:

  * Note how, within the final block of code, an error is returned as the application attempts to collect the average value within the "Percentage" column, as captured in the following image:

    ![Bug-fixing Error.](Images/7-Bugfixing_Error.png)

  * Ask the class to resist pointing out the bug in this block of code for now. Many students are likely aware that the values within the column are strings, and it is not possible to collect the mean of a string.

* The first step in fixing a bug is to keep calm.

  * Bugs happen all the time, and they are rarely the end of the world. In fact, most bugs that programmers encounter are simple enough to solve&mdash;as long as they know how and where to look for the solution.

* The second step in bug fixing an application is to identify what the bug is and where it is located.

  * Since the class is using Jupyter Notebook, finding the erroneous block of code is easy. The error will always be returned in the space following the erroneous cell.

  * Unfortunately, Pandas is not known for returning clearly understandable error text. In fact, it often returns large blocks of complex text that can easily confuse those who do not know the library's underlying code. The line following `KeyError:` is generally a good starting point.

  * For example, the text following `ValueError:` within the current code lets the programmer know that Pandas cannot convert the string values in the "Percentage" column to floats, as captured in the following image:

    ![Error Text.](Images/7-Bugfixing_ErrorText.png)

  * If the error text isn’t entirely clear, it can be helpful to print out variables/columns to the console to uncover the bug’s location. For example, printing out the "Percentage" Series lets the programmer know that the `dtype` of this series is an object and not a float.

* The third step is to research the error online for solutions that other programmers have uncovered.

  * The key part to this step is coming up with an accurate way to describe the bug, which can take multiple attempts, but it is a skill that will develop over time.

  * Google is the programmer's best friend, as typing in a description of the bug will often bring up links to possible solutions. If not, simply alter the search a bit until a solution is discovered.

    ![Google Expert.](Images/7-Bugfixing_GoogleExpert.png)

  * This particular problem requires the code to drop the percentages within the "Percentage" column, so the search could be more specific and add that information, as captured in the following image:

    ![Google Expert - Part 2.](Images/7-Bugfixing_GoogleExpertPercent.png)

  * The first link takes the class to a Stack Overflow question that asks how to drop percentages and convert a column to floats. This provides a solution for the bug.

  * Feel free to copy and paste the solution, and then modify it within the Jupyter notebook, as captured in the following image. Let the class know that copying and pasting from Stack Overflow is something almost every single programmer does.

    ![Problem Solved.](Images/7-Bugfixing_Solution.png)

* Data Source: Department of Veteran Affairs. Percentage of Veterans Served Within 75 Miles of a State or National Cemetery. [https://catalog.data.gov/dataset/percentage-of-veterans-served-within-75-miles-of-a-state-or-national-cemetery](https://catalog.data.gov/dataset/percentage-of-veterans-served-within-75-miles-of-a-state-or-national-cemetery)

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Bug-Fixing Bonanza (0:35)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* ⏰ **3-Hour Adjustment**: Skip this **Students Do** activity, and continue on to the review activity.

* The class will now be provided with a Pandas project that contains TONS of bugs. They will take the application and fix any bugs so that it works properly. This activity will test their Pandas skills while also teaching them how to teach themselves.

* Open and discuss the solved version of [08-Stu_BugfixingBonanza](Activities/08-Stu_BugfixingBonanza/Solved/BugfixBonanza.ipynb) within Jupyter Notebook to give students an idea of the application’s end results.

* Send the following files and instructions:

* **Files:**

  * [BugfixBonanza.ipynb](Activities/08-Stu_BugfixingBonanza/Unsolved/BugfixBonanza.ipynb)

  * [Bedbug_Reporting.csv](Activities/08-Stu_BugfixingBonanza/Unsolved/Resources/Bedbug_Reporting.csv)

* **Instructions:**

  * Dig through the provided Jupyter notebook, and attempt to fix as many bugs as possible. There are A LOT, and the bugs get harder to resolve as the code progresses.

  * Once you have finished bug fixing, perform some additional analysis on the provided dataset. What interesting theories and/or conclusions can you draw about bedbugs in New York City? As long as you keep challenging yourself, bugs will pop up and you’ll get more bug-fixing practice.

  * Consider other possible questions and what additional data you could search for in order to draw further conclusions from this data.

* **Hints:**

  * After fixing the bugs in each block of code, make sure to run the cell below for an updated error.

  * A few new concepts are covered within this Jupyter notebook. The most complex of these concepts is multi-indexing, and it is very likely that this is where many will get held up. Don’t worry: Multi-indexing is not in the homework, and it is not required outside of this activity. It is simply an interesting, powerful feature of Pandas.

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Bug-Fixing Bonanza (0:15)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 30 minutes on this activity.

  * Use the review section as guidance for talking points while you live-code along with the students.

  * Take your time, and answer all student questions along the way.

* Open the solved [BugfixBonanza.ipynb](Activities/08-Stu_BugfixingBonanza/Solved/BugfixBonanza.ipynb) within Jupyter Notebook, send out the file, and go through the code with the class, discussing it cell by cell. Alternatively, if you find yourself with a little extra time, you can open [BugfixBonanzaExtendedAnalysis.ipynb](Activities/08-Stu_BugfixingBonanza/Solved/BugfixBonanzaExtendedAnalysis.ipynb), which has two more cells demonstrating additional calculations that we can perform on this dataset.

  * Bugs are a fact of life for programmers; whether they are bugs that you introduce while trying to solve a problem or bugs that you are helping colleagues fix, bug fixing is a significant component of writing and working with code. As such, it is extremely helpful to practice bug fixing as much as possible.

  * The first bug is simple. No dependencies have been declared, so the application will not be able to use Pandas.

  * The second bug is also simple. The leading `../` in the CSV path is incorrect.

  * The third bug is also simple. The CSV path is being read in, but it is not being saved to a DataFrame.

  * The fourth bug is where things start to get complex. Pandas is unable to reduce the columns in the DataFrame because the "Re-infested  Dwelling Unit Count" column name contains an extra space. This column will need to be renamed.

    ![Bug-Fixing Columns.](Images/8-BugfixBonanza_Columns.png)

  * The fifth bug requires a change to the data type of the "Filing Date" column before any `.dt` functions can be performed on it.

  * The sixth bug is a little tricky. When trying to convert the "Postcode" column to type int, there is an error that reads `ValueError: Cannot convert non-finite values (NA or inf) to integer`. `.dropna()` must be performed before the column can be converted.

  * For the seventh bug, sometimes the simplest of errors, like not including a `\` or enclosing a calculation inside `()` when the calculation falls over two separate lines, can cause an error. This bug can be fixed using either approach.

  * The next bug, captured in the following image, is only a warning, but it can be fixed by turning the columns into a list with additional square brackets.

    ![Bug-Fixing Columns.](Images/8-BugfixBonanza_FutureWarning.png)

  * For the final bug, the columns to be merged on are not specified. The “Borough” column must be specified in addition to `on="Year"`, as captured in the following image:

    ![Bug-Fixing Columns.](Images/8-BugfixBonanza_Merge.png)

* Data Source: NYC Department of Housing Preservation and Development (HPD). Bedbug Reporting. [https://data.cityofnewyork.us/Housing-Development/Bedbug-Reporting/wz6d-d3jb](https://data.cityofnewyork.us/Housing-Development/Bedbug-Reporting/wz6d-d3jb)

</details>

<details>
  <summary><strong>📣 4.4 Instructor Do: Close Class (0:05)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this activity.

* Continue the slideshow, using the next few slides to present this portion of the lesson.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Bugfixing+Bonanza%21&lessonpageTitle=Merging+and+Data+Clean+Project&lessonpageNumber=4.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F3%2FLessonPlan.md)</sub>

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
