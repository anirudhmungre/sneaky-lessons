# 3.3: A Deeper Dive Into Python 

## Overview

In today's class, students will explore other Python capabilities that will be used throughout the course. Then, at the end of class, students will learn to use Git from the command line.

## Class Objectives

By the end of this lesson, the students will be able to:

* Create and use Python dictionaries.

* Read in data from a dictionary.

* Use list comprehensions.

* Write and reuse Python functions.

* Use coding logic and reasoning.

* Add, commit, and push code to GitHub from the command line.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. If so, we have provided notes within the lesson plan that will allow you to **easily adjust the length of the lesson to fit into a weekday class**.

  * Keep track of any **3-Hour Adjustment** notes at the top of the activities in this lesson plan. If this class is being taught on a weekday, please use the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class, as well.

  * Reducing activity time could prevent students from finishing, so please remind them to use office hours to clear up any questions that they may have.

* The first part of today's class will continue with Python, starting with a warm-up exercise and then moving onto dictionaries, list comprehensions, and functions.

* Some students may still be struggling with the pace of class or the Python concepts we’re covering. Ensure that TAs are circulating and aiding students who need support. If class is ahead of schedule, students may have extra time for additional problems or reviews of class material.

* The final part of today’s class will cover Github and Git from the command line. Make sure that students are comfortable creating repos and adding, committing, and pushing files to GitHub. From this point in the course, students will interact with GitHub via the command line; they will continue to submit homework to the Bootcamp Spot.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-03-python) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Lastly, as a reminder, these slideshows are **for instructor use only**. When distributing slides to students, please first export the slides to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

## 1. Welcome & Cereal Cleaner

| Activity Time:       0:30 |  Elapsed Time:      0:30  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Students (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1YOpt-Om0fwLTOkCmhfkTG4q6kq_DjO4tzHKNYzd_dnw/edit?usp=sharing), and use the first few slides to help welcome students.

* Welcome students to class, and let them know that today's class will explore more Python capabilities. The class will then finish with more Git and Github&mdash;in particular, how to use the command line to add and commit files. 

</details>

<details>
  <summary><strong>✏️ 1.2 Students Do: Cereal Cleaner (0:20)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Students Do** activity, and continue on to the **Review** activity.

* Continue through the slideshow, using the next slides as an accompaniment to this activity. **NOTE:** If a 3-hour adjustment is **observed**, please skip the appropriate slides, and continue on to the Review activity. 

* To start today's class, students will be creating an application that reads in cereal data from a CSV and then prints only those cereals that contain 5 or more grams of fiber.

* Open [01-CerealCleaner](Activities/01-Stu_CerealCleaner/Solved/cereal_bonus_solved.py) within the terminal, and run and discuss the code to give students an idea of the application’s end results, which are captured in the following image:

  ![Cereal Cleaner Output](Images/01-CerealCleaner_Output.png)

* Then, send out the following files and instructions:

* **Files**

  * [cereal.csv](Activities/01-Stu_CerealCleaner/Resources/cereal.csv)

  * [cereal_bonus.csv](Activities/01-Stu_CerealCleaner/Resources/cereal_bonus.csv)

* **Instructions**

* Open the file, `cereal.csv` and start by skipping the header row. See hints below for this.

* Read through the remaining rows and find the cereals that contain five grams of fiber or more, printing the data from those rows to the terminal.



