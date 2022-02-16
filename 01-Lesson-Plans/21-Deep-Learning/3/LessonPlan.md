# 21.3 Machine Learning Decisions and Deployment

## Overview

Today's lesson begins with a retrospective on data analysis and machine learning and finishes with deployment of a model to Amazon SageMaker.

## Class Objectives
By the end of this class, students will be able to:

* Assess the trade-offs between machine learning models.

* Choose and build an appropriate machine learning model for a given dataset and business case.

* Design an appropriate machine learning pipeline.

* Create and deploy a machine learning pipeline

## Instructor Prep

<details>
  <summary><strong>Instructor Notes:</strong></summary>

* Today's class is much more discussion-based than other classes. As much as possible, pose open-ended questions to students, encourage them to ask their own questions, and also encourage them to respond to other students' questions. Let students know that many of today's questions do not have a clear right answer. Don't be afraid of a little silence! Let students take time to think through the questions you're asking. If absolutely no one is responding, ask simpler leading questions to get students to start talking. You may also want to do a quick, light-hearted warm-up with students to get them loosened up. 

* Have your TAs refer to the [time tracker](TimeTracker.xlsx) to stay on track.

* Lastly, as a reminder, these slideshows are for instructor use only. When distributing slides to students, please first export the slides to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

| Activity time:       0:35 |  Elapsed time:      0:35  |
|---------------------------|---------------------------|


## 1. Revisiting the Great Debate

<details>
  <summary><strong> 📣 1.1 Instructor Do: Revisiting the Great Debate (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and welcome students to class. Use slides 1 - 8 to assist you with this lesson. Let students know the first half of today's class will be different than previous classes and will primarily be discussion based, starting with a thought experiment.

* On slide 6, remind students of the question asked on day 1: "Which do Americans prefer: Italian or Mexican food?" and that we'll be revisiting the question with all the newfound tools we have available to us in class.

* On slide 8, open the discussion to students asking them which steps could benefit from Machine Learning. If students need some prompting, here are some ideas:

  * Decompose the ask.
    * Clustering algorithms could help us define specifics in the question, like what “counts” as an Italian restaurant.
  * Identify data sources.
    * Using a web scraper, we could automatically collect potential data sources and rank them by how often they are mentioned in data science blogs
  * Build a data retrieval plan/retrieve the data/assemble and clean.
    * We could build a pipeline to automatically retrieve and clean the data.
    * Point out that the predictions of a machine learning model applied to the data it’s trained on can act as a form of “noise removal.”
  * Analyze for trends.
    * Instead of using machine learning models to predict, we can also use them to analyze data.
  * Acknowledge limitations/make the call or tell the story.
    * These steps still rely on the machine learning practitioner. Even if parts of these steps can be automated, it’s best to have an actual person responsible for the final call.

</details>

<details>
  <summary><strong> ✏️ 1.2 Groups Do: The Great Debate Revisited (0:15)</strong></summary>

  * Open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slide 9 to present this activity to the class.

  * Have students break into groups and devise new strategies to answer the question: "Which do Americans prefer: Italian or Mexican food?". Encourage them to come up with unconventional approaches. Let them know that at the end of the 20 minutes, each group will share their approach with the whole class, and the whole class will collaborate to see how different approaches could be combined.

  * After 15 minutes have passed, let students know that they have five more minutes and that they should choose who will represent the group and share their strategy.


</details>

<details>
  <summary><strong> ⭐ 1.3 Review Activity (0:15) </strong></summary>

  * ⏰**Three-Hour Adjustment**: Reduce activity time to 10 minutes.

  * Have each group present their new approach to the whole class. After all the groups have presented, open the discussion to the whole class. What approaches do they like? What strategies could be combined? What pitfalls would we expect to run into?

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Revisiting+the+Great+Debate&lessonpageTitle=Machine+Learning+Decisions+and+Deployment&lessonpageNumber=21.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F3%2FLessonPlan.md)</sub>

- - -


## 2. Preference Predictor

| Activity time:       0:50 |  Elapsed time:      1:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 2.1 Instructor Do: A Better Question for Machine Learning (0:05) </strong></summary>

