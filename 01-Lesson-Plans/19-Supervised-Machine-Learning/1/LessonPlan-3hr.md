# 19.1 Intro to Supervised Learning

## Overview

Today's lesson will introduce the students to the broad concepts of machine learning. It will also specifically introduce supervised learning, including regression and classification. The students will learn the model-fit-predict pattern of [scikit-learn](http://scikit-learn.org/stable/), and use it in the familiar context of linear regressions. They'll then learn logistic regression as an example of a classification algorithm.

## Class Objectives

By the end of today's class, the students will:

* Explain how machine learning algorithms are used in data analytics.

* Create training and testing sets from a specified data set.

* Implement linear and logistic regressions by using scikit-learn.

* Create confusion matrixes for classification outputs.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Be aware that the students might find the topic of machine learning intimidating. Today's class will reframe a familiar concept (linear regression) in the context of machine learning. The class will introduce the students to machine learning through the scikit-learn library. This library supplies a consistent interface for all their models, which the students should find encouraging.

* Note that the students will then use scikit-learn to create a logistic regression. This will show that they can use a small change to the linear regression to answer dissimilar questions in machine learning.

* Stress that creating a model, fitting the model to the data (that is, training the model), and then using the model to make predictions has become the standard pattern that many modern machine-learning libraries use. This common pattern eases experimenting with new algorithms and libraries when exploring machine learning solutions. The students will learn that no single right algorithm exists for any dataset or problem&mdash;and that experimentation and validation are often preferred. The students will learn to quantify and validate the performance of many models on a dataset to determine which might best suit their needs.

* Note that at the end of the class, the students will create a confusion matrix. This will act as just a teaser. The students will learn how to interpret confusion matrixes at the beginning of the next class.

* Please reference our [Student FAQ](https://github.com/coding-boot-camp/DataViz-Lesson-Plans/blob/master/05-Instructor-Resources/README.md#unit-21-machine-learning) for answers to questions that students of this program frequently ask. If you have recommendations for more questions, feel free to log an issue or create a pull request with the additions that you'd like

* Have your TAs refer to the [Time Tracker]() to stay on track.

* Please remember that the slideshows are for instructor use only. When distributing slides to students, first export them to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

| Activity Time:       1:05 |  Elapsed Time:      1:05  |
|---------------------------|---------------------------|

## 1. Intro to Machine Learning and scikit-learn

<details>
  <summary><strong> 📣 1.1 Instructor Do: Demystifying Machine Learning (Slides 1&ndash;18) (0:20)</strong></summary>

* Welcome the students to the class, and then introduce them to the topic for the next three weeks: machine learning. Also, open the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing) and use slide 2 to go over the class objectives.

* Moving forward on the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing), take the students through Slides 3&ndash;18. Make sure to cover the following points:

  * The definition of a machine learning algorithm is broad. One algorithm might include 2 internal parameters, and another might include 10,000, but the idea remains the same.

  * We can categorize machine learning into supervised learning, unsupervised learning, and reinforcement learning. (Note that the latter is outside the scope of this class.) Inform the students that this week will focus on supervised learning, that the following week will focus on unsupervised learning, and that the third week of machine learning will cover neural networks and deep learning&mdash;which are specific architectures for supervised learning.

  * We can further categorize supervised learning into classification and regression algorithms. Explain that we use classification algorithms for discrete labels and that we use regression algorithms for continuous labels.

  * Slides 12&ndash;15 discuss clustering as an example of unsupervised learning, which we'll cover in more depth next week.

  * Slides 16 and 17 cover the model-fit-predict pattern in scikit-learn. Let the students know that every model that we'll use will follow this pattern.

  * Ask the students for any questions before moving on to the next activity.

</details>

<details>
  <summary><strong> 📣 1.2 Instructor Do: Linear Regression (Slides 19&ndash;25) (0:20)</strong></summary>

