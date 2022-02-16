# 22.4 Databricks

## Overview

In today's class, students will use Spark on Databricks to perform data analysis on the cloud. They will use both the Python and SQL interfaces of Databricks, with an emphasis on the SQL interface, to perform increasingly complex queries.

## Class Objectives

By the end of today's class, students will be able to:

  * Describe the purpose of Databricks, and identify two of its key features and a use case.

  * Set up a Databricks environment.
  
  * Identify the key components of a Databricks environment. 

  * Navigate the Databricks workspace using `dbutils`. 

  * Import data into a new notebook using the following sources: Parquet, CSV, and S3.

  * Explain the advantage of Parquet as a big-data storage format.

  * Perform complex data analysis using Python and SQL interfaces, including joins.

  * Identify two advantages of using Databricks over PySpark in data analysis.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Because students have been working with Spark, students will be quickly up and running in Databricks.

* Due to the limitations of the free Community Edition of Databricks, it will not be possible for students to experience all the aspects of using Databricks, such as real-time collaboration. However, they will use today's class to familiarize themselves with the interface.

* Also due to the limitations of the free Community Edition of Databricks, you will need to detach a notebook from its cluster after using it. Remember that only one notebook should be attached to a cluster at a given time. Instructions on detaching and attaching a notebook are found toward the end of activity 2.1.

* For the sake of completeness, all lines of code in each activity are explained in the lesson plan. However, you do not need to explain each line of code in great detail, especially parts students have encountered multiple times.

* Today’s class will give students an opportunity to polish their SQL skills, which are essential for job interviews—SQL is the de facto industry standard for retrieving information from large databases. In the second half of the class, students will work in groups to perform complex queries across multiple tables. 

* If pressed for time, the Instructor and Student joins activities may be shortened, as they deal with material students have seen. You may also elect to lengthen the final group activity by 15 to 30 minutes and shorten student presentations and activity review.

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. In this case, we have provided notes within the lesson plan so that you can adjust the length of the lesson to fit into a weekday class.

  * Look for a  ⏰**3-Hour Adjustment** note at the top of activities in this lesson plan. If this class is being taught on a weekday, use the directions found in the note. Also keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class.

