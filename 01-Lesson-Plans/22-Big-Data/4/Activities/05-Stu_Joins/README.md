# Joins in Databricks

In this activity, you will perform join in in Databricks.

## Instructions

The ability to query information that is spread out in multiple tables and DataFrames is a crucial skill in data analytics. Data analysts and data scientists often work with data in multiple tables or sources. You have been asked to perform joins to work across data sources for a nonprofit client to analyze wildlife data. In this activity, you will perform queries on datasets using both PySpark and SQL interfaces in Databricks.

You will work with two sources of data and join them. Here are the links to the files on AWS S3:

  * [s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/species.csv](s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/species.csv)

  * [s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/surveys.csv](s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/surveys.csv)

**Note**: If AWS is unavailable, you’ll need to manually upload the included CSV files to Databricks.

Complete the following tasks using the PySpark interface:

* Read in the CSV files using the provided links to create a Spark DataFrame for each file.

* Use `display` to preview the DataFrames.

* Count the number of rows in each DataFrame.

* Join the two DataFrames in order to answer the following question: How many birds are there in the dataset?

* Join the two DataFrames in order to answer the following question: How many rodents were recorded in 1978?

* In order to perform SQL queries, create a temporary view for each DataFrame.

Complete the following tasks using the SQL interface:

* Create a preview of the first five rows for each table.

* Join the two tables in order to answer the following question: How many birds are there in the dataset?

* Join the two tables in order to answer the following question: How many rodents were recorded in 1978?

## Hint 

* Both PySpark and SQL must specify the type of join being performed as well as the columns that are being joined.

---

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

