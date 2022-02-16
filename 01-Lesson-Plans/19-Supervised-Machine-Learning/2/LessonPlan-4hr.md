# 19.2 Classification Models

## Overview

Today's lesson will introduce the students to the classification models in scikit-learn, the ways to derive statistical measures from a confusion matrix, and the basic preprocessing of data for machine learning models.

## Class Objectives

By the end of today's class, the students will be able to:

* Calculate and apply fundamental classification algorithms: logistic regression, support vector machine (SVM), and k-nearest neighbors (KNN).

* Quantify and validate classification models by using confusion matrixes.

* Implement one-hot encoding in Pandas and scaling and normalization with scikit-learn.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Note that today's class will introduce the students to various classification algorithms in the sklearn ecosystem.

* Realize that today's material should be exciting! The students will conceptually learn several algorithms and then apply them to a real dataset. The variety of algorithms should keep the students engaged, while the common dataset will supply a thread that ties everything together.

* Be aware that with this format, the students will be able to focus on the algorithms and their subtle performance differences rather than on data preprocessing. The students will learn how to generate classification reports to compare model performance and how to tune hyperparameters to optimize their models.

* Please reference our Student FAQ for answers to questions that students of this program frequently ask. If you have recommendations for more questions, feel free to log an issue or create a pull request with the additions that you'd like

* Have your TAs refer to the Time Tracker to stay on track.

* Please remember that the slideshows are for instructor use only. When distributing slides to students, first export them to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

## 1. Warm-Up

| Activity Time:       0:20 |  Elapsed Time:      0:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 1.1 Instructor Do: Welcome the Class (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing) and use slides 1 - 3 to welcome the students to the class, and let them know that today's class will cover classification models going over class objectives using slide 2. Remind them that the last class ended with using a logistic regression and creating a confusion matrix. So to warm up for today, they'll run another logistic regression and create another confusion matrix.

</details>

<details>
  <summary><strong> ✏️ 1.2 Students Do: Logistic Regression and Confusion Matrix Warm-Up (Slides 4 and 5) (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing) and use slides 4 and 5 to present this activity to the students.

* In this activity, the students apply logistic regression to predict whether a specified breast tumor is benign or malignant by using computed features from digitized images. They then create the associated confusion matrix.

* The students start with the following Jupyter Notebook file:

  [Stu_Cancer_Detection.ipynb](Activities/01-Stu_Logistic-Warmup/Unsolved/Stu_Cancer_Detection.ipynb)

* The following file has the student instructions:

  [README.md](Activities/01-Stu_Logistic-Warmup/README.md)

</details>

<details>
  <summary><strong> ⭐ 1.3 Review Activity (0:05) </strong></summary>

* Open [Stu_Cancer_Detection.ipynb](Activities/01-Stu_Logistic-Warmup/Solved/Stu_Cancer_Detection.ipynb), and then go through the solution with the students.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Warm-Up&lessonpageTitle=Classification+Models&lessonpageNumber=19.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F2%2FLessonPlan-4hr.md)</sub>

## 2. Confusion Matrixes

| Activity Time:       0:45 |  Elapsed Time:      1:05  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: Interpreting Confusion Matrixes (Slides 7&ndash;14) (0:15)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Interpreting-Confusion-Matrixes.ipynb](Activities/02-Ins_Interpreting-Confusion-Matrixes/Solved/Ins_Interpreting-Confusion-Matrixes.ipynb)

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing), and then step through Slides 7&ndash;14.

* Remind the students that a confusion matrix shows the breakdown of how the classification predictions interact with the actual states.

* Point out that a confusion matrix can give us a quick sense of the accuracy of a classification model. But, it can also tell us how imbalanced the datasets are and whether the predictions skew too heavily to false positives or false negatives.

* On Slide 9, remind the students of the formula for accuracy. This is the ratio of correct predictions to all predictions.

* On Slides 10 and 11, introduce precision and sensitivity/recall. Point out that while these concepts are similar, they measure different things. You might also want to point out that because machine learning has roots in many fields, many concepts have duplicate names. For example, people use "sensitivity" and "recall" to mean the same thing. Let the students know that we'll use "sensitivity" for the rest of the course.

