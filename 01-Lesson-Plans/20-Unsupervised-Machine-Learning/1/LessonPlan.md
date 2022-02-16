# 20.1 Lesson Plan: Unsupervised Learning

## Overview

Today's class will introduce students to unsupervised learning. Students will gain hands-on experience with the k-means algorithm, one of the most used unsupervised algorithms for clustering. Students also will learn how to speed up machine-learning algorithms by using principal component analysis (PCA).

## Class Objectives

By the end of the class, students will be able to:

* Compare and contrast supervised learning and unsupervised learning.

* Use the k-means algorithm to perform cluster analysis.

* Explain the steps of the k-means algorithm.

* Use the elbow method to optimize the number of clusters in k-means.

* Perform principal component analysis to reduce dimensions of a dataset.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* Students have learned the generalities of machine learning, and they already know how to apply supervised machine learning. This class offers an overview of unsupervised machine learning. Students will have hands-on experience using k-means to demonstrate how unsupervised machine learning could help decision-making.

* Examples of how companies use unsupervised learning to target customers or potential customers will be helpful for students. Try to use analogies about how companies like Amazon, Netflix, Google, or Target  use customer segmentation to provide customized offers, or how Spotify uses segmentation to improve its products and services.

* There are several theoretical aspects behind the k-means and PCA algorithms. Focus the class on the practical application of these algorithms for customer segmentation and share the additional references presented on the slides for those students interested in having a deeper understanding.

</details>

- - -

# Class Activities

## 1. Warmup

| Activity Time:       0:25 |  Elapsed Time:      0:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 1.1 Instructor Do: Welcome Class (0:05) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit?usp=sharing) and use slides 1-4 to welcome students to class. Use slide 2 to go over class objectives and let them know that we will be covering unsupervised learning today. Inform them that, as a warm-up activity, they will perform supervised learning on a dataset. Let your students know that a number of the concepts they learned in supervised learning will help them understand unsupervised learning.

</details>


<details>
  <summary><strong> ✏️ 1.2 Students Do: Supervised Learning with KNN (0:15) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit?usp=sharing) and use slides 5 and 6 to present this activity to the class.
  
* **Instructions:**

  * [README.md](Activities/01-Stu_Warmup/README.md)

* **Files:**

  * [KNN.ipynb](Activities/01-Stu_Warmup/Unsolved/KNN.ipynb)

* In this activity, students will create a KNN model and assess its performance.

</details>

<details>
  <summary><strong> ⭐ 1.3 Review Activity (0:05) </strong></summary>

* **Files:**

  * [KNN.ipynb](Activities/01-Stu_Warmup/Solved/KNN.ipynb)

* Remind students that the purpose of this activity was to refresh their knowledge of supervised learning and that they will use this knowledge to understand unsupervised learning.

* Introduce the breast cancer dataset to students: 

  * Several hundred tumor samples were examined to determine whether they were benign or malignant.

  * Additionally, other traits were measured, such as the radius, perimeter, and area.

  * The `target` column contains information on whether a particular sample is benign or malignant. In other words, this column contains labels.

  ![Images/warmup01.png](Images/warmup01.png)

* Next, explain splitting the dataset:

  ```python
  y = df['target'].values
  X = df.drop('target', axis=1)
  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
  ```
  
  * We first split the dataset into data and target (X and y). 

  * Here, the features (X) are all the variables except `target`. 

  * The target (y) is the `target` column in the data frame. 

  * Next, we use the `train_test_split` module to further split the data into training and test sets.