* **Hints**

  * Every value within the CSV is stored as a string, and certain values have a decimal. This means that they will have to be cast to be used.

  * `csv.reader` begins reading the CSV file from the first row. `next(csv_reader, None)` will skip the header row.

  * Refer to this Stack Overflow post on [how to skip the header](https://stackoverflow.com/a/14257599) for more information.

  * Integers are whole numbers and, as such, cannot contain decimals. Decimal numbers will have to be cast as a `float`.

* **Bonus**

  * Try the activity again, but this time use `cereal_bonus.csv`, which does not include a header.

* Data Source: Crawford, C. (2017, October 24). 80 cereals. [https://www.kaggle.com/crawford/80-cereals](https://www.kaggle.com/crawford/80-cereals), originally sourced from [http://lib.stat.cmu.edu/datasets/1993.expo/](http://lib.stat.cmu.edu/datasets/1993.expo/)

</details>

<details>
  <summary><strong>⭐ 1.3 Review: Cereal Cleaner (0:05)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 15 minutes on this activity.

  * Use this review section as guidance for talking points as you live-code along with the students.

  * Take your time, and answer all student questions along the way.

* Open and share the file [cereal_solved.py](Activities/01-Stu_CerealCleaner/Solved/cereal_solved.py), and go through the code with the class, answering any questions students may have.

* Cover the following key points when discussing this activity:

  * First, we import the dependencies before doing anything else in the code. This will help keep the code clean and make it easier to read and understand in the future.

  * Point out how the variable `cereal_csv` is named in a self-explanatory way; this will help ensure that future developers, including those who originally wrote this application, know precisely what this variable references.

  * The same is true of `csv_reader`, which is used to hold the data that is read in from the CSV file.

  * As captured in the following image, the `next()` function is placed before the `for` loop to skip over the first row of data&mdash;the header.

    ![Cereal Cleaner Output](Images/01-CerealCleaner_Code.png)

  * To check through all of the rows in the CSV file and find the cereals that contain 5 or more grams of fiber, a `for` loop containing an `if` statement is used.

  * Looking through the CSV file, we would find that the `fiber` data is stored within the eighth column; therefore, the `if` statement must check values stored at index 7.

* Check with the class to see what methods they used to come up with their solutions, or any alternate methods they can think of, before moving on to the next activity.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+%26+Cereal+Cleaner&lessonpageTitle=Python+Deeper+Dive&lessonpageNumber=3.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F3%2FLessonPlan.md)</sub>

- - -

## 2. Hobby Book

| Activity Time:       0:25 |  Elapsed Time:      0:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Dictionaries (0:05)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic.

* Note that another commonly used data type in Python is the dictionary, or `dict`.

* Explain that a dictionary is an object that stores a collection of data.

  * Like lists and tuples, dictionaries can contain multiple values and data types.

  * However, unlike lists and tuples, dictionaries store data in key-value pairs. The key in a dictionary is a string that can be referenced to collect an associated value.

  * To use the example of a physical dictionary, the words in the dictionary would be considered the keys, and the definitions of those words would be the values.

* Open and share [dictionaries.py](Activities/02-Ins_Dicts/Solved/dictionaries.py), and explain the code contained within. Make sure to cover the following points:

  * To initialize or create an empty dictionary, we use the syntax `actors = {}`.

    ``` python
    # Create a dictionary to hold the actor's names.
    actors = {}
    ```

  * You can also create a dictionary with the built-in Python `dict()` function, or `actors = dict()`.

    ``` python
    # Create a dictionary using the built-in function.
    actors = dict()
    ```

  * Values can be added to dictionaries at declaration by creating a key that is stored in a string, following it with a colon, and then placing the desired value after the colon.

  * To reference a value within a dictionary, we simply call the dictionary and follow it up with a pair of brackets containing the key for the desired value, as in the following image:

    ![basic dictionary](Images/02-Dictionary_OneValue.png)

  * As in the following image, values can also be added to dictionaries by placing the key within single or double quotation marks inside brackets, and then assigning the key a value; then, values can be changed or overwritten by assigning the key a new value.

    ![add value dictionary](Images/02-Dictionary_AddValue.png)

  * Dictionaries can hold multiple pieces of information by following up each key-value pairing with a comma and then another key-value pair.

    * Keys are immutable objects, like integers, floating-point decimals, or strings. Keys cannot be lists or any other type of mutable object.

    * Values in a dictionary, as captured in the following image, can be objects of any type: integers, floating-point decimals, strings, Booleans, `datetime` values, and lists.

      ![add value dictionary](Images/02-Dictionary_Lists.png)

  * Items in a list in a dictionary can be accessed by calling the key and then using indexing to access the item, as in the following image. Assure students that they only need a basic understanding of this for now; when they get into APIs, they will get a lot more practice!

    ![access list items dictionary](Images/02-Dictionary_ListIndexing.png)

  * Dictionaries can also contain other dictionaries. To access the values inside nested dictionaries, simply add another key to the reference, as in the following image:

    ![Advanced Dictionaries](Images/02-Dictionary_MultiValue.png)

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Hobby Book:  Dictionaries (0:15)</strong></summary>

* ⏰ **3-Hour Adjustment**: Reduce activity time from 15 minutes to 10 minutes.

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Let students know that they will be creating and accessing dictionaries that are based on their own hobbies.

* Open up [03-HobbyBook](Activities/03-Stu_HobbyBook-Dictionaries/Solved/HobbyBook_Solved.py) within the terminal, and run and discuss the code to give students an idea of the application’s end results, as captured in the following image:

  ![Hobby-Book Solved](Images/03-HobbyBook_Output.png)

* Then, send out the following instructions:

* **Instructions:**

  * Create a dictionary to store the following information:

    * Your name
    * Your age
    * A list of a few of your hobbies
    * A dictionary that includes a few days and the time you typically wake up on those days

  * Print out your name, how many hobbies you have, and a time you wake up during the week.

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Hobby Book (0:05)</strong></summary>

* Open and share [03-HobbyBook](Activities/03-Stu_HobbyBook-Dictionaries/Solved/HobbyBook_Solved.py), then go through the code, making sure to explain the following points:

  * A variable called `my_info` stores the primary dictionary, as noted by the curly braces.

  * The keys are "name", "occupation", "age", "hobbies", and "wake-up"; their corresponding values are stored after the colons, with each new key-value pair separated by a comma.

  * To find the number of values stored within the "hobbies" key, the `len()` function is used, as captured in the following image:

    ![Hobby-Book Solved](Images/03-HobbyBook_Code.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Hobby+Book&lessonpageTitle=Python+Deeper+Dive&lessonpageNumber=3.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F3%2FLessonPlan.md)</sub>

- - -

## 3. List Comprehensions

| Activity Time:       0:30 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: List Comprehensions (0:10)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic.

* Explain that we will be covering a powerful feature of Python called **list comprehensions**.

* Remind students that we’ve used `for` loops to iterate through a list and perform an action for each element.

  * For example, we might individually print out each of a user's favorite foods.

* Open [comprehensions.py](Activities/04-Evr_List_Comprehensions/Solved/comprehensions.py), and begin live-coding. Guide students through the different aspects of the code as you go.

* Break down the example with the `fish` variable.

  ```python
  fish = "halibut"

  # Loop through each letter in the string
  # and push to an array
  letters = []
  for letter in fish:
      letters.append(letter)

  print(letters)

  # List comprehensions provide concise syntax for creating lists
  letters = [letter for letter in fish]

  print(letters)

  # We can manipulate each element as we go
  capital_letters = []
  for letter in fish:
      capital_letters.append(letter.upper())

  print(capital_letters)

  # List Comprehension for the above
  capital_letters = [letter.upper() for letter in fish]

  print(capital_letters)
  ```

  * Explain that we can use list comprehension to treat `fish` like an array and turn it into a list of its constituent letters

  * Note that we can then use this list to create a new list of capitalized letters by using a comprehension and calling `upper` on each letter.

* Finally, guide the students through the temperature example.

  ```python
  # We can also add conditional logic (if statements) to a list comprehension
  july_temperatures = [87, 85, 92, 79, 106]
  hot_days = []
  for temperature in july_temperatures:
      if temperature > 90:
          hot_days.append(temperature)
  print(hot_days)

  # List Comprehension with conditional
  hot_days = [temperature for temperature in july_temperatures if temperature > 90]

  print(hot_days)
  ```

  * Explain that in addition to changing data, we can also filter it.

  * Note that adding conditional logic, like `if` statements, to a list comprehension allows us to select a certain value or range of values.

  * Emphasize that this example is just intended to provide exposure to the flexibility and power of list comprehensions.

* Take a moment to answer any remaining questions before sending out the example files.

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: List Comprehensions (0:10)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* In this activity, students will use list comprehensions to compose a wedding invitation, which they will send to every name on a mailing list.

* Send out the starter file [comprehensions.py](Activities/05-Stu_List_Comprehensions/Unsolved/comprehensions.py) and following instructions:

* **Instructions**:

  * Open the file called `comprehensions.py`.

  * Create a list that prompts the user for the names of five people that they know.

  * Run the provided program. Note that nothing forces you to write the name properly in title case&mdash;for example, as "Jane" instead of "jAnE". You will use list comprehensions to fix this.

    * First, use list comprehensions to create a new list that contains the lowercase versions of the names your user provided.

    * Then, use list comprehensions to create a new list that contains the title-case versions of each of the names in your lowercase list.

  * **Hint**

    * Check out the documentation for the [title](https://docs.python.org/3/library/stdtypes.html#str.title) method.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: List Comprehensions (0:10)</strong></summary>

* Open and send the solution [comprehensions.py](Activities/05-Stu_List_Comprehensions/Solved/comprehensions.py).

* Explain that the first code block simply declares a list in which to store names and then collects five names from the user.

* Ask a student to explain how to generate a list of lowercase names.

  * Explain that we can use a list comprehension that calls `lower` on each name in the list.

* Ask a student to explain how to generate a list of title-case names.

  * Explain that we can use a list comprehension that calls `title` on each name in the list.

* Ask a student to explain how to build the greeting for each cleaned string.

  * Explain that we can insert each name in `title case` into a format string.

  * Note that if we wanted to build a more complicated string, we would have to use a function, which we'll cover later in today's lesson.

* Finally, explain that we simply use a `for` loop to print every invitation in the `invitations` list.

  * Note that we use a `for` loop instead of a list comprehension because we are _not_ using `title case` to create a new list&mdash;rather, we are simply performing an action for each item in `title case`.

* Take a moment to answer any remaining questions before sending out the solution and moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+List+Comprehensions&lessonpageTitle=Python+Deeper+Dive&lessonpageNumber=3.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F3%2FLessonPlan.md)</sub>

- - -

## 4. Functions

| Activity Time:       0:30 |  Elapsed Time:      1:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Functions (0:15)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic.

* **File**:

  * [functions.py](Activities/06-Evr_Functions/Solved/functions.py)

* Remind students of the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) concept to students and that we can use functions and modules to avoid repeating code.

  * Ask a student or the class if there are any disadvantages to writing code that does the same thing in three different places.

  * Explain that if we write the same code in different places and expect it to behave the same everywhere, we will also have to update it in several places whenever we make a change.

  * Point out that this can quickly become unwieldy: In large codebases, copying code in multiple places would often require us to waste time making the _same_ change in several places. It would _also_ add the overhead of tracking duplicated code.

  * Note that efficiency is the motivation for the **d**on't **r**epeat **y**ourself mantra.

