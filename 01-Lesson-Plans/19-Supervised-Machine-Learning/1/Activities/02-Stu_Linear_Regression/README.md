# California Housing

In this activity, you'll calculate two regression lines by using a dataset of California house prices. For the first regression line, you'll explore the relationship between median income levels and median home values. For the second regression line, you'll use all the available variables to predict the median home value.

## Instructions

* For univariate regression:

    * Load the housing data, and then separate the median income feature into one variable: `med_inc`.
    * Create a scatter plot of `med_inc` vs. `y` (median home values) to visually find out if any linear trend exists.
    * Use the linear regression model of Sklearn to fit the model to the data.
    * Print the weight coefficients and the y-axis intercept for the trained model.
    * Calculate the `y_min` and `y_max` values by using `model.predict()`.
    * Plot the model fit line by using `[x_min[0], x_max[0]], [y_min[0], y_max[0]]`.

* For multivariate regression:

    * Use the linear regression model of Sklearn to perform multiple linear regression by using all eight features for `X` and median home value for `y`.
    * Compute the R2 score for the training and the testing data separately.
    * Plot the residuals for the training and the testing data.

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