* Note that you'll use the following Jupyter Notebook files during this activity:

  * [Ins_Univariate_Linear_Regression_Sklearn.ipynb](Activities/01-Ins_Linear_Regression/Solved/Ins_Univariate_Linear_Regression_Sklearn.ipynb)

  * [Ins_Multiple_Linear_Regression_Sklearn.ipynb](Activities/01-Ins_Linear_Regression/Solved/Ins_Multiple_Linear_Regression_Sklearn.ipynb)

* Start this activity by taking the students through [Slides 19](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit#slide=id.gc8a6761a46_0_17398)&ndash;25. Make sure to cover the following:

  * Explain that the best way to warm up to machine learning is to revisit an algorithm that we're already familiar with: linear regression.

  * Explain that linear regression is one of the fundamental algorithms in machine learning. Explain further that we often use linear regression as a building block for other machine learning algorithms, such as neural networks and deep learning.

  * Ask the students if they can define linear regression again:

    * Remind them that data science uses linear regression to model and predict the relationships between dependent and independent factors. **Simple linear regression** tries to predict a dependent variable from one independent variable (which is also referred to as a **feature** or a **factor** in machine learning). In contrast, **multiple linear regression** tries to predict a dependent variable from multiple independent variables.

    * Remind the students that linear regression calculates the coefficients for the slope and the intercept to create a linear equation:

      y = mx + b

      When dealing with multiple features, however, linear regression tries to determine a coefficient for each feature. That is, linear regression calculates a weighted value for each feature to determine an optimal linear equation.

  * Explain that linear regression is fast! If linear regression can solve a problem, that's often more efficient and economical than using a more-complex model, such as deep learning.

    Note that many data scientists start with a linear regression model. They then move to a more-complex model only if their data proves to be truly nonlinear.

* Instruct students to open Terminal or Git Bash and install sklearn using the following command: `conda install -c anaconda scikit-learn`

* Open [Ins_Univariate_Linear_Regression_Sklearn.ipynb](Activities/01-Ins_Linear_Regression/Solved/Ins_Univariate_Linear_Regression_Sklearn.ipynb) in Jupyter Notebook, and then take the students through the code. Make sure to cover the following:

  * Explain that we use an sklearn function named `make_regression` to generate test data.

  * Go through the `make_regression` parameter list, and explain that we define 20 samples (rows) with one feature (column) and some noise and bias.

  * Use Matplotlib to plot the data, and then show the linear trend. Explain that as X increases, y increases by a roughly constant rate, as the following image shows:

    ![A screenshot depicts the plot.](Images/trend.png)

  * Explain that linear data can also have a negative trend. In this case, as the independent value (x) increases, the dependent value (y) decreases.

  * Show the formula for univariate linear regression, and then explain that it just finds a line that best fits the data, as the following image shows:

    ![A diagram depicts the formula for univariate linear regression.](Images/linear_regression.jpg)

* Use the house price example to illustrate the process of getting new data (a new house on the market) and using linear regression to predict the home price, as the following image shows:

  ![A plot depicts the home price as a function of thousands of square feet.](Images/predict_prices_3.png)

* Briefly discuss nonlinear data by using the examples that the notebook supplies. The following image shows a plot of nonlinear data:

  ![A plot depicts nonlinear data.](Images/nonlinear.png)

* Explain the model-fit-predict pattern. Make sure to cover the following:

  * Explain that many popular machine-learning libraries follow the model-fit-predict pattern. Take the students through an example that using linear regression in sklearn. 

  * Explain that we'll import `LinearRegression` from sklearn and then create an instance of a model from it.

  * Explain that once we have a model instance, we need to fit the model to the data. This is the training process.

    Explain that the goal of the training is to find the slope and the intercept that best represent the data (that is, to fit a line to the data).

  * Show the slope and the intercept for the model by using `model.coef_` for the slope and `model.intercept_` for the y-axis intercept, as the following image shows:

    ![A screenshot depicts the output of running the functions.](Images/coeff.png)

  * Explain that we can now use the line to make predictions for new inputs. We now have a model that can take any value of X and calculate a value of y that follows the trend of the original data.

  * Note that the format for passing values to `model.predict()` is a list of lists, as the following code shows:

    ```python
    y_min_predicted = model.predict([[x_min]])
    y_max_predicted = model.predict([[x_max]])
    ```

  * Compare the first prediction to the original output value. These two values should be very close, because the model represents the trend of the original data.

  * Plot the original data vs. the predicted minimum and maximum values. This will visually show how well the model fits the original data. The following image shows the plot:

    ![A plot depicts that the original data closely follows the predicted values.](Images/line_fit.png)

* Open [Ins_Multiple_Linear_Regression_Sklearn.ipynb](Activities/01-Ins_Linear_Regression/Solved/Ins_Multiple_Linear_Regression_Sklearn.ipynb) in Jupyter Notebook, and then take the students through the code. Make sure to cover the following:

  * Explain that multiple linear regression is linear regression that uses multiple input features. Use the home price example as an analogy. Linear regression can predict the price of a home depending on one feature: square feet. With multiple linear regression, we can have multiple inputs, such as the number of bedrooms, number of bathrooms, and square feet. The following image shows the formulas:

    ![An image of text depicts the formula for multiple linear regression and specifically for the home price example.](Images/multiple_regression.png)

  * Explain that with multiple linear regression, it becomes hard to visualize the linear trends in the data. We need to rely on our regression model to correctly fit a line. Sklearn uses the Ordinary Least Squares method for fitting the line. Luckily for us, the API to the linear model is the same as before! We simply fit our data to our n-dimensional X array, as the following image shows:

      ![3dplot.png.](Images/3dplot.png)

* Explain residuals.

  Explain that with multidimensional data, we need a new way to visualize our model performance. In this example, we use a residual plot to check our prediction performance. The **residuals** are the differences between the true values of y and the predicted values of y. If we expect our residuals to be unbiased, they should equally distribute above and below the x-axis. The residual plot also gives us a visual sense of the variance of the residuals, as the following image shows:

    ![residuals.png.](Images/residuals.png)

</details>

<details>
  <summary><strong> ✏️ 1.3 Students Do: Linear Regression (Slides 26 and 27) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing) and use slides 26 and 27 to present this activity to the class.