* Live-code and guide students through the different function examples in `functions.py`.

* Explain the basic anatomy of a function:

  ```python
  def name(parameters):
    # code goes here
    return
  ```

  * In the next example, note that we use the keyword `def` to define a function, that `show` is the name of the function, and that the parentheses that follow also indicate that `show` is a function. Make sure to also note the colon at the end of the line.

  * Run the function in the console as a demonstration.

  ```python
  # Simple Function with no parameters
  def show():
    print(f"Hi!")

  # you use parentheses to run the code in a function
  show()
  ```

* Remind students that functions allow us to give a name to a set of instructions that we want to be able to repeat.

* Point out that we use block indentation for the function body.

* Explain that we can pass data to a function through parameters and arguments.

* Guide students through this code:

  ```python
   def show(message):
     print(message)
  ```

  * Explain that `message` is the data that we give the function, and the function will _do_ something with that data.

  * Explain that we **defined** the function but did not **run** it, in much the same way that having the blueprint of a house is not the same thing as living inside one.

  * Explain that we actually **run** the function with the following code:
    ```python
    show("Hello, World!")
    ```
  * Note that “calling” a function is a synonym for running it. So, when we say we call a function, it simply means that we are running, or executing, it.

* Ask a student to articulate the relationship between `message` (in the function declaration) and "Hello, World!" (in the function call).

  * Explain that a **parameter** is the name of a variable in a function, while an **argument** is the value that you pass to the parameter.