* On Slide 12, explain the trade-offs between high precision and high sensitivity. Ask the students if they can think of examples where precision or sensitivity might have more importance. You can optionally prompt the students with the following examples:

  * For a cancer screening test, more sensitivity probably has more importance than more precision. The idea is that more sensitivity increases the chances of finding true positives, and people can then follow up with a more-precise test.

  * For spam detection, precision might have more importance. If a program marks an email as spam, we want it to really be spam.

* On slide 13, introduce the F1 score as the balance between precision and sensitivity.

* On Slide 14, recap the measure formulas. Then open [Ins_Interpreting-Confusion-Matrixes.ipynb](Activities/02-Ins_Interpreting-Confusion-Matrixes/Solved/Ins_Interpreting-Confusion-Matrixes.ipynb), and show the classification report that calculates the accuracy, precision, sensitivity, and F1 score. Point out that because the classification report doesn't know which class is positive and which is negative, it gives the scores for both classes.

</details>

<details>
  <summary><strong> ✏️ 2.2 Students Do: Interpret a Confusion Matrix (Slides 15 and 16) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing) and use slides 15 and 16 to present this activity to the students.

* In this activity, the students create a logistic regression model to predict diabetes for the Pima Diabetes dataset. They then interpret the confusion matrix that the model produces.

* The students start with the following Jupyter Notebook file:

  [Stu_Confusion-Matrix.ipynb](Activities/03-Stu_Interpreting-Confusion-Matrixes/Unsolved/Stu_Confusion-Matrix.ipynb)

* The following file has the student instructions:

  [README.md](Activities/03-Stu_Interpreting-Confusion-Matrixes/README.md)

</details>

<details>
  <summary><strong> ⭐ 2.3 Review Activity (0:05) </strong></summary>

* Open [Stu_Confusion-Matrix.ipynb](Activities/03-Stu_Interpreting-Confusion-Matrixes/Solved/Stu_Confusion-Matrix.ipynb), and then go through the solution cell by cell. Point out the values in the classification report that match the manually calculated precision, sensitivity, and F1 score. Note that the following:

  * True negatives: 95
  * False positives: 28
  * False negatives: 24
  * True positives: 45

</details>

<details>
  <summary><strong> 📣 2.4 Instructor Do: Base Rate Fallacy (Slides 18&ndash;2) (0:10)</strong></summary>

* Open the slideshow at [Slide 18](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit#slide=id.gc955ab6d32_0_4138), and then let the students know that we'll take a detour to go through a hypothetical example. This example showcases one way that we can use confusion matrixes to explore the consequences of how people use a model in the real world.

* Introduce the base rate fallacy at a high level. Specifically, a seemingly accurate model applied to imbalanced data can give inaccurate results.

* Step through the slides, going through the calculations and showing the paradox: we can trust a positive result that has a 50% base rate with a high degree of confidence, but a positive result that has a 5% base rate has very low confidence.

* On Slide 22, recap that this is known as the **false positive paradox**, and let the students know that it belongs to a large branch of statistics called Bayesian Statistics.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Confusion+Matrixes&lessonpageTitle=Classification+Models&lessonpageNumber=19.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F2%2FLessonPlan-4hr.md)</sub>

- - -

## BREAK

| Activity Time:       0:40 |  Elapsed Time:      1:45  |
|---------------------------|---------------------------|

- - -

## 3. KNN

| Activity Time:       0:40 |  Elapsed Time:      2:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: Data Preprocessing (Slides 24&ndash;30) (0:10)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Preprocessing.ipynb](Activities/04-Ins_Preprocessing-Data/Solved/Ins_Preprocessing.ipynb)

* Go through [Slides 24&ndash;30](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit#slide=id.gc955ab6d32_0_4187) to explain one-hot encoding, label encoding, and scaling/normalization.

* Go through the provided example code, showing how to one-hot encode data by using `pd.get_dummies()` and how to scale data by using either `StandardScaler` or `MinMaxScaler`.

* Show how `pd.get_dummies()` expands the `workclass` column to nine columns based on the values before applying `get_dummies` to the entire DataFrame. Show how `get_dummies` converts all the categorical columns at once.

* Point out that we should fit scalers to the training set. We can then apply the same scale to both the training and the testing set.

* Ask for any questions before moving to the next activity.

</details>

<details>
  <summary><strong> 📣 3.2 Instructor Do: KNN (Slides 31&ndash;38) (0:10)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_K_Nearest_Neighbors.ipynb](Activities/05-Ins_KNN/Solved/Ins_K_Nearest_Neighbors.ipynb)

