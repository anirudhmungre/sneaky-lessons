# 19.3 Ensemble Methods and Regressions

## Overview

Today's lesson will add ensemble methods to our collection of classifiers and then move to regression models. The students will learn how to use regularization in regression models. They'll also learn how to automatically select features by using the Random Forests and least absolute shrinkage and selection operator (LASSO) models. Finally, the lesson will introduce them to the regression equivalents of classification models.

## Class Objectives

By the end of today's class, the students will be able to:

* Calculate and apply bagging and boosting methods to create and use ensemble algorithms.

* Apply regularization parameters for regressions and select the appropriate parameters for a specified problem.

* Use Random Forests and LASSO regressions to aid the feature selection process.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Note that today's class dives more deeply into some of the more conceptual aspects of machine learning. These include the aggregation of models and automated feature selection. It might prove helpful to remind the students that everything that today's class covers still uses the model-fit-predict pattern.

* Realize that today's material should be exciting! The class introduces new algorithms and new ways to combine previously used algorithms. The end of the class introduces a new context for previously learned models*mdash;expanding the students' tool sets.

* Have your TAs refer to the Time Tracker to stay on track.

* Please remember that the slideshows are for instructor use only. When distributing slides to students, first export them to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

## 1. Decision Trees and Ensemble Methods

| Activity Time:       0:45 |  Elapsed Time:       0:45 |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 1.1 Instructor Do: Decision Trees (Slides 1&ndash;5) (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing) and use slide 2 to go over the class objectives and slides 3&ndash;5to introduce this lesson to the class.

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Trees.ipynb](Activities/01-Ins_DecisionTrees/Solved/Ins_Decision_Trees.ipynb)

* Note that you might use the following Jupyter Notebook file during this activity:

  [Ins_Decision_Trees_Graphviz.ipynb](Extra_Content/Ins_Decision_Trees_Graphviz.ipynb)

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing). Go through Slides 2&ndash;4, and highlight the following points:

  * A decision tree encodes a series of true-or-false questions that we can  interpret as if-else statements.

  * A decision tree has a depth. This is the number of if-else statements that are encountered before a decision is made.

  * Decision trees can become deep and complex, depending on the number of questions that have to be answered. Deep and complex trees tend to overfit to the data and don't generalize well, as the following image shows:

    ![A diagram of a deep and complex tree.](Images/tree.png)

* Open [Ins_Trees.ipynb](Activities/01-Ins_DecisionTrees/Solved/Ins_Decision_Trees.ipynb), and then go through the scikit-learn implementation of a decision tree.

* If you can successfully install `graphviz` and `pydotplus`, open [Ins_Decision_Trees_Graphviz.ipynb](Extra_Content/Ins_Decision_Trees_Graphviz.ipynb), which is the Jupyter notebook about decision trees in the `Extra_Content` folder.

* If you can't successfully install `graphviz` and `pydotplus`, open the following `iris.png` image:

  ![The iris.png image.](Images/iris.png)

* Whether you use the Jupyter notebook or the PNG file, show how each node in the tree tries to split the data based on a criterion of the input data. The node at the top (or beginning) of the tree is the decision point that makes the biggest split. As the depth in the tree increases, the subnodes make more-granular decisions.

* Point out that the training phase of the decision tree algorithm learns which features best split the data.

</details>

<details>
  <summary><strong> 📣 1.2 Instructor Do: Ensemble Methods (Slides 6&ndash;12) (0:15)</strong></summary>

* Note that you'll use the following Jupyter Notebook files during this activity:

  [Ins_Trees.ipynb](Activities/01-Ins_DecisionTrees/Solved/Ins_Decision_Trees.ipynb)

  [Ensemble Methods.ipynb](Activities/02-Ins_Ensemble-Methods/Solved/Ensemble%20Methods.ipynb)

* Go back to the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing), and go through Slides 6&ndash;12. Be sure to make two points: decision trees can quickly become overly complicated, and anomalies in the training dataset can trick these trees. A technique that makes decision trees more useful is aggregating.