* Explain that parameters let us run that set of instructions on _different_ inputs, which allows us to get different outputs.

* Tell the students that creating a function is like creating a recipe: the arguments are like the ingredients of a recipe, and the body of the function is like the instructions of a recipe. Use the analogy of a “recipe” for quesadillas for the following example. Discuss and demonstrate the `make_quesadilla()` function in the code. Parts of the recipe are _always_ the same (they are the "function body"), but we can choose to make the recipe with either chicken _or_ beef (our "arguments").

  * Warn the students that arguments are positional, and position matters! `make_quesadilla("sour cream", "beef")` will return `"Here is a sour cream quesadilla with beef"`.

* Explain that we can make parameters optional if we specify a default parameter. Go over the following code to make this point:

  ```python
  def make_quesadilla(protein, topping="sour cream"):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)
  ```

  * Note that `topping="sour cream"` makes "sour cream" our default `topping`. That is, if no topping is specified as an argument when the function is called, the function will supply "sour cream" as the `topping`. Demonstrate what happens when we call the `make_quesadilla` function without a `topping` as an argument:

    * `make_quesadilla("chicken")`

  * Then, demonstrate what happens when the function is called with a specific `topping` argument:

    * `make_quesadilla("beef", "guacamole")`

* Explain that we can return data with the return statement:

  ```python
  def square(number):
    return number * number
  ```

  * Ask a student to explain the features of this function.

  * Point out that we often calculate values inside of functions.

  * Note that to get that value back when the function is done, we use the `return` keyword. In this case, it returns the `squared value`.