* In this activity, the students calculate a univariate regression and a multivariate regression on California housing data.

* The students start with the following Jupyter Notebook file:

  [Stu_Linear_Regression.ipynb](Activities/02-Stu_Linear_Regression/Unsolved/Stu_Linear_Regression.ipynb)

* The following file has the student instructions:

  [README.md](Activities/02-Stu_Linear_Regression/README.md)

</details>

<details>
  <summary><strong> ⭐ 1.4 Review Activity (0:10) </strong></summary>

* Reassure the students that it's okay if this was difficult. The sklearn and TensorFlow libraries share a common API. So, gaining proficiency with the model-fit-predict steps will ease switching to other machine learning models later. They'll get plenty of practice with this today!

* Open [Stu_Linear_Regression.ipynb](Activities/02-Stu_Linear_Regression/Solved/Stu_Linear_Regression.ipynb) in Jupyter Notebook.

* During the review, highlight the following:

  * Show how to assign the data and target to the `X` and `y` variables as follows:

    * Explain that it's not necessary to use `X` and `y` for the names but that doing so provides a consistent set of variable names for our models.

    * Explain that we have to call `reshape(-1, 1)` to format the array for sklearn. This is necessary only for a one-dimensional array, as the following code shows:

      ```python
      med_inc = np.array([row[0] for row in X]).reshape(-1, 1)
      ```

    * Explain that we transform the `x_min` and `x_max` values to fit the list-of-lists format that `model.predict()` requires, as the following code shows:

      ```python
      x_min = np.array([[X.min()]])
      x_max = np.array([[X.max()]])
      print(f"Min X Value: {x_min}")
      print(f"Max X Value: {x_max}")
      ```

  * Plot `x` and `y` to show the linear trend in the data. Point out that the negative slope is ok in this case. The data still follows a linear trend, as the following image shows:

    ![A plot depicts a negative linear trend.](Images/negative_trend.png)

  * Show how to create an instance of a model and then fit it to the data.

  * Print the slope and intercept values, and remind the students that we  only define the equation for the line.

  * Plot the line and the original data to visually show how well the line fits the model.

  * Ask the students what it might indicate if the line didn't appear to match the data well. Explain that it might indicate that the model wasn't a good fit or that errors existed in the code.

  * Continue to the section about multiple linear regression. Show that our API is the same (that is, we still use the model-fit-predict interface with sklearn). Only the dimensionality of the data changes. Point out that we don't have to call `reshape` for our `X` data, because it already exists in the format that sklearn expects. We have to reshape only one-dimensional input vectors.

  * Show the residual plot for this model by using both training and testing data. This plot has outliers, which might indicate that our model won't perform as expected. It's hard to say without testing with more data points.

    ![A plot depicts the residuals for the training and testing data.](Images/residuals_beer_foam.png)

  * Point out that with multiple linear regression, it's harder to visually tell if the model offers a good fit. It's better to quantify our models, which the next activity covers.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Intro+to+Machine+Learning+and+scikit-learn&lessonpageTitle=Intro+to+Supervised+Learning&lessonpageNumber=19.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F1%2FLessonPlan-3hr.md)</sub>