* Explain that instead of trying to make one complicated algorithm, **aggregating** makes lots of simple algorithms and then takes the consensus. (The simple algorithms aren't very accurate on their own. But, they can be very accurate when taken together.)

* Open [Ensemble Methods.ipynb](Activities/02-Ins_Ensemble-Methods/Solved/Ensemble%20Methods.ipynb). Let the students know that we'll be using an artificial classification dataset from scikit-learn. Create the decision tree model, and then point out two results. First, the testing set produces a decent score of 0.864. Second, even so, the score of 1.0 on the training set tells us that the tree is overfitting and that we maximized how well the decision tree can do.

* Introduce bagging by stepping through the code in the next cell. Point out that the `resample` line is where the bootstrapping happens, as the following code shows:

  ```python
  clfs = []
  scores = []
  for i in range(50):
  
      # Sample the data for each new tree
      X_train_scaled_bootstrap, y_train_bootstrap = resample(X_train_scaled, y_train, random_state=i)
    
      # Create a decision tree and append it to our list of classifiers
      clf = DecisionTreeClassifier(random_state=i+200).fit(X_train_scaled_bootstrap, y_train_bootstrap)
      clfs.append(clf)
    
      # Take the median score of all the created classifiers
      y_preds = [clf.predict(X_test_scaled) for clf in clfs]
      y_pred = pd.DataFrame(y_preds).median().round()
      score = score = accuracy_score(y_test, y_pred)
      scores.append(score)

  plt.plot(scores)
  plt.show()
  print(f'score: {score}'
  ```

* Show that the plot of scores quickly increases as we add multiple trees and that the accuracy score goes up from 0.864 to 0.904. This aggregation technique is known as **bootstrap aggregation**, or **bagging** Tell the students that "bagged decision trees" are known as **Random Forests**. Furthermore, we can implement them in scikit-learn by using `RandomForestClassifier()`.

* Remind the students that decision trees always try to make the best split. That's why we needed the **bootstrap**, or sampling, step to get different trees. We could go even further and let the trees randomly split. Point out that it might seem counterintuitive that aggregating weak models can lead to a stronger overall result. But by aggregating the models, the noise tends to cancel out, and the signal tends to amplify.

* Show that this plot of scores also quickly increases and that we improved our model to 0.924. Tell the students that this algorithm is known as **Extremely Random Trees** and that we can implement it in scikit-learn by using `ExtraTreesClassifier()`. Point out that the trees in both Random Forests and Extremely Random Trees don't have any information about each other&mdash;they operate independently.

* Explain that **Boosting** is another aggregation technique that adds weights to the observations that the previous learners classified poorly. In this way, each new learner depends on the one before it. One kind of boosting is known as **Adaptive Boosting**, which the sample code demonstrates. Let the students know that this algorithm is a bit more complicated than the previous two, so we're providing the code as a reference. It's not necessary to go over the code in depth in the class.

* Note that scikit-learn makes Adaptive Boosting available with `AdaBoostClassifier()`. Point out that in this case, **AdaBoost** did about as well as Random Forests.

* Answer any questions before moving to the next activity.

</details>

<details>
  <summary><strong> ✏️ 1.3 Students Do: Bag and Boost (Slides 13&ndash;14) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing) and use slides 13&ndash;14 to present this activity to the class.

* In this activity, the students continue to use the Pima Diabetes dataset and test three aggregated learning models.

* The students start with the following Jupyter Notebook file:

  [Bag_and_Boost.ipynb](Activities/03-Stu_Bag-and-Boost/Unsolved/Bag_and_Boost.ipynb)

* The following file has the student instructions:

  [README.md](Activities/03-Stu_Bag-and-Boost/README.md)

## Instructions

1. Import a Random Forests classifier, and then fit the model to the data.

2. Import an Extremely Random Trees classifier, and then fit the model to the data.

3. Import an Adaptive Boosting classifier, and then fit the model to the data.

4. Calculate the classification report for each model. Also, calculate the score for both the training and the testing set. Compare the performance of the three models.

## Bonus

1. Refactor to reduce repetitive code. Create a function that takes in a model and a dataset and prints a classification report to compare different models.

2. Choose one of the models, and then read the scikit-learn documentation. Use your newly created function to try different parameters. Can you improve the model?

</details>

<details>
  <summary><strong> ⭐ 1.4 Review Activity (0:05)</strong></summary>

* Open [Bag_and_Boost.ipynb](Activities/03-Stu_Bag-and-Boost/Solved/Bag_and_Boost.ipynb). Take the students through the solution, and highlight the following point:

  Each model does reasonably well. But, both the Random Forests and Extremely Random Trees models get perfect scores on the training data. This means that they overfit to the data in the training model. Because the AdaBoost model has a training score that's similar to its testing score, the bonus activity explores AdaBoost models with different parameters.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Decision+Trees+and+Ensemble+Methods&lessonpageTitle=Ensemble+Methods+and+Regressions&lessonpageNumber=19.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F3%2FLessonPlan-3hr.md)</sub>

