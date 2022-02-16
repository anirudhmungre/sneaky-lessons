# Classifying Yelp Reviews

## Instructions

* Read in the file containing Yelp reviews.

* Create a column that adds the length of the review as a feature.

* Create a list of transformations to be applied in the Pipeline:

  * Change positive and negative to an index.

  * Tokenize the review.

  * Filter out stopwords.

  * Calculate term Frequency using `HashingTF`.

  * Calculate TF-IDF.

* Create a feature vector containing the output from the IDF Model (the last stage in the pipeline) and the length.

  * Set up the pipeline and and fit it to the data.

  * Create training and testing data.

  * Create and fit the Naive Bayes model to the training data.

  * Predict outcomes using the testing set.

  * Use `MulticlassClassificationEvaluator` to evaluate the model on the testing set.
