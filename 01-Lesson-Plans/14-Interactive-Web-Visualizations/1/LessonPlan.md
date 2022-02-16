# 14.1 Intro to JavaScript Visualizations

## Overview

Today's class introduces students to the basic syntax of JavaScript through basic charts in Plotly. As a data professional, interactivity is a very powerful tool, allowing us to move from simply telling a story of the data to letting users tell the story themselves. Learning JavaScript visualizations has a two-fold benefit. First, JavaScript has been focused on providing interactivity since its inception. Second, JavaScript visualizations are the easiest interactive visualizations to share with a wide audience. 

### Class Objectives
By the end of today's class, the students will:

* Describe JavaScript variables, arrays, data types, and statements.
* Implement basic JavaScript control flow (functions, loops, if/else statements).
* Create functions in JavaScript.
* Create, update, and iterate JavaScript Objects.
* Create basic charts, including bar charts and line charts using Plotly.
* Use Plotly's layout object to customize the appearance of their charts.
* Annotate charts with labels, text, and hover text.

### Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* This class introduces the fundamentals of JavaScript in the context of creating simple Plotly charts. JavaScript fundamentals are introduced in three related chunks: the "nouns" of JavaScript (i.e. variables, objects, and arrays), control flow (e.g. iterations and conditionals), and functions. Each "chunk" of fundamentals will have two activities: one in a simple JavaScript context, and then one using that concept in practice to create a Plotly chart.

* Have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

* Please remember that the slideshows are for instructor use only. When distributing slides to students, first export them to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

## 1. Intro to JavaScript and Plotly

