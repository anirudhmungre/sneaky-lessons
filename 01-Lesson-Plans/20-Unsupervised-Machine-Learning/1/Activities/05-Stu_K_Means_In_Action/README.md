# Clustering Customers for E-Commerce

Now that you have prepared the data, it's time to start looking for patterns in the customer data. The CFO of your company has asked you to group customers based on their spending habits. You decide to use k-means for this task.

## Instructions

* Accomplish the following tasks and use k-means to cluster the customer data.

  * Load the dataset (which you previously cleaned) into a data frame.
  * Find the best number(s) of clusters using the elbow curve.
  * Create a two-dimensional scatter plot to analyze the clusters using `x="Annual Income"` and `y="Spending Score (1-100)"`.

## Bonus

* Create a function called `get_clusters(k, data)` that finds the `k` clusters using k-means on `data`. 

  * `data` represents a data frame.
  * The function should use k-means to identify clusters in the dataset.
  * The function should add a new column containing the cluster value of each sample (row).
  * The function should return a copy of the new data frame.

* Create a function called `show_clusters(df)` that will create a scatter plot of a data frame's `Annual Income` and `Spending Score (1-100)` columns, and color by the cluster.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
