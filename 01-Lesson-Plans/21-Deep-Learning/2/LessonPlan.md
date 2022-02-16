# 21.2 Neural Network Models in the Real World

## Overview
In this lesson, students will be introduced to deep learning networks, and go over examples that show how deep learning is a powerful technique. Deep learning is used in many advanced machine learning solutions, including meidcal image analysis, self-driving cars, and fraud detection.

## Class Objectives

By the end of this class, students will be able to:

* Implement deep neural network models using TensorFlow.

* Explain how different neural network structures change algorithm performance.

* Save trained TensorFlow models for later use.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes:</strong></summary>

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

</details>

- - -

# Class Activities

## 1. We Must Dig Deeper... Into Neural Networks

| Activity Time:       0:50 |  Elapsed Time:      0:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Everyone Do: Over the Moon on Basic Neural Networks (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1bruP3uKqrHb46wQW-ptelB5zMBK2BlPQL2Gk97h5cqs/edit?usp=sharing) and use slides 1–9 to assist you with this lesson.

* Welcome students and explain that, in today's class, we will be looking at basic neural networks in more detail. We will explore the different parameters in a Sequential TensorFlow model as well as learn how to preprocess data for a neural network model.

* By the end of this class, we will be able to apply a neural network model to any real-world tabular dataset (data stored in a table).

