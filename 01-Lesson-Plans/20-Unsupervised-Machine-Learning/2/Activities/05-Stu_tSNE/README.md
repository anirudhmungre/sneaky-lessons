# Grape Clusters

In this activity, you will visually analyzing the wine dataset using t-SNE.

## Instructions

* You will be working with the wine dataset, in which each sample belongs to one of three varieties of wines. Visually analyze the data using t-SNE. Follow these guidelines:

  * Standardize the data beforehand.
  * You may have to tweak the `learning_rate` parameter of your t-SNE model. The normal range is 10 to 1,000. If you wish to adjust other parameters, consult the [documentation](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html).
  * After reducing dimensions with t-SNE, create a scatter plot of the transformed data. How many clusters do you detect?
  * In this exercise, the target labels **are** available, as `labels = wine.target`. Use these labels to color your scatter plot. Does the result confirm or reject your findings?

## Bonus

* Sometimes dimensions are reduced with PCA before they are further reduced with t-SNE.

* With the supplied `breast_cancer.csv`, try performing PCA, then run t-SNE with the results. When running PCA, try setting `n_components` to 0.95, which selects the number of components that preserve 95% of the explained variance.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
