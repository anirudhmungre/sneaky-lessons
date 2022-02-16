# 3.2: Reading and Writing in Python

## Overview

In today's class, we will explore reading and writing data from and to external CSV files. Students will also delve into Python dictionaries, zipping lists, and functions.

## Class Objectives

By the end of this lesson, the students will be able to: 

* Read data into Python from CSV files.

* Write data from Python to CSV files.

* Zip two lists together.

* Create and use Python functions.

## Instructor Prep

<details>
    <summary><strong>Instructor Notes</strong></summary>

* Today is a challenging but immensely useful class that relates directly to the homework. Challenges aside, students should have some fun today as they work through the lesson’s many activities. Expect some frustration, and provide regular encouragement. 

* The first half of today's class is far more relevant to this week's homework than the second half, so feel free to provide students with additional time so they can work through the activities.

* Please refer to our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-03-python) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

</details>

- - -

# Class Activities

## 1. Welcome & Python Check-Up

| Activity Time:       0:20 |  Elapsed Time:      0:20  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 1.1 Instructor Do: Welcome Class (0:05)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1geG4Y7ymr3JfM0wCo-HCNk6vAoctKAAamw-e4m3aTEE/edit?usp=sharing), and use the first few slides to welcome the class.

* Emphasize to students that the more they work with Python, the more sense it will make. Practice makes perfect, even if it doesn’t feel that way today.

</details>

<details>
    <summary><strong>✏️ 1.2 Students Do: Python Check-Up (0:10)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Since the last class introduced a lot of new material, today's lesson will start with a quick warm-up activity to get the Python juices flowing!

* Run [01-Stu_QuickCheckup/quick_check_up.py](Activities/01-Stu_QuickCheckup/Solved/quick_check_up.py) within the terminal, and briefly introduce the solution, which is captured in the following GIF:

![Check Up Solved](Images/01-CheckUp_Solved.gif)

* Then, send out the starter file and instructions.

* **File:**

  * [01-Stu_QuickCheckup/quick_check_up.py](Activities/01-Stu_QuickCheckup/Unsolved/quick_check_up.py)

* **Instructions:**

* Create a simple Python command line application that does the following:

  * Prints "Hello User!"

  * Then asks "What is your name?"

  * Then responds "Hello &lt;user's name&gt;"

  * Then asks: "What is your favorite number? "

  * Then responds: "Your favorite number is lower than mine.", "Your favorite number is higher than mine.", or "Your favorite number is the same as mine!" depending on your favorite number.


## Hint

* Remember to cast your variables!


</details>

<details>
    <summary><strong>⭐ 1.3 Review: Python Check-Up (0:05)</strong></summary>

* Slack out [01-Stu_QuickCheckup/quick_check_up.py](Activities/01-Stu_QuickCheckup/Solved/quick_check_up.py), and go over the code with the class, answering any questions students may have about the activity.

* Cover the following key points during your discussion:

  * The `name` variable is set to match the user-input response to the question "What is your name?".

  * Since the `age` variable is taken in as a string, it must be cast as an integer when run through the conditionals, as in the following image:

  ![Check Up Code](Images/01-CheckUp_Code.png)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+%26+Python+Check-Up&lessonpageTitle=Reading%2C+Writing%2C+and+Pyrithmetic&lessonpageNumber=3.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F2%2FLessonPlan.md)</sub>

- - -

## 2. Kid in a Candy Store - Python Loops Recap

| Activity Time:       0:25 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 2.1 Instructor Do: Loop Recap (0:05)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic.

* Open up [02-Ins_SimpleLoops/simple_loops.py](Activities/02-Ins_SimpleLoops/Solved/simple_loops.py) within the editor to give the class a refresher on creating basic loops, and make sure to share the file with students.

* You may want to have the students discuss the code with the people around them before running each `for` loop separately.

  * A `for` loop will loop through a range of numbers, the letters in a string, or the elements in a list one at a time, as captured in the following GIF:

  ![Simple For Loop - Numbers](Images/02-SimpleLoops_0to9.gif)

  * A `while` loop will loop through the code contained inside of the loop until some condition is met, as captured in the following GIF:

  ![Simple While Loop - Merry-Go-Round](Images/02-SimpleLoops_MerryGoRound.gif)

* Be sure to answer any questions that the class has about loops before moving on to the next activity.

</details>