## 2. Metrics to Quantify Machine Learning Models

| Activity Time:       0:35 |  Elapsed Time:      1:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: Quantifying Regression (Slides 29&ndash;34) (0:10) </strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Quantifying_Regression.ipynb](Activities/03-Ins_Quantifying_Regression/Solved/Ins_Quantifying_Regression.ipynb)

* Note that in this activity, you'll demonstrate two popular metrics to quantify machine learning models. You'll also cover the importance of validation by splitting the data into training and testing sets.

* Open the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing), and then open [Ins_Quantifying_Regression.ipynb](Activities/03-Ins_Quantifying_Regression/Solved/Ins_Quantifying_Regression.ipynb) in Jupyter Notebook.

* Demonstrate quantification:

  * Go over [Slide 30](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit#slide=id.gc8a6761a46_0_25899) while explaining that judging the strength of a model requires more than a visual confirmation. We must quantify the model. People commonly use two quantification scores: mean squared error (MSE) and R-squared (R2).

  * Mention that sklearn supplies functions to calculate these metrics.

  * Switch to [Ins_Quantifying_Regression.ipynb](Activities/03-Ins_Quantifying_Regression/Solved/Ins_Quantifying_Regression.ipynb), and then demonstrate how to use `sklearn.metrics` to calculate the MSE and R2 scores.

  * Point out that a good MSE score is close to zero, while a good R2 score is close to 1.

  * Explain that R2 is the default score for most of the sklearn models. We can calculate it directly from the model by using `model.score`.

* Demonstrate validation:

  * Switch back to the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing), and then go over Slides 31&ndash;33.

  * Point out that to understand how the model will perform on new data, we split the data into training and testing datasets. We fit (train) the model by using the training data. We score (validate) the model by using the testing data. This gives us an unbiased measure of the effectiveness of the model.

  * Point out that this training/testing splitting is so common that sklearn supplies a mechanism for doing so. Use [Ins_Quantifying_Regression.ipynb](Activities/03-Ins_Quantifying_Regression/Solved/Ins_Quantifying_Regression.ipynb) to demonstrate to the students how to use the `train_test_split` function to split the data into training and testing data.

</details>

<details>
  <summary><strong> ✏️ 2.2 Students Do: Brains! (Slides 35 and 36) (0:15) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing) and use slides 35 and 36 to present this activity to the class.

* In this activity, the students calculate a regression line to predict head size vs. brain weight.

* The students start with the following Jupyter Notebook file:

  [Stu_Brains.ipynb](Activities/04-Stu_Brains/Unsolved/Stu_Brains.ipynb)

* The following file has the student instructions:

  [README.md](Activities/04-Stu_Brains/README.md)

</details>

<details>
  <summary><strong> ⭐ 2.3 Review Activity (0:10) </strong></summary>