* Explain that we can save the returned value. Run, or have a student explain, the following line of code:

  ```python
  squared = square(2)
  print(squared)
  ```

* Explain that we can also print the return value of a function.

  ```python
  print(square(2))
  print(square(3))
  ```

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Functions (0:10)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Send out the following file and instructions:

* **File**:

  * [Unsolved/main.py](Activities/07-Stu_Functions/Unsolved/main.py)

* **Instructions**:

  * Write a function called `average` that accepts a list of numbers as a single argument.

    * The function `average` should return the arithmetic [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) (average) for a list of numbers.

  * Test your function by calling it with different values and printing the results.

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Functions (0:05)</strong></summary>

* Open and share [Solved/main.py](Activities/07-Stu_Functions/Solved/main.py), then guide students through the solution.

* Explain that we define a function called `average` that accepts a single parameter called **numbers**.

* Point out that we can define variables inside of the function body if they are only going to be used inside of the function. For example, `length = len(numbers)` is defined inside the `average` function, and would not be referenced outside of the function. If it was, an error would occur stating "name 'length' is not defined".

* Note that we could have created another variable called `average` and returned that variable, but we can actually just return the results from `sum / length`.

  * Explain that `sum / length` is evaluated first, and then that value is returned.

* Explain that we want to test our code by calling the function with test data and printing the results.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Functions&lessonpageTitle=Python+Deeper+Dive&lessonpageNumber=3.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F3%2FLessonPlan.md)</sub>

- - -

## 5. Graduating Functions

| Activity Time:       0:20 |  Elapsed Time:      2:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>👥 5.1 Partners Do: Graduating Functions (0:15)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Partners Do** activity, and continue on to the Review activity.

* Continue through the slideshow, using the next slides as an accompaniment to this activity. **NOTE:** If a 3-hour adjustment is **observed**, please skip the appropriate slides, and continue on to the Review activity. 