* Go through [Slides 31&ndash;38](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit#slide=id.gc955ab6d32_0_4252) and highlight the following:

  * Point out that the KNN algorithm is a machine learning algorithm that's simple yet robust. We can use it for both regression and classification. However, people typically use it for classification.

  * Go through the provided examples on Slides 33&ndash;36, and show how `k` changes the classification. Make sure to point out that we use odd numbers for `k` so that we don't have a tie between neighboring points.

  * Explain that we often computationally calculate the `k` for KNN by using a loop.

* After presenting the slideshow, open [Ins_K_Nearest_Neighbors.ipynb](Activities/05-Ins_KNN/Solved/Ins_K_Nearest_Neighbors.ipynb), and then go through the scikit-learn implementation for the KNN algorithm. This code should seem familiar by now, because it uses the standard model-fit-predict pattern.

  Point out that the best k value for this dataset exists where the score both is accurate and has started to stabilize. 
  
  ```
  k: 1, Train/Test Score: 1.000/0.895
  k: 3, Train/Test Score: 0.955/0.921
  k: 5, Train/Test Score: 0.955/0.947
  k: 7, Train/Test Score: 0.946/0.947
  k: 9, Train/Test Score: 0.938/0.947
  k: 11, Train/Test Score: 0.938/0.947
  k: 13, Train/Test Score: 0.964/0.947
  k: 15, Train/Test Score: 0.955/0.947
  k: 17, Train/Test Score: 0.946/0.947
  k: 19, Train/Test Score: 0.929/0.947
  ```

  The following image shows an overlay plot of training and the testing scores depicts where both values are high and stabilizing:

  ![An overlay plot of the training and the testing scores depicts where both values are high and stabilizing.](Images/knn-plot.png)

</details>

<details>
  <summary><strong> ✏️ 3.3 Students Do: KNN (Slides 39 and 40) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing) and use slides 39 and 40 to present this activity the students.

* In this activity, the students start with the following Jupyter Notebook file:

  [Stu_KNN.ipynb](Activities/06-Stu_KNN/Unsolved/Stu_KNN.ipynb)

* The following file has the student instructions:

  [README.md](Activities/06-Stu_KNN/README.md)

</details>

<details>
  <summary><strong> ⭐ 3.4 Review Activity (0:05)</strong></summary>

* Open [Stu_KNN.ipynb](Activities/06-Stu_KNN/Solved/Stu_KNN.ipynb), and then go through the solution with the students.

* Make sure to highlight the fact that for this activity, `k`=13 seems to give the best combination of the training and testing scores, as the following image shows:

  ![An overlay plot depicts the training and the testing scores coming closest at k=13.](Images/knn-train-test.png)

* Ask the students for any more questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+KNN&lessonpageTitle=Classification+Models&lessonpageNumber=19.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F2%2FLessonPlan-4hr.md)</sub>

## 4. ROC Curves

| Activity Time:       0:30 |  Elapsed Time:      2:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 4.1 Instructor Do: ROC Curves (Slides 42&ndash;44) (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing) and use slides 42&ndash;44 to support your teaching for this topic.

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_ROC-Curve.ipynb](Activities/07-Ins_ROC-Curves/Solved/Ins_ROC-Curve.ipynb)

* Open [Ins_ROC-Curve.ipynb](Activities/07-Ins_ROC-Curves/Solved/Ins_ROC-Curve.ipynb). Run each cell up to and including the classification report, pointing out that we can use the KNN model on the Breast Cancer Wisconsin (Diagnostic) dataset that we previously used. Use this time to reinforce any concepts that the class covered so far or to answer any questions that the students have.

* Point out that most classification models use a probability estimate and then choose a cutoff, which is almost always 0.5 for a binary classification. However, a different cutoff might be necessary. For example, if a false negative is more harmful than a false positive, we might prefer that our model err on the side of giving a false positive.

