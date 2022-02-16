# Group Activity

In this activity, you will work in groups of three or four to perform data analysis using a database of a fictional company called Northwind. You’ll put together all the skills you learned today and in this course, such as the following: 

* Load multiple data sources 

* Analyze data 

* Visualize data 

* Present data findings 

Use SQL (not PySpark) to perform all queries. 

**Files**

The data files you need for this activity are provided at the following links. If S3 is unavailable, the files are available in the Resources folder.

  ```python
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/categories.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/customers.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/employee-territories.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/employees.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/order-details.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/orders.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/products.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/regions.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/shippers.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/suppliers.csv
  s3://2u-data-curriculum-team/dataviz-classroom/v1.1/22-big-data/territories.csv
  ```
## Instructions 

Complete the following tasks: 

* For each data file, create a Spark DataFrame and a temporary view. **Hint**: You may find it helpful to create a for loop.

* Run `spark.catalog.listTables()` to verify that the tables have been created.

* To establish relationships between tables, you can print the schema of each DataFrame, or you may search online for an ERD of the Northwind database.

Your team has been tasked by the management of Northwind with the following requests. Where appropriate, create a chart to visualize the results. Remember to use SQL to query the database.

* Create a list of all countries to which orders have been shipped.

  * How many orders have been placed in total?  

  * How many orders have been shipped to each country?

* For each product, list its product ID, product name, and the company name.

  * Which 5 countries have the heaviest shipments, on average?

  * Which 10 companies have placed the most orders? List the contact name of each company.

* Sort the customers by total amount spent on orders in descending order.

* Sort customers with a total spending greater than 20,000 in descending order.

* Sort the employees by the number of orders they sold in descending order.

  * How many employees account for about half of the orders? (You do not have to use SQL to answer this question. A rough estimate is sufficient.)

* List customers who have never placed an order.

* List the products with the highest level of discount in descending order.

**Note**: You don’t  have to limit yourself to these queries. Feel free to create your own queries to create data insights.

* Use the results of your data analysis to create a brief report (about 3 to 5 slides) for management. Your report should include the following:

  * Three actionable recommendations. Support each recommendation with a data finding.

  * Visualizations where appropriate.

* Send the link of your Google Slides presentation to your instructor.

**Note**: Collaboration is key for this activity. It’s unlikely that any one person will be able to complete all of the tasks in the allotted time. Work with your team! 

---

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
