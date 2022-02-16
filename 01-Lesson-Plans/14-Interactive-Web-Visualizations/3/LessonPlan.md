# 14.3 JavaScript with D3.js

## Overview

Today's lesson introduces students to DOM selection, manipulation, and events using [D3.js](https://d3js.org/). This enables students to add custom interactivity to their web visualizations. D3.js is an industry standard data visualization library written in JavaScript.

## Class Objectives
By the end of class, students will be able to:
* Create charts using data from API calls.
* Use D3 for basic document object model (DOM) manipulation and event handling.
* Apply the `this` keyword to reference elements within a function.
* Dynamically manipulate the DOM through events.
* Manipulate charts through dropdown events and click events.
* Use `Plotly.restyle()` to create dynamic charts.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* You may find that this lesson falls on a weekday due to a holiday shifting the course schedule. If this is the case, please review the notes included in this lesson to **easily adjust the length of the lesson to fit into a weekday class**.

  * Be on the lookout for a ⏰ **3-Hour Adjustment** note at the top of activities in this lesson plan. If this class is being taught on a weekday, please use the directions found in the note. Keep in mind that breaks will be reduced from 40 minutes to the typical 15 minutes for a weekday class as well.

  * Shortening these activities could potentially limit the students' ability to finish them, so please remind them they can attend office hours to clear up any questions they may have.
* Students will spend today's class working with data in JavaScript and learning how to manipulate the DOM with D3. The material covered today is intended to be an introduction to the DOM using helper methods from D3.
* Because this is the only the third day of a very rapid introduction to JavaScript, many students may be feeling overwhelmed. It is important to reassure students that it will take time (and lots of practice) to feel confident in these new skills.
* Today's class uses only a subset of D3.js to perform basic DOM manipulation and event handling. D3 is only being used as an aid to simplify interaction with the DOM. 
* Please remember that the slideshows are for instructor use only. When distributing slides to students, first export them to a PDF file. You may then distribute the PDF file through Slack. 

</details>

- - -

# Class Activities

## 1. Intro to D3 and D3.json