* Continue to [slide 13](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit#slide=id.gbe22de1969_0_6901) and tell students that for the next activity, we'll tweak the question from the previous activity to focus on something even better solved by Machine Learning. On the next slide, introduce the second thought experiment: training a model for a take-home interview assignment to predict a Yelp user's average rating of Italian restaurants, with the following assumptions:

  * The model must use data from the Yelp dataset.

  * You have one week to work on the assignment (the interviewers expect you to spend around 10 hours on it).

  * You may use external libraries, but you will have to explain how they work at a high level.

  * Be prepared to explain how your model works to interviewers of varying technical backgrounds.

* On slide 16, point out that there is a very real data set we'll be basing our analysis on, but it is over 6 GB compressed, so instead of writing any code or downloading the data, we're going to make a hypothetical plan and rely on the data description from Yelp to guide how we will approach the data. Open [the link to the Yelp dataset documentation](https://www.yelp.com/dataset/documentation/main) and distribute it to students.

</details>

<details>
  <summary><strong> ✏️ 2.2 Groups Do: Preference Predictor (0:15) </strong></summary>

* ⏰**Three-Hour Adjustment**: If today's class occurs on a weekday, make this an everyone do and open up a class-wide discussion, and reduce to 10 minutes.

* Open the slideshow and use [slide 18](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit#slide=id.gbe22de1969_0_8579) to present this activity to the class.

* Have students return to their groups and brainstorm how to create a machine learning model that predicts a Yelp user's average rating of Italian restaurants. 

* Check in with each group early on in the process. Students may gravitate toward solutions that include natural language processing. Use this as an opportunity to let them know we will be covering some NLP in the next week with big data. Challenge them to find solutions that do not rely on NLP.

</details>

<details>
  <summary><strong> ⭐ 2.3 Review Activity (0:15) </strong></summary>

* ⏰**Three-Hour Adjustment**: If today's class occurs on a weekday, skip this activity

* Once again, have each group present their proposed model to the whole class. After all the groups have presented, open the discussion to the whole class.

</details>

<details>
  <summary><strong> ⭐ 2.4 Everyone Do: Preference Predictor Critique (0:15) </strong></summary>

* ⏰**Three-Hour Adjustment**: If today's class occurs on a weekday, reduce activity time to 10 minutes.

* Move on to [slide 21](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit#slide=id.gbe22de1969_0_8602) and let students know we will now be critiquing code as a class that tries to solve this problem. 

* Now, in our thought experiment, we will be assuming the role of the interviewer, evaluating the submission of an interviewee.

* Open [YelpModel.html](Activities/02-Evr_PredictingPreference/Solved/YelpModel.html) and distribute the file to students. Point out that this is a saved copy of the original notebook in an HTML file, not a live notebook that we can run.

* Give students a few minutes to familiarize themselves with the code. Let them know that, if they see unfamiliar code, that is to be expected and they shouldn't get hung up on it for now. Every coder uses different tricks and conventions. The goal here is to try to understand their approach.

* After students have familiarized themselves with the submission, open up a discussion. What do they think of this approach? What about it do they like? What do they think could have been done better? Do they agree with the results? What questions would they like to ask the interviewee if they bring them back for another round of interviews?

* Some notable points you might want to bring up:

  * The neural network has no hidden layers, no activation layer on the output, and uses MSE for its loss. This is just a fancy way of making a linear regression. Would it be more beneficial to just use a linear regression here?

  * The model deals with missing data by just putting the middle value of three stars for every value. Would it make more sense to get each individual reviewer's average for the imputed value?

  * The analysis doesn't have much explanation of why certain methods were chosen, or why certain values were chosen. For instance, why are we limiting to users with five reviews of Italian restaurants? Why not three? Why not 10?

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Preference+Predictor&lessonpageTitle=Machine+Learning+Decisions+and+Deployment&lessonpageNumber=21.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F3%2FLessonPlan.md)</sub>

- - -

## BREAK

| Activity time:       0:40 |  Elapsed time:      2:05  |
|---------------------------|---------------------------|

- - -

## 3. Amazon SageMaker Introduction and Setup

| Activity time:       0:35 |  Elapsed time:      2:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 3.1 Instructor Do: Introduce Amazon SageMaker (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slides 23 - 27 to introduce Amazon SageMaker to the class.

* Go to [slide 24](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit#slide=id.gbe22de1969_0_8913) and let students know that the rest of the session will be about how to deploy machine learning models. 

* Up until now, all the models we've created run within a Jupyter Notebook.

* If we want to share the functionality of our models with other people (or other programs), we need to deploy them. 

* One way would we could do this is to build an API from scratch using Flask, but that takes quite a bit of work, and still needs to be hosted on a server somewhere.

* Today, we will be using Amazon SageMaker, which is built to streamline the process of training and deploying models.

 </details>

<details>
  <summary><strong> 📣 3.2 Instructor Do: Creating an Administrator User on IAM (0:10)</strong></summary>

In this activity, students will learn how to create an `administrator` user using AWS Identity and Access Management (IAM) service. This user will add some extra security for the user when working on AWS.

Explain to students that a standard best practice is to avoid using the principal, or _root_, user to manage their AWS account. This principal user is the one they used to create their AWS account. Instead, a new user for each person that requires administrator access should be created using the AWS Identity and Access Management (IAM) service.


* You may open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slides 28 - 34 to assist you to show the class the process of creating an Administrator user on IAM. 

* Open the [AWS Management Console](https://console.aws.amazon.com) using your _root_ user, and show students how to create a new user on IAM as follows.

* Look for the IAM service on the "Find Services" search box, type `iam` and click on `IAM` service.

  ![Create an administrator IAM user - Step 1](Images/iam-user-1.png)

* In the left pane menu, choose the "Users" option and click on the "Add user" button.

  ![Create an administrator IAM user - Step 2](Images/iam-user-2.png)

* On the "Add user" page, provide your new user name in the "User name" input box, then fill out the details of the new `administrator` by filling in the selections as seen below.  Afterward, click on the "Next: Permissions" button to continue.

  * **User name:** `administrator`
  * **Access type:** Select the "Programmatic access" and "AWS Management Console access" boxes.
  * **Console password:** Choose "Custom password" and type your password.
  * **Require password reset:** Unselect this box.

  ![Create an administrator IAM user - Step 3](Images/iam-user-3.png)

* On the "Set permissions" page, choose "Add user to group" and click on the "Create group" button.

  ![Create an administrator IAM user - Step 4](Images/iam-user-4.png)

* In the "Create group" dialog box, type `Administrators` in the "Group name" textbox.

* Choose "Filter policies" and then choose "AWS managed - job function" to filter the table contents.

  ![Create an administrator IAM user - Step 5](Images/iam-user-5.png)

* In the policy list, select the checkbox for "AdministratorAccess" and then choose the "Create group" button.

  ![Create an administrator IAM user - Step 6](Images/iam-user-6.png)

* After creating the group, select the checkbox for your new group. Choose "Refresh" if necessary to see the group on the list.

  ![Create an administrator IAM user - Step 7](Images/iam-user-7.png)

* Click on the "Next: Tags" button to continue.

* On the "Next: Tags" page, leave the defaults and click on the "Next: Review" button to continue.

  ![Create an administrator IAM user - Step 8](Images/iam-user-8.png)

* Review the list of group memberships to be added to the new user. When you are ready to proceed, click on the "Create user" button.

  ![Create an administrator IAM user - Step 9](Images/iam-user-9.png)

* Once the user is created, download the user's credentials by clicking on the "Download .csv" button. Keep those credentials safe.

  ![Create an administrator IAM user - Step 10](Images/iam-user-10.png)

Enable access to billing data for the IAM admin user as follows:

* On the navigation bar, choose your account name, and then select "My Account."

  ![Create an administrator IAM user - Step 11](Images/iam-user-11.png)

* Scroll down to the "IAM User and Role Access to Billing Information" section and click on the "Edit" option.

  ![Create an administrator IAM user - Step 12](Images/iam-user-12.png)

* Select the checkbox to "Activate IAM Access" and choose "Update."

  ![Create an administrator IAM user - Step 13](Images/iam-user-13.png)

Sign out from your session, open the `CSV` file with the new `administrator` user credentials and log in to the AWS Management Console using the user's URL and password. Tell students that, from now on, they should avoid using their _root user_ and work with this new admin user instead.

Answer any questions before moving on.

</details>

<details>
  <summary><strong> ✏️ 3.3 Students Do: Creating an Admin user on IAM (0:10) </strong></summary>

In this activity, students will create an administrator user to manage their AWS account.

* You may open [slide 35](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit#slide=id.gbe53dc55c6_0_135) to present this activity to the class. In case you might find necessary to show case the instructions, you may use slides 29 -32.

**Instructions:**

* [README.md](Activities/01-Stu_IAM_User/README.md)

</details>

<details>
  <summary><strong> 📣 3.4 Instructor Do: Review Creating an Admin User on IAM (0:10)</strong></summary>

  This review activity is intended to verify that all students have successfully created their admin user using IAM.

  Make sure that all students have their AWS account working correctly. Also, ask TAs to assist students who might have an issue before moving forward. Forthcoming activities will use the `administrator` IAM user by default.

  Answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Amazon+SageMaker+Intro+and+Setup&lessonpageTitle=Machine+Learning+Decisions+and+Deployment&lessonpageNumber=21.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F3%2FLessonPlan.md)</sub>

- - -


## 4. Amazon SageMaker Notebooks

| Activity time:       1:00 |  Elapsed time:      3:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong> ✏️ 4.1 Everyone Do: Create an Amazon SageMaker Notebook Instance (0:20)</strong></summary>

In this activity, students will learn how to create an instance of Amazon SageMaker and how to use Jupyter Notebooks on the AWS cloud. 

* You may open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slides 37 - 40 to assist you with this lesson. Note that the GUI on the Amazon SageMaker Notebook Instance creation will look slightly different in comparison to the images below. However, the information at its core will suffice. In case you need up to date guidance, slides 38 - 40 are up to date with the AWS GUI.   

**Files:**

* [YelpModelToDeploy.ipynb](Activities/03-Evr_SageMaker/Solved/YelpModelToDeploy.ipynb)

* [test_restaurant.json](Activities/03-Evr_SageMaker/Solved/test_restaurant.json)

* [test_review.json](Activities/03-Evr_SageMaker/Solved/test_review.json)

* [test_user.json](Activities/03-Evr_SageMaker/Solved/test_user.json)

* [business_clusters.json](Activities/03-Evr_SageMaker/Solved/business_clusters.json)

* [yelp_model.h5](Activities/03-Evr_SageMaker/Solved/yelp_model.h5)

Comment to students that you will demonstrate how to create an Amazon SageMaker Notebook instance and ask them to follow your steps as you move along the demo. Ask TAs to assist students if they get stuck along the process.

Log in to your AWS Management Console using your admin user and tell students that the first component that Amazon SageMaker requires is an [Amazon S3](https://aws.amazon.com/s3) bucket to store data to feed machine learning models or to save prediction results.

To create an Amazon S3 bucket, follow the next steps:

* On the "Find Services" search box, type `S3` and select the "S3" service from the list.

  ![Creating an Amazon SageMaker instance - step 1](Images/sagemaker-1.png)

* On the Amazon S3 console, click on the "Create bucket" button.

  ![Creating an Amazon SageMaker instance - step 2](Images/sagemaker-2.png)

* Fill in the following details on the "Create button" window:

  * **Section: Name and region**
    * _Bucket name:_ `sagemaker-<CURRENT-DATE+TIME>` (for example: `sagemaker-20190903-1026`)
    * _Region:_ `US West (Oregon)` (S3 and SageMaker instance regions should be the same)
    * _Click:_ "Next"
    ![Creating an Amazon SageMaker instance - step 3](Images/sagemaker-3.png)
  * **Section: Configure options**
    * _Click:_ "Next" (leave defaults)
    ![Creating an Amazon SageMaker instance - step 4](Images/sagemaker-4.png)
  * **Section: Set permissions**
    * _Click:_ "Next" (leave defaults)
    ![Creating an Amazon SageMaker instance - step 5](Images/sagemaker-5.png)
  * **Section: Review**
    * _Click:_ "Create bucket"
    ![Creating an Amazon SageMaker instance - step 6](Images/sagemaker-6.png)

* Note down (copy/paste/save) the name of the bucket for use in the following section.

Explain to students that the next step is to create a Jupyter Notebook instance on Amazon SageMaker. Follow the next steps:

* Navigate to the "AWS Management Console" homepage. In the "Find Services" search box, type "sagemaker" and select "Amazon SageMaker" from the list.

  ![Creating an Amazon SageMaker instance - step 7](Images/sagemaker-7.png)

* On the Amazon SageMaker console, be sure that `Oregon` is the selected region, on the left pane menu. Under the "Notebook" section, choose "Notebook instances."

  ![Creating an Amazon SageMaker instance - step 8](Images/sagemaker-8.png)

* On the "Notebook instances" page, click on the "Create notebook instance" button.

  ![Creating an Amazon SageMaker instance - step 9](Images/sagemaker-9.png)

* Fill in the following values on the "Create notebook instance" page:

  * **Section: Notebook instance settings**
    * _Notebook instance name:_ `sm-test`
    * _Notebook instance type:_ `ml.t2.medium`
    * _Elastic inference:_ `none`
    ![Creating an Amazon SageMaker instance - step 10](Images/sagemaker-10.png)
  * **Section: Permissions and encryption**
    * _IAM role:_ On the dropdown list, select the `Create a new role` option.
    ![Creating an Amazon SageMaker instance - step 11](Images/sagemaker-11.png)
    * Under the "S3 buckets you specify - _optional_" section, choose "Specific S3 buckets" and type the name of the Amazon S3 bucket you created in the preceding section (e.g., `sagemaker-20190903-1026`). Click on "Create role" to continue.
    ![Creating an Amazon SageMaker instance - step 12](Images/sagemaker-12.png)
    * _Root access:_ Be sure that the `Enable - Give users root access to the notebook` option is selected. Tell students that this option is less safe but allows more control over the instance.
    ![Creating an Amazon SageMaker instance - step 13](Images/sagemaker-13.png)

* Scroll down and click on the "Create notebook instance" button to continue. Comment to students that the creation process takes up to five minutes to finish.

  ![Creating an Amazon SageMaker instance - step 14](Images/sagemaker-14.png)

While the notebook instance is being created, explain to students that AWS charges for these and most resources as they are created, even when not in use. This instance is billed for by the second until it's turned off and deleted. Students will learn how to eliminate these resources later in today's class.

Explain to students that, as long as the free tier is used, there are no charges associated with today's activities. However, if any of the students use an account that is more than two months old, the tasks performed today using Amazon SageMaker may have an associated cost.

* Once the notebook instance status is "InService," it's ready to be used. In the "Actions" column, click on `Open Jupyter` to continue.

  ![Creating an Amazon SageMaker instance - step 15](Images/sagemaker-15.png)

* After a few seconds, you will see the Jupyter Notebook interface. Comment to students that this notebook is running on the AWS cloud.

* In the "New" dropdown, select the `conda_python3` environment to create a new notebook.

  ![Creating an Amazon SageMaker instance - step 16](Images/sagemaker-16.png)

* On the new notebook, code a `hello world` statement in Python in the first cell as a test. Be sure that all of the class has reached this point before moving forward.

  ![Creating an Amazon SageMaker instance - step 17](Images/sagemaker-17.png)

Explain to students that it's possible to code a Jupyter Notebook from scratch on this Amazon SageMaker's notebook instance, but also that you can open an existing Jupyter Notebook. Distribute the files in the [Solved](Activities/03-Evr_SageMaker/Solved] folder to students and continue the demo as follows:

* In your Amazon SageMaker notebook instance, on the upper right, click on the "Upload" button and select all five files in the [Solved](Activities/03-Evr_SageMaker/Solved] folder to upload.

  ![Creating an Amazon SageMaker instance - step 18](Images/sagemaker-18.png)

* Open the `YelpModelToDeploy.ipynb` notebook. You'll probably see the message `Select Kernel` or `Kernel not found`. Select `conda_tenserflow_p36` and click on `Select` or `Set Kernel` to continue.

* Run all the cells in the notebook, comment to students that now this notebook is running on the AWS cloud using Amazon SageMaker.

End the demo and answer any questions before moving on.

</details>

<details>
  <summary><strong> ✏️ 4.2 Everyone Do: Create and Deploy a Machine Learning Model in Amazon SageMaker (0:30)</strong></summary>

* ⏰**Three-Hour Adjustment**: If today's class occurs on a weekday, reduce activity time to 25 minutes.

**Corresponding Activity:** [04-Evr_SageMaker_Deployment](Activities/04-Evr_SageMaker_Deployment)

In this activity, students will learn how to create, train, deploy, and evaluate a machine learning model in Amazon SageMaker.

This is a collaborative activity where you will lead the class through the whole process. Be sure to keep the pace, allowing students to follow you. Ask TAs to assist any students who may be stuck during the activity.

 * You may open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slides 41 and 42 to present this collective activity to the class. 

**Files:**

* [rainfall_forecast.ipynb](Activities/04-Evr_SageMaker_Deployment/Unsolved/rainfall_forecast.ipynb)

* [x_austin_final.csv](Activities/04-Evr_SageMaker_Deployment/Resources/x_austin_final.csv)

* [y_austin_final.csv](Activities/04-Evr_SageMaker_Deployment/Resources/y_austin_final.csv)

Explain to students that Amazon has created an extensive library of machine learning models that are optimized for the cloud. This demo will show how to use one of those models.

Tell students that, in this demo, you are going to demonstrate one of Amazon's linear regression models to predict the amount of rain that will fall in Austin, given the average temperature in Fahrenheit degrees.

Slack out the unsolved version of the Jupyter Notebook and the two data files to students. Ask the class to follow you on this demo.

Start the demo by opening the Jupyter lab UI at your Amazon SageMaker instance and create a new folder called `Data`.

![Deploy SageMaker Model - step 1](Images/deploy-sagemaker-1.png)

Open the `Data` folder, upload the following `CSV` files and highlight the following:

* `x_austin_final.csv`: This file contains historical weather conditions in Austin, Texas, along 1,319 days.

* `y_austin_final.cvs`: This file contains the precipitations sum in inches in Austin, Texas, along 1,319 days.

![Deploy SageMaker Model - step 2](Images/deploy-sagemaker-2.png)

Navigate to the main folder on Jupyter lab and import the unsolved version of the Jupyter Notebook to your Amazon SageMaker notebook instance. Live code the demo by highlighting the following:

* In the `Initial imports` section, some well-known libraries are imported. The `sklearn` library will be used to split the dataset in training and testing sets, as well as to evaluate the model.

  ```python
  import os
  import io
  import json
  import numpy as np
  import pandas as pd
  from path import Path
  import matplotlib.pyplot as plt
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import mean_squared_error, r2_score
  ```

* To use Amazon SageMaker, the following libraries are needed:

  ```python
  import sagemaker
  import sagemaker.amazon.common as smac
  from sagemaker.predictor import csv_serializer, json_deserializer
  from sagemaker import get_execution_role
  from sagemaker.amazon.amazon_estimator import get_image_uri
  import boto3
  ```

* Along with the `sagemaker` modules, the `boto3` library is imported. `boto3` is the [AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

* The data to train and test the model are loaded into two Pandas data frames. Next, the data are transformed into a vector as follows:

  * The `x_austin_final.csv` data are loaded into the `features` data frame, and the `TempAvgF` column that denotes the average temperature in Austin in Fahrenheit degrees is taken as an input variable (predictor) for the linear model.

    ```python
    # Read the weather features data
    file_path = Path("Data/x_austin_final.csv")
    features = pd.read_csv(file_path)

    # Transforming the "TempAvgF" column to a vector
    X = features["TempAvgF"].values.reshape(-1, 1)
    ```

  * The `y_austin_final.csv` data are initially loaded into the `y` data frame; these data represent the target variable in the linear model.

    ```python
    # Read the target data (precipitation sum inches)
    file_path = Path("Data/y_austin_final.csv")
    y = pd.read_csv(file_path, names=["PrecipitationSumInches"], header=None)

    # Transforming y into a vector
    y = y.iloc[:, 0].values
    ```

* The data are split into training and testing datasets using the `train_test_split()` function from `sklearn`.

  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  ```

Comment to students that, once the data are loaded, the next step is to create the linear regression model. The process starts with some initial configurations as follows:

* The training and testing data should be stored in an Amazon S3 bucket, so a variable to store the name of the bucket we created before is defined.

  ```python
  bucket = "sagemaker-bucket-name-here"
  ```

* To identify the data files stored in Amazon S3, a prefix is defined.

  ```python
  prefix = "austin-rainfall-regression"
  ```

* The current role of the IAM user running the notebook is stored in the `role` variable.

  ```python
  role = get_execution_role()
  ```

Now it's time to upload the data to Amazon S3. Explain to students that, to train the machine learning model using Amazon SageMaker, the training and testing data should pass through an Amazon S3 bucket formatted using the [protobuf recordIO format](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html#td-serialization).

* The protobuf recordIO format is a method to serialize structured data (similar to `JSON`) to allow different applications to communicate with each other or for storing data.

Explain to students that using the protobuf recordIO format allows you to take advantage of _Pipe mode_ when training the algorithms that support it. In _Pipe mode_, your training job streams data directly from Amazon S3. Streaming can provide faster start times for training jobs and better throughput.

Continue with the following code to format the training data as a protobuf recordIO, and then upload it to the Amazon S3 bucket:

```python
# Encode the training data as Protocol Buffer
buf = io.BytesIO()
vectors = np.array(X_train).astype("float32")
labels = np.array(y_train).astype("float32")
smac.write_numpy_to_dense_tensor(buf, vectors, labels)
buf.seek(0)

# Upload encoded training data to Amazon S3
key = 'linear_train.data'
boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "train", key)).upload_fileobj(buf)
s3_train_data = "s3://{}/{}/train/{}".format(bucket, prefix, key)
print("Training data uploaded to: {}".format(s3_train_data))
```

Tell students that, if you provide test data, the algorithm logs include the test score for the final model. Live code the following to upload the testing data:

```python
# Encode the testing data as Protocol Buffer
buf = io.BytesIO()
vectors = np.array(X_test).astype("float32")
labels = np.array(y_test).astype("float32")
smac.write_numpy_to_dense_tensor(buf, vectors, labels)
buf.seek(0)

# Upload encoded testing data to Amazon S3
key = "linear_test.data"
boto3.resource("s3").Bucket(bucket).Object(os.path.join(prefix, "test", key)).upload_fileobj(buf)
s3_test_data = "s3://{}/{}/test/{}".format(bucket, prefix, key)
print("Testing data uploaded to: {}".format(s3_test_data))
```

Once you have uploaded your data to Amazon S3, it's time to train the machine learning model. Comment to students that, in this demo, you will use Amazon SageMaker's [_linear learner algorithm_](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) to run a linear regression prediction model.

Create the instance of the linear learner algorithm and highlight the following:

* The instance of the `linear learner` is created using the `get_image_uri()` method from the `sagemaker` library.

  ```python
  container = get_image_uri(boto3.Session().region_name, "linear-learner")
  ```

* Before creating the estimator container, an Amazon SageMaker session should be started.

  ```python
  sess = sagemaker.Session()
  ```

* The estimator container is an AWS EC2 instance that will store and run the model. The estimator container is created using a `ml.m4.xlarge` instance type for training the model.

  ```python
  linear = sagemaker.estimator.Estimator(
    container,
    role,
    train_instance_count=1,
    train_instance_type="ml.m4.xlarge",
    output_path="s3://{}/{}/output".format(bucket, prefix),
    sagemaker_session=sess
    )
  ```

* The linear learner hyperparameters are defined next. It's important to highlight that the `feature_dim` parameter should match with the number of predictors in `X`. In this case, since we only have one predictor, its value is `1`.

  ```python
  # Define linear learner hyperparameters
  linear.set_hyperparameters(
    feature_dim=1,
    mini_batch_size=100,
    predictor_type="regressor",
    epochs=10,
    num_models=32,
    loss="absolute_loss"
    )
  ```

* The model is trained using the `fit` method of the Amazon SageMaker estimator. **Note:** This step might take a few minutes.

  ```python
  linear.fit({'train': s3_train_data, 'test': s3_test_data})
  ```

Explain to students that this step might take a few minutes, and it will use resources from the AWS account. Typically, this time is not billed in the two-month trial period. However, clarify to students that policies of the AWS free and trial offer changes regularly, so they should always check the pricing pages for any service that they want to use. Below, a sample output is shown. You will notice that the output text is in blue.

**Important note:** Explain to students that this step may take up to 15 minutes since Amazon SageMaker is provisioning not only a Jupyter Notebook, but also a series of virtual machines (EC2 instances) to compute the model. If you are running out of time in this activity, open the solved version of the notebook and continue the demo by dry-walking through the code.

![Deploy SageMaker Model - step 3](Images/deploy-sagemaker-3.gif)

Once the `linear-learner` model is trained, tell students that it can be deployed to make predictions of the rainfall in Austin. Continue the demo and highlight the following:

* In order to make predictions, the model should be deployed. A `ml.t2.medium` instance type is defined since this is the instance type we selected when we created the notebook that is part of the free-tier offer.

  ```python
  linear_predictor = linear.deploy(initial_instance_count=1, instance_type="ml.t2.medium")
  ```

* Some configurations should be made to specify the type of data files that are going to be used and to define how the data are going to be serialized and deserialized.

  ```python
  linear_predictor.serializer = csv_serializer
  linear_predictor.deserializer = json_deserializer
  ```

* To make predictions, we use the `predict()` method of the model. We will make predictions using the testing data. Results are stored in the `y_predictions` array.

  ```python
  result = linear_predictor.predict(X_test)
  y_predictions = np.array([r["score"] for r in result["predictions"]])
  ```

Explain to students that, once you have the predictions, the model can be evaluated using the techniques they already know. First, a plot to contrast the predicted rainfall values versus the real values is created.

![Deploy SageMaker Model - step 4](Images/deploy-sagemaker-4.png)

Additionally, the `RMSE` and `R2` scores are calculated.

![Deploy SageMaker Model - step 5](Images/deploy-sagemaker-5.png)

Finally, after reviewing the model evaluation's results, explain to students that the endpoint needs to be deleted to avoid additional AWS resource usage and extra billing.

```python
sagemaker.Session().delete_endpoint(linear_predictor.endpoint)
```

Slack out the following page to students, where they can learn more about the different Amazon SageMaker built-in algorithms:

* [Use Amazon SageMaker Built-in Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).

Answer any questions before moving on.

</details>

<details>
  <summary><strong> 📣 4.3 Instructor Do: Pros and Cons of Deploying Machine Learning Models with Amazon SageMaker  (0:10)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slides 43 - 45 to lead and facilitate a discussion around deploying models in Amazon SageMaker and why a RESTful ML API is useful.

Have students share their opinions with the class and bring up the following points:

**Pros:**

* Data storage capacity: By using an Amazon S3 bucket to store the data, we could have trained a model on multiple terabytes of data, or a lot more space than would otherwise have fit in our personal computer.

* Hardware/GPU: By using different Amazon SageMaker instances to train our model, we can access compute power, including GPU capabilities, making powerful hardware available to us as required.

* Cost: Using AWS resources, we only pay for what we use. We'll turn off everything before ending the class and not incur further charges.

* Availability: By deploying our model to another Amazon SageMaker instance, we have made the prediction functionality available 24/7 through a secured endpoint to an application or to be consumed by others without having to make our computer available.

* RESTful API: As learned in previous units, APIs provide a standard mechanism to access data. Our ML API can be consumed through apps and other channels in a simple form while remaining secure and allowing other constraints (e.g., authentication, authorization, rate limiting, etc.).

**Cons:**

* Data privacy/security: By uploading data to a third party, you are trusting your data to them. Certain kinds of data are subject to compliance and regulatory constraints.

* Visibility: You won't have oversight on AWS internal handling of your data and infrastructure.

* Availability: Although there are SLAs in place, AWS (and any other cloud providers) can and have suffered outages at times, causing data unavailability.

Answer any questions before moving on.

</details>

---

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Amazon+SageMaker+Notebooks&lessonpageTitle=Machine+Learning+Decisions+and+Deployment&lessonpageNumber=21.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F3%2FLessonPlan.md)</sub>

## 5. SageMaker Clean-Up

| Activity time:       0:20 |  Elapsed time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong> 📣 5.1 Instructor Do: Delete Notebook Instance (0:10)</strong></summary> 

In this activity, students will learn how to delete their Amazon SageMaker notebook instance so that no billing charges are incurred for it after class.


* You may open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slides 46 and 47 to assist you with this lesson.

Open the Amazon SageMaker console then, on the left pane menu. Under the "Notebook" section, click on "Notebook instances."

![Deleting Amazon SageMaker instance - 1](Images/deleting-sm-1.png)

Select the `sm-test` notebook instance on the left by clicking the circular dot. Once selected, click on the right "Actions" menu and select "Stop."

![Deleting Amazon SageMaker instance - 2](Images/deleting-sm-2.png)

Refresh the page and wait for the instance `Status` to change to `Stopped`. **Note:** This process will take a few minutes.

![Deleting Amazon SageMaker instance - 3](Images/deleting-sm-3.png)

Select the instance again on the left circular dot. Click on "Actions," select "Delete," and then confirm the delete.

![Notebook Instance delete](Images/notebook-confirm-delete.png)

* At the end of today's lesson, the notebook instances list should be empty and state, "There are currently no resources." Otherwise, charges will be incurred for any remaining active instances.

Lastly, go to the Amazon S3 console and remove the buckets created for the activity as follows:

* Choose the checkbox next to the bucket name and click on the "Delete" button.

![Deleting Amazon SageMaker instance - 4](Images/deleting-sm-4.png)

* On the "Delete bucket" window, type the name of the bucket to confirm that you want to delete it. Next, click on the "Confirm" button to finish.

![Deleting Amazon SageMaker instance - 5](Images/deleting-sm-5.png)

Answer any questions before moving on.

</details>

<details>
  <summary><strong> ✏️ 5.2 Everyone Do: Delete AWS Resources (0:10)</strong></summary>

In this activity, students will delete all the AWS resources created in today's class to avoid additional charges.

* You may open the [slideshow](https://docs.google.com/presentation/d/13WCDpwCzIcdTu7BKHDBQvvBRmwCxbWn5n6pdP_gLRQk/edit?usp=sharing) and use slides 48 and 49 to assist you with this lesson.

Explain to students, as it was mentioned before, the policies for the AWS free tier and trials continually change. Hence, it's essential to remove any unnecessary resources created on AWS to avoid additional charges, especially Amazon SageMaker instances, since regardless when they are stopped, AWS bills you for hosting the instances.

Follow [these clean-up steps](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html) on AWS and collaborate with TAs to assist students in deleting all the AWS resources that students need to remove. Make sure students remove ALL of the following:

* Endpoint
* Endpoint configuration
* Model
* Notebook instance

Remind students, that they can save a local copy of the Jupyter notebooks, by right-clicking on the notebook name and selecting the _Download_ option.

![Downloading a Jupyter Notebook](Images/download-notebook-sm.png)

Answer any questions before finishing class.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+SageMaker+Clean-up&lessonpageTitle=Machine+Learning+Decisions+and+Deployment&lessonpageNumber=21.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F21-Deep-Learning%2F3%2FLessonPlan.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
