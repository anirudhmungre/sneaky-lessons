# 20.2 Lesson Plan: A Deeper Dive into Unsupervised Learning

## Overview

In today's class, students will continue their journey with unsupervised learning. They will learn how to use t-SNE, as well as its differences from and similarities with PCA. They will also learn about DBSCAN, including its advantages and disadvantages. And finally, they will also learn to create an efficient machine-learning pipeline that incorporates PCA, an unsupervised learning technique, into a supervised learning chain.

## Class Objectives

By the end of the class, students will be able to:

  * Explain the use of t-SNE in exploratory data analysis.

  * Perform hierarchical clustering to group elements and identify relative distances between elements.

  * Visualize a dendrogram generated by hierarchical clustering.

  * Explain the advantages and disadvantages of DBSCAN.

  * Integrate unsupervised learning into a machine learning pipeline.
  
## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* The first half of the class will build on students' prior knowledge of supervised learning and day 1 content of unsupervised learning. They will learn to build a machine-learning pipeline that avoids data leakage.

* In the second half, students will continue to learn unsupervised learning techniques to cluster and visualize their data.

* There is a lot of information in today's class. Do not feel compelled to cover every detail in this lesson plan. Emphasize the key points and adjust the amount of detail depending on your students' response.

</details>

## Slideshow

* [Slides](https://docs.google.com/presentation/d/121iCb7yBVs4sS8dTimiM9GbEukdtGGL_LEAc3Ddyejo/edit#slide=id.ga7f2154bcd_0_35)
 
 
# Class Activities

## 1. Warmup

| Activity Time:       0:25 |  Elapsed Time:      0:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> ✏️ 1.1 Students Do: Warmup (0:15) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit?usp=sharing) and use slides 3 and 4 to present this activity to the class.
  
* **Instructions:**

  * [README.md](Activities/01-Stu_Warmup/README.md)

* **Files:**

  * [grid_search.ipynb](Activities/01-Stu_Warmup/Unsolved/grid_search.ipynb)
  
</details>
 
<details>
  <summary><strong> ⭐  1.2 Instructor Do: Review Activity (0:10) </strong></summary>
  
* **Files:**

  * [grid_search.ipynb](Activities/01-Stu_Warmup/Solved/grid_search.ipynb)
  
* Open the notebook and walk students through the code.