| Activity Time:       0:40 |  Elapsed Time:      0:40  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: D3.json (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slide 2 to go over today's class objectives. Use slide 3 to start introducing this module to the class. Note that this module can either be a live code (slides 4 and 5) or you can choose to walk through the demo (skip slide 4). 

* Begin by explaining that D3.js is an incredibly powerful visualization library written in JavaScript. Data professionals use it to create interactive data visualizations in browsers. However, D3 is a very large library with many different subsets. Today's class will focus on a subset of D3 used to select and create HTML elements dynamically. 

* You will use the following files during this activity: 

  * [index.html](Activities/01-Ins_Intro_to_D3/Solved/index.html)
  
  * [demo.js](Activities/01-Ins_Intro_to_D3/Solved/demo.js)

* Explain that D3.js has a function to fetch JSON data from APIs on the web.

* Visit the [SpaceX API](https://api.spacexdata.com/v3/launchpads) to show an example of JSON data. 

* Live code or walk through the demo and highlight the following, starting with [index.html](Activities/01-Ins_Intro_to_D3/Solved/index.html):

  * Demonstrate how to import D3 in the script tag, using a CDN link:

  ```javascript
    <script src="https://d3js.org/d3.v5.min.js"></script>
  ```

  * Then open [demo.js](Activities/01-Ins_Intro_to_D3/Solved/demo.js) and continue demoing

  * Explain that `d3.json` is similar to Python `requests.get`.

  * However, `d3.json` returns a JavaScript promise: meaning it places an API call to the `url`; then once it's available, the callback function prints it to the console. 

  ```javascript
  const dataPromise = d3.json(url);
  console.log("Data Promise: ", dataPromise);
  ```

* Use the second example to explain the concept of promises in JavaScript and how we can access the data:

  * The `dataPromise` variable is assigned a promise of future data, but the data must be accessed inside of the `.then` function.
  
  * Explain that normally, code is executed without delay. This means each operator in a sequence of commands is executed after the other, without any delays. But when making a call to a server for data, there may be a delay in the delivery of that data, because we are depending on the server--a computer out of our control--to perform its task. Unlike other programming languages that wait for data to be returned in these cases, JavaScript's default behavior is _not_ to wait. JavaScript is designed to execute a command and immediately move on. Obviously, that won't work when making calls to a server for data, specifically because the server may not return the data instantaneously. For these situations, JavaScript includes `promises` or operators that wait until a return value is supplied before advancing to the next operation. `d3.json()` is a `promise` that sends a request for data that may take time to resolve. The `.then()` operator takes over once the data has been returned by the `d3.json()` operator. Think of it this way: a `promise` first makes a request, and when the request is fulfilled, _then_ the code advances to the next set of operations. 
  
  * The argument, labeled here as `data` represents the accessible data from the API call. It is the data returned by the promise, and it is passed the `.then()` operator, which in turn is passed to an anonymous callback function inside the `.then()`. Once it is inside the callback function, we can do anything we want with it. And here, we're simply writing the data to the console: 

  ```javascript
  d3.json(url).then(function(data) {
      console.log(data);
  });
  ```

</details>

<details>
  <summary><strong>✏️ 1.2 Student Do: D3.json (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 6 and 7 to present this activity to the class.

* In this activity, students make API calls to SpaceX returning information about the [roadster](https://docs.spacexdata.com/#46951cda-bdf2-481b-9697-118b1cbccaba) and [capsules](https://docs.spacexdata.com/#d65a7f85-e0c7-41ce-b41d-9ad20a238d90).

* The following file has the student instructions: [README](Activities/02-Stu_D3_json/README.md).

</details>

<details>
  <summary><strong>⭐ 1.3 Review: D3.json (0:10)</strong></summary>

* Go over the [Stu_D3_json](Activities/02-Stu_D3_json/Solved/) solution together as a class.

* Make sure to highlight the key concepts from this activity and ask students the following:

  1. Which function must we chain to our API call to access the data?

      * We attach `.then()` to the API call so we can access the data through the callback function.

  2. How do we construct the callback function?

      * We use `function` and pass an argument such as `data` to represent the API call results.

      * We then place the function statement between curly brackets `{}` and can `console.log` the data or anything else we would like to do with the results. 

```javascript
// Fetch the JSON data and console log it
d3.json(roadster).then(function(data) {
  console.log(data);
});
```

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Intro+to+D3+and+D3.json&lessonpageTitle=JavaScript+with+D3.js&lessonpageNumber=14.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F3%2FLessonPlan.md)</sub>


- - -

## 2. D3 Select and Append

| Activity Time:       0:40 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: D3 Select & Append (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 9 - 14 in case you need to assistance while you live code. Otherwise, use slides 9 and 10.

* You will use the following files during this activity: 

  * [Activities/03-Ins_D3_Select/Solved/index.html](Activities/03-Ins_D3_Select/Solved/index.html)

  * [Activities/03-Ins_D3_Select/Solved/static/js/index.js](Activities/03-Ins_D3_Select/Solved/static/js/index.js)

* Live code this activity with the class. Make sure to pause frequently to check in with the students and allow them to catch up. 

* Inform students that we will now use D3 to manipulate DOM elements (elements of a web page).

* Similar to selecting DOM elements with `soup.find()` when web scraping with Beautiful Soup, D3 can be used to extract information from an HTML document and can change its contents and styling. 

* Advise students we are importing D3 in the script tag using a d3js.org link: 

  ```javascript
    <script src="https://d3js.org/d3.v5.min.js"></script>
  ```

* Explain that `d3.select()` can be used to get a reference to an element, then capture the text of that element. Open the console and show students the output.

* Remind students that in CSS and in JavaScript a period `.` is used for class selectors and a hash sign `#` is used for ID selectors. 

* Emphasize that the element is selected with the class name 'text1'. Then, the text of the element is captured by chaining that reference with the `.text()` method.

  ![Images/select1.png](Images/select1.png)

* Demo that the text of the element can be **changed**. Code the following line and refresh the browser:

  ```javascript
  s3.select(".text1").text("Hey, I changed this!")
  ```

  * The browser now reflects the change:

    ![Images/select4.png](Images/select4.png)

* Show how to capture the inner HTML of an element by using the `html()` method. 

  ![Images/select4a.png](Images/select4a.png)

* Next, demo how to select the **child** element of an element. Remind students that the DOM of a webpage is a tree structure of elements, so a `<div>` may contain an anchor (`<a>`) element, or a list (`<ol>`) can contain list items (`<li>`), etc.:

  ```javascript
    // Select an element's child element
    // An object is returned
    var mylinkAnchor = d3.select(".mylink>a");
    console.log(mylinkAnchor);
  ```

  * With `(".mylink>a")`, the anchor element contained within the div with the class name "mylink" is selected. Let students know that depending on the structure of the page they're working on, especially if they are working with other team members (web designers, front-end engineers, etc.) this may be the only way they're able to select the element they want. 

  * When `mylinkAnchor` is printed to the console, an object is returned with a number of properties of the element.

  ![Images/select6.png](Images/select6.png)

  * Using D3's `attr()` method, the `href` value can be accessed directly.

  ![Images/select7.png](Images/select7.png)

* Code the following line to change the `href`, then demonstrate by clicking the link to navigate the page to Python's home page:

  ```javascript
  mylinkAnchor.attr("href", "https://python.org")
  ```

* Code the following to demo chaining. Chaining allows the joining of multiple methods sequentially, thus multiple aspects of an element can be changed in a single block of code.

  ```javascript
  // Use chaining to join methods
  d3.select(".mylink>a").attr("href", "https://nytimes.org").text("Now this is a link to the NYT!!");
  ```

* Code the following to show that `selectAll()` can be used to select all elements with a certain tag, class, or id, and then change the style of those elements.

  ```javascript
  // Select all list items, then change their font color
  d3.selectAll("li").style("color", "blue");
  ```

* Code the following and show that D3 can be used to first select an element, then append a child element to it.

  ```javascript
  // Create a new element
  var li1 = d3.select("ul").append("li");
  li1.text("A new item has been added!")

  //Use chaining to create a new element and set its text
  var li2 = d3.select("ul").append("li").text("Another new item!");
  ```

* Take a moment to answer any remaining questions before moving on.

</details>

⏰ **3-Hour Adjustment**: Skip the **2.2 Students Do** activity and continue on to the 2.2 review activity.

<details>
  <summary><strong>✏️ 2.2 Students Do: D3 Select (15 mins)</strong></summary>

* ⏰ **3-Hour Adjustment**: Skip this **Students Do** activity and continue on to the review activity.

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 15 and 14 to present this activity to the class.

* In this activity, students use D3 to add a new row of data to a table.

* Ask how an HTML table is structured. If students cannot recall, remind them we worked with HTML tables in week 11 [11-Web/1/06-Stu_WorkingWithTables/Solved/index.html](../../11-Web/1/Activities/06-Stu_WorkingWithTables/Solved/index.html). Before the students start this activity, review this file with them. 

* The following file has the student instructions: [README](Activities/04-Stu_D3_Select/README.md).

</details>

<details>
  <summary><strong>⭐ 2.3 Review: D3 Select (10 mins)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

* You will use the following files during this activity:

  * [Activities/04-Stu_D3_Select/Solved/index.html](Activities/04-Stu_D3_Select/Solved/index.html)

  * [Activities/04-Stu_D3_Select/Solved/static/js/app.js](Activities/04-Stu_D3_Select/Solved/static/js/app.js)

* Open the files and point out the following:

  * The first step is to select the table and add the Bootstrap striped table class. Point out that this uses the same `.attr()` method we used previously to change the `href` of an anchor. 

    ```javascript
    var table = d3.select("table");
    table.attr("class", "table table-striped");
    ```

  * To add the new row of data, select the table body and then add the new table row.
  
    ```javascript
    var tbody = d3.select("tbody");
    var row = tbody.append("tr");
    ```
  
  * The row reference can be used to add a new table cell for the student name and grade. The student name is index position 0 while the student grade is index position 1.

    ```javascript
    row.append("td").text(newGrade[0]);
    row.append("td").text(newGrade[1]);
    ```

* If time permits, review the bonus and explain the following:

  * `forEach` can be used to iterate over each item in the array.

  * Arrays can be [destructured](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) in JavaScript assignments. This is similar to unpacking a tuple in Python.

    ```javascript
    // [student, grade] destructures (unpacks) the student name and grade
    // for each item in the array
    grades.forEach(([student, grade]) => {

      // Append one table row per student/grade
      var row = tbody.append("tr");

      // append one cell for the student and one cell for the grade
      row.append("td").text(student);
      row.append("td").text(grade);
    });
    ```

* Ask if there are any questions before proceeding to the next section.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+D3+Select+and+Append&lessonpageTitle=JavaScript+with+D3.js&lessonpageNumber=14.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F3%2FLessonPlan.md)</sub>

- - -

## 3. D3 Table and Event Listeners

| Activity Time:       0:40 |  Elapsed Time:      2:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: D3 Event Listeners (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 18 - 20 to introduce this module to the class and use slide 21 when ready to live code. 

* You will use the following files during this activity: 

  * [Activities/05-Ins_Event_Listeners/Solved/index.html](Activities/05-Ins_Event_Listeners/Solved/index.html)

  * [Activities/05-Ins_Event_Listeners/Solved/index.js](Activities/05-Ins_Event_Listeners/Solved/index.js)

* Explain that the activities so far have selected or appended elements in the HTML. This code is executed once upon loading the browser. What makes JavaScript really interesting is that it can listen for user events on the page and execute code when these events are detected. This provides an incredibly powerful mechanism for building dynamic and interactive applications.

* Inform the class that several event types are supported by the browser including:

  * `click`

  * `change`

  * `keydown`

  * `keyup`

  * `scroll`

  * `pointerenter`

  * `pointerleave`

  * and many more!

* Send out a reference to [web events](https://developer.mozilla.org/en-US/docs/Web/Events) so students can see the wide variety of event types available. 

* Before demoing any syntax, first explain that events have:

  * A target: a reference to the object that dispatched the event.

  * A handler: a function which should be executed in response to the event occurring.
  
* Open [Activities/05-Ins_Event_Listeners/Solved/index.html](Activities/05-Ins_Event_Listeners/Solved/index.html).

* Click the **Click Me!** button to show the dynamic nature of the button click.

* Open the Chrome Inspector console and demonstrate the different functions available in [Activities/05-Ins_Event_Listeners/Solved/index.js](Activities/05-Ins_Event_Listeners/Solved/index.js).

* Explain the following:

  * Event handlers are just normal functions that you call when an event occurs.

    ```javascript
    // This function is triggered when the button is clicked
    function handleClick() {
      console.log("A button was clicked!");

      // We can use d3 to see the object that dispatched the event
      console.log(d3.event.target);
    }
    ```

  * Events are attached using the `.on()` function in D3.

    ```javascript
    button.on("click", handleClick);
    ```

  * The event target is the object that triggered the event. This can be referenced with `d3.event.target`.

  * Event handlers can also be defined inline.

    ```javascript
    button.on("click", function() {
      console.log("Hi, a button was clicked!");
      console.log(d3.event.target);
    });
    ```

  * Event handlers are just normal functions that can execute code or call other functions.

    ```javascript
    button.on("click", function() {
      d3.select(".giphy-me").html("<img src='https://gph.to/2Krfn0w' alt='giphy'>");
    });
    ```

  * Input elements can trigger change events. The value of the element can be referenced with `d3.event.target.value`.

    ```javascript
    inputField.on("change", function() {
      var newText = d3.event.target.value;
      console.log(newText);
    });
    ```
  

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: Button Clicks (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 22 and 23 to present this activity to the class.

* In this activity, students use D3 to create click handlers for upvotes and downvotes.

* The following file has the student instructions: [README](Activities/06-Stu_Button_Click/README.md).

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Button Clicks (10 mins)</strong></summary>

* Open [Activities/06-Stu_Button_Click/Solved/static/js/app.js](Activities/06-Stu_Button_Click/Solved/static/js/app.js) and [Activities/06-Stu_Button_Click/Solved/index.html](Activities/06-Stu_Button_Click/Solved/index.html) while you highlight the following points:

  * The Star Wars episode number is created dynamically using `Math.floor` and `Math.random`.

    ```javascript
    var text = d3.select(".star-wars")
      .text(Math.floor(Math.random() * 9) + 1);
    ```

  * The upvote and downvote buttons are selected by their class names.

    ```javascript
    var upvote = d3.select(".upvote");
    var downvote = d3.select(".downvote");
    ```

  * The counter is also selected to get the current vote count.

    ```javascript
    var counter = d3.select(".counter");
    ```

  * Each button has its own click handler. The upvote will increment the count and the downvote will decrement the count.

  * Remind students that the addition assignment operator `+=` adds the value of the right to the variable and assigns the result to the variable.

    ```javascript
    upvote.on("click", function () {
      var currentCount = parseInt(counter.text());
      currentCount += 1;
      counter.text(currentCount);
    });
    ```

  * The counter value needs to be converted from text to an integer.

    ```javascript
    var currentCount = parseInt(counter.text());
    ```

* If time permits show that the bonus uses an array of arrays format to store the vote type and the current vote for each click.

  ```javascript
  var data = [];
  // ...
  data.push(["upvote", currentCount]);
  ```

* Answer any remaining questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+D3+Table+and+Event+Listeners&lessonpageTitle=JavaScript+with+D3.js&lessonpageNumber=14.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F3%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      2:40  |
|---------------------------|---------------------------|

⏰ **3-Hour Adjustment**: Break will be 15 minutes.

- - -


## 4. Introducing `this` and Forms

| Activity Time:       0:40 |  Elapsed Time:      3:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Introducing <code>this</code> (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 26 and 27 to present this activity to the class.

* You will use the following files during this activity: 

  * [Activities/07-Ins_This/Solved/index.html](Activities/07-Ins_This/Solved/index.html)

  * [Activities/07-Ins_This/Solved/app.js](Activities/07-Ins_This/Solved/app.js)

* Explain that in JavaScript, the `this`  keyword is the object that **owns** the code. That is, the object that invokes the function where `this` is used.

* The `this` keyword is useful to identify which element triggered an event. For example, `this` inside of an event handler would refer to the specific button that was clicked.

* Open `app.js` and walk through the through the first example:

  ```javascript
  d3.selectAll("button").on("click", function() {
    console.log(this);
  });
  ```

  * `d3.selectAll("button")` is used to select all buttons in the document.

  * When a button is clicked, a function is triggered that will log `this` to the console.

  * In this example, `this` will refer to the specific button that was clicked. There are multiple buttons on the page, but only the button that was clicked will be logged to the console.
  
* An important point to explain is that arrow functions do _not_ have a `this` keyword, and therefore must never be used in event listeners. The callback function in an event listener must always be a standard JavaScript function.

* Now we will go over the second code example. Open index.html in a browser and demo how clicking a list item turns it blue.

* Next, highlight the following points:

  ```javascript
  d3.selectAll("li").on("click", function() {
    var listItem = d3.select(this);
    listItem.style("color", "blue");

    var listItemText = listItem.text();
    console.log(listItemText);
  });
  ```

  * When an item is clicked, that particular `li` element is assigned to the variable `listItem` via `d3.select(this)`.

  * Selecting the element with D3 makes it possible to use D3 functions such as `style` or `text` on the element.

  * For example, its font color is changed to blue with `listItem.style("color", "blue");`.

* For more information about the `this` keyword, send students the [this & object prototypes](https://pepa.holla.cz/wp-content/uploads/2016/08/You-Don-t-Know-JS-this-Object-Prototypes.pdf) for their reference.


</details>

⏰ **3-Hour Adjustment**: Skip the **4.2 Students Do** activity and continue on to the 2.2 review activity.

<details>
  <summary><strong>✏️ 4.2 Students Do: <code>this</code> Button (15 mins)</strong></summary>
  
* ⏰ **3-Hour Adjustment**: Skip this **Students Do** activity and continue on to the review activity.

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 28 and 29 to present this activity to the class.

* In this activity, students will refactor the button activity with the `this` keyword.

* The following file has the student instructions: [README](Activities/08-Stu_This_Button/README.md).

</details>

<details>
  <summary><strong>⭐ 4.3 Review: <code>this</code> Button Clicks (10 mins)</strong></summary>

* ⏰ **3-Hour Adjustment**: This review activity is now an **Everyone Do**.

* Open [Activities/08-Stu_This_Button/Solved/static/js/app.js](Activities/08-Stu_This_Button/Solved/static/js/app.js) while you highlight the following points:

  * Remind students the Star Wars episode number is created dynamically using `Math.floor` and `Math.random`.

    ```javascript
    var text = d3.select(".star-wars")
      .text(Math.floor(Math.random() * 9) + 1);
    ```

  * The counter is selected to get the current vote count.

    ```javascript
    var counter = d3.select(".counter");
    ```

  * The upvote and downvote buttons are selected together by their element type.

    ```javascript
    d3.selectAll("button")
    ```

  * The selected buttons have one click handler. We can determine which button was clicked by using `.select(this)`. Then based on the `value` attribute assigned to the html element the buttons will increment or decrement the count.

    ```javascript
    d3.selectAll("button").on("click", function () {
        let button = d3.select(this);
        let vote = parseInt(button.attr('value'))
        let currentCount = parseInt(counter.text())
        currentCount += vote;
        counter.text(currentCount);
    });
    ```

  * Explain that we can access attributes like the values of the buttons using `.attr()`, and for each of our buttons they are respectively set to the increment of `1` and decrement of `-1`.

  * The value and counter still need to be converted from text to an integer so that we can add them together.

    ```javascript
    let vote = parseInt(button.attr('value'))
    let currentCount = parseInt(counter.text())
    currentCount += vote
    ```

  * Finally, we can update the counter the same way with the `text()` method.

    ```javascript
    counter.text(currentCount)
    ```

* Answer any remaining questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Introducing+%60this%60+and+Forms&lessonpageTitle=JavaScript+with+D3.js&lessonpageNumber=14.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F3%2FLessonPlan.md)</sub>

## 5. Dropdowns and Plotly
| Activity Time:       0:40 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: Dropdown Events and Plotly (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 31 and 32 to live code this module to the class.

* You will use the following files during this activity: [Activities/09-Ins_Dropdown_Events/Solved/](Activities/09-Ins_Dropdown_Events/Solved/).

* In this section, you'll demo how to use events on the DOM to modify plots. Events are the key to adding interactivity to web pages. 

* Open `index.html` in the browser and use the dropdown menu to toggle between two datasets:

  ![Images/events01.png](Images/events01.png)

* Note that selecting a different dataset will re-render the plot on the screen.

* Open `plots.js` and explain the code as follows:

  * By calling the `init()` function, a default dataset is displayed when the page is rendered:
  
  ```js
  function init() {
    data = [{
      x: [1, 2, 3, 4, 5],
      y: [1, 2, 4, 8, 16]
    }];
    Plotly.newPlot("plot", data);
  }
  ```

  * The `init()` function is called at the end of the script file.

  * Otherwise, everything in this function should be familiar. It renders a simple line chart in Plotly.

* Explain event handling. When a change takes place to the dropdown menu, the `updatePlotly()` function is called.

  ```js
  d3.selectAll("#selDataset").on("change", updatePlotly);
  ```

* Explain `function updatePlotly()`:

  ```js
  var dropdownMenu = d3.select("#selDataset");
  var dataset = dropdownMenu.property("value");
  ```

  * The dropdown menu is selected using D3, and then assigned to a variable, `dropdownMenu`.

  * The value of the dropdown menu item is also assigned to a variable, `dataset`.

* Explain that, after initializing `x` and `y` as empty arrays, their values are selected depending on the `value` of the dropdown menu selection:

  ```js
  var x = [];
  var y = [];

  if (dataset == 'dataset1') {
      x = [1, 2, 3, 4, 5];
      y = [1, 2, 4, 8, 16];
  }

  if (dataset == 'dataset2') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
  }
  ```

* Next, explain that when a change takes place in the DOM, instead of drawing a new plot in Plotly, the existing one is restyled:

  ```js
  Plotly.restyle("plot", "x", [x]);
  Plotly.restyle("plot", "y", [y]);
  ```
* Send students the link to the [Plotly documentation](https://plot.ly/javascript/plotlyjs-function-reference/#plotlyrestyle) and give your students a minute or two to review it.

  * According to the documentation, restyling an existing plot is faster than drawing a new one.

  * In this code, only the `x` and `y` arrays are modified.

* Summarize the key points of this example:

  * A default plot is rendered on the page.

  * A change takes place in the DOM when a dropdown menu item is selected.

  * A function is triggered with the DOM element's value as its argument.

  * The function uses Plotly's `restyle()` method to modify an existing plot.

* Answer any questions before moving on.

</details>

<details>
  <summary><strong>✏️ 5.2 Student Do: A Musical Pie (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1eqXJHKy7RYwE-ksGfbeEQn9FJ75B_gJvM_E6Wl7dCRY/edit?usp=sharing) and use slides 33 and 34 to present this activity to the class.

* In this activity, students will enhance their event handling chops by creating a dynamic pie chart using Plotly. When a country is selected from the dropdown menu, its dataset will be displayed in the browser.

* The following file has the student instructions: [README.md](Activities/10-Stu_Event_Final/README.md).

</details>

<details>
  <summary><strong>⭐ 5.3 Review: A Musical Pie (0:10)</strong></summary>

* Go over the [10-Stu_Event_Final/Solved](Activities/10-Stu_Event_Final/Solved) solution together as a class.

* Open `index.html` in a browser and show the finished product:

  ![Images/pie01.png](Images/pie01.png)
  
* Open `index.html` with a code editor and explain the code:

  ```html
    <select id="selDataset">
        <option value="us">United States</option>
        <option value="uk">UK</option>
        <option value="canada">Canada</option>
    </select>
  ```

  * `<select>` and `<option>` tags are used to create a dropdown menu.

  * The `value` attribute of each `option` specifies the country whose data will be selected and visualized.

* Open `data.js` and explain the structure of the dataset:

  ```js
  var data = {
  us: {
      Spotify: 19,
      Soundcloud: 5,
      Pandora: 8,
      Itunes: 30
  },
  ```

  * The objects are nested within an object by country.

  * From these objects, arrays of subscriber numbers and music provider labels will need to be created for Plotly.

* Open `plots.js` and explain the creation of the needed arrays:

  ```js
  // An array of each country's numbers
  var us = Object.values(data.us);
  var uk = Object.values(data.uk);
  var canada = Object.values(data.canada);

  // An array of music provider labels
  var labels = Object.keys(data.us);
  ```

  * Explain that the `Object.values()` functions are used to create arrays of subscriber numbers by country. Then explain that `Object.keys()` creates an array of music provider labels. 

  * Show how `data` is an object filled with an object for each of the 3 countries. Then show a single object such as `data.us`. 
  
  * Explain that `Object.values()` returns an array of all values within an object.  

  * Explain that `Object.keys()` returns an array of all keys within an object. 

  * If there are further questions regarding the functions direct students to the [documentation](https://javascript.info/keys-values-entries).

  * Because the objects are nested, it is possible to use the dot notation to specify the country, e.g., `data.us`.

  ```js
  var labels = Object.keys(data.us);
  ```

  * Similarly, an array of music provider labels is created with `Object.keys()`.

* Explain that `init()` displays the default U.S. pie chart:

  ```js
  function init() {
    var data = [{
      values: us,
      labels: labels,
      type: "pie"
    }];

    var layout = {
      height: 600,
      width: 800
    };

    Plotly.newPlot("pie", data, layout);
  }

  init();
  ```

* Explain that one change of the dropdown menu, `getData()`, is called:

  ```js
  d3.selectAll("#selDataset").on("change", getData);
  function getData() {
      var dropdownMenu = d3.select("#selDataset");
      var dataset = dropdownMenu.property("value");
      var data = [];

      if (dataset == 'us') {
        data = us;
      }
      else if (dataset == 'uk') {
        data = uk;
      }
      else if (dataset == 'canada') {
        data = canada;
      }
      updatePlotly(data);
  }
  ```

  * D3 is used to assign the dropdown menu and the dropdown menu selection to variables.

  * An empty array is initialized.

  * Then, the data array that matches the country is selected and passed on as an argument of the `updatePlotly()` function.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Dropdowns+and+Plotly&lessonpageTitle=JavaScript+with+D3.js&lessonpageNumber=14.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F3%2FLessonPlan.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
