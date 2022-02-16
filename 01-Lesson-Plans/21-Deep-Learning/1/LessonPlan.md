# 21.1 Introduction to Advanced Machine Learning

## Overview
Today's lesson will introduce students to neural networks and how neural networks are collections of perceptron models, related to logistic regressions. Neural networks are a powerful class of machine learning algorithms that are an essential tool for machine learning engineers. Neural networks are also the basis of deep learning networks, which we will cover in the next lesson plan.

## Class Objectives

By the end of class, students will be able to:

* Compare the differences between the traditional machine learning classification and regression models and the neural network models.

* Describe the perceptron model and its components.

* Implement neural network models using TensorFlow.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes:</strong></summary>

* If you've had some experience with machine learning but haven't used neural network models before, we have selected a few online resources for you to review before this week's class. Please take some time to read these materials. They'll provide much needed context surrounding how neural networks function:

  * [But what is a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk): This video by 3Blue1Brown is a fantastic introduction to what a neural network is and what it does.

  * [Hands-On in the Playground](https://www.youtube.com/watch?v=ru9dXF04iSE): This video by Sundog Education is a step-by-step guide of Google's TensorFlow Playground.

* Please review our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-03-python) for the most frequently asked student questions about this program. If you have additional questions to add, log an issue or a pull request with your suggestions.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

</details>

- - -

# Class Activities

## 1. Introduction to Advanced Machine Learning


