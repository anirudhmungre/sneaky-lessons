# Understanding Customers

An online store wishes to increase revenue by offering custom offers to customers. Before you start looking for a machine learning algorithm, you ask the company for historical data about customer purchases. After checking the dataset, you realized that there is some data preprocessing work to be done.

## Instructions

You are given a dataset that contains historical data from purchases at an online store made by 200 customers. In this activity, you will put your data-preprocessing skills to work. 

* Use the starter Jupyter Notebook and perform the following tasks:

  * Load the data into the Pandas data frame and preview it.
  * List the data frame's data types to ensure that they're aligned to the type of data stored in each column. Are there any columns whose data type needs to be changed? If so, make the corresponding adjustments.

    * List the data types in the DataFrame to ensure that they align to the types of data that the columns contain. If you need to change the data type for any columns, do so.
    * Remove all rows with `null` values, if any.
    * Another best practice is to drop any column that would be unnecessary. Are there any unnecessary columns that need to be dropped? If so, make the corresponding adjustments.
    * Drop any unnecessary columns.

  * Remove duplicate entries, if any.

* To use unsupervised learning algorithms, all the features should be numeric and on similar scales. Perform the following data transformations:

* To scale the data, complete the following steps:

    * The `Previous Shopper` column contains categorical data; anytime you have categorical variables, you should transform them to a numerical value. In this case, transforming `Yes` to `1` and `No` to `0` is a feasible solution.
    * Scale the following features with Scikit-learn's `StandardScaler`: `Age`, `Annual Income`, `Spending Score (1-100)`.

* Create a new DataFrame for the scaled data. Add the `Previous Shopper` column to it. Rename the `Spending Score (1-100)` column to `Spending Score`, since standardizing it will change the score.

* Once you are done with data preprocessing, save the cleaned data frame in a new `CSV` file.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