| Activity Time:       0:50 |  Elapsed Time:      0:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Creating Interactive Charts on the Web (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use first slide while you welcome students to the class and the second slide to go over today's learning objectives. To assist you with this module use slides 3 - 5.

* Plotly is a software library for creating interactive charts and data visualizations. Because the web was intended for interaction from the beginning, it is a natural place to create interactive charts. Plotly allows us to do that.

* However, to use Plotly, we're going to need to learn a little bit of JavaScript.

* We've already learned HTML and CSS, which allows us to structure and style a web page; JavaScript will allow us to make the page interactive.

* Open [index.html](Activities/01-Ins-Interactive-Charting-With-JavaScript/Solved/index.html) in your browser to show the class a simple Plotly chart.

* Demonstrate interactions with the chart by zooming in and out, panning, and hovering over markers.

* Open [index.html](Activities/01-Ins-Interactive-Charting-With-JavaScript/Solved/index.html) in an editor and show the three different places a `<script>` element appears:

  * First, there is a `<script>` element in the `<head>` element linking to the Plotly library.
  * Second, there is a `<script>` element in the body with code inside the tags.
  * Finally, there is a `<script>` element in the body linking to an external JavaScript file.

* Now go through the three different `<script>` elements, and explain the following:

  * The first `<script>` element loads the Plotly library. This is similar to `import` in Python. It is in the `<head>` element because we want that library loaded before we access it with any other JavaScript in the page.

  * The second `<script>` element shows an "inline" script. The JavaScript is written directly into the HTML file. This is fine for simple pages and prototyping, but in general, linking to external scripts is preferred. In this example, we are creating variables for our `x` data and `y` data.

  * The third and final `<script>` element links to an external file, `plots.js`. Open up [plots.js](Activities/01-Ins-Interactive-Charting-With-JavaScript/Solved/plots.js) and show the code that is creating our chart. Assure students that you'll come back to this code to explain exactly how it creates the interactive chart, but to understand it, first we'll need to cover some JavaScript fundamentals.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: JavaScript Variables, Objects, and Arrays (10 mins)</strong></summary>

  * Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 6 - 14 to assist you with this module.

  * Open [hello-variable-world.js](Activities/02-Ins_JavaScript-Variables_and_Data_Structures/Solved/Variables/hello-variable-world.js) and walk through each line of code with students. Point out that JavaScript variables are similar to python variables. One difference, however, is JavaScript variables must be initialized. 


    * For the sake of simplicity, we only introduce students to the `let` and `const` keywords to initialize JavaScript variables. You can discuss the `var` keyword if you feel comfortable, but it isn't necessary. 
      
    * While JavaScript does provide automatic semicolon insertion at the ends of lines, it is poor form not to add them while programming. We recommend explaining that semicolons should come at the ends of lines. Although semicolons can be omitted, it can result in hard-to-solve bugs down the line.

  * When you get to the following code, open [hello-variable-world.html](Activities/02-Ins_JavaScript-Variables_and_Data_Structures/Solved/Variables/hello-variable-world.html) in your browser and show students how to open the Chrome console.

  ```JavaScript
  console.log('Hello JavaScript World!')
  console.log('We use console.log() to print in JavaScript')
  console.log('Why? Because the print() function will try to send the page to your printer!')
  console.log(`Did you know that ${name} is ${age} years old and makes $${weeklyWage} per week?`)
  ```

  * Point out that when passing variables into a string this is called a template literal, similar to f-strings in Python, and to do this we use a backtick and place the variable inside of `${}`.

  * Go back to the code, and introduce the `const` keyword, showing students that once a constant variable is assigned a value, the value cannot be changed.

    * If time permits explain that `const` stands for "constant reference." If an array is declared as a `const`, then the content of the array may be freely changed, but it cannot be replaced with a different variable type (e.g., number, string, etc.). 

    * If students have further questions, send them to the following [MDN Article](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const).

  * Next, introduce JavaScript objects and arrays with the remaining code, noting that they are similar to python dictionaries and lists, respectively.

  * Explain that this code only shows how to initialize objects and arrays, but to use them, we'll need to know how to access and add properties and elements.

  * Open [objects.js](Activities/02-Ins_JavaScript-Variables_and_Data_Structures/Solved/Arrays_and_Objects/objects.js) and go over the bracket notation and dot notation. Point out that the JavaScript convention prefers using the dot notation, but ask students if they can think of a situation where bracket notation is necessary. 

    **Note:** Since the example properties in the code are not explicitly written as strings when they are initialized, you may need to ask leading questions for students to realize that a property name could have a space in it, thus requiring the bracket notation.

  * Continue through the code and show how values can be overwritten or added to the object. 

  * Ask if there are any questions before opening [arrays.js](Activities/02-Ins_JavaScript-Variables_and_Data_Structures/Solved/Arrays_and_Objects/arrays.js).

  * Point out that JavaScript uses `push` to add array elements, instead of `append` in python. However, accessing individual elements is exactly the same; the zero-based index of the element is passed through brackets. 

  * Finally, introduce the `slice` method, which works similarly to the python range literal. Explain that the first argument is the starting index, and the second argument is the ending index, and show that `slice` returns a new array with the values from the starting index up to, but not including, the end index.

  * Ask students if they have any questions before moving to the student activity.

</details>

<details>
  <summary><strong>✏️ 1.3 Students Do: My Variables, Objects, and Arrays (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 15 and 16 to present this activity to the students.

* In this activity, students create variables and console logging strings with template literals.

* The following file has the student instructions: [README](Activities/03-Stu_JavaScript-Variables_and_Data_Structures/README.md).

</details>

<details>
  <summary><strong>⭐ 1.4 Review: JavaScript Variables, Objects, and Arrays (5 mins)</strong></summary>

* Go over the solution to the last activity, [HelloVariableWorld.js](Activities/03-Stu_JavaScript-Variables_and_Data_Structures/Solved/HelloVariableWorld.js), together as a class.

* Make sure to highlight key concepts from this activity and ask students the following:

  1. Which keyword do we use to assign values to a variable?

      * We use `let` to assign values to variables.

      ```javascript
      let name = 'Travis Taylor'
      ```

  2. How do we construct a template literal?

      * We use a backtick and place the variable inside of `${}`.

      ```javascript
      let title = `${name}'s First Plotly Chart`
      ```
  
  3. What do we use to define an array?

      * We place square brackets `[]` around the values and separate them with commas.

      ```javascript
      let timesRead = [100, 50, 25]
      ```

  4. What type of pairs do we use to create JavaScript objects?

      * We create `key value` pairs separated by a colon `:` just like in a Python dictionary.

      ```javascript
      let myData = {
          name: name,
          favoriteBooks: books,
          timesRead: timesRead,
          age: 40
      }
      ```

</details>

<details>
  <summary><strong>✏️ 1.5 Students Do: My First Plotly Chart (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 18 and 19 to present this activity to the students.

* In this activity, students use the variables created in the previous activity to create a bar chart.

* The following file has the student instructions: [README](Activities/04-Stu_Plotly-Chart/README.md).

</details>


<details>
  <summary><strong>⭐ 1.6 Review: Plotly Chart (5 mins)</strong></summary>

  * Go over the solution to the last activity, [plots.js](Activities/04-Stu_Plotly-Chart/Solved/plots.js), together as a class.

* Make sure to highlight key concepts from this activity and ask students the following:

  1. Which values should we set our `x` and `y` to in our `trace`?

      * We will want to set `x` to the `books` array and `y` to the `timesRead` array.

      ```javascript
      let trace1 = {
        x: books,
        y: timesRead,
        type: 'bar'
      };
      ```

  * Walk through the remainder of the Plotly code explaining each part.

  * We create the variable `data` to hold an array of traces, even if there is only one. Point out this is important because the Plotly function requires an array to be required so we can create multi trace charts later.

    ```javascript
    let data = [trace1];
    ```

  * The `layout` object is optional but can be used to change the style of our charts including adding our title as we do here:

    ```javascript
    let layout = {
      title: title
    };
    ```

  * To create the chart, we use the `Plotly.newPlot()` function. We need to provide a string matching the `id` of a `div` from our `index.html`, our data array object, and optionally a layout object.

    ```javascript
    Plotly.newPlot("plot", data, layout);
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Intro+to+JavaScript+and+Plotly&lessonpageTitle=Intro+to+JavaScript+Visualizations&lessonpageNumber=14.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F1%2FLessonPlan.md)</sub>

- - -

## 2. Control Flow

| Activity Time:       0:30 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Control Flow (15 mins)</strong></summary>

  * Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 21 - 25 to assist you with this module.

  * Open [iteration.js](Activities/05-Ins_Control_Flow/Solved/Iteration/static/js/iteration.js) and walk through the code with students. Specifically, show how JavaScript `for` loops increment with the following three arguments separated by semicolons:

      * First, we initialize the value of our iterator, most commonly created as `i` and set the value to whatever value we would like to begin with.
      
      * Second, we provide a conditional statement to stop the `for` loop once the condition is met.

      * Lastly, we declare how our iterator should increment or decrement. Point out the most common is to use `i++` to increment up by 1 each loop.

      ```javascript
      for (let i = 0; i < 10; i++) {
        console.log("Iteration #", i);
      }
      ```

  * Next, explain how we can loop through an array by using the `.length` function to determine our number of iterations and then use bracket notation `[]` to reference each index in the array. 

    ```javascript
    for (let j = 0; j < students.length; j++) {
      console.log(students[j]);
    }
    ```

  * Open [conditionals-reference.js](Activities/05-Ins_Control_Flow/Solved/Conditionals/conditionals-reference.js) and go over the conditional `if` statement and the `&&` and `||` operators.

      * Explain that for `if` statements in JavaScript we're required to place our `condition` inside of parentheses.
      
      * We then place our code to execute when the statement is `True` inside of curly brackets `{}`. 
      
          * Because JavaScript does not use spaces like Python, the brackets declare the beginning and end of the statement.
          
      * Explain that similar to Python, the JavaScript language uses `else`. However, the declaration of `else if` is spelled out completely compared to how it is used in Python (that is, `elif`).
      
      * Remind students we can have as many `else if` statements as we like in our conditional statement.

      * Lastly, review how we can use `&&` to represent `and` require all conditions to evaluate to `true`. As well as, how we can use `||` to represent `or` require only one condition to evaluate to `true`.
      
  * Open [conditionals.js](Activities/05-Ins_Control_Flow/Solved/Conditionals/static/js/conditionals.js) and demonstrate how we can use variables and conditional statements to create a decision tree to provide results based upon multiple factors:

      * Start by explaining that we begin with a single conditional statement evaluating if there was both `pain after the injury` and `significant swelling`.
      
      * Based on the results of our first conditions, we then determine the advice to be provided using nested conditional statements that follow.

      * Based on the three variables initialized, walk the students through the conditional statements to determine what will be console logged, then display this with the inspector.

      ```javascript
      let painAfterInjury = true;
      let significantSwelling = true;
      let ableToWalk = true;
      ```

      * Point out that our second condition `(!ableToWalk)` uses the exclamation point `!` in front of the variable to stand for `not`.
      
      * In this case, the condition evaluates to `true` if `ableToWalk` is equal to `false`. This can be a hard concept for some students to understand, so be sure to check in with the students and ask if they have any questions.

      ```javascript
      console.log("You may have a sprained ankle, or a fracture of the fibula.")
      console.log("Use ice, elevation, rest and an elastic bandage to keep the swelling under control.")
      console.log("See your doctor if the swelling and pain continue.")
      ```
      
      * Next, change which variables are commented/uncommented, and then ask the class to walk you through which conditions evaluate to true and therefore which messages will be logged to the console.

  * Ask students if they have any questions before moving to the next activity.

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Iterations and Conditionals (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 26 and 27 to present this activity to the students.

* In this activity, students create a for loop, append values into arrays based on the movie's decade, calculate the average rating of all movies, and print out how many of the top 10 movies came from each decade.

* The following file has the student instructions: [README](Activities/06-Stu_Iteration_and_Conditionals/README.md).

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Iterations and Conditionals (5 mins)</strong></summary>

* Go over the solution to the last activity, [movies.js](Activities/06-Stu_Iteration_and_Conditionals/Solved/static/js/movies.js), together as a class.

* Make sure to highlight the key concepts from this activity and ask students the following:

  1. Which arguments do we use to create our `for` loop?

      * We set `i = 0`, loop while `i` is less than then `length` of our `movies` array, and iterate `i` by one each loop with `i++`.

      ```javascript
      for (let i = 0; i < movies.length; i++) {
      ```

  2. How do we reference each movie within the loop?

      * We use bracket notation with our `i` iterator to create a variable and evaluate each individual movie one at a time.

      ```javascript
      let movie = movies[i]
      ```
      
  3. How do we evaluate the movie object with a conditional statement to assign each movie to its respective decade array?

      * Using the variable we created we can use `.year` and compare the value to the beginning of each decade.

      ```javascript
      if (movie.year < 1970) {
      } else if (movie.year < 1980) {
      } else if (movie.year < 1990) {
      } else if (movie.year < 2000) {
      } else {
      }
      ```
      
      * Point out that we do not need to use `&&`: If a conditional statement evaluates to `false`, then the next `else if` only needs to evaluate for the next decade.
      
      * For example, if the `movie.year` is not less than `1980`, then the next condition only needs to check if `movie.year` is less than `1990` because we know, based on the previous statement, that it must be greater than or equal to `1980`.

  4. Which method do we use to add movies to each array when the condition evaluates to `true`?

      * We use `.push(movie)` to add the movie to the respective array.

      ```javascript
      movies1960s.push(movie);
      ```

  5. How can we go about calculating the average score for all 10 movies?

      * Point out that if we initialize a variable to `0` before our loop, we can add to the variable during each loop to calculate the total for all 10 movies.

      ```javascript
      let sum = 0;
      ```

      * Then we can use the sum total at the end divided by the length of our array of movies to calculate the average.

      ```javascript
      let avg = sum / movies.length;
      ```
      
  * Lastly, show that when we console log the number of movies for each decade, we use `.length` on the final arrays to calculate the end result. This is more efficient than calculating a counter variable for each decade.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Control+Flow&lessonpageTitle=Intro+to+JavaScript+Visualizations&lessonpageNumber=14.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F1%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

- - -

## 3. Multiple Trace Charts

| Activity Time:       0:25 |  Elapsed Time:      2:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Multiple Trace Charts (5 mins)</strong></summary>

  * Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 30  and 31 to assist you with this module.
  
  * Open [index.html](Activities/07-Ins_Multiple-Trace-Charts/Solved/index.html) in a browser to show what the multitrace plots look like before opening the JavaScript file and reviewing the code.
  
  * Now open [plot.js](Activities/07-Ins_Multiple-Trace-Charts/Solved/plots.js) and walk through the code with students, showing specifically how we create multiple traces and the data array object that generates our multiple trace charts.

  * Explain that we need to create multiple traces (as the name implies).

  * In our example, we create 2 simple traces with 6 data points.
  
  * Point out that our `x` values are the same, and that this is necessary for them to share the x-axis.
  
  * We are also choosing two different `types` of charts matching the view of [index.html](Activities/07-Ins_Multiple-Trace-Charts/Solved/index.html) in our browser.

    ```javascript
    // Create our first trace
    let trace1 = {
      x: [0, 1, 2, 3, 4, 5],
      y: [0, 5, 10, 15, 20, 25],
      type: "bar"
    };

    // Create our second trace
    let trace2 = {
      x: [0, 1, 2, 3, 4, 5],
      y: [0, 1, 4, 9, 16, 25],
      type: "scatter"
    };
    ```

  * Both `trace1` and `trace2` are assigned to our array called `data`, which will be charted.

    ```javascript
    let data = [trace1, trace2]
    ```
    
  * In the last line of the code, we see the two arguments: `plot` and `data`. A possible third argument would be to specify the `layout`, but it is omitted here. The layout, therefore, will follow Plotly's default settings for now.

  * Ask students if they have any questions before moving to the next activity.

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: Multiple Traces (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 32 and 33 to present this activity to the students.

* In this activity, students plot the number of search results, of both Roman and Greek god names.

* The following file has the student instructions: [README](Activities/08-Stu_Multiple-Trace-Charts/README.md).

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Multiple Traces (5 mins)</strong></summary>

* Go over the [plots.js](Activities/08-Stu_Multiple-Trace-Charts/Solved/plots.js) solution together as a class.

* Make sure to highlight the key concepts from this activity and ask students the following:

  1. How do we construct our `for` loop of the array of objects?

    * We will want to loop from an `i` of `0` while `i` is less than the `length` of our `searchResults` array incrementing by one.

    ```javascript
    for (let i = 0; i < searchResults.length; i++) {
      }
    ```

  2. How do we reference each object inside of our loop?

    * We use bracket notation with `i` as our index to store the object into a variable.

    ```javascript
    row = searchResults[i];
    ```

  3. The file began with empty arrays for each `key`, which function can we use to add the respective values to the matching arrays?

    * The `.push()` function allows us to append each value to the matching arrays.

    ```javascript
    names.push(row.pair);
    greekNames.push(row.greekName);
    romanNames.push(row.romanName);
    greekSearchResults.push(row.greekSearchResults);
    romanSearchResults.push(row.romanSearchResults);
    ```

  4. For our traces, what are the `x` and `y` values for each trace?

    * For `trace1` the `x` is `names` and the `y` is `greekSearchResults`.

    * For `trace2` the `x` is `names` and the `y` is `romanSearchResults`. 

* Additionally explain that we set the:

  * `text` values to `greekNames` & `romanNames` to display them individually in the tool tip
  
  * `name` values to `Greek` and `Roman` for display in the legend.
  
* Lastly, point out the `layout` object we created, and that we set the `title` key-value pair to give our chart a descriptive title.

    ```javascript
    let layout = {
      title: "Greek vs Roman gods search results",
      barmode: "group"
    };
    ```

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Multiple+Trace+Charts&lessonpageTitle=Intro+to+JavaScript+Visualizations&lessonpageNumber=14.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F1%2FLessonPlan.md)</sub>

- - -

## 4. Preprocessing Data with Functions

| Activity Time:       1:00 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Preprocessing Data with Functions (15 mins)</strong></summary>

  * Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 35 - 42 to assist you with this module.

  * Open [functions.js](Activities/09-Ins_Functions/Solved/static/js/functions.js) and walk through the JavaScript code with students, touching specifically on how JavaScript functions are similar and different than Python functions.
  
  * Share or open the [functions.py](Activities/09-Ins_Functions/Solved/functions.py) for comparison if you feel it will help student understanding to review.

  * Compare and contrast JavaScript functions to Python functions and highlight the following:
    
    * Python function declarations begin with **def** and end with a colon, and the code belonging to the function is indented and written below the declaration:
    
      ```python
      def print_hello():
          print("Hello there!")
      ```
      
    * JavaScript functions are declared with the keyword **function**, and are immediately followed by the code of the function surrounded by curly braces:
    
      ```js
      function printHello() {
        console.log("Hello there!");
      }
      ```
      
    * Conventionally, the code inside a function is written in indented lines inside the curly braces, but, in fact, the entire function could be written on one line, for example:
    
      ```js
      function printHello() { console.log("Hello there!"); }
      ```
      
    * However, we don't recommend formatting it this way while writing code. Make sure the students understand that they should use indented lines, as we have done before with Python. This is the preferred method, as it makes the code more readable. 
    
    * JavaScript functions can be defined with parameters. For example:

      ```js
      function addition(a, b) {
        return a + b;
      }
      ```

    * Functions must be called to execute the code:

      ```js
      printHello();
      console.log(addition(44, 50));
      ```

    * Arrays can be passed to functions:

      ```js
      function listLoop(userList) {
        for (var i = 0; i < userList.length; i++) {
          console.log(userList[i]);
        }
      }

      var friends = ["Sarah", "Greg", "Cindy", "Jeff"];
      listLoop(friends);
      ```

    * Functions can call other functions:

      ```js
      // Functions can call other functions
      function doubleAddition(c, d) {
        var total = addition(c, d) * 2;

        return total;
      }

      // Log results of doubleAddition function
      console.log(doubleAddition(3, 4));
      ```

    * Finally, JavaScript also has several internal functions.

      ```js
      // Javascript built in functions
      var longDecimal = 112.34534454;
      var roundedDecimal = Math.floor(longDecimal);
      console.log(roundedDecimal);
      ```

  * Ask students if they have any questions before moving to the next activity.

</details>

<details>
  <summary><strong>✏️ 4.2 Students Do: Creating Functions (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 43 and 44 to present this activity to the students.

* In this activity, students create functions that will calculate the mean, variance, and standard deviation.

* The following file has the student instructions: [README](Activities/10-Stu_Creating-Functions/README.md).

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Creating Functions (5 mins)</strong></summary>

* Go over the [app.js](Activities/10-Stu_Creating-Functions/Solved/static/js/app.js) solution together as a class.

* Open [index.html](Activities/10-Stu_Creating-Functions/Solved/index.html) in a browser and open the Chrome Inspector console to display the results. Then open [app.js](Activities/10-Stu_Creating-Functions/Solved/static/js/app.js) in a text editor. 

* Because this activity is challenging, walk or code through the solution and highlight the following points:

  * First, a function called `mean` is created that accepts an array as an argument. This function iterates over the array, sums the values, and then divides by the length of the array.

    ```js
    function mean(arr) {
      var total = 0;
      for (var i = 0; i < arr.length; i++) {
        total += arr[i];
      }
      var meanValue = total / arr.length;

      return meanValue;
    }
    ```

  * Next, a function is defined to calculate variance. Variance can be found by subtracting the mean from each number, squaring the result, and then averaging the square differences.

    ```js
    function variance(arr) {
      var meanValue = mean(arr);
      var total = 0;

      for (var i = 0; i < arr.length; i++) {
        total += (arr[i] - meanValue) ** 2;
      }
      var varianceValue = total / arr.length;
      return varianceValue;
    }
    ```

  * Finally, a function is defined to calculate the standard deviation. This is just the square root of the variance.

    ```js
    function standardDeviation(arr) {
      var varianceValue = variance(arr);
      var standardDeviationValue = Math.sqrt(varianceValue);

      return standardDeviationValue;
    }
    ```

* Let students know that this activity was challenging, but there are statistical libraries that they can leverage in the future.

</details>

<details>
  <summary><strong>✏️ 4.4 Students Do: Preprocessing Data for Plotly (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1yR1qFEDzGV5YpQpEqdoYVfVecnJJ63MNCwBfFnqnqC4/edit?usp=sharing) and use slides 46 and 47 to present this activity to the students.

* In this activity, students will create functions that preprocess films from the Pagila database and create a bar chart of average values by age rating.

* The following file has the student instructions: [README](Activities/11-Stu_Preprocessing_Data_for_Plotly/README.md).

</details>

<details>
  <summary><strong>⭐ 4.5 Review: Preprocessing Data for Plotly (10 mins)</strong></summary>

* Go over the [plots.js](Activities/11-Stu_Preprocessing_Data_for_Plotly/Solved/plots.js) solution together as a class.

* Make sure to highlight the key concepts from this activity and ask students the following:

  1. How do we define a function in JavaScript?
     
      * We use the keyword `function` followed by the name of the function and a set of parentheses containing any arguments to be passed into the function.

      * Our arguments will be:
          * `books` to represent our books array.
          * `year` to equal the individual year we want to evaluate.
          * `metric` to be a string matching one of our 3 numeric keys.

      ```javascript
      function metricMean(books, year, metric) {
        }
      ```

  2. As we loop through the array of books, how do we evaluate only books for a specific year and collect the values for the specified metric?

      * For the year, we use an `if` statement and compare the key `Years` value for each book to the `year` argument provided in the function.
      
      * For the specified metric, we use bracket notation to access the key value associated with it. This allows us to select books matching the `year` in the `if` statement.
      
      * At this time, point out that we initialize the `count` and `total` variables with `0`. This allows us to increment them by the metric value and `1` respectively.  

      ```javascript
      let count = 0;
      let total = 0;
      for (let i = 0; i < books.length; i++) {
        row = books[i];
        if (row.Year == year){
          total += row[metric];
          count += 1
        }
      }
      ```
      
  3. At the conclusion of the function, how can we calculate the average metric value and pass the value to a variable?
  
    * We can calculate the `meanValue` by setting it equal to the `total` variable divided by the `count` variable.  
  
    * To pass the `meanValue` to a variable, we just need to `return` the value.
  
    ```javascript
      let meanValue = total / count;
  
    return meanValue;
    ```
  
* **Note:** Remind students that `bestSellers` comes from the [bestsellers.js](Activities/11-Stu_Preprocessing_Data_for_Plotly/Solved/bestsellers.js) file. You can open the file and show it to the students before the next question.
  
4. Now that we have our function, how can we use it to calculate the average `User Reviews` for each year individually?
   
      * We only need to declare a variable and set it equal to the output of our function with the matching arguments. 
    
    ```javascript
      let metric = "User Rating"
      let metric2009 = metricMean(bestSellers, 2009, metric)
      let metric2010 = metricMean(bestSellers, 2010, metric)
      let metric2011 = metricMean(bestSellers, 2011, metric)
      let metric2012 = metricMean(bestSellers, 2012, metric)
      let metric2013 = metricMean(bestSellers, 2013, metric)
      let metric2014 = metricMean(bestSellers, 2014, metric)
      let metric2015 = metricMean(bestSellers, 2015, metric)
      let metric2016 = metricMean(bestSellers, 2016, metric)
      let metric2017 = metricMean(bestSellers, 2017, metric)
      let metric2018 = metricMean(bestSellers, 2018, metric)
      let metric2019 = metricMean(bestSellers, 2019, metric)
    ```
    
  5. To create our line chart, we need an array of our average values. How can we create this with our 11 new variables?
     
      * We only need to create a new variable set equal to an array of the 11 variables. Each variable is separated by commas in the array.

    ```javascript
      let metricArray = [metric2009, metric2010, metric2011, metric2012, metric2013, metric2014, metric2015, metric2016, metric2017, metric2018, metric2019]
      ```

6. How can we construct a function to generate the Plotly line chart based on our new array?
   
      * At a minimum, we need to pass to our function our `metricArray` and the `years` array. Optionally, we can also pass our `metric` for `layout` purposes.
    
    * In our trace, the `x` value will be the `years` array, and `y` value will be the `metricArray`.
      
      * In the `layout` object, we also create a `title` using a template literal. This allows us to include the `metric` variable dynamically in the `title`.
    
    ```javascript
      function plotMetric(metricArray, years, metric){
    
      let trace1 = {
          x: years,
          y: metricArray,
          type: "line"
        }
    
      let data = [trace1]
    
      let layout = {
          title: `Amazon Best Sellers Average ${metric}`
        };
    
      Plotly.newPlot("plot", data, layout);
    
    }
    ```

  * Point out that we now need to execute the Plotly function with the proper arguments or else nothing will be charted.
  
* If time permits walk through the [refactored.js](Activities/11-Stu_Preprocessing_Data_for_Plotly/Solved/refactored.js) file to show how we can combine this all into a single simplified function.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Preprocessing+Data+with+Functions&lessonpageTitle=Intro+to+JavaScript+Visualizations&lessonpageNumber=14.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F1%2FLessonPlan.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