* For this activity, students will create a function that searches a list of students and graduates by state to determine state graduation rates for public, private nonprofit, and private for-profit institutions. 

* Open [08-Par_GraduatingFunctions/graduation_functions.py](Activities/08-Par_GraduatingFunctions/Solved/graduation_functions.py) and run the application to give students an idea how their application should function, as captured in the following image:

![Graduating Functions](Images/13-GraduatingFunctions_Run.png)

* Send out the following files and instructions.

* **Files:**

  * [08-Par_GraduatingFunctions/graduation_functions.py](Activities/08-Par_GraduatingFunctions/Unsolved/graduation_functions.py)

  * [graduation_data.csv](Activities/08-Par_GraduatingFunctions/Resources/graduation_data.csv)

* **Instructions:**

  * Analyze the code and CSV file provided to determine what needs to be added to the application.

  * Using the starter code provided, create a function called `print_percentages` that takes in a parameter called `state_data` and does the following actions:

    * The function uses the data stored within `state_data` to calculate the estimated graduation rates for each category of Title IV 4-year institutions (public, nonprofit private, and for-profit private).

    * The function prints out the graduation rates for each school type for the state to the terminal.

  Note: Some states do not have nonprofit or for-profit private schools, so data must be checked for zeros.

* **Bonus:**

  * Within the same `print_percentages()` function, calculate the overall graduation rate. Then, create a conditional that checks a state's overall graduation rate and prints "Graduation success" if the number was higher than 50 or "State needs improvement" if the number was lower than 50.