* Note that many classification algorithms, including KNN, include the `predict_proba()` function. Show the students how the `predict_proba()` output matches the `predict()` output for the first 10 rows of data.

* Introduce the students to the receiver operating characteristic (ROC) curve that the next few cells create. The ROC curve helps us visualize the effect of choosing various cutoff values. The **ROC curve** is a scatter plot of the true positive rate against the false positive rate. At a threshold of 0, the true positive and the false positive rates are both 100%. This exists at the upper-right point of the plot. At a threshold of 1, the true positive and the false positive rates are both 0. This exists at the lower-left point of the plot. Clearly, these models aren't useful. Any point along the dotted line between them represents a model that does no better than chance. The ideal cutoff point has a perfect 100% rate with no false positives. The exists at the upper-left point of the plot.

* Explain that from the ROC curve, we can also calculate the area under the curve (AUC). This represents the robustness of the model across all cutoff values. We can use the AUC to evaluate one model vs. another. A value of 0.5 means that the model is no better than chance&mdash;regardless of the cutoff choice. A value of 1 means that the model is perfect&mdash;regardless of the cutoff choice. In machine learning competitions, the AUC metric is often used to rank competing models.

</details>

<details>
  <summary><strong> ✏️ 4.2 Students Do: ROC Curves (Slides 45 and 46) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing) and use slides 45 and 46 to present this activity to the students.

* In this activity, the students practice creating another KNN model to predict the presence of heart disease. They then plot the ROC curve for that model.

* The students start with the following Jupyter Notebook file:

  [Stu_ROC-Curves.ipynb](Activities/08-Stu_ROC-Curves/Unsolved/Stu_ROC-Curves.ipynb)

* The following file has the student instructions:

  [README.md](Activities/08-Stu_ROC-Curves/README.md)

</details>

<details>
  <summary><strong> ⭐ 4.3 Review Activity (0:05)</strong></summary>

* Open [Stu_ROC-Curves.ipynb](Activities/08-Stu_ROC-Curves/Solved/Stu_ROC-Curves.ipynb), and then go through the solution with the students. Answer any questions that the students have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+ROC+Curves&lessonpageTitle=Classification+Models&lessonpageNumber=19.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F2%2FLessonPlan-4hr.md)</sub>

## 5. SVM

| Activity Time:       0:30 |  Elapsed Time:      3:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 5.1 Instructor Do: SVM (Slides 48&ndash;51) (0:10)</strong></summary>

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Support_Vector_Machine.ipynb](Activities/09-Ins_SVM/Solved/Ins_Support_Vector_Machine.ipynb)