* Refer to the [Student FAQ](../../../05-Instructor-Resources/README.md#unit-22-big-data) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* **Important:** Remember that the slideshows are for instructor use only. To distribute the slides to students, first export the slides to a PDF file, and share the PDF with the class.
</details>

- - -


# Class Activities


## 1. Introduction to Databricks and Signing Up

| Activity Time:       0:25 |  Elapsed Time:      0:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 1.1 Instructor Do: Introduction to Databricks (0:15) </strong></summary>

* Welcome students to class and open the [slideshow](https://docs.google.com/presentation/d/1257v9sT7tw-6gmLrAj1ayIEvd86YK7OVFgn3zM2r4js/edit#slide=id.g7ad77fb758_0_0).

* Congratulate the class on making it to the final day of formal in-class instruction. After today, students will consolidate their data analytics skills in their final projects. (Slide 2)

* State the learning objectives of today's class. (Slide 3)

* Inform students that, in addition to introducing Databricks, today’s class is an opportunity to brush up on SQL, and that they will use the Databricks interface to do so. Why is SQL so important?

  * In job interviews, for example, companies emphasize SQL because it is the de facto industry standard for querying databases, including filtering data and working across multiple tables.

  * For example, when a company's inventory database is spread across a number of tables, SQL is typically used to retrieve information, including summary tables.

* Explain that today’s class will also build on students’ knowledge of Spark and SQL, such as filtering data.  

* Provide the following example:

  * Using a cluster of CPUs on site to run Spark at a company requires significant work to set it up and manage it. This includes managing the hardware and scheduling any work to be performed, depending on demand.

* Give a high-level overview of Databricks. (Slide 5)

  * Databricks is a cloud platform for Spark. In other words, Databricks enables running Apache Spark on cloud servers provided by Amazon's AWS or Microsoft's Azure, for example.

  * Databricks provides a robust system to manage and optimize clusters of computers for big-scale data analysis.

* Ask students to list some possible advantages of running Spark on the cloud and then discuss them together (Slide 6). You might include any real-life experience you have in the complexities of managing a big data platform, for example:

  * **Ease of use**. Databricks can automatically scale up or down its activities depending on what’s needed. Traditionally, managing Spark clusters was a laborious and error-prone process. Databricks does away with much of the complexity involved in the process.

  * **Enables collaboration**. Multiple team members can work on the same notebook. For example, after a data engineer prepares the data, one person can work on data analysis while another person works on data visualization.

  * **Cost effective**. The time and money spent on managing clusters of computers for data analysis is often significantly reduced. For a data team with budgetary constraints, it will likely be much cheaper to run a Spark cluster in the cloud than manage an on-site cluster, which will have administrative costs.

  * **Versatile**. You can use any of Python, R, SQL, and Scala in the same Databricks notebook.

* Explain the potential downside of using Databricks. You can also discuss your own experience using a cloud Spark platform. 

  * Of the cloud platforms available to run Spark, Databricks is one of the more expensive ones. A single cluster that is heavily used can cost thousands of dollars per month or more. 

* Next, explain that Spark is designed to work with multiple sources of data, and this class will be an opportunity to put this capability into practice. We’ll work with different sources of data including CSV and Parquet files. 

* Introduce the Parquet data format. (Slide 7)

  * Parquet is a data format commonly used with Spark.

  * Unlike the CSV format, Parquet allows you to load only selected columns into a DataFrame.

* Ask the class to reflect on a possible advantage of using a format like Parquet over CSVs (slides 7–9). Explain that one advantage is how Parquet loads data—by specific columns instead of rows.

  * Traditional data formats store data by row. If Spark uses multiple nodes to perform queries, each node would need to load a copy of all rows of the dataset.

  * Especially when working with massive amounts of data, loading only the specified columns can lead to savings in time and computing resources.

* Summarize the key benefits of using Databricks: 

  * Data analytics teams can spend more time analyzing data and less time configuring and managing clusters.

  * Teams can also create visualizations quickly to explore data, as well as create dashboards for an audience. 

</details>

<details>
  <summary><strong> ✏️ 1.2 Students Do: Sign Up for Databricks (0:10)</strong></summary>

* **Instructions:** [README.md](Activities/01-Stu_Sign_up/README.md)

* **Files:**

  * [PDF Guide](Activities/01-Stu_Sign_up/Resources/signup.pdf)

  * [ufoSightings](Activities/01-Stu_Sign_up/Resources/ufoSightings.csv)

* In this activity, students will use the PDF guide to sign up for a free Databricks Community Edition account.

* TAs should be available to help students with this process, should they encounter any issues. 

* After students sign up, they can try to upload the CSV file to Databricks in order to create a DataFrame in a notebook. 

</details>

## 2. Databricks Basics

| Activity Time:       0:40 |  Elapsed Time:      1:05  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: Instructor Do: Databricks Demo (0:15) </strong></summary>

* **Files:**

  * [food_prices.parquet](Activities/02-Ins_Databricks_Demo/Resources/food_prices.parquet)

  * [ufoSightings.csv](Activities/02-Ins_Databricks_Demo/Resources/ufoSightings.csv)

  * [ufoSightingsCopy.csv](Activities/02-Ins_Databricks_Demo/Resources/ufoSightingsCopy.csv)

* Explain to students that we’ll now explore the basics of the Databricks interface. 

#### Using the Interface Tabs

* Click the Databricks tab and begin explaining how to navigate the Databricks interface.

    ![tabs](Images/tabs01.png)

    * This interface allows us to perform some common tasks, such as uploading a dataset or creating a new notebook. 

* Click the Workspace tab, and explain that this is where assets such as notebooks can be found.

  ![workspace](Images/workspace01.png)

* Show the Clusters tab. This is where clusters are created and managed. It’s also possible to manage job clusters, but this capability is limited in the free Community Edition account. 

  ![clusters](Images/clusters01.png)

#### Upload a Dataset

* Next, in the Databricks tab, demonstrate how to upload a dataset by dragging `ufoSightings.csv` and `ufoSightingsCopy.csv`, and then clicking “Create Table in Notebook.”

  ![upload](Images/upload01.png)
  
* Make an explicit connection between Colab, which students have been using this week, and Databricks: They are both capable of running Spark notebooks on the cloud.

* Attach the cluster you created to the notebook, and explain that Databricks automatically loads the dataset into a Spark DataFrame. However, this may not always lead to desired results. Click on the "play" arrow or press the Shift and Enter (or Return) keys to run the cell. Note the following to the class: 

  ![notebook01](Images/notebook01.png)

  * The CSV file is stored in `/FileStore/tables`.

  * A preview of the DataFrame is shown, but the column names are not read properly.

* Pause for a moment to ask the class why the column names are not read properly.

  * The `header` option is set to `false`.

#### Use the dbutils File System

* Next, you’ll explain the basics of the `dbutils` file system. First, click “Add Cell Below.” In the new cell, run the command to list the contents of `FileStore/tables`.

  ![notebook01](Images/notebook02.png)

  ```python
  dbutils.fs.ls("/FileStore/tables/")
  ```

  * `dbutils` stands for Databricks utilities.

  * `fs` stands for File System.

  * `dbutils.fs` is functionally similar to the command line interface used by students (Terminal or Git Bash).

  * Slack out the link to the [dbutils.fs documentation](https://docs.databricks.com/data/databricks-file-system.html) so students can reference it for more information.

#### Remove a File with dbutils (Optional)
  
* Show how to remove a file with `dbutils`.

  ```python
  dbutils.fs.rm("/FileStore/tables/ufoSightingsCopy.csv")
  ```

  * Running `dbutils.fs.ls("/FileStore/tables")` again will show that the file was deleted.

#### Manually Load a Dataset

* Next, load the dataset into a Spark DataFrame manually.

  ```python
  df2 = spark.read.csv(file_location, inferSchema=True, header=True)
  df2.show(5)
  ```

  ![df01](Images/df01.png)
  
  * This time, the column headings were read correctly because `header` was set to `True`.

  * `df2.show(5)` returns a preview of the DataFrame.

#### Use the display Function
  
* Explain that `display` is a special Databricks-specific command, and show students how to use it.

  ![display](Images/display.png)

  * Like `show`, `display` returns a preview of the DataFrame. However, it offers additional features.

  * By clicking an arrow, it’s possible to sort the DataFrame by that column.

  * It’s also possible to create a basic visualization with the visualization button.

#### Work with Multiple Programming Languages

* Show that it’s possible to work in Databricks in multiple languages. The default language for a notebook cell is Python. However, R, SQL, and Scala can also be run in the same notebook. As an example, enter the following R code.

  ![magic](Images/magic.png)

  * The magic command `%r` allows running R code in that particular cell.

* Next, create a temporary table from the DataFrame and run a SQL query on it by using the following code: 

  ```python
  df2.createOrReplaceTempView("ufo")
  ```
  ```sql
  %sql
  SELECT *
  FROM ufo
  LIMIT 5;
  ```

  * Creating a temporary table allows us to query a Spark DataFrame with SQL queries. We’ll name our temporary table `ufo`. 

  * The second cell contains the `%sql` magic command, which specifies that this cell will run SQL code.

  * The SQL query returns the same preview of the DataFrame as `display`, with the same sorting and visualization capabilities.

#### Create, Use, and Delete Widgets (Optional) 

* Demonstrate how to create a widget in a SQL cell. Otherwise, tell students to consult the notebook on their own to review the code for this task. Note that the widget code should be placed in its own notebook cell. Here’s the code: 

  ```sql
  %sql
  CREATE WIDGET TEXT state DEFAULT "tx"
  ```

  * This command creates a text widget at the top of the notebook that can be used to select rows by state.

*  Show how to use a widget. Here’s the code: 

  ```sql
  %sql
  SELECT *
  FROM ufo
  WHERE ufo.state = getArgument("state")
  LIMIT 5;
  ```
 
  ![widget](Images/widget.png)

  * The `getArgument` function retrieves the text value from the widget, in this case, `ca`.

  ![widget02](Images/widget02.png)

*  Show how to delete a widget. Here’s the code: 

  ```sql
  %sql
  REMOVE WIDGET state
  ```

#### Work with Parquet Files 

* Demonstrate how to read in a Parquet file by using the following code:

  ```python
  food_prices_file = 's3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/food_prices.parquet'
  parquet_df = spark.read.parquet(food_prices_file, inferSchema=True, header=True)
  
  display(parquet_df)
  ```

  ![Images/parquet01.png](Images/parquet01.png)
  
* Explain that the advantage of Parquet files in a big data context is that only selected columns can be loaded, saving time and cost associated with loading unnecessary data. This is shown in the following code: 

  ```python
  selected_columns_df = spark.read.parquet(food_prices_file, inferSchema=True, header=True).select('item', 'store', 'price')

  display(selected_columns_df)
  ```

  * With Parquet, it's possible to load only the `item`, `store`, and `price` columns.

  ![Images/parquet02.png](Images/parquet02.png)

* **Important**: Explain that when exiting a notebook, students should be sure to **detach** it from its cluster, as shown in the following image: 

  ![detach01](Images/detach01.png)

* Also explain that a notebook that has timed out or has been detached from a cluster can be reattached as shown in the following image: 

  ![detach02](Images/detach02.png)

#### Import and Export a Databricks Notebook

* Show how to export and import a Databricks notebook. Explain that this will be important when checking solution files for the activities.

  ![export](Images/export.png)

  * DBC is the extension used with Databricks notebook archives.

  ![import](Images/import.png)

  * Follow this menu to upload a DBC notebook to Databricks.

  * Once imported, the notebook can be found in the workspace.

* Ask the students to reflect on any differences they have noticed between running Spark on Colab, which they have done until today, and running Spark on Databricks. 

  * Unlike Colab, Databricks requires no code to set up Spark, as it’s specifically designed to run Spark.

  * Databricks offers functionality in addition to standard Spark, such as `display` and widgets.

* Recap what was covered in this Databricks demo: uploading datasets, creating DataFrames, basic file navigation, basic data analysis and visualization, and attaching and detaching clusters. 

* Answer any questions before moving on to the activity. 

</details>

<details>
  <summary><strong> ✏️ 2.2 Students Do: Databricks Basics (0:15)</summary></strong>

In this activity, students will perform basic navigation and data analysis tasks in Databricks. 
  
* **Instructions:** [README.md](Activities/03-Stu_Basics/README.md)

* **Files:**

  * [vehicles.csv](Activities/03-Stu_Basics/Resources/vehicles.csv)

  * [vehicles.parquet](Activities/03-Stu_Basics/Resources/vehicles.parquet)

</details>

<details>
  <summary><strong> ⭐ 2.3 Instructor Do: Review Activity (0:10)</strong></summary>
  
* **Files:**

  * [vehicles.csv](Activities/03-Stu_Basics/Resources/vehicles.csv)

  * [vehicles.parquet](Activities/03-Stu_Basics/Resources/vehicles.parquet)

  * [stu_basics.dbc](Activities/03-Stu_Basics/Solved/stu_basics.dbc)

* Begin by reviewing the goals of the activity at a high level: 

  * Create DataFrames and temporary views in Databricks in order to perform queries using PySpark and SQL interfaces. 

  * Create queries with aggregate operations. 

  * Create basic visualizations. 

* Then, live code the activity solution. The first task is to upload a file to Databricks: Drag `vehicles.csv` to the highlighted area, as shown in the following image.

  ![stu_basics01](Images/stu_basics01.png)

* Inform students that in the next screen, they don’t need to click either button (Create Table With UI or Create Table in Notebook). Instead, create a new notebook by clicking the Databricks tab to the left, and then clicking "New Notebook.” The following images show these steps: 

  ![stu_basics02](Images/stu_basics02.png)

  ![stu_basics03](Images/stu_basics03.png)

* At this point, you may wish to import the solutions notebook into Databricks, or continue to live code.

* Explain that we can locate the uploaded file in the Databricks storage system with `dbutils`, as shown in the following code and image: 

  ```python
  dbutils.fs.ls("/FileStore/tables")
  ```

  ![stu_basics03](Images/stu_basics04.png)

* Next, show how to create a DataFrame with the uploaded CSV.

  ```python
  file_location = '/FileStore/tables/vehicles.csv'
  df = spark.read.csv(file_location, inferSchema=True, header=True)
  display(df)
  ```

  ![stu_basics03](Images/stu_basics05.png)

  * The location of the file is given the variable `file_location`.

  * The file is previewed with `display`. 

*  Show how to obtain the number of vehicles in the database per type of transmission. You can also ask for a volunteer to share how they did this in the activity.

  ```python
  count_df = df.groupBy("transmission").count()
  count_df.show()
  ```

  ![stu_basics06](Images/stu_basics06.png)

  * The DataFrame is first grouped by the `transmission` column. 

  * The number of cars per group is obtained with `count`.

  * The results are displayed with `show`.

* Show the class how to preview the DataFrame and create a basic visualization simultaneously.

  ```python
  display(count_df)
  ```

  * The `display` method is used to display a preview, and the chart button is used to create a bar chart, as shown in the following images. 

  ![stu_basics07](Images/stu_basics07.png)

  ![stu_basics07](Images/stu_basics08.png)
  
* Compare the visualization created by `display` with one that might be created with Matplotlib, a tool that students have used previously.

  * Using Matplotlib requires more code and time, but it is more customizable.

  * `display` may be more useful when you need to create a visualization quickly, for example, during exploratory data analysis.

* Ask students what the advantages of a built-in visualization tool like `display` might be. Then share the following points. Feel free to modify them based on your experience with data visualization. 

  * A quick visualization tool is useful when exploring data; it enables the analyst to focus on exploring the data trends rather than coding a visualization. 

  * It can also quickly convey insights to collaborators or outside stakeholders.

* Next, explain the steps in creating the same query using SQL. We would use the following code: 

  ```python
  df.createOrReplaceTempView("vehicles")
  ```

  ```sql
  %sql
  SELECT *
  FROM vehicles
  LIMIT 5;

  %sql
  SELECT COUNT(*) AS vehicle_number
  FROM vehicles
  GROUP BY transmission;
  ```

  * First, we create a temporary table called `vehicles`, which can be used to query in SQL.

  * Then, we query the first 5 rows of the `vehicles` table in SQL to create a preview. We use the `%sql` magic command to indicate that the notebook cell code will be in SQL.

  * Finally, we use `GROUP BY` to group the results by the `transmission` column. `COUNT` is used to obtain the number of results.

  * In both the Python and SQL queries, we use the keywords `groupBy` and `GROUP BY` to perform aggregate functions.

* If there is time remaining, go over the bonus solution. Otherwise, instruct students to consult the solution on their own. Here’s the code: 

  ```python
  parquet_df = spark.read.parquet(parquet_file_link, inferSchema=True, header=True).select("year", "manufacturer", "transmission")

  df2 = parquet_df.groupBy("manufacturer").count()
  ```

  * The `read.parquet` method is used to read in a Parquet file. The `inferSchema` and `header` arguments, as before, are `True`.

  * Then, `select` is used to read only the specified columns. Remember, in a large dataset, the ability to selectively load columns can lead to big savings in time and computation costs.

  * The results are grouped by the `manufacturer` column and counted.

</details>


## 3. Joins

| Activity Time:       0:40 |  Elapsed Time:      1:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: Joins (0:15) </strong></summary>
  
* **Files (Use only if you and the students are unable to download the files from AWS S3.):**

  * [user_device.csv](Activities/04-Ins_Joins/Resources/user_device.csv)

  * [user_usage.csv](Activities/04-Ins_Joins/Resources/user_usage.csv)

In this section, you will demonstrate how to perform joins on a Databricks Spark notebook, using both Python and SQL interfaces. 

* **Note:** A complete code walkthrough is provided for convenience, but you do not have to go through all of it in detail. Students have already encountered PySpark joins, so if you’re pressed for time, you can focus on comparing queries in PySpark and SQL. 

* Inform the class that data is often spread out across multiple tables. The ability to query across multiple tables with joins is a key skill in data analytics.

  * For example, joins may be used to query student enrollment in a university's database.

  * In this demo, we’ll cover how to perform joins on wildlife data in both Python and SQL interfaces. 

* Load the DBC notebook into Databricks by using the following code, and then give an overview of the dataset.

  ```python
  user_device = 's3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/user_device.csv'
  user_usage = 's3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/user_usage.csv'
  
  user_device_df = spark.read.csv(user_device, inferSchema=True, header=True)
  display(user_device_df)
  
  user_usage_df = spark.read.csv(user_usage, inferSchema=True, header=True)
  display(user_usage_df)
  ```
  
  ![insjoins01](Images/insjoins01.png)
  
  ![insjoins02](Images/insjoins02.png)
  
  * The data files are stored on S3.

  * The dataset contains data on usage of a mobile app.

  * The previews of the DataFrames show that the two DataFrames have the `use_id` column in common.

* Make an explicit connection between performing joins in Databricks and the joins students performed previously.

  * Unlike previous activities, in this activity, we’ll perform PySpark and SQL queries in the same notebook. This will illustrate the flexibility of the Databricks platform. 

* Explain how to join the two DataFrames with PySpark. Instead of explaining directly, you might ask your students to identify and explain how the arguments of `join` are used in the following code.

  ```python
  merged = user_device_df.join(user_usage_df, on=['use_id'], how='inner')
  ```
  
  * In this code snippet, PySpark's `join` method is used.

  * The first argument, `user_usage_df` specifies the DataFrame joined to `user_device_df`.

  * The second argument, `on`, specifies the column on which the join is performed.

  * The third argument, `how`, specifies that this is an inner join.

* Explain that the `agg` method can be used to find out the average monthly data usage per platform, as shown in the following code.

  ```python
  merged.groupBy("platform").agg({"monthly_mb": "avg"}).show()
  ```
  
  * The results of the merged DataFrame are grouped by the `platform` column.

  * The `agg` method is used to calculate the average of the `monthly_mb` (monthly usage in megabytes) column, by platform.

  * The results show that the average monthly data usage is 4221 mb on Android, and 961 mb on iOS.

* Next, perform the same query in SQL by using the following code. Explain that temporary views are created that can be used to query the data with SQL.

  ```python
  user_device_df.createOrReplaceTempView('device')
  user_usage_df.createOrReplaceTempView('usage')
  ```
  
  * Here, the two temporary views are named `device` and `usage`.

* Go over the SQL query to find out the monthly data usage by platform. Here’s the code:

  ```sql
  %sql
  SELECT AVG(monthly_mb), platform
  FROM usage
  JOIN device
  ON usage.use_id = device.use_id
  GROUP BY platform;
  ```

* The two tables are joined on their `use_id` columns and grouped by `platform` to get the average `monthly_mb`.

* If time allows, ask students to reflect on some similarities and differences in the syntax of joins in Python and SQL. They might include the following:

  * Both use `on` to specify the columns on which the join will be performed.

  * Both use the "group by" keyword (`groupBy` and `GROUP BY`).

  * In SQL, `AVG(column_name)` is used to obtain the average value of a column. In the PySpark example, `agg` is used, and `avg` is used to specify the aggregate operation. 

* Tell students that they will perform a number of SQL joins in the group activity in the second half of today’s class.

* Share any experience you have with using joins in a professional setting. This will help underscore why it’s important to be comfortable using SQL joins. Examples might include the following: 

  * Being asked about joins during job interviews

  * Performing joins on the job, for example, querying with a join in order to analyze inventory turnover

* Answer any questions before moving on to the activity. 

</details>

<details>
  <summary><strong> ✏️ 3.2 Students Do: Joins in Databricks (0:15)</strong></summary>

* **Instructions:** [README.md](Activities/05-Stu_Joins/README.md)

* **Files:**

  * [species.csv](Activities/05-Stu_Joins/Resources/species.csv)

  * [surveys.csv](Activities/05-Stu_Joins/Resources/surveys.csv)

</details>

<details>
  <summary><strong> ⭐ 3.3 Instructor Do: Review Activity (0:10)</strong></summary>
  
* **File:** [joins.dbc](Activities/05-Stu_Joins/Solved/joins.dbc)

* State the high-level goal of the activity: to work with data across multiple tables and DataFrames in both PySpark and SQL interfaces.

* Open the notebook by importing the DBC file into your workspace. Optionally, feel free to live code.

  ![joins01](Images/joins01.png)

* Explain that the dataset files are CSV files stored on AWS S3:

  ```python
  s3link1 = 's3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/species.csv'
  s3link2 = 's3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/surveys.csv'
  ```
  
  * **Note:**If AWS S3 files are unavailable, you can upload the CSV files in the `Resources` folder.

* Explain that Spark DataFrames are created with Spark's Python interface, using the following code:

  ```
  df1 = spark.read.csv(s3link1, inferSchema=True, header=True)
  display(df1)
  ```

  ```
  df2 = spark.read.csv(s3link2, inferSchema=True, header=True)
  display(df2)
  ```

  * Both datasets are read into Spark and previewed with `display`.

  ![joins02](Images/joins02.png)

  ![joins03](Images/joins03.png)

* Explain that we can obtain the number of rows in each DataFrame with `count`, as shown in the following code:

  ```python
  df1.count()
  df2.count()
  ```

  * The first DataFrame, `df1`, which lists animal species, has 54 rows.

  * The second DataFrame, `df2`, has 35,549 records of animals.

* Show the code to obtain the number of birds in the dataset. Ask students to explain the methods and the arguments used in the following code.

  ```python
  joined_table = df1.join(df2, df1.species_id == df2.species_id, how='inner')
  results = joined_table.filter(df1.taxa == 'Bird').count()
  ```

  * PySpark's `join` method is used to join the two DataFrames.

  * The first argument of `join` is `df2`, or the DataFrame that is joined to `df1`.

  * The second argument specifies which columns the join is performed on. Here, it’s `species_id` from both DataFrames.

  * The third and final argument specifies how the join is performed. In this case, it’s an inner join.

  * The next line of code uses the `filter` method to filter for rows whose `taxa` is `Bird`. Then `count` is chained to obtain the number of rows. A total of 450 rows is returned.

* Explain the next query, which asks for the number of rodents that were recorded in 1977. Here’s the code: 

  ```python
  results2 = joined_table.filter(df1.taxa=='Rodent').filter(df2.year==1977).count()
  ```

  * Here, `joined_table` is the result of the join we performed previously.

  * The results are further filtered for `taxa` of `Rodent` and `year` of 1977.

  * Again, `count` is used to count the number of rows that meet the filter criteria. In the notebook, a total of 487 rows is returned. 

* Next, ask the class how to create temporary views that will be used to perform the same queries in SQL. Here’s the code: 

  ```python
  species = df1.createOrReplaceTempView('species')
  survey = df2.createOrReplaceTempView('survey')
  ```

  * The `createOrReplaceTempView` method is used to create temporary views. 

  * Temp views are held in memory of a single computer; they cannot be used across multiple computers.

  * SQL queries will be performed on these temp views, named `species` and `survey`.

* Next, review the following SQL queries:.

  ```sql
  %sql
  SELECT * 
  FROM species 
  LIMIT 5;
  ```

  ```sql
  %sql
  SELECT *
  FROM survey
  LIMIT 5;
  ```

  * The `%sql` magic command specifies that the code in each cell will be SQL.

  * The queries return the same previews seen previously with `display` using PySpark.

* Explain the code used to obtain the number of birds in the dataset using SQL:

  ```sql
  %sql
  SELECT COUNT(*)
  FROM species
  INNER JOIN survey
  ON species.species_id = survey.species_id
  WHERE species.taxa = 'Bird';
  ```

  * A `JOIN` is performed to join the `survey` and `species` tables on the `species_id` column from each table. In this case, an `INNER` join is the same as `JOIN`, but the code makes clear  that an inner join is being performed.

  * The number of rows is obtained by using `COUNT(*)`.

  * `WHERE` is used to filter the results whose `taxa` is `Bird`.

  * As before, a count of 450 rows is returned.

* Show the class how to create a SQL query to obtain the number of rodents recorded in 1977 by using the following code.

  ```sql
  %sql
  SELECT COUNT(*)
  FROM species
  INNER JOIN survey
  ON species.species_id = survey.species_id
  WHERE species.taxa = 'Rodent'
  AND survey.year = 1977;
  ```

  * Again, a join is performed with the two tables on the `species_id` column of each table.

  * The results are further filtered by using `WHERE` and `AND`.

  * As before, a count of 487 rows is returned.

* Conclude the activity review by asking for a volunteer to discuss the similarities between joins in the PySpark interface and the SQL interface. 

  * Both use the `join` keyword.

  * Both use the `on` keyword to specify the joined columns.

  * Both allow one to specify the join being performed, whether inner, outer, or Cartesian.

* Recap the goal of this activity: to work with data across multiple tables and DataFrames in both PySpark and SQL interfaces.
  
</details>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      2:25  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Reduce break time to 15 minutes.

- - -

## 4. Group Activity

| Activity Time:       1:35 |  Elapsed Time:       4:00 |
|---------------------------|---------------------------|

<details>
  <summary><strong> ✏️ 4.1 Students Do: Group Activity (1:00)</strong></summary>
  
* **⏰ 3-Hour Adjustment**: Reduce activity time to 50 minutes.

* **Instructions:** [README.md](Activities/06-Stu_Group_Project/README.md)

* **File:** [northwind.zip](Activities/06-Stu_Group_Project/Resources/northwind.zip)

* In this activity, students will work in groups of three or four to gather data insights from a fictional company's database. They will query the database in SQL. Many of the queries will require working across multiple tables. Based on their findings, they will create a brief report with recommendations.

* Explain the importance of communicating one's data insights to the audience. Feel free to share a personal experience you have had in communicating your data findings to others. For example: 

  * The importance of stating one's findings clearly and succinctly. If you include a real-life experience, you might discuss expectations from management and stakeholders regarding communication.

  * The role visualization can play in stating findings and supporting recommendations. A real-life experience might include how a data visualization helped to summarize findings and recommendations to management.

  * The importance of not only stating findings, but actionable insights.

* Assign students to groups of three or four.

* After about 10 to 15 minutes have elapsed, you and the TAs should check to make sure that students have loaded the datasets into Spark DataFrames and created temporary tables. Help groups that are struggling, and consider suggesting the use of a for loop to optimize the process. The code for a for loop is included in the solved notebook.

* At about the 45-minute mark, students should begin working on their presentations, even if they have not finished all the queries. Remind them that their primary goal is to create actionable insights. 

* If you find that many groups need more time, extend the activity time by 15 to 30 minutes. To accommodate this time extension, you can have fewer groups present and abbreviate the activity review at the end.

* By the end of the activity, each group should send you a link to their presentation slides.

* You and the TAs should provide guidance to groups that are struggling to come up with recommendations. Here are a few examples:

  ![groups01](Images/groups01.png)

  * Based on the number of orders by country, it appears that Mexico has placed few orders relative to the population size of that country. We recommend that Northwind consider a marketing campaign in Mexico to increase our presence.

  ![groups02](Images/groups02.png)

  * The top five countries in terms of the average freight weight are Austria, Ireland, USA, Germany, and Sweden. We recommend seeking cheaper shipping arrangements, or negotiating with our current shippers to obtain favorable rates.

  ![groups03](Images/groups03.png)

  * The top three employees in terms of orders placed account for approximately half of total orders. We recommend an incentive structure for employees responsible for placing the most orders.

</details>

<details>
  <summary><strong> 🎉 4.2 Everyone Do: Group Presentations (0:25)</summary></strong>
  
* **⏰ 3-Hour Adjustment**: Skip this activity.

In this activity, each group will present their findings and recommendations. If you extended the group project activity time, adjust for time by asking fewer groups to present.

* By the beginning of this activity, each group should have sent you links to their presentation slides.

* Depending on the number of students in your class, each group should be allotted two to three minutes per presentation.

* If time allows, encourage the class to give feedback to the presenting group. The feedback might include thoughts on the presenting group's data findings, data visualization, and recommendations.

* If time allows, invite the presenting groups to share any unusual findings, as well as thoughts about how they might use the skills used in this activity in a current or future job.

* After the presentations, congratulate the class on a job well done.

</details>

<details>
  <summary><strong> ⭐ 4.3 Instructor Do: Review Activity (0:10)</summary></strong>
  
* **File:** [group_project.dbc](Activities/06-Stu_Group_Project/Solved/group_project.dbc)

* Review that the goal of the group activity was to work together in order to integrate a number of skills: 

  * Use Databricks to load, analyze, and visualize data

  * Use SQL to create complex queries across many tables 

  * Build communication skills by conveying findings and recommendations. 

* Load the DBC notebook into Databricks.

* You likely will not have time to review every query, so focus on a few key ones. Examples are provided below. Instead of explaining the code each time, ask students to share their solutions.  

#### Create DataFrames and Temporary Views

  * A for loop can be used to create DataFrames and temporary views, as shown in the following code:

  ```python
  file_links = {
      "categories": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/categories.csv",
      "customers": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/customers.csv",
      "employee_territories": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/employee-territories.csv",
      "employees": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/employees.csv",
      "order_details": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/order-details.csv",
      "orders": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/orders.csv",
      "products": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/products.csv",
      "regions": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/regions.csv",
      "shippers": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/shippers.csv",
      "suppliers": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/suppliers.csv",
      "territories": "s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/territories.csv"
  }
  
  for table_name, table_path in file_links.items():
      df_name = table_name + "_df"
      df_name = spark.read.csv(table_path, inferSchema=True, header=True)
      df_name.createOrReplaceTempView(table_name)
  ```
  
    * The S3 links of the datasets are compiled into a dictionary.

    * The key of the dictionary is used to create a DataFrame, then a temporary view.

#### List All Countries to Which Orders Have Been Shipped 

* Query a list of all countries to which orders have been shipped by using the following code:

  ```sql
  SELECT DISTINCT ShipCountry
  FROM orders;
  ```
  
    * The keyword `DISTINCT` eliminates redundancies. Ask students to identify the equivalent of `DISTINCT` when using Pandas: `unique`.

#### Perform an Inner Join

* Another example is an inner join, in which data is retrieved from two or more tables that share a common column.

  ```sql
  SELECT ProductID, ProductName, CompanyName
  FROM products
  JOIN suppliers
  ON products.SupplierID = suppliers.SupplierID;
  ```
  
  * In this example, the ID, name, and company of each product is listed.

  * The two tables are joined by each `SupplierID` column.

  * Such joins are commonly asked in data job interviews.

#### Perform an Inner Join and an Aggregate Function

* In another example, two tables are joined, and then an aggregate operation is performed, as shown in the following code:

  ```sql
  SELECT CategoryName, COUNT(*) AS ProductCount
  FROM categories
  JOIN products
  ON categories.CategoryID = products.CategoryID
  GROUP BY CategoryName
  ORDER BY ProductCount DESC;
  ```

  * The two tables are joined on each `CategoryID` column.

  * The count of rows is obtained by grouping the results by `CategoryName`.

  * The results are sorted with the keywords `ORDER BY`.

#### Join Three Tables

* In a more challenging example, three tables are joined, as the following code shows:

  ```sql
  SELECT customers.CompanyName, SUM(Quantity * UnitPrice) AS TotalSpending
  FROM customers
  JOIN orders
  ON customers.CustomerID = orders.CustomerID
  JOIN order_details
  ON orders.OrderID = order_details.OrderID
  GROUP BY customers.CustomerID, customers.CompanyName
  ORDER BY TotalSpending DESC;
  ```
 
  * The first join is performed on `customers.CustomerID` and `orders.CustomerID`.

  * The second join is performed on `orders.OrderID` and `order_details.OrderID`.

  * The results are grouped by `CustomerID` and `CompanyName` in order to perform the `SUM` aggregate operation.

  * The results are then sorted in descending order.

* If there is time remaining, ask students to share custom queries they have created, as well as insights derived with the queries.

* End the class by congratulating students on finishing the course. Now only the final project remains.

</details>

# End Class

- - -

## References

Kaggle. (2017). UFO Sightings. [https://www.kaggle.com/hakeemtfrank/ufo-sightings-data-exploration](https://www.kaggle.com/hakeemtfrank/ufo-sightings-data-exploration)

Kaggle. (2020). Used Cars. [https://www.kaggle.com/austinreese/craigslist-carstrucks-data/activity](https://www.kaggle.com/austinreese/craigslist-carstrucks-data/activity)

Rakesh Singh. (2016). Northwind. [https://github.com/rakeshsingh/northwind-for-spark](https://github.com/rakeshsingh/northwind-for-spark)

Shane Lynn. (2017). Android User Device and User Usage (Pandas Merge Tutorial). [https://github.com/shanealynn/Pandas-Merge-Tutorial](https://github.com/shanealynn/Pandas-Merge-Tutorial)

Tracy Teal. (2015) Portal Mammals. [https://github.com/tracykteal/data](https://github.com/tracykteal/data)


- - -

### Copyright

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
 

  