* Next, explain data standardization:

  ```python
  scaler = StandardScaler()
  scaler.fit(X_train)
  X_train_scaled = scaler.transform(X_train)
  X_test_scaled = scaler.transform(X_test)
  ```

  * The KNN algorithm, by default, uses straight (Euclidean) distances between samples to compute nearest neighbors.

  * Consequently, columns with large values can have a disproportionately higher weight than columns with small values, as seen here.

  ![Images/warmup02.png](Images/warmup02.png)
  
  * The `StandardScaler` standardizes the data so that each feature has a mean of 0 and a standard deviation of 1.

  * We train the scaler with the `X_train` data, using `scaler.fit(X_train)`.

  * Once the scaler is trained, we transform the training data: `X_train` and `X_test`.

  * It is important to train (fit) the scaler with the training data, then use it to transform both training and testing data.

  * We will scale data in unsupervised learning as well.

* Next, explain using a KNN model to create predictions.

  ```python
  knn = KNeighborsClassifier(n_neighbors=9)
  knn.fit(X_train_scaled, y_train)
  y_pred = knn.predict(X_test_scaled)
  ```
  
  * A k-nearest neighbor model is instantiated with nine neighbors (another value could have been used instead; here, we're using an optimized value that was determined previously).

  * The model is trained on the training data with `knn.fit()`.

  * The model predicts target values based on `X_test_scaled` data.

* Next, explain that we can use the results to assess the performance of the model.

  ```python
  from sklearn.metrics import accuracy_score
  accuracy_score(y_test, y_pred)
  ```
  
  * The predictions (`y_pred`) are measured against the actual target values in the testing set (`y_test`).

* Finally, summarize the key points of this activity:

  * In supervised learning, datasets have features (variables) and targets.

  * Supervised learning is typically used to predict classifications or values. Scikit-learn uses the `predict` method.

  * Scikit-learn's `fit` and `transform` methods are used to train and transform data, respectively.

</details>

## 2. Introduction to Unsupervised Learning

| Activity Time:       0:50 |  Elapsed Time:      1:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: Introduction to Unsupervised Learning (0:10) </strong></summary>

* In this activity, students will be introduced to unsupervised learning and its most relevant applications.

* Open the lesson slides and go to the "Introduction to Unsupervised Learning" section [Slide 8](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit#slide=id.gcd0450fa74_0_13670). For this activity use slides 8-21.

* Start the presentation by highlighting some differences between supervised learning and unsupervised learning (Slide 9).

| Supervised Learning                | Unsupervised Learning                      |
| ---------------------------------- | ------------------------------------------ |
| Input data are labeled              | Input data are unlabeled                    |
| Uses training datasets             | Uses just input datasets                   |
| **Goal:** Predict a class or value | **Goal:** Determine patterns or group data |

* Remind your students that, in the previous activity, in which they performed supervised learning:

  * The data were labeled. Each tumor sample was labeled either malignant or benign in the `target` column.

  * The dataset was split into training and testing sets.

  * The KNN model created predictions, which were tested against the testing set.

* Explain to students some common uses of unsupervised learning:

  * Group unlabeled data into distinct clusters (clustering).

  * Detect unusual data points in a dataset (i.e., detect anomalies—anomaly detection).

  * Reduce large datasets into smaller datasets while preserving most of the useful information (dimensionality reduction).

* Ask the class how clustering might be used by retail businesses:

  * One possible answer is that it can be used to group customers by shopping habits and create customized offers via email or mobile apps (Slides 10-12).

* Ask the class how anomaly detection might be used by credit card companies:

  * One possible answer is that it can be used to detect anomalous and potentially fraudulent credit card transactions (by grouping transactions into normal and abnormal). (Slides 13-14)

* Ask the class how dimensionality reduction might be used in organizations with large-volume data:

  * It can speed up machine learning by reducing the size of large datasets. (Slide 15)

* Continue the presentation with Slide 16. Highlight the following:

  * Supervised learning is very helpful at predicting the future based on labeled historical data. However, labeled data are not always available.

  * Unsupervised learning allows us to cluster data to find hidden or unknown patterns.

* Explain that customer segmentation is one of the most popular applications of unsupervised learning. It categorizes customers based on their demographical and behavioral traits. (Slide 18)

* Explain that with unsupervised learning algorithms, we can group customer based similarities such as:

  * Customer needs (e.g., a particular that can product satisfy some of them)
  
  * Responses to online marketing channels
  
  * Buying habits (e.g., best day for buying, weekly spend)

* Explain to students that customer segmentation is driving revenue in leading companies such as Netflix and Amazon.

  * 75% of Netflix viewer activity is driven by recommendation ([source](https://www.wired.com/2013/08/qq-netflix-algorithm/)).

  * 35% of Amazon’s sales are generated through their recommendation engine ([source](https://www.martechadvisor.com/articles/customer-experience-2/recommendation-engines-how-amazon-and-netflix-are-winning-the-personalization-battle/)).

  * Netflix’s recommendation system saves the company an estimated $1 billion per year through reduced churn ([source](https://dl.acm.org/citation.cfm?id=2843948)).

</details>


<details>
  <summary><strong> 📣 2.2 Instructor Do: Data Preparation for Unsupervised Learning (0:10) </strong></summary>

* Open [slide 22](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit#slide=id.gccee139706_0_5) and use slides 22 and 23 to introduce this activity. 

* **Files:**

  * [Activities/02-Ins_Data_Prep/Unsolved/Data_Preparation.ipynb](Activities/02-Ins_Data_Prep/Unsolved/Data_Preparation.ipynb)

  * [Activities/02-Ins_Data_Prep/Resources/iris.csv](Activities/02-Ins_Data_Prep/Resources/iris.csv)

* Explain to the class that they should consider the following data preparation tasks:

  * **Data selection:** Make a good choice of what data are going to be used. It is important to consider what in the dataset is available, what is missing, and what can be removed.

  * **Data preprocessing:** Organize the selected data by formatting, cleaning, and sampling them.

  * **Data transformation:** Transform the data to a format that eases its treatment and storage for future use (e.g., CSV file, spreadsheet, database).

* Introduce the iris dataset to the students. Explain that they will look at two examples of the same dataset.

  * It has 150 records (rows) of data.

  * Each record lists five attributes of an iris, such as petal length and width, and the species of the iris.

* Next, introduce Scikit-learn's built-in iris dataset. Explain that this dataset has already been cleaned up and is ready to use.

  ```python
  from sklearn.datasets import load_iris
  iris = load_iris()
  iris.feature_names
  ```

  * The `load_iris` module is a dataset that comes with the Scikit-learn library.

  * Calling `iris.feature_names` returns the names of the features, or columns, of the dataset.

  * Calling `iris.data` returns the iris data, namely the sepal length and width, as well as petal length and width of each recorded iris.

* Similarly, explain that the labels (in this case, the name of the iris species) are also easily accessible.

  ```python
  iris.target_names
  iris.target
  ```

  * `iris.target_names` lists the names of the three iris species in the dataset: setosa, versicolor, and virginica.

  * `iris.target` comprises the actual labels. Instead of the species being specified as string, they have been encoded numerically: 0 for setosa, 1 for versicolor, and 2 for virginica.

* Remind your students that real-life datasets will usually require data cleaning. Inform them that the next example will require some preprocessing steps.

* Load the iris data CSV file into Pandas.

  * The iris species is listed in the `class` column.

  * The species names can be retrieved with `df['class'].unique()`.

* Next, explain that we can encode the string values in the `class` column into numeric values, just like in the Scikit-learn dataset.

  ```python
  class_dict = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica':2}
  df2 = df.replace({'class': class_dict})
  ```

  * We first create a dictionary of the species names and the numerical values we wish to replace them with.

  * We then use Pandas' `replace` method to replace the values in the `class` column.

* Highlight to students that the main difference in preparing data for unsupervised learning is that their algorithms don't have any target variables; they only have input features that will be used to find patterns in the data. So, they should take care of selecting features that could help to find those patterns or create groups.

</details>

<details>
  <summary><strong> ✏️ 2.3 Students Do: Understanding Customers (0:20) </strong></summary>

* Open [slide 24](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit#slide=id.gcd0450fa74_0_16341) and use slides 24 and 25 to present this activity to the class.

* In this activity, students will perform some data preparation tasks on a dataset that contains data from purchases on an e-commerce website made by 200 customers. Students will use this dataset in further activities to find customer segments.

* There are some data transformations that should be made to the dataset, so ask TAs to assist students if there are any questions about why the following changes are needed.

* **Annual Income:** This feature should be regularized since it is on a different scale from the other features; dividing by `1000` is the simplest solution.

* **Previous Shopper:** The `Previous Shopper` should be transformed to a numerical value, in this case, transforming `Yes` to `1` and `No` to `0` is a feasible solution.

* **CustomerID:** Since this column is not relevant to the clustering algorithm, it should be dropped from the DataFrame.

* **Instructions:**

  * [README.md](Activities/03-Stu_Preparing_Data/README.md)

* **Files:**

  * [preparing_data.ipynb](Activities/03-Stu_Preparing_Data/Unsolved/preparing_data.ipynb)

  * [shopping_data.csv](Activities/03-Stu_Preparing_Data/Resources/shopping_data.csv)

</details>

<details>
  <summary><strong> ⭐ 2.4 Review Activity (0:10) </strong></summary>

**Files:**

  * [preparing_data.ipynb](Activities/03-Stu_Preparing_Data/Solved/preparing_data.ipynb)

* Walk through the solution and highlight the following:

  * Unsupervised learning algorithms only work with numerical data, so checking data types is an important task to ensure that numerical values were loaded to the data frame with the appropriate data type.

  ![Data types check](Images/datatypes-check.png)

  * All the columns except `Previous Shopper` have a numeric data type. So, we need to encode only the `Previous Shopper` column.

  ```python
  df_shopping.dtypes

  CustomerID                 int64
  Previous Shopper          object
  Age                        int64
  Annual Income              int64
  Spending Score (1-100)     int64
  ```

  * All columns but `Previous Shopper` have a numeric data type. So we will only need to encode this column.

  * The `CustomerID` column can be dropped; it is not relevant for clustering since it does not denote any relevant characteristic of customer shopping habits.

    ```python
    df_shopping.drop(columns=["CustomerID"], inplace=True)
    ```
  * Checking for `null` values and duplicate entries is part of any data preprocessing workflow. There are neither `null` values nor duplicates in this DataFrame, so no additional adjustments are needed.

  * The `Previous Shopper` column is categorical, so it should be transformed into numerical values. Transforming `Yes` to `1` and `No` to `0` is a common practice.

  ```python
  def changeStatus(status):
      if status == "Yes":
          return 1
      else:
          return 0

  df_shopping["Previous Shopper"] = df_shopping["Previous Shopper"].apply(changeStatus)
  ```

  * The `Age`, `Annual Income`, and `Spending Score (1-100)` columns are standardized.

  ```python
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  scaled_data = scaler.fit_transform(df_shopping[['Age', 'Annual Income', 'Spending Score (1-100)']])
  ```

  * The transformed data is assembled into a new DataFrame, and a column is renamed.

  ```python
  new_df_shopping = pd.DataFrame(scaled_data, columns=df_shopping.columns[1:])
  new_df_shopping['Previous Shopper'] = df_shopping['Previous Shopper']
  new_df_shopping = new_df_shopping.rename(columns={'Spending Score (1-100)': 'Spending Score'})

  ```

  * Finally, the cleaned data frame is saved as a `CSV` file for being used in coming activities.

  ```python
    file_path = Path("../Resources/shopping_data_cleaned.csv")
    df_shopping.to_csv(file_path, index=False)
  ```
  
</details>

- - -

## BREAK

| Activity Time:       0:15 |  Elapsed Time:      1:30  |
|---------------------------|---------------------------|

- - -

## 3. K-Means

| Activity Time:       0:45 |  Elapsed Time:      2:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: The K-Means Algorithm (0:15) </strong></summary>

* In this activity, students will learn how the k-means algorithm works.

**File:**

* [04_Ins_K-Means.ipynb](Activities/04-Ins_KMeans/Solved/K-Means.ipynb)

* Open the lesson slides and move to "The k-means Algorithm" section [slide 28](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit#slide=id.gcd0450fa74_0_16748); go through the slides and highlight the following. This activity utilize slides 28-35.

  * The slide is a three-dimensional visualization based on the iris dataset. The three axes (x, y, and z) are three features of an iris: its sepal length, petal width, and petal length.

  * When visualized in three-dimensional space, it is easy to separate the data points into three distinct clusters.

* Explain that k-means is an unsupervised learning algorithm used to identify clusters and solve clustering issues. Explain also that `k` represents the number of clusters.

  * The k-means algorithm groups the data into `k` clusters, where each piece of data is assigned to a cluster based on some similarity or distance measure to a **centroid**.

  * A centroid represents a data point that is the arithmetic mean position of all the points on a cluster.

* Explain how the K-means algorithm works (Slide 31):

  1. Randomly initialize the `k` starting centroids: the starting centroids are assigned to random locations.
  
  2. Each data point is assigned to its nearest centroid.
  
  3. The centroids are recomputed as the mean of the data points assigned to the respective cluster.
  
  4. Repeat steps `1` through `3` until the values of the centroids are stable.

* Explain that the k-means algorithm does not determine the best number of clusters. The user must assign the value of k.

* Explain that the **elbow curve** is commonly used to figure out the best value of `k`. It is essentially used to determine the number of clusters at which the data points become tightly clustered.

  * On the elbow curve, the `x` axis is the value of clusters, while the `y` axis is a metric used to assess the value of `k`.

  * The **inertia** is commonly used as an objective function. It is the sum of squared distances of samples to their closest cluster center.

  * In other words, a low inertia value means that the data points are tightly clustered around the cluster center.

* Explain how to interpret an elbow curve:

  * The best number for `k` is the number of clusters where the curve turns like an elbow. That is, it's the inflection point where the slope takes a sharp turn and flattens out.

  * Alternatively, we can take a numerical approach. Using the inertia, we choose the best `k`, the value at which adding more clusters only marginally decreases the inertia.

  * The goal isn't to find the number of clusters at which the inertia is lowest. If we had as many clusters as data points, each cluster would be the most tightly packed. But that is not what we want. Instead, it is to find the optimal number of clusters.

* Reassure students that k-means is actually quite simple to implement using Python. Open the Jupyter Notebook and highlight the following points:

  * The k-means algorithm is imported from the `sklearn` library.

  ```python
  from sklearn.cluster import KMeans
  ```

  * An instance of the k-means algorithm is created and initialized with the desired number of clusters (k). Here, we use `k = 3` since we already know we have three classes of irises.

  ```python
  model = KMeans(n_clusters=3, random_state=5)
  ```

  * Next, we train the model with the unlabeled data. When the model is being trained (fit to the data), the k-means algorithm will iteratively look for the best centroid for each of the `k` clusters.

  ```python
  model.fit(df_iris)
  ```

  * After the model is trained, the corresponding cluster for every iris plant in the dataset can be found using the `predict()` method.

  ![K-Means predictions](Images/kmeans-predictions-iris.png)

* Explain that three clusters are labeled as `0`, `1`, and `2`. Clarify that naming classes is done by a subject matter expert; the k-means algorithm is just able to split the dataset into the given number of clusters and label them with numbers.

* Continue the demo by adding a new column to the data frame with the predicted classes.

![Adding predicted classes](Images/adding-classes-column.png)

* Explain that visualizing the clusters helps to understand how they are arranged graphically. In this case, we actually have too many features to represent visually, but we can take two of them to plot the clusters.

  ```python
  # Plotting the clusters with two features
  plt.scatter(x=df_iris["sepal_length"], y=df_iris['sepal_width'], c=df_iris['class'])
  plt.xlabel('Sepal Length')
  plt.ylabel('Sepal Width')
  plt.show()
  ```

  ![2 Features](Images/kmeans01.png)

* As you demonstrate how to identify the best value of `k`, highlight the following:

  * Two lists are created to store the values for the `inertia` and to define how many values of `k` we want to try. Ten values of `k` is normally a good number to start with.

  ```python
  inertia = []
  k = [1,2,3,4,5,6,7,8,9,10]  
  ```

  * A `for` loop is defined to fit the k-means model with the data from `df_iris` and a number of clusters ranging from 1 to 10. The `inertia` is fetched in each iteration to be compared with the elbow curve.

  ```python
  for i in k:
      km = KMeans(n_clusters=i, random_state=0)
      km.fit(df_iris)
      inertia.append(km.inertia_)
  ```

* The elbow curve is plotted:

  ```python
  elbow_data = {
    "k": k,
    "inertia": inertia
  }
  
  plt.plot(df_elbow['k'], df_elbow['inertia'])
  plt.xticks(range(1,11))
  plt.xlabel('Number of clusters')
  plt.ylabel('Inertia')
  plt.show()
  ```

* As seen on the elbow curve, visually the best value for `k` is `3`.

  ![Elbow Curve](Images/elbow01.png)
  
  * This reflects what we already know about the dataset, namely that there are three species.

* To close out the activity, summarize the following key points:

  * In supervised learning, the labels are provided. Previously, labeled data are used to predict future unlabeled data.

  * In unsupervised learning, the labels are detected by the algorithm.

  * The k-means algorithm does not determine the optimal number of clusters, but this can be accomplished with the elbow method.

</details>

<details>
  <summary><strong> ✏️ 3.2 Students Do: Customer Segmentation (0:20) </strong></summary>

* Open [slide 36](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit#slide=id.gcd0450fa74_0_19576) and use slides 36 and 37 to present this activity to the class.

* In this activity, the students will identify the best number of clusters in a customer-clustering scenario by using the elbow curve. Then, the students will use the K-means algorithm to cluster data, and they'll make conclusions about the results.

**Instructions:**

* [README.md](Activities/05-Stu_K_Means_In_Action/README.md)

**Files:**

* [k_means_in_action.ipynb](Activities/05-Stu_K_Means_In_Action/Unsolved/k_means_in_action.ipynb)

* [shopping_data_cleaned.csv](Activities/05-Stu_K_Means_In_Action/Resources/shopping_data_cleaned.csv)

</details>

<details>
  <summary><strong> ⭐ 3.3 Review Activity (0:10) </strong></summary>
**File:**

* [k_means_in_action.ipynb](Activities/05-Stu_K_Means_In_Action/Solved/k_means_in_action.ipynb)

* Walk through the solution and highlight the following:

  * This activity uses the customer shopping data that was preprocessed earlier.

  ```python
  file_path = Path("../Resources/shopping_data_cleaned.csv")
  df_shopping = pd.read_csv(file_path)
  ```

  * The elbow curve is used to find the best value for `k`. A `for` loop is used to loop 10 times, fitting the k-means model and fetching the `inertia` to create the plot.

  ```python
  inertia = []
  k = list(range(1, 11))

  # Calculate the inertia for the range ok k values
  for i in k:
      km = KMeans(n_clusters=i, random_state=0)
      km.fit(df_shopping)
      inertia.append(km.inertia_)
  ```

  * The elbow curve is plotted:

  ```python
  elbow_data = {"k": k, "inertia": inertia}
  df_elbow = pd.DataFrame(elbow_data)
  
  plt.plot(df_elbow['k'], df_elbow['inertia'])
  plt.xticks(range(1,11))
  plt.xlabel('Number of clusters')
  plt.ylabel('Inertia')
  plt.title('Elbow curve for customer data')
  plt.show()    
  ```

![elbow curve](Images/elbow02.png)

* Explain that elbows appear at `k` of 2 and 3, and that here, we will go with 3, as the drop in inertia is much more diminished after this value.

* Explain that it's possible to create functions to bundle tasks:
  
  * The `get_clusters()` function returns a data frame of the dataset, now with a `class` column with clusters predicted by k-means.

  ```python
  def get_clusters(k, data):
      model = KMeans(n_clusters=k, random_state=0)
      model.fit(data)
      predictions = model.predict(data)
      data["class"] = model.labels_

      return data
  ```
  
  * The `show_clusters()` function displays a scatter plot of a data frame:

  ```python
  def show_clusters(df):
      plt.scatter(df['Annual Income'], df['Spending Score'], c=df['class'])
      plt.xlabel('Annual Income')
      plt.ylabel('Spending Score')
      plt.show()
  ```

* Explain that, when we plot annual income vs. spending at k = 3, we see three mostly distinct clusters:

  ![Images/scatter01.png](Images/scatter01.png)

  * The scatter plots only considered two of the features in the dataset (income and spending). Other ones, such as age, could also be used to group the data.

* Finally, go over some considerations in using k-means:

  * k-means performance can suffer when detecting clusters of very different sizes or shapes.

  * k-means works by computing the distance of each data point from a centroid. A feature with very large values can, for example, have disproportionate weight in the algorithm. While the datasets we have used don't require scaling, k-means typically benefits from scaling.

</details>

## 4. PCA

| Activity Time:       0:45 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 4.1 Instructor Do: Speed Up Machine Learning with PCA (0:15) </strong></summary>

* In this activity, students will learn how to use principal component analysis to speed up machine-learning algorithms by reducing the number of features. Open [slide 39](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit#slide=id.gccee139706_0_0) and use slides 39 and 40 to introduce this activity.

* **File:**

  * [06_Ins_PCA.ipynb](Activities/06-Ins_PCA/Solved/Ins_PCA.ipynb)

* Explain to students that principal component analysis (PCA) is a statistical technique to speed up machine-learning algorithms.

  * It  does so by reducing the number of input features (or dimensions).

  * The PCA algorithm transforms a large set of variables into a smaller one that contains most of the information in the original large set.

  * PCA can be quite helpful with enormous datasets, saving both time and computing resources.

* Open the Jupyter Notebook, demonstrate the code, and highlight the following:

  * Again, we are using the iris dataset, which has four features.

  ![The iris dataset without target class](Images/iris-dataset-no-targets.png)

  * Before using PCA, we need to standardize the data. Scikit-learn's `StandardScaler` module is used here. The `fit_transform()` method combines training and transforming data into a single step.

  ![Using StandardScaler](Images/using-standardscaler.png)

  * Once the features are standardized, PCA can be used to reduce the number of features in the dataset. 

  * A PCA model is created. The `n_components` parameter specifies the final number of features. Here, the number of features is reduced from `4` to `2`.

  ```python
  pca = PCA(n_components=2)
  ```

  * PCA then reduces the dimensions of the scaled dataset with the familiar `fit_transform` method.

  ```python
  iris_pca = pca.fit_transform(iris_scaled)
  ```

* Inform students that PCA reduces the dataset into a smaller set of dimensions called **principal components**. 

  * There isn’t a particular meaning assigned to each principal component: the new components are just the two main dimensions of variations that contains most of the information in the original dataset.

* Show students the transformed PCA data: 

  ![PCA Data](Images/pca-df.png)
  
  * These data will be fed into the k-means algorithm, as we have done before.

  * The principal component values bear little resemblance to the original dataset. They can be seen as a reduced representation of the original data.

* Explain that we can assess the amount of information that has been preserved in PCA's dimensionality reduction with the `explained_variance_ratio_` attribute:

  ![Explained variance](Images/explained-variance.png)

  * Here, the first principal component is responsible for `72.77%` of the variance, and the second principal component contains `23.03%` of the variance. 
  
  * Together, the principal components preserve `95.80%` of the information.

  * In other words, a little over 4% of the useful information was lost in the dimensionality reduction performed by PCA.

* Explain that, after reducing the dataset, we can continue to perform unsupervised learning with the k-means algorithm:

  ![PCA Elbow Curve](Images/pca-elbow-curve.png)
  
  * Even though dimensionality reduction led to some loss of information, the elbow curve still suggests a `k` of 3.

  * The k-means algorithm is then used to predict the clusters for the iris data with a `k` of 3.

  ```python
  # Initialize the K-Means model
  model = KMeans(n_clusters=3, random_state=0)

  # Fit the model
  model.fit(df_iris_pca)

  # Predict clusters
  predictions = model.predict(df_iris_pca)
  ```

* Finally, the clusters are plotted. Now they are easier to analyze since we have only two features.

  ![Clusters plot](Images/pca01.png)
  
  * The reduced dataset still splits the dataset into three distinct clusters.

</details>


<details>
  <summary><strong> ✏️ 4.2 Students Do: PCA in Action (0:20) </strong></summary>

* Open [slide 41](https://docs.google.com/presentation/d/1XdLZazG07eaJlW3LyftPNts4o_abrIegvz25ON_gVuA/edit#slide=id.gcd0450fa74_0_19602) and use slides 41 and 42 to present this activity to the class.

* In this activity, students will use PCA to reduce the dimensions of the consumers' shopping dataset.

**Instructions:**

* [README.md](Activities/07-Stu_PCA/README.md)

**Files:**

  * [07_Stu_PCA.ipynb](Activities/07-Stu_PCA/Unsolved/Stu_PCA.ipynb)

  * [shopping_data_cleaned.csv](Activities/07-Stu_PCA/Resources/shopping_data_cleaned.csv)

</details>


<details>
  <summary><strong> ⭐ 4.3 Review Activity (0:05) </strong></summary>

**Files:**

* [Stu_PCA.ipynb](Activities/07-Stu_PCA/Solved/Stu_PCA.ipynb)

* Walk through the solution and highlight the following:

  * Since the dataset was previously standardized, standardization is not required here. Otherwise, it is common practice to standardize data before applying PCA.

  * We use PCA to reduce the number of dimensions from four to two.

  ```python
  pca = PCA(n_components=2)
  shopping_pca = pca.fit_transform(shopping_scaled)
  ```

  * The first principal component contains approximately `72%` of the variance, and the second principal component contains about `14%` of the variance. We have `86%` of the information in the original dataset, but will see whether increasing the number of principal components to 3 will increase the explained variance, and by how much.

  ![Explained variance with two PCs](Images/explained-variance-2pcs.png)

  * Increasing the number of principal components to three preserves `93%` of the information in the original dataset.

  ![Explained variance with three PCs](Images/explained-variance-3pcs.png)

  * The k-means algorithm is run on the principal components data to predict the clusters. A value of `k = 3` is used, as this was the number we used in the last activity.

  ```python
  model = KMeans(n_clusters=3, random_state=0)
  model.fit(df_shopping_pca)
  predictions = model.predict(df_shopping_pca)

  # Add the predicted class columns
  df_shopping_pca["class"] = model.labels_
  ```

* If you have Plotly Express installed, show the visualization of the data in three dimensions.

  ![Clusters plot](Images/pca-data-plot.png)
  
  * Each of the three axes represents a principal component.

  * Visualizing the clusters in 3-D space shows clearer separation between the clusters.

* Explain to students that PCA becomes especially powerful with datasets that have hundreds or even thousands of features. For datasets with up to 10 features, PCA can simplify data analysis and visualization.

</details>

---

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