* Start class by returning to the [TensorFlow Playground](https://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=gauss&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=6&seed=0.16934&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false).

* Explain that yesterday we were able to build a basic neural network capable of accurately classifying a linearly separable dataset.

* Run the swirl dataset simulation for a few seconds and pause the simulation.

* Point out that, when our input data are not linearly separable, this same basic neural network model will struggle to classify our data points.

* In order for us to use more complex data (including real-world data), we will need to learn how to expand the capabilities of our neural network models.

* For our first warm-up activity, we will rebuild our basic neural network in Jupyter Notebook and apply it to a nonlinear dataset.

* Open up a new Jupyter Notebook and run this first code block to produce our **moons dummy data**, and be sure to show students the plotted dummy data:

  * **Note:** It is a good idea to slack out this code, so students may follow along in their own notebooks.

```python
# Import our dependencies
import pandas as pd
import matplotlib as plt
import sklearn as skl
import tensorflow as tf
from sklearn.datasets import make_moons

# Creating dummy nonlinear data
X_moons, y_moons = make_moons(n_samples=1000, noise=0.08, random_state=78)

# Transforming y_moons to a vertical vector
y_moons = y_moons.reshape(-1, 1)

# Creating a DataFrame to plot the nonlinear dummy data
df_moons = pd.DataFrame(X_moons, columns=["Feature 1", "Feature 2"])
df_moons["Target"] = y_moons

# Plot the nonlinear dummy data
df_moons.plot.scatter(x="Feature 1",y="Feature 2", c="Target",colormap="winter")
```

![dummy moon plot](Images/dummy_moon_plot.png)

* Point out that, similar to the swirl input data we saw in TensorFlow playground, the moons dataset (made from Scikit-learn's *make_moons* method) is not linearly separable.

* Run the next code block to rebuild the model, scale the dummy data, and create the training/test datasets:

```python
# Use sklearn to split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_moons, y_moons, random_state=78)

# Create scaler instance
X_scaler = skl.preprocessing.StandardScaler()

# Fit the scaler
X_scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Create the Keras Sequential model
nn_model = tf.keras.models.Sequential()

# Add our first Dense layer, including the input layer
nn_model.add(tf.keras.layers.Dense(units=1, activation="relu", input_dim=2))

# Add the output layer that uses a probability activation function
nn_model.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

# Check the structure of the Sequential model
nn_model.summary()
```

![moons neural net summary](Images/moon_nn_summary.png)

* Explain that, because our next steps are exactly the same as those in the last class, we must compile and train our neural network model to classify between our two moon-shaped samples that are plotted on our x-axis and y-axis.

* Run the following code block that compiles, trains, and evaluates the neural network model:

```python
# Compile the Sequential model together and customize metrics
nn_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Fit the model to the training data
fit_model = nn_model.fit(X_train_scaled, y_train, epochs=100)

# Evaluate the model using the test data
model_loss, model_accuracy = nn_model.evaluate(X_test_scaled,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
```

* Point out to students that this time the predictive accuracy of our model was not able to accurately predict more than 90% of our training data.

  * **Note:** If your model is unable to achieve a predictive accuracy of greater than 80%, try regenerating your model and retraining.

* Depending on the dataset or the use case for the model, a predictive accuracy of approximately 85% may be sufficient for a first-pass model.

  * For example, let's say we were trying to build a neural network that can predict whether students are left-handed or right-handed. A model that was able to predict correctly 85% of the time would be pretty accurate!

* Caution students that, in many industrial and medical use cases, a machine learning model must exceed 95%, or even 99%, classification accuracy. In these cases, we would not accept the basic single-neuron, single-layer model.

* Point out that one possible solution to our performance problem is to add more neurons.

* Caution students that, although adding more neurons is the most straightforward solution, it is not the most robust. Adding more neurons to a single hidden layer only boosts performance if there are subtle differences between values.

* In our dataset, our two groups are separated by drawing a complex polynomial line. Therefore, a single-layer, multiple-neuron model would still struggle to adequately classify our two groups with only two inputs.

![dummy moon separated by hand](Images/dummy_moon_separate.png)

* Explain that, in these cases, we must create a neural network model capable of identifying nonlinear, complex relationships.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Getting Deep with Deep Learning Models (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1bruP3uKqrHb46wQW-ptelB5zMBK2BlPQL2Gk97h5cqs/edit?usp=sharing) and use slides 9–14 to assist you with this lesson.

* Explain to students that, when it comes to basic neural network models, they are designed such that input values are evaluated *only once* before they are used in an output classification or regression equation.

  * Therefore, basic neural networks are limited to interpreting simple linear relationships and data with few **confounding factors**, or factors that have hidden effects on more than one variable.

* In order to address and overcome the limitations of the basic neural network, we can implement a more robust neural network model by adding more hidden layers.

* A neural network model with more than one hidden layer is known as a **deep neural network** or **deep learning model**.

* Show students the following image:

![deep learning model diagram](Images/deep_learning_model.png)

* Explain that deep learning models function similarly to the basic neural network with one major exception. The outputs of one hidden layer become the inputs to additional hidden layers of neurons.

* As a result, the next layer of neurons can evaluate higher-order interactions between weighted variables and identify complex, nonlinear relationships.

* Explain the following features of deep learning models:

  * A deep learning model can identify and account for more information than any number of neurons in any single hidden layer.

  * Deep learning models got their name from their ability to learn from example data, regardless of the complexity or data type.

  * Just like humans, deep learning models can identify patterns, determine severity, and adapt to changing input data from a wide variety of sources.

  * Although the numbers are constantly debated, many data scientists believe that even the most complex interactions can be characterized by as few as three hidden layers.

  * Deep learning models can train on images, natural language data, soundwaves, and even traditional tabular data, all with minimal preprocessing and direction.

* Explain that, just like basic neural network models, deep learning models are not a new concept. But because deep learning models are computationally intensive, they were not feasible for data science until implementation became easier with libraries like TensorFlow, and then until computing power became more affordable.

* Deep learning models typically require longer training iterations and memory resources than their basic neural network counterparts, which allow for deep learning models to achieve higher degrees of accuracy and precision.

  * In other words, deep learning models may have more upfront costs, but they also have higher performance potential.

* The easiest way to conceptualize the performance differences between basic neural network and deep learning models is to return to the TensorFlow Playground.

* Slack out the link to the [TensorFlow Playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=6&seed=0.14370&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false) to the students. Note that this link will prepopulate the simulation with:

  * The spiral dataset selected

  * One layer with six neurons

![TF Playground Deep 1](Images/tf_playground_deep_1.png)

* Point out that, in this TensorFlow Playground simulation, we will use the spiral dataset, which is nonlinearly separable.

* Explain that we will start by training our basic single-layer, six-neuron basic neural network over 1,000 epochs. Run the model through approximately 1,000 epochs in your web browser.

![TF Playground Deep 1](Images/tf_playground_deep_3.gif)

* Point out that, with only six neurons, the neural network model struggles to correctly predict the test datapoints.

* Explain that we will now add an another hidden layer with six neurons by pressing the plus (+) button next to "Hidden Layer" to add an extra layer as well as the plus button to add neurons to the second hidden layer.

![TF Playground Deep 1 Point](Images/tf_playground_deep_points.png)

* Run the new deep learning model through 1,000 epochs. Point out to  students that the deep learning model is able to reduce the test loss at a much faster rate than the basic neural network model.

![TF Playground Deep 1](Images/tf_playground_deep_4.gif)

* Explain that TensorFlow Playground shows us that the output of each neuron in the first layer is an input to each neuron in the second layer. As a result, the model is able to identify interactions between different features in more complex dimensions.

* The model is able to achieve better performance with the same input data in fewer epochs because the model has more opportunities to identify features and interactions of interest within each epoch.

* Although it may be tempting to add more and more layers to boost a deep learning model performance, there are diminishing returns. Explain the drawbacks to building a deep learning model with too many layers:

  * Deep learning models require more and more computational resources—such as memory and CPU power—for each layer. If we have limited resources or time, a larger deep learning model may be infeasible.

  * A deep learning model takes considerably more time to train than a basic neural network. Each hidden layer adds another order of magnitude and more computations.

  * The more hidden layers a model has, the more dimensions the model will consider. Therefore, a model with multiple hidden layers will require more training data to produce an adequate model.

</details>

<details>
  <summary><strong>⭐ 1.3 Students Do: Back to the Moon (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1bruP3uKqrHb46wQW-ptelB5zMBK2BlPQL2Gk97h5cqs/edit?usp=sharing) and use slides 15 and 16 to present this activity to the class.

* In this activity, students will try to build a deep learning classification model that can adequately predict the class from our moons dummy dataset.

**Instructions:**

* Upload the starter notebook to Google Colab and run the cells to recreate the moons dummy dataset.

* Create your Keras Sequential model and add **more than one** Dense hidden layer to create a deep learning model.

  * **Notes:**

  * Only your first Dense layer uses the *input_dim* parameter.

  * All of your hidden layers should use the "ReLU" activation function.

* Compile your model and train the deep learning model on at least 100 epochs.

* Evaluate the performance of your model by calculating the loss and predictive accuracy of the model on your test dataset.

* **Bonus:** If time permits, try recreating your deep learning model with a different set of hidden layers and neurons, and then evaluate the performance of your new model. Are you able to achieve 100% predictive accuracy?

</details>

<details>
  <summary><strong>📣 1.4 Review: Picking Our Brains on Neural Networks (0:10)</strong></summary>

* Open [02-Stu_BackToTheMoon/Back_To_The_Moon.ipynb](Activities/02-Stu_BackToTheMoon/Solved/Back_To_The_Moon.ipynb) within Jupyter Notebook and go through the code line by line with the class, answering whatever questions they may have. Be sure to point out the following:

  * To convert our basic neural network model to a deep learning model in Keras, we add dense layers.

  * The layers in a deep learning model do not need a large number of neurons. In this case, we only used six neurons in both hidden layers.

  * Because of the number of computations and dimensionality, deep learning models tend to require more training iterations/epochs to achieve desired performance compared with basic neural networks. In this example, our model achieved 100% predictive accuracy after roughly 150 epochs.

* Be sure to answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+We+Must+Dig+Deeper...Into+Neural+Networks&lessonpageTitle=Neural+Network+Models+in+the+Real+World&lessonpageNumber=21.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F2%2FLessonPlan.md)</sub>

- - -

## 2. Getting the Most Out of a Neural Network Model

| Activity Time:       1:00 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Getting Hands on With Model Optimization (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1bruP3uKqrHb46wQW-ptelB5zMBK2BlPQL2Gk97h5cqs/edit?usp=sharing) and use slides 18–20 to assist you with this lesson.

* As with any machine learning model, neural networks and deep learning models are not perfect.

* When it comes to model performance, there are two major pain points that we will commonly encounter:

  * A model has high variance, or the model adjusts too much to fit the training data and will not generalize well. As a reminder, this is known as **overfitting** the model.

  * A model can have high bias, or the input data are very noisy and the model is **underfitting** the data. In other words, our model struggles to classify or predict our training dataset.

* Explain that, when a model is overfit and does not meet performance expectations, it is usually due to one of two causes:

  * Training and test data are unbalanced/training data are not representative of the test data.

  * There is not enough complexity in the training data, and the model converges too quickly. (We will discuss **convergence** in detail later in the lesson.)

* Point out that, to fix a model that has high variance and is considered overfit, the most straightforward solution is to add more training data.

* There are two ways to increase our training data, each with its own pros and cons.

* The first way to increase the training data is to collect more data for your input dataset.

  * This is the safest means of increasing training data if collected properly, using the same protocol as initial data collection.

  * The problem with collecting more input data is that it may be logistically or financially impossible.

* Explain that the second means of increasing the training data is to change the training and testing data split of the original input data.

  * The benefit of this method is that no new data collection is necessary; therefore, there is no additional financial or logistical cost.

  * The con of this method is that there will be less data to use to test and validate the model. This means that there is a higher risk that we might erroneously consider an underperforming model as adequate.

* Point out that, alternatively, we can keep our training data the same and retrain the model using fewer epochs.

  * This can be a safer alternative with smaller, simpler datasets but may be ineffective for larger datasets with many features.

* Explain that, when a neural network model is considered underfit and does not meet performance expectations, it is usually because of one of two different causes:

  * Training data that contain too many outliers/confusing variables.

  * Inadequate/inappropriate model design parameters that are often referred to as **hyperparameters**.

* Point out that it is better to start by checking the training data because the process is fast and straightforward.

* Remind students how to check for outliers by running the following block of code in a Jupyter Notebook (locally or on Colab):

```python
# Dependencies
import numpy as np
import matplotlib.pyplot as plt

# Example outlier plot of reaction times
times = [96,98,100,105,85,88,95,100,101,102,97,98,5]
fig1, ax1 = plt.subplots()
ax1.set_title('Reaction Times at Baseball Batting Cage')
ax1.set_ylabel('Reaction Time (ms)')
ax1.boxplot(times)
plt.show()

# Determine which data points are outside of the 1.5*IQR range
quartiles = np.quantile(times,[.25,.75])
iqr = quartiles[1]-quartiles[0]
lower_bound = quartiles[0]-(1.5*iqr)
upper_bound = quartiles[1]+(1.5*iqr)

potential_outliers = [print(time) if time < lower_bound or time > upper_bound else next for time in times]
```

![Outliers](Images/outlier_boxplot.png)

* Explain to students that these data could represent a sample collected within a larger dataset of MLB player statistics.

* The easiest way to check for outliers is qualitatively by using a boxplot, or quantitatively by applying the **1.5*IQR** rule.

* Caution students that, while neural networks are tolerant of noisy characteristics in a dataset, neural networks can learn bad habits (like the brain does).

  * It is important that we identify variables that contain a number of potential outliers because they can affect our data preprocessing and cause more important variables and features to disappear.

* Explain that, later in this class, we will learn how to handle different types of input data and how to use preprocessing tools to maximize the effectiveness of noisy data.

* When it comes to tweaking our underfit neural network model, figuring out which hyperparameters to tweak can become overwhelming. For the purposes of this course, we will focus on higher-level hyperparameters that can be altered to achieve desired performance, such as:

  * The number of neurons in a hidden layer.

  * The number of hidden layers in a deep learning model.

  * The activation function for each hidden layer.

  * The number of epochs in the training regimen.

* Point out that we have already been tweaking and testing different hyperparameters in our neural network and deep learning models without realizing it! However, there are general rules we can apply to our hyperparameter tuning to make our models more effective.

* Remind students that there is a trade-off between computational resources and model strength when adding more neurons. Therefore, a good rule of thumb when building the initial model is to use 2–3 times as many neurons as there are input features.

  * If this does not achieve desired performance, we can always add more neurons as long as we have the computational resources.

* Explain that, similarly, we can try to boost the performance of a deep learning model by creating additional hidden layers.

* Point out that deep learning models require substantially more training iterations and memory resources with each additional hidden layer.

* Explain that, although the numbers are constantly debated, many data scientists and engineers believe that even the most complex interaction can be characterized by as few as three hidden layers. Therefore, a good starting point for deep learning model optimization is to try to limit the number of hidden layers to between two and four.

  * Depending on the size and complexity of the input data, we may need to exceed the recommended number of hidden layers.

* Explain that one of the most effective means of optimizing our neural network and deep learning models is to alter the activation functions for each hidden layer.

* Depending on the shape and dimensionality of the input data, one activation function may focus on specific characteristics of the input values, while another activation function may focus on others.

* Point out that it is important to use an activation function that matches the complexity of the input data. Each of the most popular activation functions has ideal use cases and datasets:

  * The **sigmoid function** values are normalized to a probability between 0 and 1, which is ideal for a binary classification dataset.

  * The **tanh function** can be used for classification or regression, as the normalized values range between –1 and 1.

  * The **ReLU function** is ideal for modeling positive, nonlinear input data for classification or regression. The ReLU function is always a good starting point, but not all data are positive, especially when normalized.

  * The **leaky ReLU function** is a good alternative to the ReLU function because of its ability to characterize negative input values.

* A good rule of thumb is to try selecting activation functions for your hidden layers that are slightly more complex than your output layer. Using a higher-complexity activation function will assess the input data differently without any risk of censoring or ignoring lower-complexity features.

* Explain that, if your model has still not met performance expectations, we can increase the number of training epochs.

* As the number of epochs increases, so does the amount of information provided to each neuron.

  * Each training iteration tweaks the neuron's weight coefficients; therefore, each epoch increases the likelihood that the model is utilizing effective weight coefficients.

* Caution students that adding more epochs to the training parameters is not a perfect solution: if the model produces weight coefficients that are too effective at analyzing the training data (i.e., the model is custom tailored to meet the demands of the current data), then it may not generalize well.

* Point out that, if a model only performs well on the training dataset, the model is **overfitted**.

* Explain that models should be tested and evaluated each time the number of epochs is increased to reduce the risk of overfitting.

* A good rule of thumb is to start with a smaller number of epochs (such as 100) and add more training epochs until training loss starts to decrease at a slower rate.

  * This threshold for number of epochs can vary substantially between datasets. For example, large datasets with hundreds of thousands of input values can start at 1,000 epochs (or even more!) without risk of overfitting.

* Show students the following table:

![Optimization Table](Images/optimization_table.png)

* Explain that this list of model optimization techniques is not exhaustive: there are many more nuanced and specific optimization tweaks we can perform on TensorFlow neural network models.

* Slack out links to model optimization resources that students may find useful, such as [this article that lays out 20 different techniques to optimize deep learning models](https://machinelearningmastery.com/improve-deep-learning-performance/).

</details>

<details>
  <summary><strong>📣 2.2 Instructor Do: Take the Guesswork out of Model Optimization (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1bruP3uKqrHb46wQW-ptelB5zMBK2BlPQL2Gk97h5cqs/edit?usp=sharing) and use slides 21–24 to assist you with this lesson.

* Point out that model optimization is often the most tedious and critical step in designing an effective machine learning model. When it comes to neural network models, even small changes to model hyperparameters can cause large changes to overall model performance.

* Explain that, when TensorFlow 2.0 was released, they also released libraries and tools that can automate neural network model optimization. These tools take a lot of the guesswork out of where to start with a nominal neural network and deep learning model.

* Start by uploading [Automated_NN_Optimizer.ipynb](Activities\04-Ins_AutoOptimization\Solved\Automated_NN_Optimizer.ipynb) to Google Colab.

* Run the following cell and explain that this command will install the *keras-tuner* package:

```
!pip install keras-tuner
```

* Explain that the keras-tuner package allows us to build a testing environment that evaluates a number of model configurations and returns the best performing model design and hyperparameters.

  * **Note:** This testing framework is not comprehensive, and there may be further tweaking required to achieve the desired results. However, the keras-tuner will most likely provide a "good enough" model.

* Run the following code block to import our dependencies and recreate our previous moon training/test datasets:

  * **Note:** Be sure to distribute this code to students, so they can code along with you.

```python
# Import our dependencies
import pandas as pd
import matplotlib as plt
import sklearn as skl
import tensorflow as tf
from sklearn.datasets import make_moons

# Creating dummy nonlinear data
X_moons, y_moons = make_moons(n_samples=1000, noise=0.08, random_state=78)

# Transforming y_moons to a vertical vector
y_moons = y_moons.reshape(-1, 1)

# Creating a DataFrame to plot the nonlinear dummy data
df_moons = pd.DataFrame(X_moons, columns=["Feature 1", "Feature 2"])
df_moons["Target"] = y_moons

# Use sklearn to split dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_moons, y_moons, random_state=78)

# Create scaler instance
X_scaler = skl.preprocessing.StandardScaler()

# Fit the scaler
X_scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

* Explain that we will once again use the moons dataset to try to build a deep learning model that can accurately predict the classes within the test dataset. However, this time we will allow keras-tuner to decide the hyperparameters of our model.

* Unlike our previous workflow—in which we design, compile, and train our neural network model in separate steps—a hyperparameter tuning workflow requires us to build a testing framework and let keras-tuner design, compile, and train for us.

* Point out that there are benefits and costs to using a hyperparameter tuner:

  * Once the testing framework is designed, a hyperparameter tuner will exhaustively test all possible configurations of the model hyperparameters to determine which configuration performs best. This reduces the risk of selecting inadequate hyperparameters that can severely limit the capabilities of your model.

  * Because of the exhaustive nature of hyperparameter tuners, these tools take a long time to complete. You can reduce the runtime of a tuner by reducing the possible testing options, but this will limit the overall effectiveness of the tuner.

  * If time and computing resources are not limited, you can provide the tool with a large number of hyperparameter options and training epochs to create extremely effective neural network and deep learning models.

* Reassure students that building the testing framework is very similar to building a neural network or deep learning model with two exceptions:

  * Our model design will need to be wrapped in a custom method.

  * Any hyperparameters we want to evaluate will use a special syntax.

* Run the following code block:

```python
# Create a method that creates a new Sequential model with hyperparameter options
def create_model(hp):
    nn_model = tf.keras.models.Sequential()

    # Allow keras tuner to decide which activation function to use in hidden layers
    activation = hp.Choice('activation',['relu','tanh','sigmoid'])

    # Allow keras tuner to decide number of neurons in first layer
    nn_model.add(tf.keras.layers.Dense(units=hp.Int('first_units',
        min_value=1,
        max_value=10,
        step=2), activation=activation, input_dim=2))

    # Allow keras tuner to decide number of hidden layers and neurons in hidden layers
    for i in range(hp.Int('num_layers', 1, 6)):
        nn_model.add(tf.keras.layers.Dense(units=hp.Int('units_' + str(i),
            min_value=1,
            max_value=10,
            step=2),
            activation=activation))

    nn_model.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

    # Compile the model
    nn_model.compile(loss="binary_crossentropy", optimizer='adam', metrics=["accuracy"])

    return nn_model
```

* Explain that the first step when building the tuner framework is to instantiate the Keras Sequential model. Each time our *create_model* method is called by the tuner, it will create a new model.

* The next step in our framework is to allow *keras_tuner* to select the activation function to use within the hidden layers. To create a list of hyperparameters to choose from, we will use the [choice method](https://keras-team.github.io/keras-tuner/documentation/hyperparameters/#choice-method).

  * The **choice method** requires two arguments: a reader-friendly name for the hyperparameter being tested and a list of hyperparameter options.

* Explain that, once we finish setting up the activation function test case, we need to set up our first layer. Remind students that the first Dense layer contains the input layer and first hidden layer.

* Point out that the first Dense layer will have two hyperparameters to test:

   * The activation function, which will use the activation variable.

   * The number of neurons in the first hidden layer, which will use the [int method](https://keras-team.github.io/keras-tuner/documentation/hyperparameters/#int-method) to test a range of values.

* Explain that the **int method** will test a range of possible values starting from the *min_value* to *max_value* separated by the *steps*.

  * Depending on how large a range and how wide the steps are, the **int method** can create a large number of test cases for the tuner.

  * To minimize our search space and the runtime of our tuner, we will limit the maximum number of neurons to 10 and steps to two.

* The next step in our framework is to allow keras tuner to determine how many dense layers our data require, and how many neurons will be in each layer. Both of these hyperparameters will use the int method.

* Point out that this step is very resource-intensive because it contains nested test cases. Therefore, we will limit both int methods for the sake of runtime.

  * In an ideal case, you would allow the tuner to test a large combination of layer and neuron sizes. Oftentimes, people will allow hyperparameter tuners to test a dozen or more layers and up to 100 neurons per layer.

* Point out that our final step of the framework is to add our output layer, compile the neural network model, and return the model at the end of the method.

* Explain that, now that the framework is ready, we need to import the `kerastuner` library and create our tuner class.

* Run the next line of code to create our tuner instance:

```python
# Import the kerastuner library
import kerastuner as kt

tuner = kt.Hyperband(
    create_model,
    objective="val_accuracy",
    max_epochs=20,
    hyperband_iterations=2)
```

* Point out the following features of our tuner instance:

  * The **hyperband** tuner is currently the most popular tuning algorithm in keras-tuner because of its semi-intelligent search function and early stopping capabilities. There other alternative tuning algorithms we can use, but they run longer with no substantial benefits.

  * The *objective* argument of the hyperband tuner tells keras-tuner what metric the model should try to minimize or maximize. In most cases, we want our model to maximize the analytical accuracy against the validation/testing dataset.

  * The *max_epochs* argument tells the tuner how many epochs to train the model before moving on. To maximize the (resource) cost to benefit ratio, we want to set our *max_epochs* to when our model **converges** to, or approaches, its minimum training loss. When it comes to our moons dataset, convergence will typically occur within 10–30 epochs, but convergence can happen much later in more complex datasets.

    * Generally speaking, a model is considered to be converging when the model loss metric stops decreasing between epochs or does not meet a cutoff rate.

    * Feel free to show students the following image that illustrates model convergence. We typically refer to convergence in terms of model loss rather than model accuracy.

    ![convergence example image](Images/convergence_example.png)

  * The *hyperband_iterations* argument tells keras-tuner how many times to run the testing framework. Since each iteration uses different starting points for each model, more iterations means more chances for the tuner to identify the best performing hyperparameters.

* Let the students know, for the sake of class time, we are severely limiting the search space of our hyperparameter tuner. However, if we were to use a tuner on our own models outside of class, it is in our best interest to maximize the search parameters that our time and computing resources will allow in order to increase the chance of finding the best model.

  * The parameters we should increase to maximize effectiveness should be (in order of priority) *hyperband_iterations*, *max_value* argument for each int tuner, and the *step* argument for each int tuner.

* Run the next block of code, which runs our testing framework to search for the best hyperparameters:

```python
# Run the kerastuner search for best hyperparameters
tuner.search(X_train_scaled,y_train,epochs=20,validation_data=(X_test_scaled,y_test))
```

* Depending on how many test cases, epochs, and iterations you included in the testing framework, *keras-tuner's* *search* method can take from minutes to hours to complete. Thankfully, we selected smaller test parameters, so our algorithm will only take a few minutes to complete.

  * **Note:** On most computers, this search function should complete within five minutes. Use this opportunity to answer any student questions while the search algorithm is working.

* Explain that, once the search is complete, we can look at the best performing hyperparameters as well as obtain the trained model directly!

* Run the next block of code, which stores the parameters as well as evaluates the best tuned model:

```python
# Get best model hyperparameters
best_hyper = tuner.get_best_hyperparameters(1)[0]

# Evaluate best model against full test data
best_model = tuner.get_best_models(1)[0]
model_loss, model_accuracy = best_model.evaluate(X_test_scaled,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
```

* Point out that, from our tuner, we were able to produce a model capable of accurately predicting our testing data without any direct influence.

* If the tuned model were still underperforming, we could train the model with more epochs to boost performance.

* Explain that, although hyperparameter tuning is not always ideal, it takes away much of the guesswork needed to build an adequate model from a large or difficult dataset.

</details>

<details>
  <summary><strong>⭐ 2.3 Student Do: Giving Your Model Building a Tune-Up (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1bruP3uKqrHb46wQW-ptelB5zMBK2BlPQL2Gk97h5cqs/edit?usp=sharing) and use slides 25 and 26 to present this activity to the class.

* In this activity, students will use keras-tuner to create a model that can adequately predict Scikit-learn's *make_circles* dataset.

**Instructions:**

* Run the starter code provided in Google Colab to create the circles dummy dataset.

* Convert the circles dataset to a data frame and plot the circles dataset using Pandas.

* Create a method that creates and compiles a new Sequential deep learning model with hyperparameter options. Be sure to include the following features:

  * Allow keras tuner to select between **ReLU** and **tanh** activation functions for each hidden layer.

  * Allow keras tuner to decide from 1 to 30 neurons in the first Dense layer.

    * **Note:** To limit the tuner runtime, increase your *step* argument to at least five.

  * Allow keras tuner to decide from one to five hidden layers and 1 to 30 neurons in each Dense layer.

* Import the kerastuner library and create a **hyperband** tuner instance. Your tuner instance should use the following parameters:

  * The *objective* is "val_accuracy."

  * *max_epochs* equal to 20.

  * *hyperband_iterations* equal to two.

* Run the keras tuner search for best hyperparameters over 20 epochs.

* Retrieve the top three model hyperparameters from the tuner search and print the values.

* Retrieve the top three models from the tuner search and compare their predictive accuracy against the test dataset.

</details>

<details>
  <summary><strong>📣 2.4 Review: Giving Your Model Building a Tune-Up (0:10)</strong></summary>

* Open [05-Stu_TuneUp/NN_TuneUp.ipynb](Activities/05-Stu_TuneUp/Solved/NN_TuneUp.ipynb) within Jupyter Notebook and go through the code line by line with the class, answering whatever questions they may have. Be sure to point out the following:

  * The circle dataset is another dummy dataset where our two classes are not linearly separable. The circles dataset is known for being a particularly challenging classification problem when using only the x-axis and y-axis as our input data.

  * The custom method to create a new Sequential model is very similar to what we made during the demonstration. There are only a few exceptions:

    * The hyperparameter tuner only needs to choose between "ReLU" and "tanh" activation functions.

    * Because the range of neurons is larger than our demonstration model, we needed to increase the step argument proportionately. Otherwise, the tuner will test more designs than necessary to find an acceptable model.

  * To obtain more than one set of hyperparameters and models from the tuner search, we will provide a number to the *get_best_hyperparameters* and *get_best_models* methods.

  * Point out that, across the top three model hyperparameters, there are differences between the activation function within our hidden layers, the number of hidden layers, and the number of neurons within each layer.

    * Although it is not surprising that the hyperparameters vary between each of the top models, it may be surprising how different the combination of parameters are from one another.

    * Typically, we try to stick with the most complex activation function, the ReLU activation function. But our hyperparameter tuner has demonstrated that sometimes the most complex activation function is not the best.

    * By exhaustively testing all allowable combinations of hyperparameters, the tuner allows us to find combinations of hyperparameters that may not be intuitive but are comparable in performance.

  * Once we have our set of hyperparameters and models, we can print the results using a for-loop.

* Be sure to answer any student questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Getting+the+Most+Out+of+a+Neural+Network+Model&lessonpageTitle=Neural+Network+Models+in+the+Real+World&lessonpageNumber=21.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F2%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      2:05  |
|---------------------------|---------------------------|

- - -

## 3. Using Real-World Data in Keras Neural Network Models

| Activity Time:       0:55 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>⭐ 3.1 Instructor Do: Getting Real with Neural Network Datasets (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1bruP3uKqrHb46wQW-ptelB5zMBK2BlPQL2Gk97h5cqs/edit?usp=sharing) and use slides 29–34 to assist you with this lesson.

* Explain to students that, for the last lesson of today's class, we will learn how to prepare real-world data for our neural network models.

* Point out that, when building machine learning models, most of the design effort is not writing code to build the complex model. Rather, most of the effort is preprocessing and cleaning up the input data; neural network and deep learning models are no exception to this rule.

* In reality, neural network models tend to require the most preprocessing of input data compared with all other statistical and machine learning models.

  * This is because most neural networks are really good at identifying patterns and trends in data; therefore, they are susceptible to getting stuck when looking at abstract or raw data.

* Point out that, when data have many categorical values, or large gaps between numerical values, a neural network might think that these variables are less important (or more important) than they really are.

* Explain the following example to students:

  * If a bank wanted to build a neural network model to identify if a company were eligible for a loan, it might look at factors such as a company’s net worth.

  * If the bank’s input dataset contained information from large Fortune 500 companies, such as Google and Facebook, as well as small mom-and-pop stores, the variability in net worth would be outrageous.

  * Without normalizing the input data, a neural network could look at net worth as being a strong indicator of loan eligibility, and as a result, could ignore all other factors, such as debt-to-income ratio, credit status, or requested loan amount.

  * Instead, if the net worth were normalized on a factor such as number of employees, the neural network would be more likely to weigh other factors more evenly with net worth.

  * This would result in a neural network model that assesses loan eligibility more fairly, without introducing any additional risk.

* Explain that this is an example of **preprocessing** the input data: we alter the input dataset before any computational model training or evaluation.

* Explain that, when it comes to preprocessing data for a neural network, we must first preprocess the categorical data before we preprocess the numerical data.

* Explain that we can preprocess our categorical data using the **one-hot encoding** method from Scikit-learn.

  * Remind students that one-hot encoding identifies all unique column values and splits a single categorical column into a series of columns, each containing information about a single unique categorical value.

* Show students the following table:

![eye color table](Images/eye_color_table.png)

* Ask students to consider the following "eye_color" variable containing a list of eye colors from different people.

* Show students the next table:

![eye color one-hot](Images/eye_color_onehot.png)

* Point out that this table is the exact same "eye_color" variable encoded using one-hot encoding. Each row only has one column with a value of 1—the corresponding categorical variable from the original dataset.

* Explain that this binary encoding ensures that each neuron receives the same amount of information from the categorical variable.

* Point out that, as a result, the neural network will interpret each value independently and provide each categorical value its own weight in the algorithm.

* Caution students that, although one-hot encoding is a very robust solution, it can be memory-intensive. Therefore, categorical variables with a large number of unique values (or very large variables with only a few unique values) might become difficult to navigate or filter once encoded.

* Explain that, to address the issue of memory resourcing, we must reduce the number of unique values in the categorical variables.

* Point out that the process of reducing the number of unique categorical values in a dataset is known as **bucketing** or **binning**.

* There two approaches to **bucketing** categorical data:

  * Collapse all of the infrequent and rare categorical values into a single “other” category.

  * Create generalized categorical values and reassign all data points to the new corresponding values.

* The first bucketing approach takes advantage of the fact that uncommon categories and "edge cases" are rarely statistically significant.

* Regression and classification models are unlikely to be able to use rare categorical values to produce robust models. By using the first bucketing method, the algorithm will ignore the rare events altogether and focus on more informative values.

* The second bucketing approach collapses the number of unique categorical values and maintains relative order and magnitude.

* The second approach is particularly useful when dealing with categorical variables whose distribution of unique values is relatively even.

* Explain to students that bucketing is less effective when there are only a few unique values. Therefore, a good rule of thumb is to only apply a bucketing strategy when the categorical variables contain 10 or more unique values.

* Point out that, once we encode all categorical variables using one-hot encoding, all the variables in our dataset are now numeric.

* Unlike categorical data, neural network models can interpret and evaluate all forms of numerical data.

* Caution students that, even though a neural network model *can* train on raw numerical data, it does not mean that it *should* train on raw data.

* Explain the main reasons why we should not train a neural network model on raw numerical data:

  * Raw data often has outliers or extreme values that can artificially inflate a variable’s importance.

  * Numerical data can be measured using different units across a dataset—such as time versus temperature or length versus volume.

  * The distribution of a variable can be skewed, leading to misinterpretation of the central tendency.

* Explain that the easiest way to minimize the risks associated with raw numerical data is to standardize the numerical data prior to training. In Python, we can standardize the numerical data using Scikit-learn's **StandardScaler** module.

* Point out that we have already standardized our numerical dummy data using StandardScaler in our previous activities.

* If we use the StandardScaler module to standardize our numerical variables, we reduce the overall likelihood that outliers, variables of different units, or skewed distributions will have a negative impact on a model’s performance.

* Slack out the [HR dataset](Activities/06-Ins_GettingReal/Solved/Resources/HR-Employee-Attrition.csv) as well as the following code block and run the code block in your Jupyter environment:

```python
# Import our dependencies
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
import tensorflow as tf

# Import our input dataset
attrition_df = pd.read_csv('Resources/HR-Employee-Attrition.csv')
attrition_df.head()
```

* Explain that our first real-world dataset contains a combination of categorical and numerical data for 1,400 former IBM employees. This dataset was obtained from Kaggle.

* Tell students that we are trying to build a neural network model that can predict if an employee is at risk of attrition (being fired or quitting) by training on former IBM employee metadata.

* Point out that, in order to build a proper neural network model, we must first encode the categorical data as well as standardize the numerical data.

* Slack out and run the next block of code:

```python
# Generate our categorical variable lists
attrition_cat = attrition_df.dtypes[attrition_df.dtypes == "object"].index.tolist()

# Check the number of unique values in each column
attrition_df[attrition_cat].nunique()
```

* Explain that the first step to categorical encoding is to get a list of all categorical variables in the dataset.

* Once we get our categorical variable list, we must check whether or not we need to perform any binning.

* Explain that the `nunique()` method returns the number of unique elements in the data frame, and point out that, according to its output here, there are no categorical variables that require binning.

* Slack out and run the next block of code:

```python
# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(attrition_df[attrition_cat]))

# Add the encoded variable names to the DataFrame
encode_df.columns = enc.get_feature_names(attrition_cat)
encode_df.head()
```

![HR one-hot](Images/one_hot_table.png)

* Explain that Scikit-learn's *OneHotEncoder* expects a dataset containing only categorical variables. We can use our categorical variable list to subset our raw data frame.

* Point out that Scikit-learn's *OneHotEncoder* produces an array of encoded values. In order to make our encoded data more readable, we transform the data back to a Pandas data frame.

* Slack out and run the next block of code:

```python
# Merge one-hot encoded features and drop the originals
attrition_df = attrition_df.merge(encode_df,left_index=True, right_index=True)
attrition_df = attrition_df.drop(attrition_cat,1)
attrition_df.head()
```

* Explain that our next step is to merge our encoded variables with our original numerical variables.

* Slack out and run the next block of code:

```python
# Split our preprocessed data into our features and target arrays
y = attrition_df["Attrition_Yes"].values
X = attrition_df.drop(["Attrition_Yes","Attrition_No"],1).values

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
```

* Explain that, once we have our numerical data, we need to split our input data into our model features (labeled **X**) versus our target data (**Y**). In addition, we need to split our training and test data.

* Slack out and run the next block of code:

```python
# Create a StandardScaler instance
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
```

* Explain that the next step is to standardize all of the input data using Scikit-learn's **StandardScaler** module.

* Point out that we fit the StandardScaler to only the training features. This is because we do not want our test dataset used for anything except evaluating the performance of our model. However, we still need to standardize our test data, so the trained model will not get confused.

* Explain that, now that our input data have been encoded and standardized, they are ready for our neural network model.

* Slack out and run the last block of code:

```python
# Define the model - deep neural net
number_input_features = len(X_train[0])
hidden_nodes_layer1 =  8
hidden_nodes_layer2 = 5

nn = tf.keras.models.Sequential()

# First hidden layer
nn.add(
    tf.keras.layers.Dense(units=hidden_nodes_layer1, input_dim=number_input_features, activation="relu")
)

# Second hidden layer
nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer2, activation="relu"))

# Output layer
nn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

# Check the structure of the model
nn.summary()
```

* Explain that, for our HR dataset, we will build a two-layer deep learning model.

* The final step is to compile, train, and evaluate our deep learning model on the HR dataset.

* Slack out and run the final block of code:

```python
# Compile the model
nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model
fit_model = nn.fit(X_train,y_train,epochs=100)

# Evaluate the model using the test data
model_loss, model_accuracy = nn.evaluate(X_test,y_test,verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")
```

![Preprocessing HR Final](Images/preprocessing_final.png)

* Slack out the [neural network preprocessing logic flowchart](Images/NN_Preprocess_Flowchart.pdf) and show students the image of the flowchart:

![neural network preprocessing logic flowchart image](Images/NN_Preprocess_Flowchart.png)

* Explain that we can rely on this logic workflow to help us remember what steps are needed to preprocess any real-world dataset and use it in our basic and deep learning neural networks.

* Be sure to answer any student questions before moving on.

</details>

<details>
  <summary><strong>⭐ 3.2 Student Do: Detecting Diabetes through Deep Learning (0:20)</strong></summary>

* In this activity, students will preprocess a medical dataset and create a deep learning model capable of predicting whether a patient will be diagnosed with diabetes.

**Instructions:**

* Upload the [starter notebook](Activities\07-Stu_DetectingDiabetes\Unsolved\DetectingDiabetes.ipynb) to Google Colab and run the code to import the dependencies and load the diabetes dataset.

* Separate the diabetes **Outcome** target from the other features in the dataset.

* Split the features and target into training and test datasets.

* Preprocess the input data accordingly:

  * If preprocessing categorical data, use Scikit-learn's **OneHotEncoder** module.

  * If preprocessing numerical data, use Scikit-learn's **StandardScaler** module.

* Define a deep learning model with the following features:

  * A first Dense layer with eight inputs and the "ReLU" activation function

  * A second Dense layer with at least eight neurons and the "ReLU" activation function

  * An output layer with one neuron and the "sigmoid" activation function

* Compile and train the model across no more than 100 epochs.

* Evaluate the performance of the deep learning model by calculating the test loss and predictive accuracy.

</details>

<details>
  <summary><strong>📣 3.3 Review: Detecting Diabetes Through Deep Learning (0:10)</strong></summary>

* Upload [07-Stu_DetectingDiabetes/DetectingDiabetes.ipynb](Activities/07-Stu_DetectingDiabetes/Solved/DetectingDiabetes.ipynb) to Google Colab and go through the code line by line with the class, answering whatever questions they may have. Be sure to point out the following:

  * The diabetes dataset only contains numerical data; therefore, we only need to standardize the data using Scikit-learn's **StandardScaler** module.

  * Our diabetes dataset contains a number of features across hundreds of data points; therefore, these data are more complex than any dataset we have worked with previously.

  * Due to the complexity of the dataset, a two-layer deep learning model is not going to be able to produce a adequate predictive model.

* Ask students what they can do to increase the performance of the deep learning model against the diabetes dataset. Point out the following possibilities:

  * We can add more neurons and hidden layers manually and evaluate the performance of each model change.

  * Alternatively, we can use keras tuner to search for an adequate deep learning model across multiple layers, neurons, and activation functions.

</details>
<details>
  <summary><strong>⭐ 3.4 Instructor Do: Debrief and End Class (0:05)</strong></summary>

* Use this time to allow the class to decompress and to remind students what they've learned today:

  * Deep neural network implementation using TensorFlow.
  * How different neural network structures change algorithm performance.
  * How to save a trained TensorFlow model for later use.

* Be sure to ask the students if they have any final questions and answer questions if they arise.

</details>
<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Using+Real-World+Data+in+Keras+Neural+Network+Models&lessonpageTitle=Neural+Network+Models+in+the+Real+World&lessonpageNumber=21.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F2%2FLessonPlan.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

