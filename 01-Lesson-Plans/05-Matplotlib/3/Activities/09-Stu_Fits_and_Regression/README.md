# Fits and Regression

This activity is an opportunity to use SciPy to fit data and Matplotlib to display the fit.

## Instructions

* Open the [crime.ipynb](Unsolved/crime.ipynb) file, and execute the starter code. This starter code will import the dependencies you will need as well as load the FBI CIUS (Crime in the United States) dataset.

* Generate a scatter plot with Matplotlib using the year as the independent (*x*) variable and the violent crime rate as the dependent (*y*) variable.

* Use `stats.linregress` to perform a linear regression with the year as the independent variable (*x*) and the violent crime rate as the dependent variable (*y*).

* Use the information returned by `stats.linregress` to create the equation of a line from the model.

* Calculate the predicted violent crime rate of the linear model using the year as the *x* values.

* Plot the linear model of year versus violent crime rate on top of your scatter plot.

  * Your scatter plot and line plot share the same axis.

  * To overlay plots in a notebook, the plots must be in the same code block.

* Repeat the process of generating a scatter plot, calculating the linear regression model, and plotting the regression line over the scatter plot for the following pairs of variables:

  * Year versus murder rate.

  * Year versus aggravated assaults.

## Bonus

* Use `pyplot.subplots` from Matplotlib to create a new figure that displays all three pairs of variables on the same plot. For each pair of variables, there should be a scatter plot and a regression line.

  * All three plots share the same x-axis.

* Use the regression lines you created to predict what the violent crime rate, murder rate, and assault rate will be in 2019.

## Hint

* Review the documentation for [stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html).

* Recall that `stats.linregress` returns a slope, called *m*, and a *y* intercept, called *b*. These let you define a line for each fit simply by writing `y-values = m * x-values + b` for each linear regression you perform.

## References

Federal Bureau of Investigation. (2020). Crime in the United States by Volume and Rate per 100,000 Inhabitants, 1994-2013. [https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls](https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls)

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