* Data Source: U.S. Department of Education, National Center for Education Statistics, IPEDS, Winter 2012-13, Graduation Rates component (final data). [https://nces.ed.gov/datalab/table/library/detail/12572](https://nces.ed.gov/datalab/table/library/detail/12572)
</details>

<details>
  <summary><strong>⭐ 5.2 Review: Graduating Functions (0:05)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 10 minutes on this activity.

  * Use the Review section as guidance for talking points as you live-code along with the students.

  * Take your time, and answer all student questions along the way.

* Open and send out the file [08-Par_GraduatingFunctions/graduation_functions.py](Activities/08-Par_GraduatingFunctions/Solved/graduation_functions.py) from the previous activity, and go over the code line by line with the class, answering any questions that they may have.

* Cover the following key points for this activity:

  * First, checking the CSV data helps us figure out how to calculate the total number of students who enrolled and the total number who graduated. It would also help students identify what each index in a row referred to.

  * Even though `row` is the variable being passed into the function, `state_data` is still used within the function itself. The data within `row` is essentially moved into `state_data` for use within the function.

  ```python
  def print_percentages(state_data):
    # For readability, it can help to assign your values to variables with descriptive names
    # CSV headers: State or jurisdiction, Adjusted cohort (Public), Completers (Public),
    # Adjusted cohort (Nonprofit Private), Completers (Nonprofit Private), 
    # Adjusted cohort (For-profit Private), Completers (For-profit Private)
    state = str(state_data[0])
    public_students = int(state_data[1])
    public_graduates = int(state_data[2])
    nonprofit_students = int(state_data[3])
    nonprofit_graduates = int(state_data[4])
    forprofit_students = int(state_data[5])
    forprofit_graduates = int(state_data[6])

    # Total students can be found by adding students of each category together
    total_students = public_students + nonprofit_students + forprofit_students
    # Total graduates can be found by adding graduates of each category together
    total_graduates = public_graduates + nonprofit_graduates + forprofit_graduates

    # Public grad rate can be found by dividing the total public graduates by the total public 
    # students and multiplying by 100
    public_grad_rate = (public_graduates / public_students) * 100
  ```

  * Some states do not have nonprofit or for-profit private schools. Therefore, we must check if those corresponding values are 0 to avoid producing a divide-by-zero error.
  
  ```python
    # Nonprofit grad rate can be found by dividing the total nonprofit graduates by the total nonprofit 
    # students and multiplying by 100
    if nonprofit_students == 0:
        nonprofit_grad_rate = 0
    else:
        nonprofit_grad_rate = (nonprofit_graduates / nonprofit_students) * 100

    # Forprofit grad rate can be found by dividing the total forprofit graduates by the total forprofit 
    # students and multiplying by 100
    if forprofit_students == 0:
        forprofit_grad_rate = 0
    else:
        forprofit_grad_rate = (forprofit_graduates / forprofit_students) * 100

    # Calculate the overall graduation rate
    overall_grad_rate = (total_graduates / total_students) * 100

    # If the overall graduation rate is over 50, message is "Graduation success". 
    # Otherwise it is "State needs improvement".
    if overall_grad_rate > 50:
        message = "Graduation success"
    else:
        message = "State needs improvement"

    # Print out the state's name and their graduation rates
    print(f"Stats for {state}")
    print(f"Public School Graduation Rate: {str(public_grad_rate)}")
    print(f"Private Non-Profit School Graduation Rate: {str(nonprofit_grad_rate)}")
    print(f"Private For-Profit School Graduation Rate: {str(forprofit_grad_rate)}")
    print(f"Overall Graduation Rate: {str(overall_grad_rate)}")
    print(f"{message}")
  ```

    * Explain that `header = next(reader)` will read the header row from the CSV file.


</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Wrestling+With+Functions&lessonpageTitle=Python+Deeper+Dive&lessonpageNumber=3.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F3%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      2:55  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Reduce break time from 40 minutes to 15 minutes.

- - -

## 6. Git & Command Line

| Activity Time:       1:00 |  Elapsed Time:      3:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 6.1 Instructor Do: Intro to Git (0:25)</strong></summary>

* Explain to the students that so far, we have used GitHub as a sort of “drop box” to store our files. Although this is one way to use GitHub, it has much deeper capabilities. Today, we will delve into Git and how to use it through the terminal to interact with GitHub.

* **Note**: If teaching with VS Code, consider using the [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) extension to demonstrate this section's concepts.

* Continue the slideshow to facilitate discussion of the next topic.

  * Explain that Git is essentially a way for us to keep track of our work over time. Whenever we get another piece of a project working, we can save the change with Git.

  * Note that this "save" is called a **commit**. It represents a checkpoint for our project where we save and describe our work, as in the following image:

![A commit is a lot like a changelog note](https://cdn-images-1.medium.com/max/1600/1*zj-d8TopjgBml2QVM-672w.jpeg)

* Emphasize that if we break something while working on our code, this system allows us to restore working code from earlier.

* Note that since Git remembers these checkpoints, we can work on several different concerns all at once. 

* Provide the following example:

  * Suppose we need to analyze Uber ride data for a project.

  * Explain that we might decide to analyze the average age of riders. Git essentially allows us to write this code and save it with the name `age analysis`.

* Emphasize that this code is _different_ from the code we started with and that it lives separately from it.

  * Explain that in this scenario, we have a version of the code called `main`, which is the main version of our code; we also have a version called `age analysis`, which contains updates.

* Note that each version of the code lives on a different **branch**.

  * Explain that a **branch** is essentially a history of changes.

  * Note that in this case, we say that the `age analysis` branch **diverged** from the `main` branch.

  * Take a moment to demonstrate the difference between the files on the `age_analysis` and `main` branches.

* Explain that saving the age analysis code in a different branch gives our teammates a chance to review it for errors and offer suggestions.

* After the proposed change has been reviewed, we can update the `main` branch to include the changes in `age analysis` by doing a **merge**.

* Explain that **merging** two branches combines them into one branch.

* Explain that this is how we can work on new features or bug fixes without making changes to working code.

  * Note that this also makes working with teammates easier, as people can avoid stepping on each others' toes by working on different branches.

* Finally, review Git's **snapshot model**. Slack out the link to _Pro Git_ (a book of GitHub documentation) where this is discussed: [“Getting Started - What is Git?”](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F). 

  * A commit in GitHub is like a snapshot of what your project or file looks like at a particular moment in time.

  * If a file doesn’t contain any changes, the file is not stored again; instead, Git provides a link to the identical file that it previously stored. 

  * According to the documentation, “Git thinks about its data more like a stream of snapshots.”

 * Highlight the images (available at the previous link) that capture the Git snapshot model, which differentiate between changed and unchanged files.

</details>

<details>
  <summary><strong>🎉 6.2 Everyone Do: Adding Files from the Command Line (0:10)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Tell students that so far, they have only added files using the GitHub website, which works well enough when just dealing with one or two files. What happens when we need to quickly add multiple files?

  * The command line comes to the rescue!

* Have students follow along with creating a repo and adding files with Terminal/Git Bash.

  * First, create a new repo.

  * From the repo page, click the green box in the top-right labeled "Clone or download", select "Use SSH", and copy the link to the clipboard, as captured in the following GIF:

  ![clone repo](Images/GitClone.gif)

  * Open Terminal (or Git Bash for Windows users), and navigate to the home folder using `cd ~`.

  * Type `git clone <repository link>` in the terminal to clone the repo to the current directory. Once this code has run, everyone should find a folder with the same name as the repo, as captured in the following image:

    ![terminal clone](Images/GitClone_command.png)

  * Open the folder in VS Code, and create two python script files, named `script01.py` and `script02.py`.

  * Then, open Terminal/Git Bash, and navigate to the repo folder. Run the following lines, explaining each line as you go.

  ```bash
  # Displays that status of files in the folder
  git status

  # Adds all the files into a staging area
  git add .

  # Check that the files were added correctly
  git status

  # Commits all the files to your repo and adds a message
  git commit -m <add commit message here>

  # Pushes the changes up to GitHub
  git push origin main
  ```

  * Finally, navigate to the repo on [Github.com](https://github.com/) to confirm that the changes have been pushed up.

* Make sure every student was able to successfully clone a repo, add files to the repo, commit the changes, and then push the changes to GitHub, all from the command line.

* Using slide 45, discuss the "main" branch and how it was previously referred to as the "master" branch. 

</details>

<details>
  <summary><strong>✏️ 6.3 Students Do: Adding More to the Repo (0:15)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Students Do** activity, and continue on to the Review activity.

* Continue through the slideshow, using the next slides as an accompaniment to this activity. **NOTE:** If a 3-hour adjustment is **observed**, please skip the appropriate slides, and continue on to the Review activity. 

* Send out the following instructions:

* **Instructions**

Using the repo that we just created, make or add the following changes:

* Add new lines of code to one of the Python files.
* Create a new folder.
* Add a file to the newly created folder.
* Add, commit, and push the changes.
* Delete the new folder.
* Add, commit, and push the changes again.

</details>

<details>
  <summary><strong>⭐ 6.4 Review: Git (0:10)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

  * Spend only 15 minutes on this activity.

  * Use the Review section as guidance for talking points as you live-code along with the students.

  * Take your time, and answer all student questions along the way.

* Ask the class for any questions, and take a few minutes to review any commands that weren't clear. Offer to help students throughout the day and during office hours.

* Explain to students that this will be the new, primary way of submitting homework to GitHub (no more manual uploads!).

* Reassure them that it's okay if it takes them time to get comfortable with Git. By the end of the course, they will be Git pros!

* Encourage students to continue adding and committing today’s activities into a repo for additional practice.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=6+-+Git+%26+Command+Line&lessonpageTitle=Python+Deeper+Dive&lessonpageNumber=3.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F3%2FLessonPlan.md)</sub>

- - -

## 7. Close Class 

| Activity Time:       0:05 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 7.1 Instructor Do: Close Class (0:05)</strong></summary>

* Continue the slideshow to help close out the class.

* Before finishing up for the night, encourage students to review any activities they struggled with, and use office hours if they have additional questions.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=7+-+Close+Class+%26+Additional+Activities&lessonpageTitle=Python+Deeper+Dive&lessonpageNumber=3.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F3%2FLessonPlan.md)</sub>

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.

