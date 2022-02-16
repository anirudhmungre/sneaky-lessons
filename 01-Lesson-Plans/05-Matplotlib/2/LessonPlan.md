# 5.2: Plotting with Pandas

## Overview

Today's lesson introduces the students to Pandas plotting, a quick and effective means for creating charts from DataFrames.

## Class Objectives

By the end of this lesson, the students will be able to:

* Create plots by using the `DataFrame.plot()` method.

* Explain the advantages and disadvantages of creating charts by using the `DataFrame.plot()` method.

* Use Pandas to analyze a complex dataset and chart the visualizations.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Today's class is lighter on new material because plotting charts with Pandas makes visualizing large datasets easier than before.

* If the students have trouble displaying plots, explore the following potential remedies:

  * Try a different kernel in Jupyter.

  * Place `%matplotlib notebook` at the top of the notebook.

  * Consult [Stack Overflow](https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline/43028034) to find possible solutions.

* Please refer to our [Student FAQs?](../../../05-Instructor-Resources/README.md#unit-05-matplotlib) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

* The slideshow is for instructor use only. When distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

</details>

- - -

# Class Activities

## 1. Intro and PyPlot Warmup

| Activity Time:       0:20 |  Elapsed Time:      0:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Introduction to Class (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1aCB2PVWcKMzgNGbNGwBzbjtD_vnbZY4ChC8tiZVtCVo) as you welcome the class and introduce today's lesson. Be sure to cover the following:

* Poll the students on how comfortable they are with plotting in Python after the last class.

  * Today’s class is all about reinforcing concepts. By the end of class, everyone should feel more comfortable with plotting in Python and choosing appropriate plots for a given dataset.

  * Today, we will talk through multiple dataset examples, asking ourselves what plots best visualize the data.

  * We will also design plots using a different Python method than we used in the last class. However, the plot types will all be familiar.

</details>

<details>
  <summary><strong>✏️ 1.2 Student Do: PyPlot Warmup (0:10)</strong></summary>

Send the following links to the students and go over the instructions:

* **File:** [plot_drills.ipynb](Activities/01-Stu_PlotsReview/Unsolved/plot_drills.ipynb)

* **Instructions:** [README.md](Activities/01-Stu_PlotsReview/README.md)

* In this activity, the students will use PyPlot to create the most effective visualization for a variety of datasets.

* **Important:** Do not open any examples before reviewing this activity. Part of the challenge is for the class to come up with charts that fit the data, so providing them with reference code would give it all away.

* Continue through the slideshow to introduce the students to the first activity. Cover the following talking points:

  * Before getting into the bulk of today's lesson, we will spend some time warming up our minds with PyPlot drilling exercises.

  * This activity will not only test our plot creation skills; it will also make us think about what plot fits a dataset best.

</details>

<details>
  <summary><strong>⭐ 1.3 Review: PyPlot Warmup (0:05)</strong></summary>

* Open [01-Stu_PlotsReview](Activities/01-Stu_PlotsReview/Solved/plot_drills.ipynb) within Jupyter Notebook, and go through the code line by line with the class, answering whatever questions they have. Make sure to discuss the following points:

  * The first dataset is ideal for a bar chart since the programmer is provided with nothing but a list of strings&mdash;gym names&mdash;and a list of integers&mdash;gym memberships&mdash;that should be compared against each other.

  * To ensure that the graph is as aesthetically pleasing as possible, the tick locations for the x-axis are modified so that they fall in the center of their associated bar when the bars are aligned to the edge of the chart. The limits of the x- and y-axes are then also modified to ensure that there is separation between the bars and the edge of the chart, as captured in the following image:

    ![Drills - Bar Chart.](Images/01-PyPlotDrills_Bar.png)

  * The second dataset fits a line chart best because the values within the lists change over time in relation to one another.

  * This chart needs less aesthetic editing, but a horizontal line should be added where the y-axis is equal to 0 so that it is easy to tell when a value is positive or negative, as captured in the following image:

    ![Drills - Line Chart.](Images/01-PyPlotDrills_Line.png)

  * Although it may seem obvious that the third dataset would be used for a pie chart, the only thing that differentiates it from the first dataset is the inclusion of the "colors" list and "explode" tuple. Still, since pie charts are helpful when comparing parts of a whole, the pie chart provides a different perspective from the bar chart example.

  * It is important to note that the axes are being set to "equal", so that the pie chart is circular, and that the parameter of `autopct=%1.1%%` is passed into the `plt.pie()` method, so that the values within the "members" list are converted into percentages with a single decimal point, as captured in the following image:

    ![Drills - Pie Chart.](Images/01-PyPlotDrills_Pie.png)

  * The final dataset compares the relationship between two lists with unique values. Therefore, a scatter plot is the ideal method for visualizing the relationship.

  * Scatter plots require very little aesthetic styling, so the chart doesn’t require any additional editing to be visually interesting, as captured in the following image:

    ![Drills - Scatter Plot.](Images/01-PyPlotDrills_Scatter.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Intro+and+PyPlot+Warmup&lessonpageTitle=Plotting+With+Pandas&lessonpageNumber=5.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F05-Matplotlib%2F2%2FLessonPlan.md)</sub>

- - -

## 2. Union Settlements: Plotting Pandas Data

| Activity Time:       0:35 |  Elapsed Time:      0:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Plotting Pandas Data (0:10)</strong></summary>

* Use the next few slides while covering the following talking points:

  * The plots in the previous activity were generated using mock data. In real applications, data could be messy, incomplete, or strangely formatted.

  * When dealing with real data, analysts will typically spend a lot of time "cleaning" it before generating any graphics. Once the data is clean, they can create an accurate and effective plot.

  * Last week, we learned how to clean up and preprocess datasets using Pandas. Therefore, we can expect that most real-world data that we analyze will come from within a Pandas DataFrame.

  * The creators of Pandas realized that most people using Pandas would then visualize their plots using Matplotlib. In a moment of pure genius, they built Matplotlib methods into their library to allow data analysts to easily generate complex charts in very little time.

* Open and run [02-Ins_PandasPlot](Activities/02-Ins_PandasPlot/Solved/avg_state_rain.ipynb) within Jupyter Notebook, and describe to the students how Pandas can be used to create intricate plots and data visualizations by using the values stored within DataFrames. Cover the following talking points:

  * Using PyPlot, it took a lot of code to create a bar chart of average rainfall by state.

  * Scroll down to the "Using Pandas to Chart a DataFrame" section of the application. See how the original DataFrame is being cut down to only those values that the application should chart. The index for the DataFrame is then set to the "State" column so that Pandas will use these values later on.

  * `DataFrame.plot()` is called, and the parameters `kind="bar"` and `figsize=(20,3)` are passed into it. This tells Pandas to create a new bar chart using the values stored within the DataFrame. The values stored within the index will be the labels for the x-axis, while the values stored within the other column will be used to plot the y-axis.

  * The bar chart produced is automatically styled. The header for the index is now the label for the x-axis, while the header for the other column has been placed inside a legend.

  * The chart can still be edited just like any other kind of PyPlot. For example, the title for the chart can still be set using `plt.title()`, as captured in the following image:

    ![Pandas Plotting Basics.](Images/02-PandasPlot_Basics.png)

  * Pandas will plot multiple columns as long as the DataFrame contains multiple columns of data.

  * We can also modify a specific Pandas plot by storing the plot within a variable and then using built-in methods to modify it. For example, `PandasPlot.set_xticklabels()` will allow the user to modify the tick labels on the x-axis without having to manually set the DataFrame's index, as captured in the following image:

    ![Multi Plotting.](Images/02-PandasPlot_MultiPlot.png)

  * To use a different plotting type, simply change the "kind" that is being passed as a parameter.

* Data Source: M. Palecki, I. Durre, J. Lawrimore, and S. Applequist, 2021: U.S. Annual/Seasonal Climate Normals (2006-2020) [National Centers for Environmental Information, National Oceanic and Atmospheric Administration](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc%3AC01623/html). N.B. This data was downloaded, combined, reduced, and calculated in Pandas.

</details>

<details>
  <summary><strong>✏️ 2.2 Student Do: Union Settlements (0:20)</strong></summary>

* **Files:**

  * [settlements.ipynb](Activities/03-Stu_Settlements-PlottingPandas/Unsolved/settlements.ipynb)

  * [union_settlements_1995.csv](Activities/03-Stu_Settlements-PlottingPandas/Unsolved/Resources/union_settlements_1995.csv)

* **Instructions:** [README](Activities/03-Stu_Settlements-PlottingPandas/README.md)

* In this activity, the students will create a bar chart that visualizes the total number of major collective-bargaining settlements by select unions in 1995.

* Open [03-Stu_Settlements](Activities/03-Stu_Settlements-PlottingPandas/Solved/settlements.ipynb) within the Jupyter notebook, and run and discuss the code to give the students an idea of the application’s end results.

* You may also use the slideshow to introduce this activity.

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Union Settlements (0:05)</strong></summary>

* Open [03-Stu_Settlements](Activities/03-Stu_Settlements-PlottingPandas/Solved/settlements.ipynb) within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they have. Make sure to discuss the following points:

  * Since the purpose of this chart will be to uncover how many settlements were agreed to by each union, the `value_counts()` must be collected for "Union".

  * Next, use `Series.plot(kind="bar")` to create the desired plot. This function will accept arguments for all the labels and other modifications to the overall size and appearance of the chart, as in the following image:

```python
# Get total settlements by union
union_data = settlement_data["UNION"].value_counts()

# Configure plot, figsize, title, and axis labels
figure1 = union_data.plot(kind="bar", facecolor="red", figsize=(8,6),
                                title="Major Collective Bargaining Settlements (1995)",
                                xlabel="Union",
                                ylabel="Settlements")

# Configure x-tick rotation
xticklabels = union_data.index
figure1.set_xticklabels(xticklabels, rotation=45, rotation_mode="anchor", ha="right", wrap=True)

# Show plot
plt.show()
```


  * Finally, the x-tick labels are quite long, so it is necessary to call the `.set_xticklabels()` function to rotate and position the labels to make them readable. `plt.tight_layout()` is then used to ensure all the labels are visible in the chart, which is captured in the following image:

    ![Settlement Chart.](Images/03-Settlement_Chart.png)

* Open [settlements_bonus.ipynb](Activities/03-Stu_Settlements-PlottingPandas/Solved/settlements_bonus.ipynb) within the Jupyter notebook, and point out that the first few cells are the same as the previous notebook&mdash;until it comes to filtering the settlement data. Discuss the following points:

  * A new DataFrame must be created with the data from the first Series that was created and the Series of filtered data. Display and discuss the DataFrame, and note that there is a field with a null value. Use `.fillna(0)` to ensure that the data will be plotted correctly.

  * Like the Series in the first part of this activity, this DataFrame can be used to call `.plot(kind="bar")` directly. Point out that to display the two columns as different colors, as in the following image, a list of colors must be passed as an argument in the `.plot()` function.

    ![Settlement Bonus Chart.](Images/03-Settlement_Bonus_Chart.png)

* Data Source: The National Archives. Major Collective Bargaining Settlements Public Use File, 1/1995 - 12/1995 (Partial Records). [https://aad.archives.gov/aad/](https://aad.archives.gov/aad/display-partial-records.jsp?dt=298&sc=1520%2C1523%2C1501%2C1502%2C1537%2C1503%2C1505%2C1507&cat=PS33&tf=F&bc=%2Csl%2Cfd&q=&as_alq=&as_anq=&as_epq=&as_woq=&nfo_1520=V%2C5%2C1900&op_1520=0&txt_1520=&nfo_1523=V%2C47%2C1900&op_1523=0&txt_1523=&nfo_1501=V%2C2%2C1900&cl_1501=&nfo_1502=V%2C1%2C1900&cl_1502=&nfo_1537=V%2C2%2C1900&cl_1537=&nfo_1503=V%2C7%2C1900&cl_1503=AAAA%2CAEA%2CALPA%2CNATC%2CAPA%2CUAW%2CBCW%2CMLBPA%2CNBPA%2CACTWU%2CIUEC&nfo_1505=N%2C6%2C1900&op_1505=3&txt_1505=&txt_1505=&nfo_1507=D%2C6%2C1900&op_1507=3&txt_1507=&txt_1507=)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Battling+Kings+-+Plotting+Pandas+Data&lessonpageTitle=Plotting+With+Pandas&lessonpageNumber=5.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F05-Matplotlib%2F2%2FLessonPlan.md)</sub>

- - -

## 3. Library Usage

| Activity Time:       0:30 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Plotting Groups (0:05)</strong></summary>

* Continue through the slideshow as you cover the talking points for this section.

* Ask the students if they remember how to group data using Pandas. Then, remind students of the following:

  * We can group and summarize data by using the Pandas `groupby()` function. The output of this is a GroupBy object.

  * A DataFrame is returned when a method such as `mean()` is called on a GroupBy object.

  ```python
  # Returns a DataFrame from a GroupBy object
  df.groupby('state').mean()
  ```

  * If the method is called on a specific column on a GroupBy object, then a Series is returned.

  ```python
  # Returns a Series from a GroupBy object
  states = df.groupby('state')
  states['city'].mean()
  ```

  * `DataFrame.plot()` or `Series.plot()` can then be used to quickly and easily create charts based on summary data.

* Open [04-Ins_GroupPlots](Activities/04-Ins_GroupPlots/Solved/plotting_groups.ipynb) in Jupyter Notebook, and go through the code with the class.

  * This example takes accident data from the National Highway Traffic Safety Administration's Fatality Analysis Reporting System, which allows users to explore data about accidents that have occurred on U.S. roadways.

  * Within this application, the original DataFrame is grouped by the values of the "FUNC_SYSNAME" column (which categorizes the type of roadway that the accident took place on) and returned as a GroupBy object.

  * Those values are then counted in the column "FUNC_SYSNAME", returning a Series with the count of each type of roadway.

  * This Series is then charted using Pandas, as captured in the following images

```python
# Create a bar chart based on the group series from before
count_chart = count_road_types.plot(kind='bar', figsize=(6,8))

# Set the xlabel and ylabel using class methods
count_chart.set_xlabel("Road Type")
count_chart.set_ylabel("Number of Accidents")

plt.show()
plt.tight_layout()
```

  ![Charting Groups Accident Chart.](Images/accidents.png)

* Data Source: National Highway Traffic Safety Administration. 2019 National Accidents - Fatality Analysis Reporting System  [https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/2019/National/](https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/2019/National/)

</details>

<details>
  <summary><strong>✏️ 3.2 Student Do: Library Usage: Grouped Charts (0:20)</strong></summary>

* **Files:**

  * [library_usage.ipynb](Activities/05-Stu_LibraryUsage-Groupby/Unsolved/library_usage.ipynb)

  * [library_usage.csv](Activities/05-Stu_LibraryUsage-Groupby/Resources/library_usage.csv)

* **Instructions:** [README](Activities/05-Stu_LibraryUsage-Groupby/README.md)

* In this activity, the students will create a pair of charts based on library usage collected from San Francisco. This activity will require them to create and analyze GroupBy objects before printing some visualizations of their findings to the screen.

* Open [05-Stu_LibraryUsage](Activities/05-Stu_LibraryUsage-Groupby/Solved/library_usage.ipynb) within the Jupyter Notebook and run the code to show the results of the application.

* You may choose to use the slideshow to accompany this activity.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Library Usage (0:05)</strong></summary>

* Open [05-Stu_LibraryUsage](Activities/05-Stu_LibraryUsage-Groupby/Solved/library_usage.ipynb) within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they have. Make sure to discuss the following points:

* For the bar chart, the original DataFrame is filtered on "Total Checkouts" to ensure we are only capturing the data on patrons who have checked out at least one item since they became a patron.

  * This filtered DataFrame is then grouped by the values within the "Patron Type Definition" column and counted. Note that if we had not filtered the data, then we would have counted patrons who had never checked out items from the library.

  * The title for the chart is set within the `Series.plot()` method, while the x- and y-axis labels are set using Matplotlib's `Axes.set_xlabel()` and `Axes.set_ylabel()` methods, as captured in the following image:

    ```python
    # Filter data so it only includes patrons who checked out at least one item
    library_loans_df = pd.DataFrame(library_usage_df.loc[library_usage_df['Total Checkouts']>0,:])

    # Split up our data into groups based upon 'Patron Type Definition'
    patron_groups = library_loans_df.groupby('Patron Type Definition')

    # Find out how many of each patron type borrowed library items
    patron_borrows = patron_groups['Total Checkouts'].count()

    # Chart our data, give it a title, and label the axes
    patron_chart = patron_borrows.plot(kind="bar", title="Library Usage by Patron Type")
    patron_chart.set_xlabel("Patron Type")
    patron_chart.set_ylabel("Number of Patrons Borrowing Items")

    plt.show()
    plt.tight_layout()
    ```

    The chart produced by this code is represented in the following image:

    ![Bar Chart](Images/05-LibraryUsage_BarChart.png)

  * For the pie chart, the original DataFrame is grouped by both the "Home Library Definition" and "Patron Type Definition" columns and returns a GroupBy object.

  * Since there are multiple columns of numeric DataTypes, the sum analysis is performed on only the column we are interested in, "Total Checkouts". Including the column name in a list produces a DataFrame containing multiple indexes so that the total checkouts is calculated by patron type and home library branch.

    ```python
    # Split up our data into groups based upon 'Home Library Definition' and 'Patron Type Definition'
    library_groups = library_usage_df.groupby(['Home Library Definition','Patron Type Definition'])

    # Create a new variable that holds the sum of our groups
    sum_it_up = library_groups[['Total Checkouts']].sum()
    sum_it_up.head(20)
    ```

    The DataFrame this code produces is captured in the following image:

    ![Multiple Indexes.](Images/05-LibraryUsage_MultiIndex.png)

  * To create a chart based on one branch alone, `loc` must be used, and a single branch name or "Home Library Definition" must be passed. This returns a DataFrame with only the "Patron Type Definition" column as the index and "Total Checkouts" as the value.

  * Since there are several patron types with minimal checkouts, the pie charts could look messy with overlapping text if we do not filter the data. Creating a variable for the minimum number of checkouts allows us to change that variable in one place and include it in the chart title to ensure a complete picture of the data is included in the chart. Since some branches are busier than others, this also allows us to change the values of `branch` and `min_checkouts` as needed.

  * When creating a pie chart, a _y_ value must be passed into the `DataFrame.plot()` method. This lets Pandas know what label or position of the column to plot. Here, we are plotting “Total Checkouts”.

  * The title for the pie chart is dynamically set by concatenating strings:

    ```python
    # Make a variable called branch and store a 'Home Library Definition' in it
    branch = "Anza"

    # Make a variable called min_checkouts that you can change depending on how busy the library branch you've chosen is
    min_checkouts = 5000

    # Collect the loans of the branch above
    just_one_branch = sum_it_up.loc[branch]

    # Filter the data to patron types with greater than the value set for min_checkouts
    just_one_branch = just_one_branch.loc[just_one_branch['Total Checkouts']>min_checkouts,:]

    # Create a pie chart based upon the total checkouts (or loans) of that single branch
    branch_pie = just_one_branch.plot(kind="pie", y='Total Checkouts', title=("Loans of " + branch +
                                                                              " Branch for Patron Types Over "
                                                                            + str(min_checkouts) + " Loaned Items"))
    branch_pie.set_ylabel("Branch Checkouts")

    plt.axis("equal")
    plt.show()
    ```

    The pie chart produced by this code is captured in the following image:

    ![Pie Chart Code.](Images/05-LibraryUsage_PieChart.png)


* Data Source: [City and County of San Francisco. (2019). Library Usage. San Francisco Open Data.](https://data.sfgov.org/Culture-and-Recreation/Library-Usage/qzz6-2jup)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Bike+Trippin%27&lessonpageTitle=Plotting+With+Pandas&lessonpageNumber=5.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F05-Matplotlib%2F2%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:40  |
|---------------------------|---------------------------|

- - -

## 4. Miles per Gallon

| Activity Time:       0:20 |  Elapsed Time:      2:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>✏️ 4.1 Student Do: Miles per Gallon: Scatter Plot (0:15)</strong></summary>

* **Files:**

  * [mpg.ipynb](Activities/06-Stu_MilesPerGallon-ScatterPlot/Solved/mpg.ipynb)

  * [MPG.csv](Activities/06-Stu_MilesPerGallon-ScatterPlot/Resources/mpg.csv)

* **Instructions:**

  * [README](Activities/06-Stu_MilesPerGallon-ScatterPlot/README.md)

* In this activity, the students will create a scatter plot using vehicle data, Pandas, and Matplotlib.

* Open [06-Stu_MilesPerGallon](Activities/06-Stu_MilesPerGallon-ScatterPlot/Solved/mpg.ipynb) within the Jupyter notebook, and run and discuss the code to give students an idea of the application’s end results.

* You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students the chart that they will be attempting to create, which is captured in the following image:

![MPG_example_plot.](Images/06-MPG_Output.png)

</details>

<details>
  <summary><strong>📣 4.2 Instructor Do: Review Miles Per Gallon (0:05)</strong></summary>

* Open [06-Stu_MilesPerGallon](Activities/06-Stu_MilesPerGallon-ScatterPlot/Solved/mpg.ipynb) within Jupyter Notebook, and go through the code line by line with the class, answering whatever questions they may have. Make sure to discuss the following points:

  * There are quite a few rows with missing values in the original dataset. These rows are filtered out using a `loc[]` filter that finds any rows that do not contain a "?" value.

  * The data stored within the "horsepower" column is not numeric by default. This is due to the "?" values that were there, so `pandas.to_numeric()` must be used to convert the column into a usable format.

  * The `x` and `y` parameters in `DataFrame.plot()` allow users to specify which columns they would like to chart. This allows the user to create graphs without having to filter the DataFrame down to just 2 columns, as captured in the following image:

```python
# Create a scatter plot that compares MPG to horsepower
car_data.plot(kind="scatter", x="horsepower", y="mpg", grid=True, figsize=(8,8),
              title="MPG Vs. Horsepower")
plt.show()
```
  ![MPG Output.](Images/06-MPG_Output.png)

* Data Source: Ramos, Ernesto and David Donoho. (1983). 1983 Data Exposition Auto MPG Data Set. Revised from CMU StatLib library. University of California-Irvine Machine Learning Repository. [https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/](https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Miles+Per+Gallon&lessonpageTitle=Plotting+With+Pandas&lessonpageNumber=5.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F05-Matplotlib%2F2%2FLessonPlan.md)</sub>

- - -

## 5. Traveling Companions

| Activity Time:       1:00 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Plotting Multiple Lines (0:05)</strong></summary>

* In this activity, we will explore creating a multiplot with Matplotlib and then with Pandas.

* Use the next few slides to cover the following talking points:

  * We’ve already learned that Pandas plotting has many of the same features and capabilities as Matplotlib.

  * The final feature that we will learn about today will be adding multiple plots to a single figure.

  * Fundamentally, adding multiple plots to the same figure using Pyplot is the same as using `dataframe.plot()`. We pass multiple plots in the same code block before using the `pyplot.show()` function.

* Open [07-Ins_PandasMultiLine](Activities/07-Ins_PandasMultiLine/Solved/unemploy_chart.ipynb) within Jupyter Notebook, and go through the code with the class.

  * Explain to the class how this data, which keeps track of international unemployment numbers, has been split between two CSV files and, therefore, must be merged.

  * After the files have been merged, the duplicate "Country Code" column should be deleted, and the original "Country Code" column should be reset to its original name, as captured in the following image:

    ![Merging DataFrames.](Images/07-MultiLine_Merge.png)

  * The average global unemployment rate can be found by identifying the means of the DataFrame.

  * Since all of the years are stored within the column headers, they can be collected by taking the Series created by the means calculation and examining its keys, as in the following image:

    ![Average and Years.](Images/07-MultiLine_Lists.png)

  * The two line plots are then created using `plt.plot()`; the first uses the average unemployment findings for its *x* values, while the second takes in the values of a single row. The *x* values for both charts should be the "years" list created earlier.

  * The tuples method discussed during the previous class is used to create the legend for the plots, as captured in the following image:

    ![MultiLine Plot.](Images/07-MultiLine_Plot.png)

* Demonstrate that an identical plot can be created with Pandas, as captured in the following image:

    ![MultiLine Plot.](Images/multiline01.png)

  * Pandas can generate many common charts, but Pandas plots are generally less flexible and customizable than Matplotlib plots.

* Data Source: International Labour Organization, ILOSTAT database. Data retrieved on June 15, 2021. The World Data Bank. Unemployment, total (% of total labor force) (modeled ILO estimate). [https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS)

</details>

<details>
  <summary><strong>✏️ 5.2 Student Do: Traveling Companions, Part 1 (0:15)</strong></summary>

* **Files:**

  * [traveling_companions.ipynb](Activities/08-Stu_Travel-Part1/Unsolved/traveling_companions.ipynb)

  * [2016_travelers.csv](Activities/08-Stu_Travel-Part1/Resources/2016_travelers.csv)

  * [2017_travelers.csv](Activities/08-Stu_Travel-Part1/Resources/2017_travelers.csv)

  * [2018_travelers.csv](Activities/08-Stu_Travel-Part1/Resources/2018_travelers.csv)

* **Instructions:** [README.md](Activities/08-Stu_Travel-Part1/README.md)

* The rest of class will be dedicated to creating a plot using Pandas and Matplotlib; the plot will visualize a comparison of travelers to Malaysia from different countries of origin.

* This mini-project has been broken down into three parts and was designed for students to work together in groups.

* In this first part, the students will take three CSV files and merge them. They will then need to rename and style the columns so that they reflect the data properly.

* Open [08-Stu_Travel-Part1](Activities/08-Stu_Travel-Part1/Solved/traveling_companions.ipynb) within the Jupyter notebook, and run and discuss the code to give the students an idea of the application’s end results.

* You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students what they will be attempting to create, which is captured in the following image:

  ![Merged Table.](Images/08-TravelingCompanion_Output.png)

</details>

<details>
  <summary><strong>⭐ 5.3 Review: Traveling Companions, Part 1 (0:05)</strong></summary>

* Open [08-Stu_Travel-Part1](Activities/08-Stu_Travel-Part1/Solved/traveling_companions.ipynb) within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they have. Make sure to discuss the following points:

  * The DataFrames should be merged on the "Country of Nationality" column. Using an outer join ensures that no data will be lost even if the country is unique to a single CSV&mdash;although that is not the case with these files and the countries involved.

  * As DataFrames are merged, columns should be renamed so that it is clear what year each column is from.

  * Although it is possible to merge all of the DataFrames using one incredibly long series of nested merge statements, it is far simpler to merge the DataFrames one pair at a time, as captured in the following image. This allows programmers to modify columns as they go and reduces the risk of naming a column incorrectly.

```python
# Merge the first two datasets on "COUNTRY OF NATIONALITY" so that no data is lost (should be 44 rows)
combined_travel_df = pd.merge(travel_2016_df, travel_2017_df,
                                 how='outer', on='COUNTRY OF NATIONALITY')
```
```python
# Rename our _x columns to "2016 Alone", "2016 With Spouse", "2016 With Children", "2016 With Family/Relatives",
# "2016 Student Group", "2016 With Friends", "2016 With Business Associate", "2016 With Incentive Group",
# and "2016 Others"

combined_travel_df = combined_travel_df.rename(columns={"ALONE_x":"2016 Alone",
                                                        "WITH SPOUSE_x":"2016 With Spouse",
                                                        "WITH CHILDREN_x":"2016 With Children",
                                                        "WITH FAMILY/RELATIVES_x":"2016 With Family/Relatives",
                                                        "STUDENT GROUP_x":"2016 Student Group",
                                                        "WITH FRIENDS_x":"2016 With Friends",
                                                        "WITH BUSINESS ACCOCIATE_x":"2016 With Business Associate",
                                                        "WITH INCENTIVE GROUP_x":"2016 With Incentive Group",
                                                        "OTHERS_x":"2016 Others"})

# Rename our _y columns to "2016 Alone", "2016 With Spouse", "2016 With Children", "2016 With Family/Relatives",
# "2016 Student Group", "2016 With Friends", "2016 With Business Associate", "2016 With Incentive Group",
# and "2016 Others"
combined_travel_df = combined_travel_df.rename(columns={"ALONE_y":"2017 Alone",
                                                        "WITH SPOUSE_y":"2017 With Spouse",
                                                        "WITH CHILDREN_y":"2017 With Children",
                                                        "WITH FAMILY/RELATIVES_y":"2017 With Family/Relatives",
                                                        "STUDENT GROUP_y":"2017 Student Group",
                                                        "WITH FRIENDS_y":"2017 With Friends",
                                                        "WITH BUSINESS ACCOCIATE_y":"2017 With Business Associate",
                                                        "WITH INCENTIVE GROUP_y":"2017 With Incentive Group",
                                                        "OTHERS_y":"2017 Others"})

combined_travel_df.head()
```

* Data Source: Tourism Malaysia. (2021). Travelling Companion. [https://www.data.gov.my/data/en_US/dataset/travelling-companion](https://www.data.gov.my/data/en_US/dataset/travelling-companion)

</details>

<details>
  <summary><strong>✏️ 5.4 Student Do: Traveling Companions, Part 2 (0:05)</strong></summary>

* **Files:**

  * [traveling_companions.ipynb](Activities/09-Stu_Travel-Part2/Unsolved/traveling_companions.ipynb)

  * [2016_travelers.csv](Activities/09-Stu_Travel-Part2/Resources/2016_travelers.csv)

  * [2017_travelers.csv](Activities/09-Stu_Travel-Part2/Resources/2017_travelers.csv)

  * [2018_travelers.csv](Activities/09-Stu_Travel-Part2/Resources/2018_travelers.csv)

* **Instructions:** The instructions for this activity are contained within the unsolved notebook.

* In this second part, the groups will examine the averages of each column, decide which columns they want to keep in their DataFrame for analysis, and set the index.

* Open [09-Stu_Travel-Part2](Activities/09-Stu_Travel-Part2/Solved/traveling_companions.ipynb) within the Jupyter notebook, and run and discuss the code to give the students an idea of the application’s end results.

* You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students what they will be attempting to create, which is captured in the following image:

  ![Companion Calculations.](Images/09-TravelingCompanion2_Output.png)

</details>

<details>
  <summary><strong>⭐ 5.5 Review: Traveling Companions, Part 2 (0:05)</strong></summary>

* Open [09-Stu_Travel-Part2](Activities/09-Stu_Travel-Part2/Solved/traveling_companions.ipynb) within the Jupyter notebook, and go through the code line by line with the class, answering whatever questions they have. Make sure to discuss the following points:

  * To calculate the average of each column, use `.mean()` on the DataFrame and examine the results.

  * Three types of travel companions do not have at least 1% of travelers across all three observed years, so a new DataFrame is created to leave those columns out.

  * The index is set to "Country of Nationality" so it can be used to more easily locate the rows of interest to chart in the next part, as captured in the following image:

    ![Time to Calculate.](Images/09-TravelingCompanion2_Code.png)

* Data Source: Tourism Malaysia. (2021). Travelling Companion. [https://www.data.gov.my/data/en_US/dataset/travelling-companion](https://www.data.gov.my/data/en_US/dataset/travelling-companion)

</details>

<details>
  <summary><strong>✏️ 5.6 Student Do: Traveling Companions, Part 3 (0:20)</strong></summary>

* **Files:**

  * [traveling_companions.ipynb](Activities/10-Stu_Travel-Part3/Unsolved/traveling_companions.ipynb)

  * [2016_travelers.csv](Activities/10-Stu_Travel-Part3/Resources/2016_travelers.csv)

  * [2017_travelers.csv](Activities/10-Stu_Travel-Part3/Resources/2017_travelers.csv)

  * [2018_travelers.csv](Activities/10-Stu_Travel-Part3/Resources/2018_travelers.csv)

* **Instructions:** The instructions for this activity are contained in the unsolved notebook.

* In this final part, the class will take the DataFrame that they created and, using Matplotlib, chart a comparison of travelers from three different countries visiting Malaysia with their spouse over time.

* Open [10-Stu_Travel-Part3](Activities/10-Stu_Travel-Part3/Solved/traveling_companions.ipynb) within the Jupyter notebook, and run and discuss the code to give the students an idea of the application’s end results.

* You may choose to use the slideshow to accompany this activity. Otherwise, show and describe to the students what they will be attempting to create, which is captured in the following image:

  ![Traveling Companion Calculations.](Images/10-TravelCompanion3_Output.png)

</details>

<details>
  <summary><strong>⭐ 5.7 Review: Traveling Companions, Part 3 (0:05)</strong></summary>

* Open [10-Stu_Travel-Part3](Activities/10-Stu_Travel-Part3/Solved/traveling_companions.ipynb) within the Jupyter notebook and go through the code line by line with the class, answering whatever questions they may have. Make sure to discuss the following points.

  * Three Series must be created for the graph using `loc[]` filtering. They all look for the row with a country name equal to the saved variable; since the countries are stored in all uppercase characters, the variable must also be in all uppercase characters. By also having a variable store the type of traveling companion, we can easily use that variable to collect all of the columns to be included. Storing these values in variables means that we can easily change what we’re charting by only changing the variable.

  * The "years" list that will serve as the chart's x-axis can be made manually because the years are consistent and known to the programmer.

  * Although the `Series.plot()` method could theoretically be used to create the plots for each country, the data is stored within different data types, so it is easier to use the `plt.plot()` method, as captured in the following images:

```python
# Create a variable for each country to chart
country1 = "USA"
country2 = "THAILAND"
country3 = "PHILIPPINES"

# Set type of traveling companion
columns_to_compare = "With Spouse"

# Create a Series for each chosen country that looks for the chosen travel companion from 2016 to 2018
country1_traveler_over_time = travel_reduced.loc[country1,
                                                [f"2016 {columns_to_compare}",
                                                 f"2017 {columns_to_compare}",
                                                 f"2018 {columns_to_compare}"]]

country2_traveler_over_time = travel_reduced.loc[country2,
                                                [f"2016 {columns_to_compare}",
                                                 f"2017 {columns_to_compare}",
                                                 f"2018 {columns_to_compare}"]]

country3_traveler_over_time = travel_reduced.loc[country3,
                                                [f"2016 {columns_to_compare}",
                                                 f"2017 {columns_to_compare}",
                                                 f"2018 {columns_to_compare}"]]

# Create a list of the years that we will use as our x axis
years = [2016,2017,2018]

# Plot our line that will be used to track the first country's traveling companion percentage over the years
plt.plot(years, country1_traveler_over_time, color="green", label=country1)

# Plot our line that will be used to track the second country's traveling companion percentage over the years
plt.plot(years, country2_traveler_over_time, color="blue", label=country2)

# Plot our line that will be used to track the third country's traveling companion percentage over the years
plt.plot(years, country3_traveler_over_time, color="orange", label=country3)

# Place a legend on the chart in what Matplotlib believes to be the "best" location
plt.legend(loc="best")

plt.title("Traveling " + columns_to_compare + " Country Comparison")
plt.xlabel("Years")
plt.xticks(np.arange(min(years), max(years)+1, 1.0))
plt.ylabel("% Travelers")

# Print our chart to the screen
plt.show()
```

  ![Charting Companions.](Images/10-TravelCompanion3_Output.png)

* Open [traveling_companions_bonus.ipynb](Activities/10-Stu_Travel-Part3/Solved/traveling_companions_bonus.ipynb) within the Jupyter notebook, go through the cells that have previously been covered. From Part 3, go through the code line by line with the class, comparing the differences with the previous notebook, answering whatever questions that students may have. Make sure to discuss the following points:

  * Inputs can still function within Jupyter Notebook. Whenever the cell containing the input line is run, a prompt will be printed within the space that follows, allowing a user to add a response.

  * There are many types of traveling companion columns that a user might be interested in charting, but it is unlikely that the user would know what they all are. In this case, it would be helpful to provide a numbered menu so the user can easily input a number selection. That number could then be used to create the string for the chosen column.

  * A `while` loop is included as part of this menu selection as a way of error-checking to ensure that the user selects an option that will provide a traveling companion type. If the Boolean variable is not changed to `True`, the loop will again prompt the user for their selection.

  * Since the user does not know that the countries are stored in all caps, `.upper()` is used to change the user country input to uppercase within the `loc[]` row searches.

  * Note that the charting code remains the same.

* Data Source: Tourism Malaysia. (2021). Travelling Companion. [https://www.data.gov.my/data/en_US/dataset/travelling-companion](https://www.data.gov.my/data/en_US/dataset/travelling-companion)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Winner+Wrestling&lessonpageTitle=Plotting+With+Pandas&lessonpageNumber=5.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F05-Matplotlib%2F2%2FLessonPlan.md)</sub>

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