* Remind the students that they must reshape the data, because sklearn expects the data to come in a particular format.

* Ask the students why the MSE score is so large. Explain that it's because MSE doesn't have an upper bound. Optionally slack out the formula for [MSE](https://en.wikipedia.org/wiki/Mean_squared_error).

* Highlight the fact that the model should always perform better on the training dataset than on the testing dataset. This is because the model was trained on the training data. Intuitively, we expect the model to perform better on data that it's encountered before than on data that it hasn't.

* Note that `r2_score` and `model.score` produce the same R2 score.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Metrics+to+Quantify+Machine+Learning+Models&lessonpageTitle=Intro+to+Supervised+Learning&lessonpageNumber=19.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F1%2FLessonPlan-3hr.md)</sub>

- - -

## BREAK

| Activity Time:       0:15 |  Elapsed Time:      1:55  |
|---------------------------|---------------------------|

- - -

## 3. Logistic Regression

| Activity Time:       0:40 |  Elapsed Time:       2:35 |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: Logistic Regression (Slides 39&ndash;41) (0:10)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Logistic_Regression.ipynb](Activities/05-Ins_Logistic_Regression/Solved/Ins_Logistic_Regression.ipynb)

* Return to the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing), and then highlight the following points on Slides 40&ndash;41:

  * **Logistic regression** is a statistical method for predicting binary outcomes from data. With linear regression, our linear model might provide a numerical output, such as age. With logistic regression, we can then translate each numerical value for age into a probability from 0 to 1. We can then label this discrete output as "young" vs. "old." The following image illustrates the equations and the line plots for both types of regression:

    ![A diagram illustrates the differences between linear and logistic regression.](Images/logistic-regression.png)

  * We calculate the logistic regression by applying an activation function as the final step to our linear model. This transforms a numerical range to a bounded probability from 0 to 1.

  * We can use logistic regression to predict which category or class a new data point should belong to. For example, assume that we have two classes of data: a red class and a blue class. The data points in each class cluster near each other on a plot. Applying logistic regression gives us a line on the plot that separates the two classes. Now, we can predict which class a new data point should belong to&mdash;according to which side of the line it falls on. The following three images illustrate this process:

    ![A plot depicts two classes of data points and a new data point.](Images/logistic_1.png)
    ![The same plot depicts the process of applying logistic regression.](Images/logistic_2.png)
    ![The same plot depicts the logistic regression line, with the new data point now falling into one of the existing classes.](Images/logistic_3.png)

* Open [Ins_Logistic_Regression.ipynb](Activities/05-Ins_Logistic_Regression/Solved/Ins_Logistic_Regression.ipynb) in Jupyter Notebook, and then go through the scikit-learn implementation for logistic regression as follows:

  * Explain that we can use the `make_blobs` function to generate two groups (classes) of data. We can then apply logistic regression to determine if new data points belong to the purple group or the yellow group. The following image shows a plot of both classes of data that we generated:

    ![A plot depicts both sets of data points.](Images/make-blobs.png)

  * Point out that we create our model by using the `LogisticRegression` class from sklearn, as the following image shows:
    ![A code block depicts the code that we use.](Images/logistic-regression-model.png)

  * Point out that we then fit the model by using our training data, as the following image shows:

    ![A code block depicts the code that we use.](Images/train-logistic-model.png)

  * Point out that we then validate the model by using the test data, as the following image shows:

    ![A code block depicts the code that we use.](Images/test-logistic-model.png)

  * Point out that finally, we can make predictions. First, we generate a new data point, as the following image shows:

    ![A code block depicts the code that we use, and the same plot depicts the addition of the new data point.](Images/new-data.png)

    Then we predict the class of the new data point, as the following image shows:

    ![A code block depicts the code that we run and its output.](Images/predicted-class.png)

</details>

<details>
  <summary><strong> ✏️ 3.2 Students Do: Counterfeit Catcher (Slides 42 and 43) (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing) and use slides 42 and 43 to present this activity to the class.

