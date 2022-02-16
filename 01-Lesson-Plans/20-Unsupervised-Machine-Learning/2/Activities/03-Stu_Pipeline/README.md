# Credit Modeling

In this activity, you will create a classification model with logistic regression using a dataset collected in the1970’s in Germany. Tune the model hyperparameters with grid search to evaluate the performance of the model, and the best parameters. 

## Instructions

* The dataset was collected in the 1970s in Germany. Each row contains information on a loan, such as the amount of the loan, as well as whether the loan was repaid. See [here](https://archive.ics.uci.edu/ml/datasets/South+German+Credit+%28UPDATE%29) for more information.

* Create a classification model with logistic regression, completing the following tasks:

  * Read in the dataset and check to see if there are rows with null values.
  * Remove all rows with null values.
  * Split the dataset into data (X) and labels (y), then split them further into training and testing datasets. The `kredit` column should be the labels.
  * Create a pipeline with the following estimators: standardization of data, dimensionality reduction, logistic regression.
  * Tune the model hyperparameters with a grid search. Evaluate the performance of the model and the best parameters.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
