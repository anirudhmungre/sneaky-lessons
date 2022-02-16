# Databricks Basics

In this activity, you will perform basic navigation and data analysis tasks in Databricks.

## Instructions

In order to get started as a data analyst, your next task at XYZ Corporation is to familiarize yourself with the Databricks interface. Your manager has asked you to learn how to upload datasets, as well as perform basic file navigation and data analysis using Databricks. In this activity, you will create a Databricks notebook and then perform basic data analysis and visualization using Python and SQL interfaces.

* Complete the following tasks:

  * Upload `vehicles.csv` to Databricks.

  * Create a blank Databricks notebook.

  * Use `dbutils` to note the location of the CSV.

  * Create a Spark DataFrame of the dataset and preview the DataFrame.

  * Create a PySpark query to obtain the number of vehicles for sale by type of transmission.

  * Create a bar chart of the results.

  * Perform the same query and visualization using SQL. You will need to create a temporary table in order to do this.

## Bonus

The same dataset is available in Parquet format. It’s stored at `s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/vehicles.parquet`. Using this file, complete the following tasks.

* Load only the following columns of the dataset into a Spark DataFrame: year, manufacturer, and transmission.

* Using PySpark, obtain the number of vehicles per sale by manufacturer.

---

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