* The students start with the following Jupyter Notebook file:

  [Counterfeit-Detection.ipynb](Activities/06-Stu_Counterfeit_Catcher/Unsolved/Counterfeit-Detection.ipynb)

* The following file has the student instructions:

  [README.md](Activities/06-Stu_Counterfeit_Catcher/README.md)

</details>

<details>
  <summary><strong> ⭐ 3.3 Review Activity (0:10)</strong></summary>

* Go through the [solution](Activities/06-Stu_Counterfeit_Catcher/Solved/Counterfeit-Detection.ipynb), and highlight the following:

  * Remind the students that we use logistic regression to predict categories or labels.

  * Explain that we performed logistic regression on our dataset to predict the `authentic (0)` or `counterfeit (1)` label.

  * Point out that when fitting the regression, if a warning appeared that the solver didn't converge, one of the provided suggestions was to scale the data. Let the students know that scaling the data is a form of preprocessing that we'll cover later in this lesson.

  * Show the prediction results for at least 10 test data samples. We get output labels of `0` or `1`, as the following image shows:

    ![A screenshot depicts the actual and the predicted labels for the first 10 test data samples.](Images/counterfeit-predictions.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Logistic+Regression&lessonpageTitle=Intro+to+Supervised+Learning&lessonpageNumber=19.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F1%2FLessonPlan-3hr.md)</sub>

## 4. Confusion Matrixes

| Activity Time:       0:25 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Confusion Matrix (Slides 45&ndash;48) (0:10)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Confusion_Matrix.ipynb](Activities/07-Ins_Confusion-Matrixes/Solved/Ins_Confusion_Matrix.ipynb)

* Open the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing), and then take the students through Slides 45&ndash;47, introducing them to confusion matrixes. Reassure the students that this is just a brief preview and that we'll revisit confusion matrixes in the next class. Make sure to cover the following points:

  * Explain that while accuracy is helpful, it's not the only measure that we want to consider when evaluating the performance of a classification model.

  * Explain that confusion matrixes help us get a bigger picture by showing the number of true positives, true negatives, false positives, and false negatives from a model's classification of the testing data.

  * Show the students how to calculate accuracy from a confusion matrix. Point out that we can derive many other measures from the confusion matrix and that we'll discuss them in the next class.

* Open [Ins_Confusion_Matrix.ipynb](Activities/07-Ins_Confusion-Matrixes/Solved/Ins_Confusion_Matrix.ipynb) in Jupyter Notebook. Then go through each line of code, showing the students how to create a confusion matrix from a model's predictions based on testing data.

</details>

<details>
  <summary><strong> ✏️ 4.2 Students Do: Create a Confusion Matrix (Slides 49 and 50) (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1NPscwHwQv9bYJeyIMybC-beqxc0Q5bDRaqeUyZKO2SY/edit?usp=sharing) and use slides 49 and 50 to present this activity to the class. 

* The students start with the following Jupyter Notebook file:

  [Confusion Matrix](Activities/08-Stu_Confusion-Matrixes/Unsolved/Stu_Confusion_Matrix.ipynb)

* The following file has the student instructions:

  [README.md](Activities/08-Stu_Confusion-Matrixes/README.md)

</details>

<details>
  <summary><strong> ⭐ 4.3 Review Activity (0:05)</strong></summary>

* Go through the [solution](Activities/08-Stu_Confusion-Matrixes/Solved/Stu_Confusion_Matrix.ipynb), and highlight the following:

   No agreed-on convention exists for confusion matrixes. Some people put the predicted values in columns, and others use rows. Some people put the true positives in the top-left cell (that is, the cell in the first row and first column). Others&mdash;such as scikit-learn&mdash;use the bottom-right cell (that is, the cell in the last row and last column). So, we need to take care.

* Let the students know that we'll be using the confusion matrix more in the next class. Invite them to think about other measures that we might be able to calculate.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Confusion+Matrixes&lessonpageTitle=Intro+to+Supervised+Learning&lessonpageNumber=19.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F1%2FLessonPlan-3hr.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