## 2. Feature Selection with Random Forests

| Activity Time:       0:35 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: Feature Selection with Random Forests (Slides 16&ndash;18) (0:10)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [RandomForest-Feature-Selection.ipynb](Activities/04-Ins_Forest-Features/Solved/RandomForest-Feature-Selection.ipynb)

* Go back to the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing), and go through Slides 16&ndash;18. Introduce the concept of feature selection, and then explain how we can use Random Forests for feature selection.

* Open [RandomForest-Feature-Selection.ipynb](Activities/04-Ins_Forest-Features/Solved/RandomForest-Feature-Selection.ipynb). Point out that we create a classification with 50 features&mdash;however, only 5 of them are informative, as the following code shows:

  ```python
  # Create data
  X, y = make_classification(random_state=1, n_features=50, n_informative=5, n_redundant=0)
  ```

* Fit the `RandomForestClassifier()` to the data. After the model has been fit, show that `clf.feature_importances_` has a score for the importance of each feature according to the model. To get a sense of the numbers, we can use a bar chart to visualize their relative magnitudes.

* Demonstrate that we can use `SelectFromModel()` and `get_support()` to automatically select features from a Random Forests model.

* Point out that we can use feature selection for any model and that we'll demonstrate this with a logistic regression. When fit to the original data, the logistic regression gets a training score of 1.0 (that is, it overfits). And, it gets a testing score of only 0.68. After using the features that Random Forests selects, the score improves to 0.84.

* Answer any questions before moving to the next activity.

</details>

<details>
  <summary><strong> ✏️ 2.2 Students Do: Finding the Features from the Trees (Slides 19 and 20) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing) and use slides 19 and 20 to introduce this activity to the class.

* In this activity, the students find the important features for predicting arrhythmia in heartbeats.

* The students start with the following Jupyter Notebook file:

  [RandomForest-Feature-Selection.ipynb](Activities/05-Stu_Forest-Feature-Selection/Unsolved/RandomForest-Feature-Selection.ipynb)

* The following file has the student instructions:

  [README.md](Activities/05-Stu_Forest-Feature-Selection/README.md)

</details>

<details>
  <summary><strong> ⭐ 2.3 Review Activity (0:10) </strong></summary>

* Open [RandomForest-Feature-Selection.ipynb](Activities/05-Stu_Forest-Feature-Selection/Solved/RandomForest-Feature-Selection.ipynb), and then go through the solution with the students. Answer any questions that the students have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Feature+Selection+with+Random+Forests&lessonpageTitle=Ensemble+Methods+and+Regressions&lessonpageNumber=19.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F3%2FLessonPlan-3hr.md)</sub>

- - -

## BREAK

| Activity Time:       0:15 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

- - -

## 3. Regressions

| Activity Time:       0:35 |  Elapsed Time:      2:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: Regressions (Slides 23 and 24) (0:10)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [RegularizedRegressions.ipynb](Activities/06-Ins_Regressions_and_Regularization/Solved/RegularizedRegressions.ipynb)

* Go back to the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing), and then go through slides 23 and 24. Let the students know that for the remainder of the class, we'll focus on regressions.

* Remind the students that they've already explored a regression before: the linear regression.

* Point out that the first regressions we'll start with closely relate to linear regressions, but they have an extra factor added to the model.

* Open [RegularizedRegressions.ipynb](Activities/06-Ins_Regressions_and_Regularization/Solved/RegularizedRegressions.ipynb).

* Note that in the created dataset, the first three features highly correlate with each other (and with the target variable). The remaining three features are just noise. Therefore, a unique solution doesn't exist even for the theoretically perfect model.

* Step through each of the three new models, explaining how their regularization factors affect the model, as follows:

  * In LASSO regression, the coefficients of unimportant features can drop all the way to zero.

  * In Ridge regression, the coefficients won't go to zero, but the collinear features have roughly the same value.

  * ElasticNet regression combines both regularization factors, giving us the best of both worlds.

* Answer any questions before moving on to the next activity.

</details>

<details>
  <summary><strong> ✏️ 3.2 Students Do: Regularized Regressions (Slides 25 and 26) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing) and use slides 25 and 26 to present this activity to the class.

* In this activity, the students predict the prices of constructed houses in Tehran based on a wide array of features.

