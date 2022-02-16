# 4.2 Exploring Pandas

## Overview

Today's lesson takes a deep dive into Pandas and covers some of the library's more complex functions, such as `loc`, `iloc`, and grouping, while also solidifying the concepts introduced in the last class.

## Class Objectives

By the end of this lesson, the students will be able to:

* Navigate through DataFrames by using `loc` and `iloc`.

* Filter and slice Pandas DataFrames.

* Create and access Pandas `groupby` objects.

* Sort DataFrames.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-04-pandas) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

</details>

- - -

# Class Activities

## 1. Welcome and Good Movies

| Activity Time:       0:40 |  Elapsed Time:      0:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Students (0:05)</strong></summary>

* Open the [slideshow](https://drive.google.com/open?id=1jgd7JSBtoXVXWrfaf2F2sT9UskkEpHM5hGQgbr0zgxw), and use the first few slides to welcome the class and introduce today's lesson.

* Welcome the students back to class, and inform them that we will be delving into Pandas today. Explain that we will cover a lot of material, and assure the students that they will have plenty of time to practice using Pandas&mdash;not only this week, but throughout the course. Today, we will continue to learn new functions in Pandas.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Exploring Data With Loc and Iloc (0:10)</strong></summary>

* Continue stepping through the slideshow while covering the following points:

* One of the most powerful aspects of Pandas is that programmers can easily collect specific rows and columns of data from a DataFrame using the `loc[]` and `iloc[]` methods.

  * The `loc[]` method allows us to select data using label-based indexes. In other words, it takes in strings as the keys and returns data based on those keys.

  * Using `loc[]` to search through rows is really only useful when the index of a dataset is a collection of strings. However, it is almost always useful when selecting data from columns because column headers are exclusively strings. We can select data from columns by using the `df.set_index()` function and passing in the desired column header for the index, as in the following image:

  ![Set Index.](Images/1-LocAndIloc_SetIndex.png)

  * The `iloc[]` method also allows us to select data, but instead of using labels, it uses integer-based indexing for selection by position. In other words, it selects data like one would select data from within a list: it uses a numeric index.

* Open [01-Ins_LocAndIloc](Activities/01-Ins_LocAndIloc/Solved/LocAndIloc.ipynb) in Jupyter Notebook, send the file to students, and go through the code line by line with the class.

  * The typical way in which data is called using both `loc[]` and `iloc[]` is by using a pair of brackets which contain the rows desired, followed by a comma, and then the columns desired. For example, `loc["ADDINGTON", "STREET FULL NAME"]` or `iloc[3,1]`, as captured in the following image:

  ![Row and Column.](Images/1-LocAndIloc_RowColumn.png)

  * It is also possible to select a range of data using `loc[]` and `iloc[]` by placing all of the values within brackets and/or using a colon to tell Pandas to search for a range. For example, `loc[["PRIVATE STREET", "4TH", "11TH", "ADDINGTON", "CHALFONT"],["STREET NAME ID", "STREET FULL NAME", "POSTAL COMMUNITY"]]` or `iloc[0:5, 0:3]`, as captured in the following image:

  ![Row and Column.](Images/1-LocAndIloc_Range.png)

  * By passing in a colon by itself, `loc[]` and `iloc[]` will select all rows or columns depending on where the colon is placed in relation to the comma. For example, `loc[:, ["STREET FULL NAME", "POSTAL COMMUNITY"]` will select all rows of data but will only return the "STREET FULL NAME" and "POSTAL COMMUNITY" columns, as captured in the following image:

  ![Exploring Data.](Images/1-LocAndIloc_ExploringData.png)

* Another exciting feature of `loc[]` and `iloc[]` is that these methods can be used to conditionally filter rows of data based on the values contained within a column.

  * We can conditionally filter rows of data by calling `loc[]` or `iloc[]` on a DataFrame and passing a logic test in place of the rows section of the call. For example, `loc[df["id"] >= 10, :]` will return all rows of data from the “id” column that have a value greater than or equal to 10.

  * It’s then possible to select which columns to return simply by adding their references into the columns section of the `loc[]` or `iloc[]` expression.

  * If multiple conditions should be checked, `&` and `|` may also be added into the logic test to represent `and` and `or`, respectively, which allows for a great amount of customization, as captured in the following image:

  ![Loc Conditions.](Images/1-LocAndIloc_Conditions.png)

City Parish Planning Commission (2021). [https://data.brla.gov/Transportation-and-Infrastructure/Street-Names/whw6-pbh2](https://data.brla.gov/Transportation-and-Infrastructure/Street-Names/whw6-pbh2), modified in Pandas.
</details>

<details>
  <summary><strong>✏️ 1.3 Students Do: Good Movies (0:20)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Now that the class has covered exploring and filtering DataFrames using `loc[]` and `iloc[]`, the students will create an application that searches through IMDB data to find _only_ the best movies out there.

* Send out the following files and instructions:

* **Files:**

  * [goodMovies_unsolved.ipynb](Activities/02-Stu_GoodMovies-Loc/Unsolved/goodMovies.ipynb)

  * [movie_scores.csv](Activities/02-Stu_GoodMovies-Loc/Unsolved/Resources/movie_scores.csv)

* **Instructions:**

  * Use Pandas to load and display the CSV provided in `Resources`.

  * List all the columns in the dataset.

  * We're only interested in IMDb data, so create a new table that takes the film and all the columns related to IMDb.

  * Filter out only the good movies&mdash;any film with an IMDb score greater than or equal to 7&mdash;and remove the norm ratings.

  * Find less popular movies that you may not have heard about&mdash;anything with under 20K votes

  * Finally, export this file to a spreadsheet, excluding the index, so we can keep track of our future watchlist.

</details>

<details>
  <summary><strong>⭐ 1.4 Review: Good Movies (0:05)</strong></summary>

* Open and share [02-Stu_GoodMovies](Activities/02-Stu_GoodMovies-Loc/Solved/good_movies.ipynb), then go through the code with the class, answering any questions that students may have.

* Cover the following key points during your review:

  * Since the user is only interested in data that pertains to IMDb, all rows that contain non-IMDb review information are filtered out manually by simply dropping those rows.

  * To collect only the films with a score greater than or equal to 7, a conditional `loc[]` filter is used that looks into the "IMDB" column and only collects those rows that pass through the logic test with a True value.

  * In order to collect those films that have fewer than 20K votes, another conditional `loc[]` filter is used that searches through the "IMDB_user_vote_count" column and only collects those rows that pass through the logic test with a True value.

  * The following image captures the code and outputs for this activity:

  ![Good Movies Code.](Images/2-GoodMovies_Code.png)

* Data Source: Willison, S. (2020). Fivethirtyeight. [https://fivethirtyeight.datasettes.com/fivethirtyeight](https://fivethirtyeight.datasettes.com/fivethirtyeight)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+%26+Good+Movies&lessonpageTitle=Exploring+Pandas&lessonpageNumber=4.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F2%2FLessonPlan.md)</sub>

- - -

## 2. Portland Crime

| Activity Time:       0:45 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Cleaning Data (0:05)</strong></summary>

* Continue stepping through the slideshow, while you cover the following talking points:

* When dealing with massive datasets, it’s almost inevitable that we’ll encounter duplicate rows, inconsistent spelling, and missing values.

  * Although these issues may seem insignificant in the grand scheme, they can severely hinder the analysis and visualization of a dataset by skewing the data one way or another.

  * Thankfully, Pandas includes methods for removing missing values, replacing duplicates, and changing values with relative ease.

* Open [03-Ins_CleaningData](Activities/03-Ins_CleaningData/Solved/CleaningData.ipynb) within Jupyter Notebook, share the file, and run and discuss the code line by line with the class.

  * To delete a column of extraneous information from a DataFrame, use `del <DataFrame>[<Column>]`.

  * To figure out if any rows are missing data, simply run the `count()` method on the DataFrame and check that all columns contain equal values.

  * To drop rows with missing information from a DataFrame, use `<DataFrame>.dropna(how="any")`, as in the following image:

  ![Drop NaN].(Images/3-CleaningData_DropNa.png)

  * Sometimes, the rows containing "NaN" values should not be removed but should instead be filled with another value. In such cases, simply use the `<DataFrame>.fillna(value=<Value>)` method and pass the desired value into the parentheses.

  * To find similar or misspelled values, simply run the `value_counts()` method on the column in question and check the returned values.

  * To replace similar or misspelled values, simply run the `replace()` method on the column in question, and pass in a dictionary with the keys as the values to replace and the values as the replacements, as in the following image:

  ![Replace Values.](Images/3-CleaningData_Replace.png)


* Data Source: Federal Election Commission (2021). Contributions by individuals, 2021-2022. [https://www.fec.gov/data/browse-data/?tab=bulk-data](https://www.fec.gov/data/browse-data/?tab=bulk-data), extracted, reduced, and modified in Pandas.

</details>

<details>
  <summary><strong>👥 2.2 Partners Do: Portland Crime - Cleaning Data (0:20)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* The students will now take a crime dataset from Portland, OR, and do their best to clean it up so that the DataFrame is consistent and no rows are missing data.

* Open up [04-Par_PortlandCrime](Activities/04-Par_PortlandCrime-Cleaning/Solved/PortlandCrime.ipynb) within the Jupyter Notebook, and run and discuss the code to give students an idea of the application’s end results, which are captured in the following image:

![Portland Crime Output.](Images/4-PortlandCrime_Output.png)

* Send the following files and instructions:

* **Files:**

  * [PortlandCrime.ipynb](Activities/04-Par_PortlandCrime-Cleaning/Unsolved/PortlandCrime.ipynb)

  * [crime_incident_data2017.csv](Activities/04-Par_PortlandCrime-Cleaning/Unsolved/Resources/crime_incident_data2017.csv)

* **Instructions:**

  * Read in the CSV using Pandas, and print out the DataFrame that is returned.

  * Get a count of the rows within the DataFrame to determine if there are any null values.

  * Drop the rows that contain null values.

  * Search through the "Offense Type" column, and replace any similar values with one consistent value.

  * Create a couple DataFrames that look into one neighborhood only, and print them to the screen.

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Portland Crime (0:05)</strong></summary>

* Open [15-Par_PortlandCrime](Activities/04-Par_PortlandCrime-Cleaning/Solved/PortlandCrime.ipynb) within the Jupyter Notebook, and briefly go over the solution with the students while answering any questions.

* Data Source: [Portland Crime Data](https://www.portlandoregon.gov/police/71978)

</details>

<details>
  <summary><strong>🎉 2.4 Everyone Do: Pandas Recap and Data Types (0:15)</strong></summary>

* Continue stepping through the slideshow, while you cover the following talking points for this section:

* This activity will recap what we have covered in Pandas up to this point.

* Open and send out the unsolved version of [05-PandasRecap](Activities/05-Evr_PandasRecap/Unsolved/PandasRecap.ipynb) along with [CT_fires_2015.csv](Activities/05-Evr_PandasRecap/Unsolved/Resources/CT_fires_2015.csv).

  * Go through the cells within the unsolved version of the Jupyter notebook, and have the class help you create the code to accomplish the tasks listed within the comments.

  * If the students seem to be struggling, feel free to refer to the solved version of [05-PandasRecap](Activities/05-Evr_PandasRecap/Solved/PandasRecap.ipynb) to help keep the class on track.

  * Disregard the "low-memory" warning produced after loading the CSV. This occurs because Pandas is analyzing the data type of each column.

  * Upon reaching the final section, let the class know that this DataFrame has a small problem: The date columns are being stored as objects.

  * A list of a DataFrame's data types can be checked by accessing its `dtypes` property, as captured in the following image:

    ![Pandas Recap - DataTypes.](Images/5-PandasRecap_DataTypes.png)

  * With the date columns stored as objects, it is currently impossible to perform any form of calculation on any columns with date data. Luckily, Pandas includes a way to easily change a column's data type.

* To change a non-numeric column to a numeric column, use the `df.astype(<datatype>)` method and pass in the desired data type as the parameter.

* Data Source: National Fire Incident Reporting System (NFIRS). Connecticut Fire Department Incidents (2012-2016). [https://data.ct.gov/Public-Safety/Connecticut-Fire-Department-Incidents-2012-2016-/qem9-rt8k](https://data.ct.gov/Public-Safety/Connecticut-Fire-Department-Incidents-2012-2016-/qem9-rt8k), reduced in Pandas.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Portland+Crime&lessonpageTitle=Exploring+Pandas&lessonpageNumber=4.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F2%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:40  |
|---------------------------|---------------------------|

- - -

## 3. Exploring U.S. Census Data with GroupBy

| Activity Time:       0:45 |  Elapsed Time:      2:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Pandas Grouping (0:10)</strong></summary>

* Continue stepping through the slideshow, while you cover the following talking points:

* In the last activity, the class created a DataFrame that contained the sum of loss incidents in each city. This acted as a summary table but does not include other interesting data points. For example, it does not contain the total monetary value of property and contents loss for each city.

  * Although it would be possible to collect and calculate the sum of property and contents loss for each city through ample use of `.loc[]` filtering, the `.groupby()` method is a much simpler and time-effective approach.

* Open [06-Ins_GroupBy](Activities/06-Ins_GroupBy/Solved/GroupBy.ipynb) in Jupyter Notebook, and go through the code with the class, explaining it cell by cell.

  * The start of the code is much the same as earlier. Import in dependencies, select the columns we want, fix NA values, convert the date columns to `datetime`, calculate the response time and duration, filter the DataFrame so that it shows only incidents of loss information, and count the number of incidents per state.

  * The `df.groupby([<Columns>])` method is then used to split the DataFrame into multiple groups, with each group being a different city within Connecticut.

  * The object returned by the `.groupby()` method is a GroupBy object, and it cannot be accessed like a normal DataFrame. In fact, one of the only ways to access values within a GroupBy object is to use a data function on it, as in the following image:

    ![Single GroupBy.](Images/6-GroupBy_SingleGroup.png)

  * We can create new DataFrames using purely GroupBy data by taking the `pd.DataFrame()` method and passing the desired GroupBy data in as the parameter.

  * A DataFrame can also be created by selecting a single Series from a GroupBy object and passing it in as the values for a specified column, as in the following image:

    ![GroupBy DataFrame.](Images/6-GroupBy_DataFrame.png)

  * It is also possible to perform a `df.groupby()` method on multiple columns by simply passing two or more column references into the list parameter, as in the following image:

    ![Grouping on Multiple Columns.](Images/6-GroupBy_MultiGroup.png)

  * A new DataFrame can be created from a GroupBy object, as in the following image:

    ![GroupBy DataFrame.](Images/6-GroupBy_object_dataframe.png)

  * `.sum()` is not the only useful function to use with a `.groupby()`. Another useful function is `.mean()`, as captured in the following image:

    ![GroupBy Mean.](Images/6-GroupBy_mean.png)

* Encourage the students to further explore this dataset on their own and to apply what they have learned in this demonstration to other columns.

* Data Source: National Fire Incident Reporting System (NFIRS). Connecticut Fire Department Incidents (2012-2016). [https://data.ct.gov/Public-Safety/Connecticut-Fire-Department-Incidents-2012-2016-/qem9-rt8k](https://data.ct.gov/Public-Safety/Connecticut-Fire-Department-Incidents-2012-2016-/qem9-rt8k), reduced in Pandas

</details>

<details>
  <summary><strong>👥 3.2 Partners Do: Exploring U.S. Census Data with GroupBy (0:25)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Students will now take some time to create two DataFrames that contain calculations made by using U.S. Census data. They will do so by using the `groupby()` method and then converting their findings into DataFrames.

* Open and discuss the solved version of [07-Par_Census-GroupBy](Activities/07-Par_Census-GroupBy/Solved/census.ipynb) within Jupyter Notebook to give students an idea of the application’s end results, as captured in the following images:

  ![Census Totals Output](Images/7-Census_Totals_Output.png)

  ![Census Avg Output](Images/7-Census_Avg_Output.png)

* Send out the following files and instructions:

* **Files:**

  * [census_data_2016-2019.csv](Activities/07-Par_Census-GroupBy/Unsolved/Resources/census_data_2016-2019.csv)

  * [census.ipynb](Activities/07-Par_Census-GroupBy/Unsolved/census.ipynb)

* **Instructions:**

  * Read in the census CSV file using Pandas.

  * Create two new DataFrames, one to find totals and another to find averages. DataFrames should include:

    * Totals for population, employed civilians, unemployed civilians, people in the military, and poverty count.

    * Averages for median age, household income, and per capita income.

  * Create new DataFrames once the totals and averages have been grouped by each year and state.

  * Rename any columns to reflect the data calculations.

  * Export the resulting tables to CSVs. We will use them again in our next class.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Exploring U.S. Census Data with GroupBy (0:10)</strong></summary>

* Open the solved version of [07-Par_Census-GroupBy](Activities/07-Par_Census-GroupBy/Solved/census.ipynb) within Jupyter Notebook, send the file to students, and work through the code with the class, making sure to cover the following points:

  * The original dataset is read into a Pandas DataFrame and then cut down into two separate DataFrames so that `sum()` and `mean()` can be calculated on only the relevant columns.

  * The DataFrames are then grouped according to the values contained within the "Year" and "State" columns. Totals are calculated using the `df.sum()` method, and averages are calculated using the `df.mean()` method, as captured in the following images:

    ![Census Totals.](Images/7-Census_Totals.png)

    ![Census Averages.](Images/7-Census_MeanDataFrame.png)

* Answer any questions that the class may have before moving on to the next activity.

* Data Source: [U.S. Census API - ACS 5-Year Estimates 2016-2019](https://www.census.gov/data/developers/data-sets/census-microdata-api.ACS_5-Year_PUMS.html)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Building+a+PokeDex&lessonpageTitle=Exploring+Pandas&lessonpageNumber=4.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F2%2FLessonPlan.md)</sub>

- - -

## 4. Search for the Worst

| Activity Time:       0:35 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Sorting Made Easy (0:10)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Open [08-Ins_Sorting](Activities/08-Ins_Sorting/Solved/Sorting.ipynb) within Jupyter Notebook, send the file to students, and go through the code with the class, discussing it cell by cell as you cover the following talking points:

  * It’s possible to sort the Vermont meals and rooms tax statistics data by using the values in different columns.

  * To sort a DataFrame based on the values within a column, simply use the `df.sort_values()` method and pass in the column name to sort by as a parameter.

  * The "ascending" parameter is always marked as True by default. Therefore, the `sort_values()` method will always sort from lowest to highest unless the parameter of `ascending=False` is also passed into the `sort_values()` method, as captured in the following image:

    ![Sorting - Ascending v Descending](Images/8-Sorting_Ascending.png)

  * It’s also possible to sort the data based on values stored within multiple columns by passing a list of columns into the `sort_values()` method as a parameter. The first column will be the primary sorting method, while the second column determines the row order when the first column has multiple rows with the same value.

    * This can be demonstrated by comparing a second column sort on "Rent Count" and "Alcohol Count" and using `.head(15)`, comparing the order of the two rows where "Meals Count" has a value of "54".

  * An immensely helpful method when dealing with sorted DataFrames is the `df.reset_index()` method. This method will recalculate the index for each row based on its position within the new DataFrame, and it will, therefore, allow for simpler row referencing in the future.

  * Passing `drop=True` into `df.reset_index()` will ensure that no new column is created when the index is reset.

* Data Source: Vermont Agency of Administration, Department of Taxes. Meals and Rooms Tax Statistics (2020 Multiple Periods Update, Calendar Year). [https://tax.vermont.gov/data-and-statistics/mrt](https://tax.vermont.gov/data-and-statistics/mrt)

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Search for the Worst (0:20)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* The students will now use a dataset on San Francisco Airport’s utility consumption to determine which day had the worst consumption for each utility.

* Open and discuss the solved version of [09-Stu_SearchForTheWorst](Activities/09-Stu_SearchForTheWorst/Solved/SearchForTheWorst.ipynb) within Jupyter Notebook to give students an idea of their application’s end results, which are captured in the following image:

  ![The Worst Tenant Electricity Day.](Images/9-SearchForTheWorst_TenantElectricity.png)

* Send out the following files and instructions:

* **Files:**

  * [SearchForTheWorst.ipynb](Activities/09-Stu_SearchForTheWorst//Unsolved/SearchForTheWorst.ipynb)

  * [SFO_Airport_Utility_Consumption.csv](Activities/09-Stu_SearchForTheWorst//Unsolved/Resources/SFO_Airport_Utility_Consumption.csv)

* **Instructions:**

  * Read in the provided CSV file, and print it to the screen.

  * Print out a list of all of the values within the "Utility" column.

  * Select a value from this list, and create a new DataFrame that only includes that utility. Note that some utilities have more than one option for "Owner," and you may want to limit this new DataFrame to a single "Owner."

  * Sort the DataFrame based on the level of consumption, from most to least.

  * Reset the index for the DataFrame so that the index is in order.

  * Print out the details of the worst day to the screen.

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Search For the Worst  (0:05)</strong></summary>

* Open [09-Stu_SearchForTheWorst](Activities/09-Stu_SearchForTheWorst/Solved/SearchForTheWorst.ipynb) within Jupyter Notebook, and go through the code with the class, discussing it cell by cell.

  * To collect a list of all the utilities in the dataset, the `unique()` method is run on the "Utility" column within the DataFrame.

  * To filter on a particular utility, use `df.loc[]` and have it collect only those rows where "Utility" is equal to the desired utility. Where a utility has more than one option for "Owner," a second row search on the "Owner" column is required, with parentheses around each condition and an `&` symbol to separate them, as captured in the following image:

    ![Tenant Electricity Loc](Images/9-SearchForTheWorst_TenantElectricityLoc.png)

  * To sort the values within the new DataFrame from highest to lowest, simply run the `df.sort_values()` method, pass in the "Usage" column to sort by, and then make sure that `ascending = False`, as in the following image:

    ![Sorted Table](Images/9-SearchForTheWorst_SortedTable.png)

* Data Source: SFO Airport Monthly Utility Consumption for Natural Gas, Water, and Electricity. [https://data.sfgov.org/Energy-and-Environment/SFO-Airport-Monthly-Utility-Consumption-for-Natura/gcjv-3mzf](https://data.sfgov.org/Energy-and-Environment/SFO-Airport-Monthly-Utility-Consumption-for-Natura/gcjv-3mzf)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Search+for+the+Worst&lessonpageTitle=Exploring+Pandas&lessonpageNumber=4.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F04-Pandas%2F2%2FLessonPlan.md)</sub>

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