| Activity Time:       0:45 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Surfing the Neural Net (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 1 and 2 to cover our class objectives and slides 3 - 7 to welcome students to class and explain that in our final week of machine learning we will be focusing on one of the most in-demand skills for any data scientist - **neural networks**.

* Explain to students that neural networks are a powerful machine learning technique modeled after neurons in the brain.

  * They are used by industry leaders such as Google, Facebook, Twitter, and Amazon to analyze complex datasets.

* Show students the following image of the MNIST dataset:

![MNIST example](Images/mnist_dataset.png)

* Point out that neural network models can analyze numerical data, natural voice, text, and even images. One classic neural network example is a handwriting classification model such as MNIST.

  * The MNIST (Modified National Institute of Standards and Technology) dataset contains black-and-white images of handwritten numbers.

  * A neural network can train on each pixel of each image as a scaled value from zero (completely white) to one (completely black). With enough data points, a trained neural network model can classify handwritten numbers with a high degree of accuracy.

* Show students the example diagram of a neural network:

![Neural Network Diagram](Images/nn_diagram.png)

* Point out to students that those who have experience building neural network models tend to get hired faster and have better salaries than other data scientists.

* Show students the following diagram plotting the different types of machine learning models:

![machine_learning_diagram](Images/machine_learning_diagram.png)

* Throughout the past two weeks, we have learned and implemented a number of supervised and unsupervised models.

  * These models range in accuracy and interpretabilty and each have their specific use cases.

* This week we'll focus on neural networks and their more complex variant: deep learning models.

  * Just like our previous machine learning models, neural networks have many use cases and can be applied to a wide variety of datasets.

  * By the end of this week, we will be able to implement and optimize neural network models, and we'll compare the performance of neural networks to other supervised and unsupervised machine learning models.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: What is a Neural Network? (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 8 - 11 to assist you to present this activity.

* Ask students if any of them have heard of a **neural network** model.

  * If anyone raises their hand, ask if they can describe what a neural network is.

* Explain that a **neural network** is an advanced form of machine learning that contains multiple layers of **nodes**, which perform individual computations.

  * Point out that neural networks were modeled after the human brain; therefore, the nodes in a layer are often referred to as **neurons**.

* Show students the following example of a neural network diagram:

![example neural network diagram](Images/neural_network_example_dog_cat.png)

* Explain that the layers of **neurons** are connected and weighed against one another until the neurons reach the final outer layer. The outer final layer returns a numerical, or encoded categorical, result.

* Neural networks are particularly useful in data science because they serve multiple purposes.

  * One of the most popular uses for a neural network is a classification algorithm that determines how to categorize an input.

  * Another popular use of neural networks is as a regression model, where a dependent output can be predicted from independent input variables.

* Point out that neural networks are a great alternative to many of the machine learning models we have learned throughout the course—logistic regression, random forest, or multiple linear regression.



</details>

<details>
  <summary><strong>📣 1.3 Students Do: Working through the Logistics (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 12 and 13 to present this activity to the class. 

* In this activity, students will use the logistic regression to build a binary classification model, the precursor to neural networks.

**Instructions:**

* Use the starter code provided to create your *make_blobs* dataset from Scikit-learn.

* Split your dataset into training and testing sets using Scikit-learn's *train_test_split* module.

* Create a LogisticRegression instance from Scikit-learn's *LogisticRegression* model.

  * **Hint:** If you need a reminder on how to create a LogisticRegression model, see [Scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).

* Train your LogisticRegression model on the training dataset.

* Evaluate your trained LogisticRegression model using the *accuracy_score* metric from Scikit-learn.

</details>

<details>
  <summary><strong>📣 1.4 Review: Picking Our Brains on Neural Networks (0:10)</strong></summary>

* Open [01-Stu_WorkThroughLogisics/WorkThroughLogisitcs.ipynb](Activities/01-Stu_WorkThroughLogistics/Solved/WorkThroughLogistics.ipynb) within Jupyter Notebook and go through the code line by line with the class, answering whatever questions they may have. Point out the following:

  * Up to today's class, we have been performing our entire machine learning workflow through Scikit-learn. After today, we will start to incorporate other Python libraries that can help us build neural network models with the same ease and efficiency as Scikit-learn.

  * Scikit-learn has fantastic tools to create synthesized training and testing datasets, and we will need these same tools to build our neural network models.

</details>


<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Introduction+to+Advanced+Machine+Learning&lessonpageTitle=Introduction+to+Advanced+Machine+Learning&lessonpageNumber=21.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F1%2FLessonPlan.md)</sub>

- - -

## 2. Neural Network Basics

| Activity Time:       1:05 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Perceptron, the Computational Neuron (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 15 - 23 to assist you to present this activity.

* Reassure students that neural networks may sound intimidating, but in reality they are simply layers and layers of smaller models such as our logistic regression model.

* The original design for computational neurons (and subsequently the neural network) dates as far back as the 1950s.

* Explain that, at that time, Frank Rosenblatt created the **perceptron model**. The perceptron model is a single neural network unit that mimics the biological neuron by receiving input data, weighing the information, and producing a clear output.

* Show students the following image of the perceptron model:

![perceptron model](Images/perceptron_model.png)

* Explain to students that the perceptron model has four major components:

  ![perceptron model input](Images/perceptron_model_input.png)

  * The **input values**, which are typically labeled as *𝜒*, or chi. Depending on how many features or variables exist in the dataset, the number of input values will change.

  ![perceptron model weight](Images/perceptron_model_weights.png)

  * The **weight coefficients** are applied to each input value to help the machine learning model identify features of interest. The weight coefficients are typically labeled as *w*, or omega.

  ![perceptron model bias term](Images/perceptron_bias_term.png)

  * The **bias term** is an additional input typically labeled as *⍵*. The bias term helps to shift the output of the model, which may be necessary for properly training the model.

  ![perceptron model net summary](Images/perceptron_net_summary.png)

  * The **net summary function** aggregates all weighted inputs to provide an output value. In this example, the net summary function is a summation.

* Explain that the perceptron model—also known as a **linear binary classifier**—is most commonly used to separate data into two groups.

  * In other words, the perceptron algorithm works to separate and classify the data into two groups using a linear equation. If they can be separated that way, they are considered **linearly separable**.

* Show students the following image that compares two datasets—one that is linearly separable and one that is not.

![linearly versus not-linearly separable](Images/linearly_versus_notlinearly.png)

* Point out to students that the perceptron model is a form of **supervised machine learning** because we provide the model our input features and parameters.

* The easiest way to understand how the perceptron model works is by walking through the algorithm step by step.

* Show students the following image for our perceptron example:

![perceptron dataset](Images/perceptron_dataset_1.png)

* In our example, we want to generate a perceptron classification model that can distinguish between purple squares and blue circles.

* Because our model will try to classify values in a two-dimensional space, our perceptron model will use three inputs:

  * *𝜒1*, the *x* value

  * *𝜒2*, the *y* value

  * *⍵0*, the bias constant

* The end result of our two-dimensional perceptron model is the net sum function: **⍵0 + 𝜒1⍵1 + 𝜒2⍵2**.

* Explain that, as with any untrained machine learning model, the weights and coefficients are arbitrary and oftentimes random.

* Show students the following image of an untrained perceptron model on our dataset:

![perceptron model untrained](Images/perceptron_dataset_2.png)

* Point out that the untrained model did a decent job classifying the two groups, but it is not perfect: one of the blue circles was misclassified.

* Show students the next image:

![perceptron model incorrect](Images/perceptron_dataset_3.png)

* Explain that the perceptron model will evaluate each data point and determine if the input weights should change. If a data point is classified correctly, the weights will not change. If a data point is misclassified, the weights will move the model closer to the missed data point.

* Show students the next image:

![perceptron model correct](Images/perceptron_dataset_4.png)

* As with other machine learning algorithms and models, perceptron model training continues until one of three conditions is met:

  * The perceptron model exceeds a predetermined performance threshold, determined by the designer before training. In machine learning, this is quantified by minimizing the loss metric.

    * For example, if we are working with noisy data that cannot be preprocessed or excluded, our model may not be able to exceed a certain level of performance without overfitting. Therefore, we would want to set a training cutoff at the point of model convergence.

  * The perceptron model training performs a set number of iterations, determined by the designer before training.

    * For example, if we know roughly how many iterations it takes for a model to achieve desired performance, we can just "set it and forget it" to train over a specific interval.

  * The perceptron model is stopped or encounters an error during training.

    * This will typically be a hardware or power issue, as our input data go through cleaning and preprocessing before use. If we set up our model to save itself after a specific number of training iterations, we can resume training immediately.

* Point out that a simple perceptron model is very similar to our basic statistical models. However, the power of the perceptron model comes from its ability to handle multidimensional data, as well as to interact with other perceptron models.

  * As more multidimensional perceptrons are meshed together and layered, a new, more powerful classification and regression algorithm emerges: the neural network.

</details>

<details>
  <summary><strong>📣 2.2 Instructor Do: Make the Connections in a Neural Network (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 24 - 31 to assist you to present this activity.

* Explain that the perceptron model can be thought of as a single "neuron". Now that we understand the structure of a single neuron, it is time to understand the structure of the neural network.

* Show students the following diagram of a neural network:

![neural network diagram](Images/neural_network_diagram.png)

* Explain to students that a basic neural network is composed of three layers:

  * An **input layer** of input values (transformed by weight coefficients).

  * A single **hidden layer** of neurons (single neuron or multiple neurons).

  * An **output layer** reports the classification or regression value.

* Neural networks link together neurons and produce a clear, quantitative output.

* Ask students the following rhetorical question:

  * If each neuron has its own output, how does the neural network combine each neuron's output into the model's classification or regression output?

* Neural networks use an **activation function** to transform the output of each neuron to a quantitative value. The transformed output is used as an input value for other layers in the neural network model.

* There are a variety of activation functions that can be used for many specific purposes. However, most neural networks will use one of the following activation functions:

  * The **linear function** transforms the output into the coefficients of a linear model (the equation of a line).

  * The **sigmoid function** is identified by a characteristic S curve. It transforms the output to a range between 0 and 1.

  ![sigmoid example](Images/sigmoid_example.png)

  * The **tanh function** is also identified by a characteristic S curve; however, it transforms the output to a range between –1 and 1.

  ![tanh example](Images/tanh_example.png)

  * The **rectified linear unit (ReLU) function** returns a value from 0 to infinity, so any negative input through the activation function is 0. It is the most used activation function in neural networks due to its computational simplicity and effectiveness, but it might not be appropriate for simpler models.

  ![relu example](Images/relu_example.png)

  * The **leaky ReLU** function is a "leaky" alternative to the ReLU function, whereby the negative input values will return very small, nonzero, negative values.

  ![leaky relu example](Images/leaky_relu_example.png)

* Point out that, at this point, we have looked at all of the components of a neural network model. Now it is time to explore how the components of a neural network model interact with each other.

* Be sure to answer any questions before moving to the student activity.

</details>

<details>
  <summary><strong>📣 2.3 Everyone Do: Playing in Tensorflow Playground (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 32 - 38 to assist you to present this activity.

* Explain that in this next activity we will explore all of the different components of a neural network and how each component interacts with others using a teaching application known as the **TensorFlow Playground**.

* Explain that **TensorFlow** is a neural network and machine learning library for Python that has become an industry standard for developing robust neural network models.

* TensorFlow developed its playground application as a teaching tool to "demystify the black box" of neural networks.

  * It provides a working simulation of a neural network, as it trains on a variety of different datasets and conditions.

* As an added bonus, we can also use TensorFlow Playground to test different configurations of our neural network models as an abstract form of our **model -> fit -> predict** workflow.

* Remind students that, regardless of what machine learning model or technology we use, we follow the same general modeling workflow across all of data science:

  * Decide on a model and create a model instance.

  * Split into training and testing sets and preprocess the data.

  * Train/fit the training data to the model.

  * Evaluate the model for predictions and transformations.

* As we progress through the week and experiment with different hyperparameters and configurations, encourage students to try them out ahead of time within the Playground.

* Slack out the link to the [TensorFlow Playground](https://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=gauss&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=1&seed=0.10587&showTestData=false&discretize=true&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false&discretize_hide=true&regularization_hide=true&learningRate_hide=true&regularizationRate_hide=true&percTrainData_hide=true&showTestData_hide=true&noise_hide=true&batchSize_hide=true) to students.

![TF Playground Basic Page](Images/tf_playground_1.png)

* Point out the following components of the playground:

  * The **input data** are located on the left-hand side of the page.

  ![TF Playground Input](Images/tf_playground_2.png)

  * The **input features and layer structure** are located in the "Features" section of the page. For this example, we will use *x1* and *x2* for our *x* and *y* values. We can add and subtract neurons using the plus and minus buttons above the neurons. As more neurons are added, each is responsible for keeping track of different weights.

  ![TF Playground Features](Images/tf_playground_3.png)

  * The output of the neural network is visualized in the "Output" section of the page. In the output of TensorFlow Playground, we are most concerned about the "test loss" function: the better the model performs, the lower the test loss value.

  ![TF Playground Output](Images/tf_playground_4.png)

  * The **simulation parameters** are found at the top of the page. There are many parameters to tweak and test, such as "Learning rate," "Activation," and "Regularization." However, for our purposes, we will only concentrate on the "Activation" and "Problem type" parameters.

  ![TF Playground Parameters](Images/tf_playground_5.png)

  * The **simulation controls** are found to the left of the simulation parameters, along with the **epoch counter**. Each epoch is a single training iteration in TensorFlow machine learning training. By pressing the play button, we allow the model to simulate epochs until we press stop.

  ![TF Playground Controls](Images/tf_playground_6.png)

* Once you have finished covering the different features of the TensorFlow Playground, explain to students that they are ready to start simulating their neural network models.

* Explain that, in the first simulation, we will try to classify two groups using the x1 and x2 features and one neuron.

  * Does this example sound familiar? That's because it's our previous perceptron model!

* Alongside students, run the model using the sigmoid function for roughly 100 epochs. Reassure students that they do not need to stop the training at *exactly* 100 epochs.

* Point out that the model's test loss was less than 0.01, which means that the model is capable of correctly classifying both groups with high precision.

* Ask students to rerun their models but use a different activation function.

  * Did your model training behave differently? Why or why not?

* Explain that, for the next simulation, we will change our activation function from sigmoid to tanh and train the model through 100 epochs.

* Alongside students, run the tanh simulation through 100 epochs.

* Point out that the tanh function performs even better than sigmoid in approximately the same number of iterations. Explain that, because tanh transforms the values between –1 and 1, the changes are more dramatic than sigmoid.

* For the final simulation, we'll add more neurons to the classification simulation. For this simulation, we'll add two more neurons for a total of three neurons in the hidden layer.

* Ask students to think about what will happen to our model training as we add more neurons to our model. Will training get faster? Will our model be more accurate?

* Alongside students, run the multi-neuron model until the test loss metric reaches 0.001. Ask students: Approximately how many epochs will it take?

* Point out to students that, by adding two more neurons while using the tanh function, the characteristics of the dataset are much easier to identify. In this case, we were able to achieve the same model performance of our single neuron model in roughly 33 epochs.

* **Time permitting:** Allow students an additional 5–10 minutes of "free play" to explore the functionality of the TensorFlow Playground and see what happens when they tweak different parameters.

* Be sure to answer any questions before moving on.

</details>

<details>
  <summary><strong>📣 2.4 Instructor Do: Setup Google Colab (0:15)</strong></summary>

* We understand enough basic neural network concepts to start programming our very first neural network.

* However, TensorFlow can be picky about what version of Python it works with, as well as what modules need to be installed, so we will use Google Colab to run our notebooks in the cloud.

* Navigate to [Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb). Then explain that:

  * We'll use **cloud-based notebooks** to run TensorFlow.

  * Google Colaboratory, or Colab, is Google-hosted notebooks.

  * These cloud-based notebooks allow for easy installation of Spark and the use of cloud computing power.

* Students will need a Google account to use them. If they do not have one already, encourage them to sign up for one.

* Once a Google account is set up, navigate to [Google drive](https://www.google.com/drive/) and select *Go to Google Drive*.

  ![go to google drive](ColabImages/google_go_to_google_drive.png)

* After you have navigated to Google Drive, click the "New" button and select "Folder" to create a new folder. Refer to the following screenshots. Name the folder “DataClassNotebooks.”

  ![new google folder](ColabImages/google_new.png)

* Navigate to the new folder. Once in the notebook, we’ll need to connect (download) our Google Colab application by following these steps:

  1. Click "New."
  2. Scroll down to "More" and expand the dropdown menu.
  3. At the bottom of the menu, click "Connect more apps."

  ![connect apps](ColabImages/google_add_colab.png)

  4. Type “colab” in the top-right search field and press "Enter" to search for the Colaboratory application.

  ![search colab](ColabImages/google_connect-colab.png)

  5. Click the "Connect" button to download the Colaboratory application.

* Create a Colab notebook by clicking "New" followed by "More" and then selecting "Colaboratory."

  ![launch colab notebook](ColabImages/google_create-notebook.png)

* A new tab will launch with a new notebook. The functionality is very similar to using Jupyter Notebook, except now everything is hosted online.

* Notebooks can be uploaded directly to Colab. Follow the steps to upload the [WorkThroughNN.ipynb](Activities/02-Ins_WorkThroughNN/Solved/WorkThroughNN.ipynb) file.

  1. From the Colab notebook you just opened, click "File" and then "Upload notebook."

  ![upload notebook](ColabImages/google_upload_notebook.png)

  2. Drag the [WorkThroughNN.ipynb](Activities/02-Ins_WorkThroughNN/Solved/WorkThroughNN.ipynb) file into the box to upload.

* **Note:** When you upload notebooks, the location in Google Drive will default to a folder called **Colab Notebooks**. These files can easily be moved to the PythonData folder created earlier.

</details>

<details>
  <summary><strong>📣 2.5 Instructor Do: Understanding the TensorFlow Neural Network Structure (0:15)</strong></summary>

* In Colab, run the first cell of "WorkThroughNN.ipynb" and explain that there are a number of smaller modules within the TensorFlow 2.0 library that make it even easier to build machine learning models.

* Point out that, for our purposes, we'll use the Keras module to help build our neural networks.

* Keras contains multiple classes and objects that can be combined to design a variety of neural network types.

* These classes are order-dependent, which means that depending on what Keras objects are used (and in what order), the behavior of the neural network model will change accordingly.

* For the basic neural network, we will use two Keras classes:

  * The **Sequential class** is a linear stack of neural network layers where data flow from one layer to the next. This class is what we simulated in the TensorFlow Playground.

  * The generalized **Dense class** allows us to add layers within the neural network.

* Explain that, using the Sequential model, we will add multiple dense layers that will act as our input, hidden, and output layers.

  * For each Dense layer, we'll define the number of neurons and activation functions.

* Point out that, once we have completed the Sequential model design, we will apply the same Scikit-learn **model -> fit -> predict/transform** workflow we have used previously.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Neural+Network+Basics&lessonpageTitle=Introduction+to+Advanced+Machine+Learning&lessonpageNumber=21.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F1%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      2:05  |
|---------------------------|---------------------------|

- - -

## 3. Hello Neural Network World

| Activity Time:       0:55 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Everyone Do: Work Through A Neural Network Workflow (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 43 - 53 to assist you to present this activity.

* Explain that in this activity, we will work together to build our first neural network model in TensorFlow.

* Point out that, with our basic neural network model, we will include parameters and steps that we have not previously discussed.

* Reassure students that we will review each step in detail throughout the week, such that, by the end of the unit, they will feel comfortable implementing and tweaking the neural network models on their own.

* Explain that the first step to implementing a basic neural network is to import our dependencies in Python. Open a notebook and run the following block of code.

  * **Note:** Be sure to distribute the code blocks to students, so they can code alongside your example.

```python
# Import our dependencies
import pandas as pd
import matplotlib as plt
from sklearn.datasets import make_blobs
import sklearn as skl
import tensorflow as tf
```

* Explain that the next step is to create our dummy data using Scikit-learn's *make_blobs* method. *make_blobs* is used to create values for a sample dataset. For our purposes, we'll use *make_blobs* to create 1,000 samples with two features that are linearly separable.

* Point out that our two-feature dataset is also known as our *x* and *y* values.

* Run the following code block that generates and visualizes our dummy data:

```python
# Generate dummy dataset
X, y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=78)

# Creating a DataFrame with the dummy data
df = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
df["Target"] = y

# Plotting the dummy data
df.plot.scatter(x="Feature 1", y="Feature 2", c="Target", colormap="winter")
```

![make_blobs example](Images/make_blobs_example.png)

* Explain that the next step is to separate our dataset into training and test datasets using Scikit-learn's *train_test_split* method.

* Run the following code block that splits our dummy data into training and test datasets:

```python
# Use sklearn to split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
```

* Explain that, once we have the training data, we need to prepare the dataset for our neural network model. Point out that—as with any machine learning algorithm—it is crucial to normalize or standardize our numerical variables to ensure that our neural network does not focus on outliers and can apply proper weights to each input.

* In most cases, the more that input variables are normalized to the same scale, the more stable the neural network model is, and the better the neural network model will generalize.

* Run the following code block that normalizes our dummy data:

```python
# Create scaler instance
X_scaler = skl.preprocessing.StandardScaler()

# Fit the scaler
X_scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

* Explain that, now that our dataset is preprocessed, we are ready to build the neural network in Python. To create the neural network in our notebook, run the following code block to create the Sequential model:

```python
# Create the Keras Sequential model
nn_model = tf.keras.models.Sequential()
```

* Point out that the `nn_model` object will store the entire architecture of our neural network model. Next, we must add our layers to the Sequential model.

![neural network input and hidden](Images/neural_network_in_hidden.png)

* Explain that the Keras module simplifies the process of building our layers by combining the input layer with the first hidden layer. Therefore, all we need to concentrate on are three parameters:

  * The **units** parameter indicates how many neurons we want in the hidden layer. For the first neural network, we will use one.

  * The **activation** parameter indicates which activation function to use. We’ll use the ReLU activation function to allow our hidden layer to identify and train on nonlinear relationships in the dataset.

  * The **input_dim** parameter indicates how many inputs will be in the model. In this case, we will have two.

* Run the following code block that creates the first Dense layer:

```python
# Add our first Dense layer, including the input layer
nn_model.add(tf.keras.layers.Dense(units=1, activation="relu", input_dim=2))
```

* Explain that our next step is to add the output layer. Because we are trying to build a neural network classification model, we want the activation function of the output layer to be the **sigmoid** activation function to produce a probability output.

* Run the following code block that produces the output Dense layer:

```python
# Add the output layer that uses a probability activation function
nn_model.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))
```

* Now that we have added our layers to the Sequential model, we can double-check our model structure using the summary method. Try running the following code in your notebook:

```python
# Check the structure of the Sequential model
nn_model.summary()
```

![Basic Neural Network Summary](Images/basic_nn_summary.png)

* Explain that the next step is to compile and train the model. Depending on the function of the neural network, we will need to compile and train the neural network model with a specific **loss metric**, **optimization function**, and **evaluation metric**.

* Reassure students that TensorFlow and Keras have many parameters to tweak the performance, but most basic classification and regression models use the same parameters.

* Run the following code block that compiles and trains the basic neural network model. For our purposes, understanding `binary_crossentropy` loss and the `adam` optimizer are outside the scope of this class. As a rule of thumb, whenever we make a classification neural network, we will always use a `binary_crossentropy` loss. For all of our models, we will always use the `adam` optimizer. The `metrics` parameter is used to print a performance metric at the end of each epoch so that we can judge how well the model is doing during training.

```python
# Compile the Sequential model together and customize metrics
nn_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Fit the model to the training data
fit_model = nn_model.fit(X_train_scaled, y_train, epochs=100)
```

* Point out that we now have a trained neural network model. Explain that now we have to test the performance of our neural network to ensure that our model does not need retraining.

* Run the following code block that visualizes the model's training loss over 100 epochs:

```python
# Create a DataFrame containing training history
history_df = pd.DataFrame(fit_model.history)

# Increase the index by 1 to match the number of epochs
history_df.index += 1

# Plot the loss
history_df.plot(y="loss")
```

![basic nn loss](Images/basic_nn_loss.png)

* Run the following code block that visualizes the model's predictive accuracy over the same timeframe:

```python
# Plot the accuracy
history_df.plot(y="accuracy")
```

![basic nn accuracy](Images/basic_nn_accuracy.png)

* Explain that the final step of our neural network workflow is to evaluate the performance of the trained model against the test dataset. When it comes to a classification model, we want our neural network to have a predictive accuracy as close to 100%, or 1.0.

* Run the following code that evaluates the test loss and predictive accuracy of the model on our testing dataset:

```python
# Evaluate the model using the test data
model_loss, model_accuracy = nn_model.evaluate(X_test_scaled,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
```

![basic nn performance](Images/basic_nn_performance.png)

* Point out that, by looking at the performance of our model, we can see that our trained basic neural network was able to classify every test datapoint correctly. Although perfect model performance is ideal, more complex datasets and models may not be able to achieve 100% accuracy.

* Explain that it is important to establish model performance thresholds before designing any machine learning model. Depending on the type of data and the use case, we may have to recreate and retrain a model using different parameters, different training/test data, or even look to use a different model entirely.

* Be sure to answer any questions before moving on to the next activity.

</details>

<details>
  <summary><strong>📣 3.2 Student Do: BYONNM - Build Your Own Neural Network Model (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1HJG1NEai2rDufRuJKJTBavijnfHBfyEWfFgWuXWwg3M/edit?usp=sharing) and use slides 54 and 55 to present this activity to the class.

* In this activity, students will implement their own basic classification neural network model using the TensorFlow Keras module. In addition, they will create their own dummy data, split the data into training and test sets, and normalize the data using Scikit-learn.

* **Instructions:**

  * Using the starter code provided, visualize the blobs dummy dataset using a Pandas scatter plot.

  * Randomly split the dummy data into training and test datasets using Scikit-learn's *train_test_split* method.

  * Normalize both datasets using Scikit-learn's *StandardScaler* class.

  * Create a basic neural network with five neurons in the hidden layer using the Keras module.

    * **Note:** Your neural network should use two inputs and produce one classification output.

  * Compile your basic neural network model.

  * Train the neural network model over 50 epochs.

  * Evaluate the performance of your model, printing your test loss metric and the predictive accuracy of the model on the test dataset.

  * **Bonus:**

  * Try creating a new neural network with a different number of neurons.

  * Train the new neural network model on the same training data and test the performance on the same testing dataset.

  * Create a line plot that visualizes the neural network predictive accuracy over each epoch.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: BYONNM - Build Your Own Neural Network Model (0:10)</strong></summary>

* Open [03-Stu_BYONNM/BYO_Neural_Network.ipynb](Activities/03-Stu_BYONNM/Solved/BYO_Neural_Network.ipynb) within Jupyter Notebook and go through the code line by line with the class, answering whatever questions they may have.

* Point out that the `make_blobs()` method has a new parameter that we haven't used before, `cluster_std`. This parameter allows us to change the variability in our training dataset. In this case, we increased the variability so that the datasets would overlap.

* Explain that, since the data overlap, the dataset is not (perfectly) linearly separable.

* No matter how many neurons we provide the model, the neural network will never be able to achieve 100% classification. This is due to some datapoints being indistinguishable by only *x* and *y* coordinates.

* Be sure to answer any questions before moving on.

</details>

<details>
  <summary><strong>⭐ 3.4 Instructor Do: Debrief and End Class (0:05)</strong></summary>

* Explain to students that, at this point, we should be building a neural network model capable of classifying any two groups that are linearly separable.

* Point out that, today, we have only scratched the surface of neural network model capabilities.

* In our next class, we will start to look at more complex nonlinear datasets and how to make more robust models to handle these datasets. Additionally, we will learn how to preprocess real-world data for use in a neural network model.

* Once again, encourage students to use the TensorFlow Playground to help visualize any of the features of our neural network models, especially how model performance changes as the input data becomes more complicated.

* Be sure to answer any outstanding questions before ending class.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Hello+Neural+Network+World&lessonpageTitle=Introduction+to+Advanced+Machine+Learning&lessonpageNumber=21.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F1%2FLessonPlan.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.