<details>
    <summary><strong>✏️ 2.2 Students Do: Kid in a Candy Store - Loop Recap (0:15)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* In this activity, students are creating the code that a candy store will use in their state-of-the-art candy vending machine. The following GIF captures the code for this activity:

![Kid In Candy Store](Images/03-KidInCandyStore_Solved.gif)

* Open up [03-Stu_KidInCandyStore-LoopsRecap/kid_in_candy_store.py](Activities/03-Stu_KidInCandyStore-LoopsRecap/Solved/kid_in_candy_store.py) within the terminal, and run through the application to give students an idea of how it functions.

* Then, send out the following file and instructions:

* **File:**

  * [KidInCandyStore_Unsolved.py](Activities/03-Stu_KidInCandyStore-LoopsRecap/Unsolved/kid_in_candy_store.py)

* **Instructions:**

  * Create a loop that prints all candies in the store to the terminal, with their index stored in brackets beside them.

    * For example: `"[0] Snickers"`

  * Create a second loop that runs for a number of times determined by the variable `allowance`.

    * For example: If allowance is equal to five, the loop should run five times.

  * Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable `candy_cart`.

    * For example: If the user enters "0" as their input, "Snickers" should be added into the `candy_cart` list.

  * Use another loop to print all of the selected candies to the terminal.

  * **Bonus:**

    * Create a version of the code that allows a user to select as much candy as they want until they say they do not want any more.

</details>

<details>
    <summary><strong>⭐ 2.3 Review: Kid in a Candy Store (0:05)</strong></summary>

* Send out the [solution](Activities/03-Stu_KidInCandyStore-LoopsRecap/Solved/kid_in_candy_store.py), and go over the code with the class, answering whatever questions they may have.