* The students start with the following Jupyter Notebook file:

  [Regularized_Regressions.ipynb](Activities/07-Stu_Regularization/Unsolved/Regularized_Regressions.ipynb)

* The following file has the student instructions:

  [README.md](Activities/07-Stu_Regularization/README.md)

</details>

<details>
  <summary><strong> ⭐ 3.3 Review Activity (0:10) </strong></summary>

* Open [Regularized_Regressions.ipynb](Activities/07-Stu_Regularization/Solved/Regularized_Regressions.ipynb), and then go through the solution with the students. Answer any questions that the students have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Regressions&lessonpageTitle=Ensemble+Methods+and+Regressions&lessonpageNumber=19.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F3%2FLessonPlan-3hr.md)</sub>

## 4. Feature Selection with LASSO

| Activity Time:       0:35 |  Elapsed Time:      2:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 4.1 Everyone Do: Feature Selection with LASSO (Slides 28 and 29) (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing) and use slides 28 to present this lesson and slide 29 to start live code along with the class.

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Lasso_FeatureSelection.ipynb](Activities/08-Evr_Lasso-Features/Solved/Lasso_FeatureSelection.ipynb)

* Let the students know that LASSO gives us another feature selection tool. If a coefficient goes to zero in the LASSO model, we can safely discard it from the model.

* Open [Lasso_FeatureSelection.ipynb](Activities/08-Evr_Lasso-Features/Solved/Lasso_FeatureSelection.ipynb). Step through the example, showing how selecting features from the LASSO model improves the linear regression from a weak model to a perfect model (in this toy example).

</details>

<details>
  <summary><strong> ✏️ 4.2 Students Do: Feature Selection with LASSO (Slides 30 and 31) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing)and use slides 30 and 31 to present this activity to the class.

* In this activity, the students use a LASSO model to select relevant features for the residential building dataset.

* The students start with the following Jupyter Notebook file:

  [WranglingFeatures.ipynb](Activities/09-Stu_Lasso-Feature-Selection/Unsolved/WranglingFeatures.ipynb)

* The following file has the student instructions:

  [README.md](Activities/09-Stu_Lasso-Feature-Selection/README.md)

</details>

<details>
  <summary><strong> ⭐ 4.3 Review Activity (0:10) </strong></summary>

* Open [WranglingFeatures.ipynb](Activities/09-Stu_Lasso-Feature-Selection/Solved/WranglingFeatures.ipynb). Go through the solution with the students, answering any questions that they have. Point out the following:

  The initial dataset overwhelms the linear regression, and the model has no predictive power. But after using LASSO to select relevant features, the model becomes excellent with a 0.95 score.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Feature+Selection+with+LASSO&lessonpageTitle=Ensemble+Methods+and+Regressions&lessonpageNumber=19.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F3%2FLessonPlan-3hr.md)</sub>

## 5. Familiar Regressors

| Activity Time:       0:15 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 5.1 Instructor Do: Familiar Regressors (Slides 33 and 34) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eUTx5sa1Yw7Re3mFOWDhsRj2WpS4SoiZIpxRj5yj9KQ/edit?usp=sharing) and use slide 33 to present and slide 34 to live code this lesson with the class. 

* Note that you'll use the following Jupyter Notebook file during this activity

  [FamiliarRegressors.ipynb](Activities/10-Ins_Familiar_Regressors/FamiliarRegressors.ipynb)

* Open [FamiliarRegressors.ipynb](Activities/10-Ins_Familiar_Regressors/FamiliarRegressors.ipynb). Tell the students that in addition to Linear Regression, LASSO, Ridge, and ElasticNet, five more regression models exist that they're already familiar with! Specifically, we can adapt KNN, Random Forests, Extremely Random Trees, AdaBoost, and SVM to work on regression models.

* Run the cells that create the toy regression dataset, and then run all the models on the dataset. Point out that some models do better than others (and that some are downright bad), but they all still have their place.

* Create the swiss roll dataset, and then show the students that it greatly differs from the previous dataset. If you have time, point out that this dataset is **nonlinear**. We therefore don't expect linear regressions to perform well on it. However, the five familiar models can handle nonlinear data. Show that each of these models performs well on the swiss roll dataset.

* Answer any questions before ending the class.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Familiar+Regressors&lessonpageTitle=Ensemble+Methods+and+Regressions&lessonpageNumber=19.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F3%2FLessonPlan-3hr.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