* Go through [Slides 48&ndash;51(https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit#slide=id.gc955ab6d32_0_4440), and highlight the following points:

  * The goal of a linear classifier is to find a line that separates two groups of data. However, many possible lines might exist, with each creating a different boundary. Choosing a line thus might result in the misclassification of new data. The following image illustrates this problem:

    ![A plot depicts two sets of data points and a new data point.](Images/linear-discriminative-classifiers.png)

    The following image shows three possible lines that each separate the two existing groups of data. A new data point can fall into either group, depending on the line:

    ![The same plot now includes three possible separator lines.](Images/classifier-boundaries.png)

  * The SVM algorithm tries to find a **hyperplane** that maximizes the boundaries between groups. Hyperplanes are decision boundaries in data spaces that are "flat" (In 2-dimensional data spaces, hyperplanes are lines; in 3-dimensional data spaces, hyperplanes are planes. Hyperplanes extend this concept to higher dimensional data spaces as well). The SVM algorithm uses hyperplanes like building a virtual wall between the groups, where the wall is as thick as possible but still separates the groups. The resulting distance is known as the **margin**.  And, the optimal hyperplane crosses the wall at its halfway point. A new data point will clearly fall on one side of the optimal hyperplane and thus into one of the existing groups. The following image illustrates these concepts:

    ![The same plot now depicts the optimal hyperplane instead of the three possible separator lines.](Images/svm-hyperplane.png)

* Open [Ins_Support_Vector_Machine.ipynb](Activities/09-Ins_SVM/Solved/Ins_Support_Vector_Machine.ipynb). Go through the scikit-learn implementation of the SVM classifier algorithm, and highlight the following:

  * Point out that scikit-learn makes different kernels available for the SVM model. We use the linear model, as the following image shows:

    ![A screenshot depicts the code.](Images/svm-linear.png)

  * Show how to plot the decision boundaries for the trained model. It's not important that the students fully understand the plotting code. But, they should conceptually understand how the algorithm maximized the boundaries between the two groups, as the following image shows:

    ![A plot depicts the boundaries between two groups of data and the optimal hyperplane between those boundaries.](Images/svm-boundary-plot.png)

    * Show an example of real data where the boundaries overlap. In this case, the SVM algorithm softens the margins. **Softening** means that the SVM algorithm gets a fit by allowing some data points to cross over the margin boundaries, as the following image shows:

    ![A plot depicts a few data points from each group crossed over the margins.](Images/svm-soften.png)

  * Show how to generate a classification report to quantify and validate the model performance, as in the following code and output:

  ```python
  # Calculate the classification report
  from sklearn.metrics import classification_report
  print(classification_report(y_test, predictions,
                              target_names=["blue", "red"]))
  ```

  ```text
  
                precision    recall  f1-score   support

          blue       0.83      1.00      0.91        10
           red       1.00      0.87      0.93        15

      accuracy                           0.92        25
     macro avg       0.92      0.93      0.92        25
  weighted avg       0.93      0.92      0.92        25
  ```

  * From the output, we can see that the accuracy is 92%. We also have results on the precision and recall (or sensitivity) for each group.

</details>

<details>
  <summary><strong> ✏️ 5.2 Students Do: SVM (Slides 52 and 53) (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit?usp=sharing) and use slides 52 and 53 to present this activity to the students.

* In this activity, the students start with the following Jupyter Notebook file:

  [Stu_SVM.ipynb](Activities/10-Stu_SVM/Unsolved/Stu_SVM.ipynb)

* The following file has the student instructions:

  [README.md](Activities/10-Stu_SVM/README.md)

</details>

<details>
  <summary><strong> ⭐ 5.3 Review Activity (0:05)</strong></summary>

* Open [Stu_SVM.ipynb](Activities/10-Stu_SVM/Solved/Stu_SVM.ipynb), and then go through the solution with the students.

  Highlight that the F1 scores indicate that this model is slightly more accurate at predicting negative cases of diabetes than positive cases, as the following image shows:

  ![A screenshot points out the F1 scores in the classification report.](Images/svm-f1.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+SVM&lessonpageTitle=Classification+Models&lessonpageNumber=19.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F2%2FLessonPlan-4hr.md)</sub>

## 6. Hyperparameter Tuning

| Activity Time:       0:35 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 6.1 Instructor Do: Grid Search and Randomized Search (Slides 55&ndash;58) (0:10) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit#slide=id.gc955ab6d32_0_4440) and use slides 55&ndash;58 to introduce this lesson to the class.

* Note that you'll use the following Jupyter Notebook file during this activity:

  [Ins_Hyperparameters.ipynb](Extra-Activities/01-Ins_Hyperparameters/Solved/Ins_Hyperparameters.ipynb)

* Open [Ins_Hyperparameters.ipynb](Extra-Activities/01-Ins_Hyperparameters/Solved/Ins_Hyperparameters.ipynb). Run the first four cells up to and including the following code:

  ```python
  # Create the SVC model
  from sklearn.svm import SVC
  model = SVC(kernel='linear')
  model
  ```

* Send out the [scikit-learn documentation about SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC). Point out all the options that we can send to the `SVC()` function. Note that scikit-learn refers to them as parameters but that they're not the internal parameters of the model. Remind the students that a machine learning model sets its internal parameters based on data. So, machine learning practitioners refer to these external parameters as **hyperparameters**. We use hyperparameters to affect the model's learning process.

  **Note:** SVC stands for support vector classification.

* In the scikit-learn documentation, specifically point out the `C` and `gamma` hyperparameters. Mention that a deep understanding of how changing these parameters affects the model is outside the scope of this class. But, we can try several values and find out what happens to our model.

* Go back to the Jupyter notebook, and then run the next two cells:

  ```python
  param_grid = {'C': [1, 5, 10, 50],
                'gamma': [0.0001, 0.0005, 0.001, 0.005]}
  param_grid
  ```

  ```python
  from sklearn.model_selection import GridSearchCV
  grid_clf = GridSearchCV(model, param_grid, verbose=3)
  ```

* Point out that in the first of these cells, we try four values for the `C` parameter and four values for the `gamma` parameter.

* Explain that scikit-learn has a built-in function for trying all the possible combinations of parameters. This is the `GridSearchCV()` function, which also follows the model-fit-predict pattern. We thus consider `GridSearchCV()` to be a **hypermodel**. We initialize it with a base model and a dictionary of parameters.

* In the next cell, fit the `GridSearchCV()` model to the training data:

  ```python
  # Fit the model by using the grid search classifier. 
  # This will take the SVC model and try each combination of parameters.
  grid_clf.fit(X_train, y_train)
  ```

* Show the students the output. Point out that each possible pair of parameters ran five times and that the scores were then averaged.

* Point out that in the next cell, we list the pair of parameters that `GridSearchCV()` selected as the best option:

  ```python
  # List the best parameters for this dataset
  print(grid_clf.best_params_)
  ```

  Here's the resulting output:

  ```text
  {'C': 5, 'gamma': 0.0001}
  ```

* Note that the following two cells show that we don't even need to print the parameters or create a new `SVC` model. This is because the hypermodel still has the `predict()` and `score()` functions, and it accesses the trained base model for us. Here's the first of these cells:

  ```python
  # Make predictions with the hypertuned model
  predictions = grid_clf.predict(X_test)
  predictions
  ```

  Here's the resulting output:

  ```text
  array([0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1,
       1, 0, 0])
  ```

  Here's the second of these cells:

  ```python
  # Score the hypertuned model on the test dataset
  grid_clf.score(X_test, y_test) 
  ```

  Here's the resulting output:

  ```text
  0.88
  ```

* Let the students know that in this toy example, running our model went quickly. But with four values to test for `C` and four for `gamma` and running each model five times, the base model has to run 4 &times; 4 &times; 5 = 80 times. If our base model takes 60 seconds to run, the entire example will take 80 minutes.

* Mention that luckily, another option exists. Instead of trying every combination, we can try a random subsample and then take the best of the results. A function exists in scikit-learn for doing this: `RandomizedSearchCV()`.

* Point out that in the next cell, we create another parameter grid for `C` and `gamma`. However, it has more values. If we use it with `GridSearchCV()`, it will have to run the base model 50,000 times! Instead, we'll run a random sample of parameter combinations.

* Run the remaining cells, and then show that `RandomizedSearchCV()` still fits the model-fit-predict pattern. It also still accesses the trained base model for us. Finally, we can create a confusion matrix from the predictions.

* Ask the students if they have any questions before moving on to the next activity.

</details>

<details>
  <summary><strong> ✏️ 6.2 Students Do: Grid Search (Slides 59 and 60) (0:15) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1Z8TXtj_1Itc2oLRURvm7e1WNC8SJc5dOYhmWGGgl0BY/edit#slide=id.gc955ab6d32_0_8044) and use slides 59 and 60 to present this activity to the class.

* In this activity, the students use `GridSearchCV()` and `RandomizedSearchCV()` to create a classification model that's based on the Pima Diabetes dataset.

* The students start with the following Jupyter Notebook file:

  [Stu_Hyperparameters.ipynb](Extra-Activities/02-Stu_Hyperparameters/Unsolved/Stu_Hyperparameters.ipynb)

* The following file has the student instructions:

  [README.md](Extra-Activities/02-Stu_Hyperparameters/README.md)

</details>

<details>
  <summary><strong> ⭐ 6.3 Review Activity (0:10) </strong></summary>

* Open [Stu_Hyperparameters.ipynb](Extra-Activities/02-Stu_Hyperparameters/Solved/Stu_Hyperparameters.ipynb), and then step through each cell, answering any questions that the students might have.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=6+-+Hyperparameter+Tuning&lessonpageTitle=Classification+Models&lessonpageNumber=19.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F19-Supervised-Machine-Learning%2F2%2FLessonPlan-4hr.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