* Explain that we first split the dataset into training and testing sets.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
  ```
  
* Next, go over the steps taken to scale the data:

  ```python
  scaler = StandardScaler()
  scaler.fit(X_train)
  X_train_scaled = scaler.transform(X_train)
  X_test_scaled = scaler.transform(X_test)
  ```
  
  * Emphasize that the scaler should be trained only on the training data. It should not be trained on the entire dataset.

  * Since the purpose of the testing data is to evaluate the performance of the model, there should not be peeks into the testing set. This is why the standard scaler is trained on `X_train` only and why `X_train` and `X_test` are transformed separately.
  
* Next, explain that the support vector classifier is instantiated and that lists of possible parameters for this model are prepared:

  ```python
  from sklearn.svm import SVC
  model = SVC()
  
  param_grid ={
      'C': [0.001, 0.01, 0.1, 1, 10, 100],
      'gamma': [0.001, 0.01, 0.1, 1, 10, 100]
  }
  ```
  
* Explain hyperparameter tuning with `GridSearchCV`:

  ```python
  grid_clf = GridSearchCV(model, param_grid)
  grid_clf.fit(X_train_scaled, y_train)
  grid_clf.best_params_
  grid_clf.score(X_test_scaled, y_test)
  ```

  * It essentially performs `for` loops through the parameters to find the optimal values.

  * A model is created and is trained with the scaled training data.

  * It then reports the best parameters through its `best_params_` property: C of 1 and gamma of 0.01 in this case.

  * The accuracy score here is 0.977.

* Inform students that with this approach, there's still a problematic data leakage, and briefly go over the concept of cross validation. 

  ![Images/cv01.png](Images/cv01.png)

  * The original dataset is split into a training set and a testing set.

  * The training set is randomly further split into, say, five equal segments. Four of these segments are used to train the model, and the fifth one is reserved to validate it. The process is repeated, and the segments take turns being the validating portion.

  * After this process, the model is tested on the testing set, which has been untouched up to this point.

* Explain that, because the entire training set is used to standardize the data, the validating portions have already been exposed to the data. (This is a fairly subtle point, so do not feel compelled to dwell on it.) Inform the class that we will see how to address this problem in the next activity.

</details>

## 2. Machine Learning Pipeline

| Activity Time:       0:35 |  Elapsed Time:      1:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: Machine Learning Pipeline (0:15) </strong></summary>

* Open [slide 6](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit#slide=id.gc7dd28b02d_0_8529) and use slides 6 and 7 to introduce ML pipeline to the class before going through the code.

* **Files:**

  * [pipeline.ipynb](Activities/02-Ins_Pipeline/Solved/pipeline.ipynb)

  * [gridcv.ipynb](Activities/02-Ins_Pipeline/Solved/gridcv.ipynb)

* In this activity, you will first introduce Scikit-learn's `Pipeline`, then show your students how to integrate cross-validation into a machine-learning pipeline.

* Open the [pipeline.ipynb notebook](Activities/02-Ins_Pipeline/Solved/pipeline.ipynb) and remind the class that this is the same cancer dataset that they have worked with before.

* Explain how using a pipeline can simplify performing a sequence of machine-learning tasks.
 
  * Up until this point, when performing a preprocessing step such as standardization, we were required to first standardize the data and pass off the results to the machine-learning model.

  * With a pipeline, we can first define the steps and then execute them with less code.

* Begin to go through the code to illustrate an example of using a pipeline.

  ```python
  X = cancer_data.data
  y = cancer_data.target
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```
  
  * The data from the cancer dataset (X) and the target labels (y) are split into training and testing sets.

* Next, explain that the sequence of operations is specified.

  ```python
  steps = [('scaler', StandardScaler()), 
           ('svm', SVC())]
  ```
  
  * Inside a list, each tuple contains two items. The first is the name of the operation, and the second is the instance of the class.

  * Here, the first tuple contains the standard scaler. The first item, `scaler`, is arbitrary and we could choose a different name for it. The second is an instance of the `StandardScaler` class, as seen by the parentheses (`StandardScaler()`).

  * The operations proceed in the specified order. Here, the order is to perform scaling first, then run SVM.

* Next, explain that we incorporate these steps into a pipeline.

  ```python
  pipe = Pipeline(steps)
  pipe.fit(X_train, y_train)
  pipe.score(X_test, y_test)
  ```
  
  * The first line, which creates an instance of `Pipeline`, incorporates the steps defined above into a pipeline.

  * The next line scales the data and internally passes the results to the SVM model, which learns from the scaled data.

  * The final line evaluates the model performance on the testing dataset.

* Now open the [gridcv.ipynb notebook](Activities/02-Ins_Pipeline/Solved/gridcv.ipynb) and let your students know that we will incorporate `GridSearchCV` into a pipeline, which will let us add **cross-validation** and **hyperparameter tuning** into the process.

  * The hyperparameter tuning of `GridSearchCV` essentially performs a `for` loop of all the possible combinations of model parameters to identify optimal settings.

  * Incorporating a grid search into a pipeline **avoids** the data leakage problem we saw in the previous activity. The algorithm automatically takes care of this issue.

* Explain that we are using the same dataset and that we again define the steps of the pipeline:

  ```python
  steps2 = [
      ('scaler', StandardScaler()),
      ('pca', PCA()),
      ('svm', SVC())
  ]
  pipe2 = Pipeline(steps2)
  ```
  
  * The scaler standardizes the data, PCA reduces the number of features of the data, and the SVM model learns from the data to make predictions.
  
* Next, explain that, as we've done before, we set the parameters:

  ```python
  params = {'svm__C': [0.0001, 0.001, 0.01, 0.1, 1, 5, 10, 50, 100, 1000],
           'svm__gamma': [0.0001, 0.001, 0.01, 0.1, 1, 5, 10, 100],
            'pca__n_components':[2]
           }
  ```
  
  * The parameters for SVM and PCA are defined in a dictionary.

  * **Important:** The parameter names (the dictionary keys) are required to follow a convention.

  * For example, in `svm__C`, the name of the step (`svm`, defined above in `steps2`) is followed by double underscores, then the name of the parameter, `C`. It will not work if this procedure is not followed.

* Walk through the rest of the code.

  ```python
  cv = GridSearchCV(pipe2, params)
  cv.fit(X_train, y_train)
  cv.score(X_test, y_test)
  cv.best_params_
  ```
  
  * `GridSearchCV` is instantiated with the pipeline, as well as the required parameters.

  * It is trained on the training dataset.

  * It evaluates the model's performance on the testing dataset.

  * The best parameters are returned.

</details>

<details>
  <summary><strong> ✏️ 2.2 Students Do: Credit Modeling (0:15) </strong></summary>

* Open [slide 8](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit#slide=id.gc7dd28b02d_0_9886) and use slides 8 and 9 to present this activity to the class.
  
* **Instructions:**

  * [README.md](Activities/03-Stu_Pipeline/README.md)

* **Files:** 

  * [german_credit.csv](Activities/03-Stu_Pipeline/Resources/german_credit.csv)

  * [credit.ipynb](Activities/03-Stu_Pipeline/Solved/credit.ipynb)

</details>

<details>
  <summary><strong> ⭐ 2.3 Instructor Do: Review Activity (0:05) </strong></summary>
  
* **Files:** 

  * [credit.ipynb](Activities/03-Stu_Pipeline/Solved/credit.ipynb)

* Open the notebook and go over the key points of the activity. 

* Briefly go over the preparatory steps:

  ```python
  df.isnull().sum()
  df = df.dropna()
  
  X = df.drop(['kredit'], axis=1)
  y = df['kredit']
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
  ```
  
  * The number of null values per column is identified.

  * Rows with null values are dropped.

  * The dataset is split into X and y sets.

  * X and y are further split into training and testing sets.

* Walk through the code for the pipeline:

  ```python
  steps = [
      ('scaler', StandardScaler()),
      ('pca', PCA(n_components=0.9)),
      ('lr', LogisticRegression())
  ]
  
  pipe = Pipeline(steps)
  
  params = {'lr__C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
         'lr__solver': ['sag', 'lbfgs']}
         
  cv = GridSearchCV(pipe, params)
  cv.fit(X_train, y_train)
  ```
  
  * Each step in the pipeline is defined as a tuple.

  * A pipeline instance is created.

  * The parameters for the pipeline are defined. Here, only logistic regression parameters are defined.

  * A `GridSearchCV` instance is created with the pipeline and parameters from above.

  * The model is trained and cross-validated.
  
* Discuss the results of the model.

  ```python
  cv.score(X_test, y_test)
  cv.best_params_
  ```

  * The accuracy score is 0.755 in this example.

  * The best parameters are 0.1 for `C` (the regularization parameter) and `sag` for the logistic regression solver.

* Explain that, while logistic regression isn't as sensitive to hyperparameter tuning to other algorithms such as support vector machine, a grid search can help squeeze out some extra performance.

</details>

## 3. t-SNE

| Activity Time:       0:35 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: t-SNE (0:15) </strong></summary>
  
* **Files:**

  * [t-SNE.ipynb](Activities/04-Ins_tSNE/Solved/t-SNE.ipynb)

* To introduce this activity to the class, open [slide 11](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit#slide=id.gce6cca3d29_0_47) and use slides 11-17 prior to open the Jupyter notebook and going through the code.

* Remind the class that PCA, or principal component analysis, reduces the number of dimensions of a dataset.

  * It does so by re-orienting the data in the direction of maximum variance.

* Open the slideshow (Slide 12) and explain that t-SNE, like k-means and PCA, is an unsupervised learning algorithm.

  * t-SNE takes unlabeled data and sorts the data points into clusters.

  * Like PCA, t-SNE reduces the dimensions of a dataset.

  * **Important**: Unlike PCA, t-SNE is mainly used to visualize data, usually in two dimensions, sometimes three.


* Explain that t-SNE (rhymes with "Disney") stands for "t-distributed stochastic neighbor embedding." (Slide 12)

  * **t-distributed**: A probability curve is generated.

  * **Stochastic**: There is randomness involved. There will be some randomness is the output.

  * **Neighbor embedding**: Similar data points become neighbors.

  * The meaning of these terms will become clearer as we explore t-SNE more in-depth.

* Explain that the t-SNE algorithm clusters data by plotting similar points closely to each other, and dissimilar points farther away. Emphasize the following: (Slides 13-15)

  * t-SNE doesn't directly project multidimensional data onto fewer dimensions. (Slide 13)

  * For each point, a probability curve is generated. Every other point is compared to this point. The original data point is at the middle of the curve. Ones similar to it are plotted closely together, and ones dissimilar to it are plotted distally on the curve. (Slide 14)

  * Actually, two probability curves are generated: one in high-dimensional space, and another in lower-dimensional space. The two curves are overlaid and compared to one another, and the difference between the two are minimized. (Slide 15)

  * An example of t-SNE can be seen with handwritten digits from 0 through 9 (Slide 16). There are, as expected, 10 clusters.

* Open the Jupyter Notebook and introduce the dataset:

  ![Images/tsne01.png](Images/tsne01.png)

  * It is the iris dataset, which we have seen previously.

  * Since there are three species of irises in the dataset, we should expect to visualize three clusters.
  
* Explain that, since the dataset already contains labels (the `class` column), we'll set it aside and use it to verify t-SNE's performance.

  ```python
  df2 = df.drop(['class'], axis=1)
  labels = df['class']
  ```

* Next, explain that we create a t-SNE model, train it, and transform the dataset by reducing its dimensions.

  ```python
  tsne = TSNE(learning_rate=35)
  tsne_features = tsne.fit_transform(df2)
  tsne_features.shape
  ```
  
  * The model is initiated here with a `learning_rate` of 35, but other values can be tried. The normal range for this parameter is between 10 and 1,000. A learning rate that is too low can lead to data points that are clumped into a single cluster. If too high, it may lead to too many small clusters.

  * The `fit_transform` method looks for patterns in the data and reduces its dimensions.

  * The `shape` property returns `(150, 2)`, indicating that the transformed dataset has 150 rows. The number of columns has been reduced to two.

* Next, explain that we can use the transformed dataset to plot the clusters in the dataset.

  ```python
  df2['x'] = tsne_features[:,0]
  df2['y'] = tsne_features[:,1]
  ```
  
  * Of the two columns in the transformed dataset, the first can be used to create values for the x-axis in the plot. The second can be used to create y-axis values.

* Next, show the results of the visualization.

  ```python
  plt.scatter(df2['x'], df2['y'])
  ```
  
  ![Images/tsne02.png](Images/tsne02.png)
  
  * There appear to be three clusters, or possibly one small cluster and one larger cluster.

  * **Note:** The rendition in your notebook is likely to be similar, but not identical.
  
* Now discuss the same visualization with labeled classes:

  ```python
  plt.scatter(df2['x'], df2['y'], c=df2['class'])
  ```

  ![Images/tsne03.png](Images/tsne03.png)
  
  * The plot confirms that there are indeed three clusters, two of which are positioned closely together.

* Show that a plot of two of the variables from the original iris dataset similarly show two closely related clusters and a more distant one.

  ![Images/tsne04.png](Images/tsne04.png)

* Explain the following caveats of using t-SNE:

  * The t-SNE model parameters, such as `perplexity` and `learning_rate` can significantly alter the results, especially the former.

  * Because there is randomness involved during the optimization process, the visualizations will not be the same every time. Hence, the word `stochastic`, which means "random," in the name of t-SNE.

  * Cluster sizes and distances between clusters are not necessarily indicative of actual cluster sizes and distances.

* Conclude the activity with the following summary of t-SNE:

  * t-SNE is a useful tool to visualize high dimensional data in two-dimensional (and sometimes three-dimensional) space.

  * The Scikit-learn implementation of t-SNE uses the familiar `fit-transform` paradigm to train the model and transform the data.

  * The model parameters can greatly affect t-SNE's output.

  * t-SNE is especially good at detecting non-linear patterns.

</details>

<details>
  <summary><strong> ✏️  3.2 Students Do: Grape Clusters (0:15) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit?usp=sharing) and use slides 18 and 19 to present this activity to the class.

* **Instructions:**

  * [README.md](Activities/05-Stu_tSNE/README.md)

* **Files:**

  * [wine.ipynb](Activities/05-Stu_tSNE/Unsolved/wine.ipynb)

  * [dataset for bonus activity](Activities/05-Stu_tSNE/Resources/breast_cancer.csv)

</details>

<details>
  <summary><strong> ⭐  3.3 Instructor Do: Review Activity (0:05) </strong></summary>
  

* **Files:**

  * [wine.ipynb](Activities/05-Stu_tSNE/Solved/wine.ipynb)

* After opening the notebook, briefly note the dataset used.

  ```python
  wine = load_wine()
  data = wine.data
  wine.feature_names
  wine.target_names
  labels = wine.target
  ```
  
  * This wine dataset contains data on three types of wines, as seen in `wine.target_names`. So, ideally, t-SNE would reveal three clusters.

  * The target values are assigned to `labels`, which we'll later use to differentiate the clusters in the t-SNE plot.

* Next, highlight the following points from the code for t-SNE.

  ```python
  scaler = StandardScaler()
  scaled_features = scaler.fit_transform(data)
  
  tsne = TSNE(learning_rate=250)
  tsne_features = tsne.fit_transform(scaled_features)
  ```
  
  * Scaling the data gives equal weight to each feature.

  * A t-SNE instance is created and trained.

  * A `learning_rate` of 100 is used here, but a different value, such as 5,000, can render very different results (students are welcome to try it for themselves).

* Finally, show the plots of the results:

  ```python
  plt.scatter(tsne_features[:,0], tsne_features[:,1], c=labels)
  ``` 

  * Since t-SNE reduces the dataset to two features, `tsne_features[:,0]` is the first column of the transformed dataset, and `tsne_features[:,1]` is the second column.

  ![Images/tsne05.png](Images/tsne05.png)

  * The t-SNE plot appears to show three distinct clusters (because of the randomness involved in t-SNE, the plot will not be identical).

  ![Images/tsne06.png](Images/tsne06.png)

  * Coloring by labels (specifying the type of wine) confirms the previous findings.

</details>

- - -

## BREAK

| Activity Time:       0:15 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

- - -

## 4. DBSCAN


| Activity Time:       0:30 |  Elapsed Time:      2:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 4.1 Instructor Do: DBSCAN (0:15) </strong></summary>
  
* **File:**

  * [moons.ipynb](Activities/06-Ins_DBSCAN/Solved/moons.ipynb)

* Open [slide 22](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit#slide=id.gc7dd28b02d_0_10330) and use slides 22-24 to introduce the DBSCAN clustering algorithm.

  * DBSCAN stands for density-based spatial clustering of applications with noise.

  * In DBSCAN, a random data point is chosen.

  * If the data point meets a threshold for the number of neighbors, it is part of a cluster. This is performed recursively for each of its neighbors.

  * When that data point runs out of neighbors to inspect, another random data point is chosen, and the process is repeated.

* Compare and contrast k-means and DBSCAN. (Slide 24)

  * k-means is best suited for ball-shaped clusters, while DBSCAN deals better with asymmetrical shapes.

  * In k-means, the number of clusters must be determined by the user. DBSCAN figures this out on its own.

  * k-means is sensitive to outliers, while DBSCAN has a more robust tolerance for outliers.

  * k-means is relatively fast, while DBSCAN can slow down dramatically with larger datasets.

* Open Jupyter Notebook and introduce the dataset.

  ```python
  X, y = make_moons(n_samples=500, noise=0.1)
  ```
  
  * This is an artificially generated dataset.

  * `X` is the set of coordinates of all the points in the dataset. `y` is the set of target labels.

* Explain that we scale the data before using DBSCAN:

  ```python
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)
  ```
  
* Take a moment to note some caveats to feature scaling:

  * Up to this point, we have scaled data with many examples. With DBSCAN as well, datasets usually benefit from scaling. However, this should not be an automatic assumption.

  * An example where scaling can lead to distortion is latitude and longitude.

  * It is always a good idea to examine the dataset before diving into feature engineering.

* Next, show the plot of the dataset:

  ```python
  df = pd.DataFrame()
  df['x'] = X_scaled[:,0]
  df['y'] = X_scaled[:,1]
  plt.scatter(df['x'], df['y'])
  ```
  
  ![Images/dbscan1.png](Images/dbscan1.png)
  
  * The x and y coordinates each have their own column.

  * There are two main clusters, each shaped like a semi-circle.

* Now show the two clusters colored by label:

  ```python
  plt.scatter(df['x'], df['y'], c=y)
  ```

  ![Images/dbscan2.png](Images/dbscan2.png)
  
  * If our DBSCAN model is successful, the plot of the results should look roughly like this.

* Walk through the DBSCAN code, explaining the parameters.

  ```python
  from sklearn.cluster import DBSCAN
  dbscan = DBSCAN(eps=0.3, min_samples=5)
  dbscan.fit(X_scaled)
  ```
  
  * The DBSCAN model is first initialized with two parameters: `eps` and `min_samples`.

  * `eps`, which stands for epsilon, determines which two points can be considered neighbors. If the distance between two data points is smaller than the `eps`, they are considered neighbors.

  * Therefore, if the `eps` is too low, many data points will be considered to be noise. If too high, clusters won't be differentiated.

  * `min_samples` refers to the minimum number of neighbors a data point must have to be considered a core point.

  * A rule of thumb is that the `min_samples` should be greater than the number of dimensions in the dataset plus one. Here, since there are two dimensions, it should be at least three, but we chose five. 

  * Noisier data tend to benefit from a higher `min_samples`.

  * The `fit` method is used to train the model.

* Explain how to access the labels generated by DBSCAN:

  ```python
  labels = dbscan.labels_
  set(labels)
  ```
  
  * After training the model with `fit`, the cluster labels can be accessed through the `labels_` property of the model instance.

  * `set(labels)` returns the unique cluster values. Here, the values are `{-1, 0, 1}`; -1 refers to samples labeled as noise. DBSCAN has therefore detected two clusters (0 and 1) and detected some outliers as well.
  
* Show the plot of the results, colored by labels generated by DBSCAN.

  ![Images/dbscan3.png](Images/dbscan3.png)
  
  * As seen from above, it shows two main clusters, with some outliers.

</details>

<details>
  <summary><strong> ✏️  4.2 Students Do: DBSCAN with Iris (0:10) </strong></summary>

* Open [slide 25](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit#slide=id.gc7dd28b02d_0_10335) and use slides 25 and 26 to introduce this activity to the class.
  
* **Instructions:**

  * [README.md](Activities/07-Stu_DBSCAN/README.md)

* **Files:**

  * [iris.ipynb](Activities/07-Stu_DBSCAN/Unsolved/iris.ipynb)

</details>

<details>

  <summary><strong> ⭐  4.3 Instructor Do: Review Activity (0:05) </strong></summary>
  
* **Files:**

  * [iris.ipynb](Activities/07-Stu_DBSCAN/Solved/iris.ipynb)

* Open the Jupyter Notebook and briefly note the scatter plots of the iris dataset.

  ![Images/dbscan4.png](Images/dbscan4.png)
  
  * Since only two of the columns are featured in this plot, it isn't completely representative of the dataset; it is a rough approximation.

  * At a glance, there appear to be two main clusters: a smaller cluster in the bottom left, and a larger cluster in the top right.

  * The same scatter plot, colored by species, shows that the larger cluster is actually composed of two clusters.

  ![Images/dbscan5.png](Images/dbscan5.png)

* Next, walk through the DBSCAN code.

  ```python'
  scaler = StandardScaler()
  features_standardized = scaler.fit_transform(data)
  ```
  
  * The data are scaled.

  ```python
  dbscan = DBSCAN(eps=0.6, min_samples=5)
  dbscan.fit(features_standardized)
  ```
  
  * A DBSCAN model is instantiated and trained.

  * Here, the `eps` was set to 0.6 and `min_samples` to 5, but different values can be tried.

  * `set(labels)` returns two clusters and outliers.

* Show the scatter plot, labeled by DBSCAN's labels, and discuss the results, inviting students to explain their results.

  ![Images/dbscan6.png](Images/dbscan6.png)
  
  * DBSCAN has detected only two clusters instead of three.

  * However, this is to be expected. Since DBSCAN determines its clusters on areas of density, the larger single area of density is interpreted as a single cluster.

* Summarize the activity before moving on.

  * Although DBSCAN offers a number of advantages over k-means, it also suffers drawbacks like the one we have seen.

  * There is no single best tool for the job in unsupervised learning. It is important to know the strengths and weaknesses of each approach.

</details>


## 5. Hierarchical Clustering


| Activity Time:       0:40 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 5.1 Instructor Do: Hierarchical Clustering (0:15) </strong></summary>

* Open [slide 28](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit#slide=id.gc7dd28b02d_0_10358) and use slides 28-30 to introduce hierarchical clustering to the students.
  
* **Files:**

  * [eurovision.ipynb](Activities/08-Ins_Hierarchical_Clustering/Solved/eurovision.ipynb)

  * [breast_cancer.ipynb](Activities/08-Ins_Hierarchical_Clustering/Solved/breast_cancer.ipynb)

* Open **eurovision.ipynb** to give an overview of hierarchical clustering.

* Introduce the dataset:

  ![Images/dendro0.png](Images/dendro0.png)
  
  * Eurovision is an international song contest in which member countries vote on songs submitted by other participating countries.

  * Each row represents how that country voted for other countries.

* Scroll down to the dendrogram and explain several basic ideas of hierarchical clustering:

  ![Images/dendro1.png](Images/dendro1.png)
  
  * The tree-like structure seen here is called a dendrogram.

  * Here, each cluster starts at the **bottom** of the dendrogram. Each country is its own cluster.

  * For each cluster, the hierarchical clustering algorithm finds the closest neighbor, and merges two clusters into one. 

  * This process is repeated until there is a single cluster.

  * A pair of clusters that join at a lower vertical height are closer to each other than a pair of clusters that join at a higher height.

  * A horizontal line at a given height determines the number of clusters. For example, if a horizontal line is drawn slightly below the top of the graph, it will cut across two vertical lines. This means that there are two clusters at that height.

* Explain the following particulars of this dendrogram to the class:

  * Each country is paired with its closest neighboring cluster based on voting patterns.

  * For example, Estonia's closest neighbor is Latvia, and they merge into a single cluster before merging with Lithuania (see the labels on the bottom left of the dendrogram).

  * There appear to be two large clusters: the cluster on the left, in which Western European countries are more heavily represented, and the one on the right, in which Eastern European countries are more heavily represented.

* Next, open **breast_cancer.ipynb** to explain the Python implementation of hierarchical clustering.

* Explain that, while hierarchical clustering can be used to examine the relationship of each sample to others, as seen in the Eurovision example, it can also be used to generate cluster labels.

* Explain the code to perform hierarchical clustering and to create a dendrogram:

  ```python
  normalized = normalize(df)
  mergings = linkage(normalized, method='ward')

  dendrogram(mergings,
          leaf_rotation=90,
          leaf_font_size=5)

  plt.show()
  ```

  * Because the mergings are based on distances between samples, the dataset should be standardized or normalized. Here, we use Scikit-learn's `normalize` method.

  * The actual clustering is performed here using SciPy's `linkage` method. We're using the `ward` method to compute distances between clusters.

  * To generate the dendrogram, SciPy's `dendrogram` method is used:

      * Its first argument, `mergings`, is the linkage matrix we just generated.

      * The `leaf_rotation` and `leaf_font_size` refer to the text label of each sample. Here, the text is turned vertically and its font size set at 5.

* Open the slideshow and take a moment to explain some of the linkage methods of hierarchical clustering: (Slide 29)

  * Single: The difference between two clusters is defined by the closest distance between two clusters.

  * Complete: The difference between two clusters is defined by the farthest distance between two clusters.

  * Ward: This method is based on the squared euclidean distance between clusters. It's the method used in our example, and often used as a default.

* Return to the notebook to discuss the findings:

  ![Images/dendro2.png](Images/dendro2.png)
  
  * A rough rule of thumb is to look for the clusters with the longest branches. Here, at the level of two clusters, there is maximum vertical distance. However, this practice is not always reliable.

  ![Images/dendro04.png](Images/dendro04.png)

* Next, walk through the code that uses hierarchical clustering to generate labels:

  ```python
  cluster = AgglomerativeClustering(n_clusters=2,
                                   affinity='euclidean',
                                   linkage='ward')
  labels = cluster.fit_predict(df2)
  ```
  
  * The algorithm used here is Scikit-learn's `AgglomerativeClustering`, meaning the clustering is performed from bottom to top.
  
  * `n_clusters`: Based on the dendrogram, the number of clusters with is set to 2.

  * The `affinity` refers to the metric used to compute the matrix of distances.

  * The cluster labels are generated by the `fit_predict` method.

* Open the slideshow and take a moment to explain the `affinity` parameter of Scikit-learn's agglomerative clustering: (Slide 30) 

  * Euclidean: This is the shortest distance between two points.

  * Manhattan: This is the sum of absolute values of the differences between two points. The path in a Manhattan distance resembles the Manhattan city grid.

* As you close out the activity, point out the following strength and drawback of hierarchical clustering:

  * Strength: Unlike k-means, the number of clusters does not need to be predetermined by the user.

  * Drawback: It slows down exponentially with larger datasets.

</details>

<details>
  <summary><strong> ✏️  5.2 Students Do: Customer Data (0:15) </strong></summary>

* Open [slide 31](https://docs.google.com/presentation/d/1qE62meTqGf9j59DfJBhaaVXORnbzkQRhri9KpJBeDXU/edit#slide=id.gc7dd28b02d_0_10363) and use slides 31 and 32 to present this activity to the class.
  
* **Instructions:**

  * [README.md](Activities/09-Stu_Hierarchical_Clustering/README.md)

* **Files:**

  * [wholesale_customers.csv](Activities/09-Stu_Hierarchical_Clustering/Resources/wholesale_customers.csv)

  * [customers.ipynb](Activities/09-Stu_Hierarchical_Clustering/Unsolved/customers.ipynb)

</details>

<details>

  <summary><strong> ⭐  5.3 Instructor Do: Review Activity (0:10) </strong></summary>
  
* **Files:**

  * [customers.ipynb](Activities/09-Stu_Hierarchical_Clustering/Solved/customers.ipynb)

* Open the notebook and explain the data preparation steps.

  ```python
  df = pd.read_csv(file)
  normalized = normalize(df)
  df2 = pd.DataFrame(normalized)
  df2.columns = df.columns
  ```
  
  * After reading in the dataset, it is normalized.

  * Since the normalized data are formatted as an array, they are copied into a new data frame.

  * The column names from the original data frame are copied over as well.

* Go over the code for hierarchical clustering.

  ```python
  mergings = linkage(normalized, method='ward')
  
  dendrogram(mergings,
            leaf_rotation=90,
            leaf_font_size=5)
  ```
  
  * A matrix of distances is generated with the `linkage` function, here using the `ward` method.

* Discuss the dendrogram generated by hierarchical clustering.

  ![Images/dendro04.png](Images/dendro04.png)
  
  * The largest vertical distance is found with two clusters, suggesting that explore two clusters.
  
* Next, explain generating cluster labels.

  ```python
  cluster = AgglomerativeClustering(n_clusters=2,
                                   affinity='euclidean',
                                   linkage='ward')
  labels = cluster.fit_predict(df2)
  ```
  
  * Scikit-learn's `AgglomerativeClustering` method performs essentially the same task as SciPy's `linkage` but also allows us to generate predicted labels.

* Finally, discuss the plots.

  ![Images/hierarchical01.png](Images/hierarchical01.png)
  
  ![Images/hierarchical02.png](Images/hierarchical02.png)
  
  * Because each plot only uses two of the dataset's features, it should be regarded as a rough approximation, not an accurate representation.

  * However, there do appear to be two reasonably separable clusters.

</details>
  
---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.

  