* Cover the following key points in your discussion of the code:

  * There are three `for` loops being used in this activity. One loop prints out the original candy list. A second loop collects all of the candy choices that the user has. And a third loop prints the final list of choices to the screen.

  * When adding candies into the `candy_cart` list, the `selection` variable has to be cast as an integer because all inputs are naturally set as strings.

  * To solve the bonus, we would simply use a `while` loop instead of a `for` loop, asking after each selection whether the user would like to make another selection. If they ever answer anything other than "Yes", the loop will stop.

    ```python
    # The list of candies to print to the screen
    candy_list = [
        "Snickers",
        "Kit Kat",
        "Sour Patch Kids",
        "Juicy Fruit",
        "Swedish Fish",
        "Skittles",
        "Hershey Bar",
        "Starbursts",
        "M&Ms"
    ]

    # The amount of candy the user will be allowed to choose
    allowance = 5

    # The list used to store all of the candies selected inside of
    candy_cart = []

    # Print all of the candies to the screen and their index in brackets
    for candy in candy_list:
        print(f'[{str(candy_list.index(candy))}] {candy}')

    # Another option to run the for loop involves Python's enumerate method
    # This method obtains both the index and the value of an item during a for loop
    # for index, candy in candy_list:
    #     print(index, candy)

    # Run through a loop that allows the user to choose which candies to take home with them
    print("Which candy would you like to bring home?")
    for x in range(allowance):
        selected = input("Input the number of the candy you want: ")

        # Add the candy at the index chosen to the candy_cart list
        candy_cart.append(candy_list[int(selected)])

    # Loop through the candy_cart to say what candies were brought home
    print("I brought home with me...")
    for candy in candy_cart:
        print(candy)
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Kid+in+a+Candy+Store+-+Python+Loops+Recap&lessonpageTitle=Reading%2C+Writing%2C+and+Pyrithmetic&lessonpageNumber=3.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F2%2FLessonPlan.md)</sub>

- - -

## 3. House of Pies - Advanced Python Loops

| Activity Time:       0:30 |  Elapsed Time:      1:15  |
|---------------------------|---------------------------|

<details>
    <summary><strong>✏️ 3.1 Students Do: House of Pies - Advanced Loops (0:20)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* From one form of sweets to another! In this activity, the class will construct an order form that will display a list of pies and then prompt users to make a selection. It will continue to prompt for selections until the user decides to terminate the process.

* This activity comes in two parts: an easy version that is very much like the previous activity and a hard version, which is very challenging. Encourage students to try their luck on the hard version if they are feeling confident. 

* The following GIF captures the code for this activity:

![House of Pies](Images/04-HouseOfPies_Solved.gif)

* Open up  [04-Stu_HouseOfPies-AdvancedLoops/Solved/house_of_pies_bonus.py](Activities/04-Stu_HouseOfPies-AdvancedLoops/Solved/house_of_pies_bonus.py) within the terminal, and guide students through the application to give them an idea of how it functions.

* Then, send the following instructions to students:

* **Instructions:**

    * Create an order form that will display a list of pies to the user in the following way:

    ```
    Welcome to the House of Pies! Here are our pies:

    ---------------------------------------------------------------------
    (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
    ```

    * Then, prompt the user to enter the number for the pie that they'd like to order.

    * Immediately follow up their order with `Great! We'll have that <PIE NAME> right out for you`, and then ask if they would like to make another order. If so, repeat the process.

    * Once the user is done purchasing pies, print the total number of pies ordered.

  * **Bonus** 

  * Modify the application so that at the conclusion of the transaction, the user's purchases are listed out, with the total pie count broken by _each_ pie. For example:

    ```
    You purchased:
    0 Pecan
    0 Apple Crisp
    0 Bean
    2 Banoffee
    0 Black Bun
    0 Blueberry
    0 Buko
    0 Burek
    0 Tamale
    1 Steak
    ```

</details>

<details>
    <summary><strong> ⭐ 3.2 Review: House of Pies (0:10)</strong></summary>

* Send out the [solution](Activities/04-Stu_HouseOfPies-AdvancedLoops/Solved/house_of_pies_bonus.py), and go over the code with the class, answering whatever questions they may have.

* Explain the following key points during this discussion:

  * Since the GUI for the application starts with 1, we need to subtract 1 from the user's input when referencing the pie's actual index&mdash;because all indexes start at 0 by default.

  * The primary loop being used is a `while` loop that is constantly checking whether the user's response to the question `Would you like to make another purchase?` ever changes from `y`.

  * The total number of pies is calculated in the original solution by determining the length of the `pie_purchases` array.

  * In the bonus, the code tracks the number of pie purchases for each pie type by using a second list filled with 0 values, each corresponding to a pie in the first list. Therefore, every time a pie is chosen, the code adds one to the index of the `pie_purchases` list, which is equal to that of the original `pie_list`.

    ```python
    # While we are still shopping...
    while shopping == "y":

        # Show pie selection prompt
        print("---------------------------------------------------------------------")
        print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
              " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
              " (9) Tamale, (10) Steak ")

        pie_choice = input("Which would you like? ")

        # Get index of the pie from the selected number
        choice_index = int(pie_choice) - 1

        # Add pie to the pie list by finding the matching index and adding one to its value
        pie_purchases[choice_index] += 1

        print("------------------------------------------------------------------------")

        # Inform the customer of the pie purchase
        print("Great! We'll have that " + pie_list[choice_index] + " right out for you.")

        # Provide exit option
        shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

    # Once the pie list is complete
    print("------------------------------------------------------------------------")

    # Count instances of each pie
    print("You purchased: ")

    # Loop through the full pie list
    for pie_index in range(len(pie_list)):
        pie_count = str(pie_purchases[pie_index])
        pie_name = str(pie_list[pie_index])

        # Gather the count of each pie in the pie list and print them alongside the pies
        print(pie_count + " " + pie_name)
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+House+of+Pies+-+Advanced+Python+Loops&lessonpageTitle=Reading%2C+Writing%2C+and+Pyrithmetic&lessonpageNumber=3.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F2%2FLessonPlan.md)</sub>

- - -

## 4. Module Playground

| Activity Time:       0:20 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 4.1 Instructor Do: Reading Text Files (0:05)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic.

* Note that Python is also capable of reading in data from external text files and then performing tasks on that data.

* Open up [05-Ins_BasicRead/read_file.py](Activities/05-Ins_BasicRead/Solved/read_file.py) and [05-Ins_BasicRead/Resources/input.txt](Activities/05-Ins_BasicRead/Resources/input.txt), and go over the syntax and purpose of the code contained within, covering the following points as you go:

  * When dealing with external files, Python requires precise directions on what path to follow to reach the desired file. Therefore, if the desired file is stored in a subfolder called "Resources", the path needed would be "Resources/FileName.txt".

  * It’s critical that you note that different operating systems use different paths to locate files. For example, Windows machines will often use forward slashes to separate folders, and Mac devices will use backslashes.

  ```python
  # Store the file path associated with the file (note the backslash may be OS specific)
  file = '../Resources/input.txt'
  ```

  * The `with` statement is simply saying that, for as long as we are dealing with the code within the following block, save the text variable. Once the code block has completed, the text variable will be "cleaned up" and removed to save memory.

  * `open(<File Path>, <Read/Write>)` is the function that Python uses to open and work with external text files. By specifying either `'r'`, `'w'`, or `'rw'`, we can use the `open()` function to either read from a text file, write to a text file, or perform both operations in the code block that follows it.

  * `text.read()` parses the data that is read in by the `open()` function and converts it to a string type. If this function was not used, all that would be printed to the screen would be an unhelpful text-wrapper object.

  
  ```python
  # Open the file in "read" mode ('r') and store the contents in the variable "text"
  with open(file, 'r') as text:

      # This stores a reference to a file stream
      print(text)

      # Store all of the text inside a variable called "lines"
      lines = text.read()

      # Print the contents of the text file
      print(lines)
  ```

</details>

<details>
    <summary><strong>📣 4.2 Instructor Do: Introduction to Modules (0:05)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic, covering the following points as you go:
 
* Although Python includes many built-in functions, coders sometimes need to add external modules to perform specific tasks.

  * For example, if a coder wanted to use a random number generator for a dice game that they were making, they would most likely want to use the `random` module rather than create the code from scratch.

* Importing modules into Python is very simple. All we need to do is install the module and import it into our code.

  * All of today’s modules come packaged with Python, so there is no need to install anything new.

* Open [06-Ins_Modules/imports.py](Activities/06-Ins_Modules/Solved/imports.py) in your editor, and guide the class through the process for importing modules into their code.

  * Note that the `string` module contains many helpful constants and methods that pertain to strings. For example, we can use `string.ascii_letters`, and Python will instantly grab a reference to every ASCII character.

  ```python
  # Import the String Module
  import string

  # Utilize the string module's custom method: ".ascii_letters"
  print(string.ascii_letters)
  ```
  * The following GIF demonstrates the outcome when this code is run.

  ![Ascii Gif](Images/06-Modules_String.gif)

  * Explain that the `random` module does exactly what we might expect: it allows Python to randomly select values from set ranges, lists, or even strings.

  ```python
  # Import the Random Module
  import random

  # Utilize the random module's custom method randint
  for x in range(10):
      print(random.randint(1, 10))

  ```

  * The following GIF demonstrates the outcome when this code is run.

  ![Random Module](Images/06-Modules_Random.gif)
  

</details>

<details>
    <summary><strong>✏️ 4.3 Students Do: Module Playground (0:05)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* There are too many built-in modules in Python for us to cover all of them in one class. Instead, give the students time to go through and play around with some Python modules.

* Send out the following link:

* **Link:**

  * [List of Built-In Python Modules](https://docs.python.org/3/py-modindex.html)

* Before moving on, bring the class back together to discuss the modules that they uncovered.

</details>

<details>
    <summary><strong>⭐ 4.4 Review: Module Playground (0:05)</strong></summary>

* Call the class back together, and ask the students if any modules were particularly useful. Have any volunteers discuss the module that they found and how they would use it.

* If no one offers up any modules, call on random students to encourage engagement.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Module+Playground&lessonpageTitle=Reading%2C+Writing%2C+and+Pyrithmetic&lessonpageNumber=3.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F2%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

- - -

## 5. Reading Comic Book Data

| Activity Time:       0:30 |  Elapsed Time:      2:20  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 5.1 Instructor Do: Reading in CSV Files (0:10)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic while covering the following key points:

* Although reading in text files can be useful in some circumstances, CSV files are more common in the data industry.

  * CSV stands for **comma** **separated** **values**. This file type is essentially a table that has been converted into a text format with each row and column separated by specified symbols.

  * Most frequently, each row is located on a new line, and each column is separated by a comma, as captured in the following image:

    ![Example CSV](Images/07-ReadCSV_ExampleFile.png)

* Python has a module called `csv`, which allows users to easily pull in data from external CSV files and then perform operations on the data.

* Open [08-ReadCSV](Activities/08-Ins_ReadCSV/Solved/read_csv.py) within the editor, and guide the class through the code contained within.

  * The first major piece of code to discuss is the import and use of the `os` module. This module allows Python programmers to easily create dynamic paths to external files that will function across different operating systems.

  ```py
  # First we'll import the os module
  # This will allow us to create file paths across operating systems
  import os
  csvpath = os.path.join('..', 'Resources', 'contacts.csv')
  ```

  * In the next major piece of code, point out that we use `csv.reader()` instead of `text.read()` to translate the object being opened by Python. It is critical to note the `delimiter=','` parameter, which tells Python that each comma within the CSV should be read as moving into a new column for a row.

    * Reiterate to students that the reading of the file must be done within the `with open()` statement. The variable `csvreader` will not be useful outside that block of code because the file will be closed when the `with open()` block ends. In a later example, students will learn that one option for working with the data outside of `with open()` is to append it to a list.

  ```python
  import csv
  with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        print(row)
  ```

  * The code then loops through each row of the CSV and prints out the contents. Point out that each value is a string and that all the rows are lists, as captured in the following image:

    ![Read CSV Run](Images/07-ReadCSV_ReadRun.png)

* Data Source: Data generated by Mockaroo, LLC. (2021) Realistic Data Generator. https://www.mockaroo.com/. Modified by Trilogy Education Services, LLC.

</details>

<details>
    <summary><strong>✏️ 5.2 Students Do: Reading Comic Book Data (0:15)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* In this activity, students will be provided with a CSV file containing comic book data from the British Library. They will create an application that searches the data for a specific graphic novel title and then returns the title, publisher's name, and year published.

  ![Read Comic Books](Images/08-ReadComicBooks_Alien.png)

* Open [09-Stu_ReadComicBooksCSV/comicbooks.py](Activities/09-Stu_ReadComicBooksCSV/Solved/comicbooks.py) and discuss with students how their application should function, and send out the following file and instructions.

* **File:**

  * [comic_books.csv](Activities/09-Stu_ReadComicBooksCSV/Resources/comic_books.csv)

* **Instructions:**

  * Prompt the user for the book title they’d like to search.

  * Search through `comic_books.csv` to find the user's book.

  * If the CSV contains the user's book, then print out the title, the publisher's name, and the year it was published.

    * For example: `'Alien was published by DC Comics in 2015'`

  * If the CSV does not contain the user's comic book, then print out a message telling the user that their comic book could not be found.

    * Set a variable to `False` to check if we found the comic book.

    * In the `for` loop, change the variable to confirm that the comic book is found.


</details>

<details>
    <summary><strong>⭐ 5.3 Review: Reading Comic Book Data (0:05)</strong></summary>

* Send out [09-Stu_ReadComicBooksCSV/comicbooks.py](Activities/09-Stu_ReadComicBooksCSV/Solved/comicbooks.py) and go over the code with the class, answering whatever questions they may have.

* Cover the following key topics when discussing this activity:

  * First, Python imports both the `os` and `csv` modules for use later on. It is common practice to import all modules at the start of an application.

  * When opening the CSV file, the code dictates that each new line in the file should be viewed as a new line of data to be read in.

  * We create a variable, set to `False`, that will be changed only when a title is found. That way, we can alert the user when their title is _not_ found.

  ```python
  # Set path for file
  csvpath = os.path.join("..", "Resources", "comic_books.csv")

  # Set variable to check if we found the video
  found = False
  ```

  * When reading the CSV file, the delimiter is set to `","` to ensure that Python splits up the data into the proper columns whenever a comma is found.

  * The code loops through each row, searching for the row whose first value, index 0, is equal to the search term entered.

  * The publisher of a book is located at index 8, and the year published is located at index 9.

  * The `found` variable is set to `True` so we do not display the "Not Found" message after searching through the CSV file.

  ```python
  # Open the CSV
  with open(csvpath) as csvfile:
      csvreader = csv.reader(csvfile, delimiter=",")

      # Loop through looking for the video
      for row in csvreader:
          if row[0] == book:
              print(row[0] + " was published by " + row[8] + " in " + row[9])

              # Set variable to confirm we have found the video
              found = True
  ```

  * After the `for` loop is complete, the code displays an apology message if the `found` variable is still set to `False`. 

  ```python
    # If the book is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")
  ```

* Data Source: Data modified from "Comic books CSV" Updated April 2021. Initially released in 2014 to accompany the British Library's exhibition Comics Unmasked. [https://www.bl.uk/collection-metadata/downloads](https://www.bl.uk/collection-metadata/downloads)

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Reading+Netflix&lessonpageTitle=Reading%2C+Writing%2C+and+Pyrithmetic&lessonpageNumber=3.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F2%2FLessonPlan.md)</sub>

- - -

## 6. Census Zip

| Activity Time:       0:40 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 6.1 Instructor Do: Writing CSV Files (0:05)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic.

* Cover the following key points:

  * Explain that Python can also write data _into_ CSV files.

  * Although this may not seem useful at first, it allows Python users to easily modify and/or create datasets based on previous data.

* Open [10-Ins_WriteCSV/write.py](Activities/10-Ins_WriteCSV/Solved/write.py) within the editor, send the file to students, and go through the code with the class, explaining each line as you proceed.

  * The syntax for writing data into a CSV file is, thankfully, very similar to the syntax used for reading data in from an external file.

  * First, the code references the path to the CSV file that the user would like to write to.

  * Next, the `with open()` statement is used once more, but with one significant difference: instead of passing the parameter `'r'` and directing Python to read a file, the parameter `'w'` is passed to inform Python to write to the file.

  * Instead of `csv.reader()`, `csv.writer()` is used to once again inform Python that this application will be writing code into an external CSV file.

  * To write a new row into a CSV file, simply use the `csv.writerow(<DATA LIST>)` function and pass in an array of data as the parameter, as in the following image:

  ![Write CSV](Images/09-WriteCSV_Code.png)

* Run the code, then open up the new CSV file and briefly discuss what the code accomplished.

</details>

<details>
    <summary><strong>📣 6.2 Instructor Do: Zipping Lists (0:05)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic while covering the following key points:

* Although it is possible to write new rows of data into a CSV file using many `csv.writerow()` statements, Python users can write data into a new CSV file more efficiently by using the `zip()` function.

  * `zip()` takes in a series of lists as its parameters and joins them together in a stack.

* Open up [11-Ins_Zip/Solved/zipper.py](Activities/11-Ins_Zip/Solved/zipper.py) within the editor, and go through the code with the class, explaining each line as you go.

  * This application has three lists, all of which are the same length and pertain to each other. By zipping these lists together, there is now a single, joined list whose indexes reference all three of the lists inside.

  * Zipped lists are lazy iterators, so their output is not stored in memory and iterated over, but generated at each iteration and discarded.  This means each zipped object can only be used once. For example, you can write the zipped object to a CSV or print to the terminal, but you cannot do both.

  ```python
  # Three Lists
  indexes = [1, 2, 3, 4]
  employees = ["Michael", "Dwight", "Meredith", "Kelly"]
  department = ["Boss", "Sales", "Sales", "HR"]

  # Zip all three lists together into tuples
  roster = zip(indexes, employees, department)

  # Print the contents of each row
  for employee in roster:
      print(employee)
  ```

  The output of this code is captured in the following image:

  ![Zip Run](Images/10-Zip_Run.png)


  * In order to save the contents of the zipped list to a CSV, the for loop must be commented out or removed, and the following code can be used instead.

  ```python
  # save the output file path
  output_file = os.path.join("output.csv")

  # open the output file, create a header row, and then write the zipped object to the csv
  with open(output_file, "w") as datafile:
      writer = csv.writer(datafile)

      writer.writerow(["Index", "Employee", "Department"])

      writer.writerows(roster)
  ```

</details>

<details>
    <summary><strong>✏️ 6.3 Students Do: U.S. Census Zip (0:20)</strong></summary>

* Continue through the slideshow, using the next slides as an accompaniment to this activity.

* Now that students have a decent idea of how to write and read data to and from CSV files, they will revisit data from the U.S. Census, clean it up, and create a new CSV file that is easier to comprehend, as captured in the following image:

![Clean CSV](Images/11-CensusZip_CleanCSV.png)

* Compare the starter sheet (at[12-Stu_CensusZip/Resources/census_starter.csv](Activities/12-Stu_CensusZip/Resources/census_starter.csv)) to the final sheet (at [12-Stu_CensusZip/Solved/census_final.csv](Activities/12-Stu_CensusZip/Solved/census_final.csv)) of this activity, explain to students how their application should function, and then send out the following file and instructions.

* **File:**

  * [census_starter.csv](Activities/12-Stu_CensusZip/Resources/census_starter.csv)

* **Instructions:**

  * Create a Python application that reads in the data from the 2019 U.S. Census. 

  * Then, store the contents of `Place`, `Population`, `Per Capita Income`, and `Poverty Count` into Python lists.

  * Then, zip these lists together into a single tuple.

  * Finally, write the contents of your extracted data into a CSV. Make sure to include the titles of these columns in your CSV.

  * **Notes:**
    * Windows users may get a `UnicodeDecodeError`. To avoid this, pass in `encoding="utf8"` as an additional parameter when reading in the file.

    * As with many datasets, the file does not include the header line. Use the following list as a guide to the columns: "Place,Population,Median Age,Household Income,Per Capita Income,Employed Civilians,Unemployed Civilians,People in the Military,Poverty Count"

  * **Bonus:**

    * Find the poverty rate (percentage of population living in poverty). Include this in your final output, converting the rate to a string and including a "%" at the end of the string.

    * Parse the string associated with `Place`, separating it into `County` and `State`, so we can store both in separate columns.

Data Source: [U.S. Census API - ACS 5-Year Estimates 2019](https://www.census.gov/data/developers/data-sets/census-microdata-api.ACS_5-Year_PUMS.html)


</details>

<details>
    <summary><strong>⭐ 6.4 Review: U.S. Census Zip (0:05)</strong></summary>

* Open and send out the [12-Stu_CensusZip/census_solved.py](Activities/12-Stu_CensusZip/Solved/census_solved.py) of the previous activity, and go over the code line by line with the class, answering whatever questions they may have.

* Cover the following key points during this discussion:

  * Seven empty lists are created at the start of this application. These lists will be used to hold specific data from the original CSV, and they will ultimately be zipped together before being written to a new CSV file.

  * For every new row that is read in from the original CSV file, new data is appended onto the lists. In the cases of `poverty_rate`, `county`, and `state`, the data is being altered before it is placed in the list.

  ```py
  # Lists to store data
  place = []
  population = []
  income = []
  poverty_count = []
  poverty_rate = []
  county = []
  state = []

  with open(census_csv) as csvfile:
      csvreader = csv.reader(csvfile, delimiter=",")
      for row in csvreader:
          # Add place
          place.append(row[0])

          # Add population
          population.append(row[1])

          # Add per capita income
          income.append(row[4])

          # Add poverty count
          poverty_count.append(row[8])

          # Determine poverty rate to 2 decimal places, convert to string
          percent = round(int(row[8]) / int(row[1]) * 100, 2)
          poverty_rate.append(str(percent) + "%")

          # Split the place into county and state
          split_place = row[0].split(", ")
          county.append(split_place[0])
          state.append(split_place[1])
  ```

  * Once all data has been read in, the lists are zipped together and written into a new CSV file. A header row is also written in before the zipped rows.

  ```py
  # Zip lists together
  cleaned_csv = zip(place, population, income, poverty_count, poverty_rate, county, state)

  # Set variable for output file
  output_file = os.path.join("census_final.csv")

  #  Open the output file
  with open(output_file, "w") as datafile:
      writer = csv.writer(datafile)

      # Write the header row
      writer.writerow(["Place", "Population", "Per Capita Income", "Poverty Count", "Poverty Rate",
                      "County", "State"])

      # Write in zipped rows
      writer.writerows(cleaned_csv)
  ```

</details>

<details>
    <summary><strong>📣 6.5 Instructor Do: Introduction to Functions (0:05)</strong></summary>

* Continue the slideshow to facilitate discussion of the next topic while covering the following key points:

* DRY is a popular acronym that many coders live by. It stands for **d**on't **r**epeat **y**ourself**, and it essentially states we should avoid similar/repeated lines in code whenever possible.

* One of the best ways to prevent repetition is the frequent use of Python functions.

  * A function is a block of organized, reusable code that can perform a single, related action. In other words, functions are placeable blocks of code that perform a specific action.

* Open up [13-Ins_Functions/functions.py](Activities/13-Ins_Functions/Solved/functions.py) within the editor, and go through the code line by line with your class.

  * To create a new function, simply use `def <Function Name>():` and then place the code that you would like to run within the block underneath it.

  * To run the code stored within a function, the function itself must be called in the program. Functions will not run unless called upon.

    ```python
    def print_hello():
      print(f"Hello!")

    print_hello()
    ```

  * Functions that take in parameters can also be created simply by adding a variable into the parentheses in the function's definition. This allows specific data to be passed into the function.

    ```python
    def print_name(name):
        print("Hello " + name + "!")

    print_name("Bob Smith")
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=6+-+Udemy+Zip&lessonpageTitle=Reading%2C+Writing%2C+and+Pyrithmetic&lessonpageNumber=3.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F03-Python%2F2%2FLessonPlan.md)</sub>

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.

