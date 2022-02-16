# 14.2 Functional Programing for Data Processing

## Overview

Today's lesson introduces students to JavaScript methods that will help them organize and prepare data for charts in Plotly. As we've seen in prior weeks, data often needs to be prepared before it can be visualized. Here we will be taking advantage of some of the functional programming tools provided in JavaScript to prepare our data. Functional programming is used in many languages, and JavaScript provides a gentle introduction.

### Class Objectives
By the end of class, students will be able to:

* Apply map and filter to parse data.
* Create and use arrow functions to simplify code.
* Use `filter()` and arrow functions to manipulate and filter datasets.
* Use ES6 JavaScript methods.

### Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* In this lesson, we introduce students to functional programming methods in JavaScript through preprocessing data for a Plotly chart. Similar to the last lesson, concepts are first introduced in a purely JavaScript context. Students will then be asked to apply the concepts by processing data for a Plotly chart.

After each JavaScript functional programming method is introduced, there will be two student activities. The first activity, students will apply a simple JavaScript content. In the second activity, students will apply the concept to create a Plotly chart.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx).

* Please remember that the slideshows are for instructor use only. When distributing slides to students, first export them to a PDF file. You may then distribute the PDF file through Slack.

</details>

- - -

# Class Activities

## 1. Map Method

| Activity Time:       0:55 |  Elapsed Time:      0:55  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Map Method & Arrow Functions (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slide 2 to present today's class objectives and slide 3 to start presenting this module to the class. Use slides 4 and 5 to present `.map()` and 6 and 7 to present `arrow functions` to the class.

* You will use the following files during this activity: 

  * [Activities/01-Ins_Mapping/Solved/map.js](Activities/01-Ins_Mapping/Solved/map.js)

  * [Activities/01-Ins_Mapping/Solved/index.html](Activities/01-Ins_Mapping/Solved/index.html)

* This activity covers the use of the `.map()` function. This is an important activity because it introduces a powerful tool within the JavaScript arsenal: functional programming. Functional programming is a programming paradigm in many other languages, such as R, Scala, and even Python. **Note:** You can either demonstrate the code or have the class code along with you. 

* Begin by walking through the first example:


  * Explain that JavaScript makes heavy use of callback functions. A **callback function** is a function that is passed into another function or procedure. The callback takes the output of the outer function/procedure and processes it further. What happens with the result of that processing depends on the procedure that calls it. In the case of the `map` array operator, a new array is produced from the output of the callback function, and the original array is left unaltered.

  * Explain that the `.map()` method iterates over an array where the value returned in the callback function is added to the new array with the assignment operator `=`.

  ```javascript
  let theStagesOfJS = ["confidence", "sadness", "confusion", "realization", "debugging", "satisfaction"];
  
  let mapSimpleArray = theStagesOfJS.map(function(item) {
    return item;
  });
  
  console.log("Map:", mapSimpleArray);
  ```

  ![map1](Images/map1.png)

  * In this example, the `.map()` method created a new array that is an exact copy of the existing array.

* Walk through the following code example to demonstrate using `.map()` to provide an index position of the array:

  ```javascript
  let mapArrayWithIndex = theStagesOfJS.map(function(item, index) {
    return `Stage ${index}: ${item}`;
  });

  console.log("Map With Index:", mapArrayWithIndex);
  ```

  ![map2](Images/map2.png)

  * This is similar to `enumerate` in Python, where both the item and its index position is passed to the function.

  * Point out that the original array is unchanged, for example:

  ```javascript
  console.log("Original:", theStagesOfJS);
  ```

  ![map3](Images/map3.png)
  
* Explain how mapping over an array of objects is similar, and shows that we can use dot notation to access the key values:

  ```javascript
  let students = [
    {name: "Malcolm", score: 80},
    {name: "Zoe", score: 85},
    {name: "Kaylee", score: 99},
    {name: "Simon", score: 99},
    {name: "Wash", score: 79}
  ];

  let names = students.map(function(student) {
    return student.name;
  });

  console.log("Names:", names)
  ```

  ![map4](Images/map4.png)
  
  * With `.map()`, a new array was created from the original array. The new array holds student names.

* At this point reiterate that `.map()` creates a new array containing the results of the function called on each element in the original array.

* Point out how this is different than `forEach`, which executes a function on each element in an array, but does not create a new array unless specifically stated within the function.

* **Note:** For more information about the differences between these methods, you can send students the [Map vs. ForEach](https://codeburst.io/javascript-map-vs-foreach-f38111822c0f) article.

* Now briefly explain `arrow functions` to the class. Again, you can either demonstrate the code or have the class code along with you.

* Explain that the `arrow functions` teach techniques and syntax they will likely encounter in future data applications. Compact one-line functions make functional programming easier to read and use. 

* Begin by explaining that an `arrow function` is a new and concise syntax for JavaScript functions.

  * Arrow functions allow us to drop the `function` keyword and only show the parameters, for example:

  ```javascript
  let mapArrow1 = theStagesOfJS.map((item) => {
    return item;
  });
  ```

  ![arrow1](Images/arrow1.png)

  * Note that the fat arrow `=>` that was added indicates an arrow function.

* In the next example, demonstrate we can further simplify the function by removing the curly braces and `return statement` as follows:

  ```javascript
  let mapArrow2 = theStagesOfJS.map(item => item);
  ```

  ![arrow2](Images/arrow2.png)

* Explain that the first `item` on the left of the arrow is the name of the function parameter, and the second item is the returned value. Compare this code to the original function.

* Next, demonstrate an arrow function with more than one parameter:

  ```javascript
  let mapArrow3 = theStagesOfJS.map((item, index) => `Stage ${index}: ${item}`);
  ```

  ![arrow3](Images/arrow3.png)

  * Note that the parentheses are still in use when a function is called on two parameters.

* Ask students if they have any questions before moving to the next activity.

</details>

<details>
  <summary><strong>✏️ 1.2 Students Do: Mapping (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 8 and 9 to present this activity to the class.

* In this activity, students create an array of names from the princesses array and an array of strings for each princess including their name and age.

* The following file has the student instructions: [README](Activities/02-Stu_Mapping/README.md).

</details>

<details>
  <summary><strong>⭐ 1.3 Review: Mapping (5 mins)</strong></summary>

![Princess Mapping](Images/princess_map.png)

* Go over the  [Stu_Mapping](Activities/02-Stu_Mapping/Solved/) solution together as a class.

* Make sure to highlight key concepts from this activity and ask students the following:

  1. How do we apply a map function to an array?

      * We attach `.map()` to the array we want to iterate over.

  2. How do we construct the callback function?

      * We use `function` and pass the iterated value as a parameter, in this case `princess`.

      * We then place the function statement between curly brackets `{}` and use `return` to assign a value to the new array.

```javascript
// Create an array of just the names from the princesses array
let names = princesses.map(function(princess) {
  return princess.name;
});
console.log("Names:", names);
```
* Next, ask the students what is different in creating the array of strings?

* Explain we return a string literal instead, passing our variables into the string by using backticks \` and identifying each variable with `${}`, for example:

```javascript
// Create an array of strings for each princess name, followed by a colon, followed by their age
let namesAndAges = princesses.map(function(princess) {
  return `${princess.name}: ${princess.age}`;
});
console.log("Names and Ages:", namesAndAges);
```

* (Optional) Show the students how the second array could be created with arrow functions:

```javascript
let namesAndAgesArrow = princesses.map(princess => `${princess.name}: ${princess.age}`);

console.log("Names and Ages:", namesAndAgesArrow);
```

</details>

<details>
  <summary><strong>✏️ 1.4 Students Do: Mapping with Plotly (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 11 and 12 to present this activity to the class.

* In this activity, students create a bar chart of Greek god search results using `.map()` and Plotly.

* The following file has the student instructions: [README](Activities/03_Stu_Greek_Mapping/README.md).

</details>

<details>
  <summary><strong>⭐ 1.5 Review: Mapping with Plotly (5 mins)</strong></summary>

![Greek Mapping](Images/greek_map.png)

* Go over the [Stu_Greek_Mapping](Activities/03_Stu_Greek_Mapping/Solved) solution together as a class.

* Make sure to highlight the key concepts from this activity and ask students the following:

  1. Which key in the array of objects includes our name values?

    * The `greekName` key returns the name of the Greek god.

    * Confirm this by opening the Chrome inspector console.

  2. Which key in the array of objects includes our search values?

    * The `greekSearchResults` key returns the value of the Greek god search results.

  3. How do we construct these callback functions?
  
    * We use `function` and pass the iterator parameter `row` followed by curly brackets `{}` with `return row.greekName` to populate a `names` array. This is the longer notation for callback functions. Later, when we create our `trace1` object, we use fat arrow notation for the callback, and we use `return row.greekSearchResults` in that callback to retrieve search results.

    ```javascript
    // Greek god names
    names = data.map(function (row){
      return row.greekName
    });
    
    // In the trace1 object:
    y: data.map(row => row.greekSearchResults)
    ```

  4. What are the 3 necessary key values pairs for our trace object?

    * We need to provide an `x` array, `y` array, and `type: "bar"` key value pairs.
    
    * Make sure the students understand that the `.map()` function returns a new array that is populated with the callback function inside of it. The `x` and `y` variables will therefore hold arrays that hold the return values of the callbacks.

    * Demonstrate how instead of using the `x` and `y` variables we can easily use a single line arrow function directly within the trace.

    ```javascript
    // Trace for the Greek data
    let trace1 = {
        x: data.map(row => row.greekName),
        y: data.map(row => row.greekSearchResults),
        type: "bar"
      };
    ```

  5. What do we need to do before we can pass our trace to the `.newPlot()` function?
  
    * Create an array of our trace values, and reiterate that this is required even if we only have 1 trace, i.e., the `traceData` needs to be in an array, regardless.

    ```javascript
    // Data trace array
    let traceData = [trace1];
    ```

  6. What object do we need to create if we want to add a title to the chart?

    * We need a `layout` object with the key `title` and a value of the chart title to use.

    ```javascript
    // Apply the group barmode to the layout
    let layout = {
      title: "Greek gods search results"
    };
    ```

  7. How do we render the plot to our div with the id of "plot"?
  
    * We use the `Plotly.newPlot()` function. For arguments, we first reference the `div` in the HTML with an id of "plot", then our data trace array, and finally the layout object.

    ```javascript
    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("plot", traceData, layout);
    ```

</details>


<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Map+Method&lessonpageTitle=Functional+Programing+for+Data+Processing&lessonpageNumber=14.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F2%2FLessonPlan.md)</sub>

- - -

## 2. Filter Method

| Activity Time:       0:55 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Filter Method (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 14 - 16 to present this module to the class.

* You will use the following files during this activity:

  * [Activities/04-Ins_Filtering/Solved/filter.js](Activities/04-Ins_Filtering/Solved/filter.js)

  * [Activities/04-Ins_Filtering/Solved/index.html](Activities/04-Ins_Filtering/Solved/index.html)

* This activity explains the `filter` function. You can either demonstrate the code or have the class code along with you.

* Open the Chrome inspector console to show that the `.filter` method created a new array that is a filtered subset of the `simpsons` array:

  ![filter1](Images/filter1.png)
  
* Explain that the `filter` iterates over an array. It passes each element of the array to a callback function whose return value is either true or false. When the return value is true, the current array element is added to a new array, which is the end product of the `filter` method. We save the new array to a variable using the `=` assignment operator. `filter` is therefore used when we need a new array composed of elements of an existing array, but whose elements must fit a specific criteria.

* Explain that we create a custom callback function for testing elements of our array against a criteria. It will be passed as the argument to the filter function as the callback function. Notice that it returns a Boolean value.

  ```javascript
  function selectYounger(person) {
    return person.age < 30;
  }
  ```

* Once we've created the function, we pass it as the sole argument of our `.filter()` method. The`filter` will then return a new array composed of elements from the original array that match the criteria in the callback function.

  ```javascript
  let youngSimpsons = simpsons.filter(selectYounger);
  ```

</details>

<details>
  <summary><strong>✏️ 2.2 Students Do: Filtering (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 17 and 18 to present this activity to the class.

* In this activity, students create a custom function to return the players who made the team and how many there were.

* The following file has the student instructions: [README](Activities/05-Stu_Filtering/README.md).

</details>

<details>

  <summary><strong>⭐ 2.3 Review: Filtering (5 mins)</strong></summary>

* Go over the [Stu_Filtering](Activities/05-Stu_Filtering/Solved) solution together as a class.

* Make sure to highlight key concepts from this activity and ask students the following:

  1. For our custom filter function, which key will we evaluate?

    * The `madeTeam` key returns the boolean `True` value for players who made the team.

    * Confirm this by opening the inspector console and show the resulting array of objects.

    ![Team Filter](Images/team_filter.png)

  2. For our custom filter function, what will we return?

    * Students may first suggest `player.team == True`.

    * Be sure to point out a more concise way to express a Boolean conditional would simply be `return player.madeTeam`.

    ```javascript
    function madeCut(player) {
      return player.madeTeam;
    }
    ```

  3. How can we count the number of players who made the cut?
  
    * Some students may have done this the hard way, i.e., by creating a counter variable and a conditional statement within the `filter` function to iterate the counter.

    * Although a counter variable will work, the simpler solution is to use `.length` on our output array.

    ```javascript
    let numberOfPlayers = playersOnTeam.length;
    console.log(`${numberOfPlayers} players made the team.`);
    ```

</details>

<details>
  <summary><strong>✏️ 2.4 Students Do: Filtering with Plotly (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 20 and 21 to present this activity to the class.

* In this activity, students create a bar chart of top Roman god search results using `.filter()` and Plotly.
  
* The following file has the student instructions: [README](Activities/06-Stu_Popular_Roman_Gods/README.md).

</details>

<details>
  <summary><strong>⭐ 2.5 Review: Filtering with Plotly (5 mins)</strong></summary>

![Roman Filtering](Images/roman_filter.png)

* Go over the [Stu_Popular_Roman_Gods](Activities/03-Stu_Popular_Roman_Gods/Solved) solution together as a class.

* Make sure to highlight key concepts from this activity and ask students the following:

  1. For our custom filter function which key will we evaluate and what will we return?

    * The `romanSearchResults` key returns the number of search results for each Roman god.

    * In the filter function, we will `return player.romanSearchResults > 1000000`.

    ```javascript
    function popular(roman) {
      return roman.romanSearchResults > 1000000;
    }
    ```

  2. How do we call the custom function on the dataset?
  
  
    * Remind students that similar to `.map()`, we chain `.filter()` to the dataset, and to call the function we pass it as the argument.

    ```javascript
    let popularRomans = data.filter(popular);
    ```
  
  * Demonstrate how the rest of the solution is nearly identical to the mapping activity. The only difference is that we are using the filtered dataset and the new `x` & `y` keys to create our trace values.

  ```javascript
  // Trace for the Roman data
  let trace1 = {
      x: popularRomans.map(row => row.romanName),
      y: popularRomans.map(row => row.romanSearchResults),
      type: "bar"
  };

  // Data trace array
  let traceData = [trace1];

  // Apply title to the layout
  let layout = {
    title: "Popular Roman gods search results"
  };

  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("plot", traceData, layout);
  ```

</details>


<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Filter+Method&lessonpageTitle=Functional+Programing+for+Data+Processing&lessonpageNumber=14.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F2%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      2:05  |
|---------------------------|---------------------------|

- - -

## 3. Sorting and Slicing

| Activity Time:       0:55 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Sorting and Slicing Methods (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 24 and 25 to present this module to the class.

* You will use the following files during this activity:

  * [Activities/07-Ins_Sort_and_Slice/Solved/slicing.js](Activities/07-Ins_Sort_and_Slice/Solved/slicing.js)

  * [Activities/07-Ins_Sort_and_Slice/Solved/sorting.js](Activities/07-Ins_Sort_and_Slice/Solved/sorting.js)

  * [Activities/07-Ins_Sort_and_Slice/Solved/index.html](Activities/07-Ins_Sort_and_Slice/Solved/index.html)
  
* This activity covers the use of the `sort` & `slice` functions. We recommend that you live code the sorting activity because the concept of using a comparator function will be new to students and may take more time and explanation for students to absorb. 

* Open `sorting.js` and use `index.html` to display the results. Cover the following points:

  * When working with data, it is often necessary to sort the data, either in ascending or descending order.

  * To sort an array in JavaScript, we call its `sort()` method.

  * By default, the `sort()` method converts the entries of the array to strings, and sorts the elements of the array in dictionary order.

  * For most instances, when we call `sort`, we must pass it a callback function specifying _how_ to sort.
  
  * Here we are passing a named function, `compareFunction`, as the callback function. But we could have passed in an anonymous function, i.e., a function lacking a name. Also, we could declare `compareFunction` elsewhere in our JavaScript and simply pass in the name of the function. Any one of these methods would work:

  ```js
  // Version with named callback function in place as the argument to sort()
  let sortedAscending = [3, 2, 1].sort(function compareFunction(firstNum, secondNum) {
    return firstNum - secondNum;
  });
  
  // Version with anonymous callback function:
  let anonymousSortedAscending = [3, 2, 1].sort(function (firstNum, secondNum) {
    return firstNum - secondNum;
  });
  
  // Version calling a function declared elsewhere in the code:
  function compare(firstNum, secondNum) {
    return firstNum - secondNum;
  };
  
  let sortedAscendingAnotherWay = [3, 2, 1].sort(compare);
    
  ```

* Explain that to produce a descending numerical sort, subtract the first argument from the second argument in the callback function:

  ```js
  // Subtract the first argument from the second argument to produce a descending sort:
  let sortedDescending = [3, 2, 1].sort(function (firstNum, secondNum) {
    return secondNum - firstNum;
  });
  ```
* Reiterate here that we're subtracting the second argument from the first argument to produce an ascending sort, and this version is what we're using going forward:

  ```js
  // Subtract the second argument from the first argument to produce an ascending sort:
  let sortedAscending = [3, 2, 1].sort(function (firstNum, secondNum) {
    return firstNum - secondNum;
  });
  ```
  
* Explain that regardless of the sort direction (ascending or descending) `compareFunction` compares two values at a time.

  * In this example, `compareFunction` first compares 3 and 2. The parameters `firstNum` and `secondNum` are arbitrary names, but there must be two arguments.

  * The callback function returns `firstNum - secondNum`. In this case, since `firstNum`, 3, is greater than `secondNum`, 2, it returns a positive number.

  * If the compare function returns a _positive_ number for a given pair of numbers `[firstNum, secondNum]`, it will put them in the _reverse order_ in the final array: `[secondNum, firstNum]`.

  * Likewise, if the compare function returns a _negative_ number for a given pair `[firstNum, secondNum]`, it will preserve their order in the output array: `[firstNum, secondNum]`.
  
  * The `compareFunction` continues comparing values in the array, two at a time, until all values have been compared and the array is sorted.

* Emphasize that `sort` modifies the array it's called on _in place_. This means that the original array itself is revised. This is in contrast to `filter()` and `.map()`, which create new arrays for their output and leave the original array untouched. Because `sort()` alters the original array, it is often safer to sort a _copy_ of an array rather than the input itself.

* Open the `index.html` to display the output.

* Next, discuss the `slice()` method. Open `slicing.js` and explain the code:

  ```js
  let names = ["Jane", "John", "Jimbo", "Jedediah"];
  let left = names.slice(0, 2);
  ```

* Explain that the `slice()` method is similar to slicing a list in Python: it allows cutting a subsection of a JavaScript array.
  
  * `slice()` does not affect the original array: it produces a new array that must be saved as a variable for subsequent use, just like `filter()` and `.map()`.
  
  * `slice()` takes two arguments. The first is the index position of the subsection. The second is the index position, up to which the slicing will take place. Note that the value at the second index is not included in the slice.

  * In this case, slicing begins at index position 0 and continues up to, but not including, index position 2.

* Finally, explain the `reverse()` method: it simply reverses the order of an array _in place_, again meaning that it alters the original array.

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: Sorting and Slicing (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 26 and 27 to present this activity to the class.

* In this activity, students sort, slice, and reverse an array.

* The following file has the student instructions: [README](Activities/08-Stu_Sort_and_Slice/README.md).

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Sorting and Slicing (5 mins)</strong></summary>

* Go over the [Stu_Sort_and_Slice](Activities/08-Stu_Sort_and_Slice/Solved) solution together as a class.

* Open up `sliceSort.js`. First, explain the `sort()` method:

  ```js
  let sorted = numArray.sort(function sortFunction(a, b) {
      return b - a;
  });
  ```

  * The `sort()` method calls another function as an argument.

  * The custom `sortFunction()` here compares two numbers at a time and returns `b - a`.

  * If the custom function returns a positive number, it _reverses_ the order of the two numbers. That is, if `a` is 1, and `b` is 100, `b - a` is a positive number, so the order is reversed.

* Explain that `reverse()` reverses the order of an array.

  ```js
  let reversedArray = sorted.reverse();
  ```

* Point out that slicing from index position 0 of an array, up to but not including index position 5, yields the first 5 elements of an array:

  ```js
  let sliced = sortedAscending.slice(0, 5);
  ```

</details>

<details>
  <summary><strong>✏️ 3.4 Students Do: Sorting and Slicing with Plotly (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1MtQDtKAutQTt94ASpPVK1vnA-HUx9f7HnSiHJomWkZM/edit?usp=sharing) and use slides 29 and 30 to present this activity to the class.

* In this activity, students sort, slice, and reverse an array of Greek god search results to build a horizontal bar chart.

* The following file has the student instructions: [README.md](Activities/09-Stu_Top_Ten_Greek_Gods/README.md).

</details>

<details>
  <summary><strong>⭐ 3.5 Review: Sorting and Slicing with Plotly (5 mins)</strong></summary>

  ![Greek Top Ten](Images/greek_top_ten.png)

  * Go over the  [Stu_Top_Ten_Greek_Gods](Activities/09-Stu_Top_Ten_Greek_Gods/Solved) solution together as a class.

  * Open `index.html` and show students the chart.

  * Next, remind students the `data` is an array of objects. 

  * Due to the complexity of sorting, walk students through the solution.
  
  * To start the objects need to be sorted by the `greekSearchResults` property.

    ```js
    let sortedByGreekSearch = data.sort((a, b) => b.greekSearchResults - a.greekSearchResults);
    ```

  * Explain that `slice()` and `reverse()` are used to select the first 10 elements of the sorted dataset, and then reverse their order:

    ```js
    slicedData = sortedByGreekSearch.slice(0, 10);
    reversedData = slicedData.reverse();
    ```

    * The array was reversed to accommodate Plotly's plotting conventions: it builds a horizontal bar chart from bottom to top.

    * The array can be sorted in ascending order instead.

  * Point out that `orientation: h` in `trace1` creates a horizontal bar chart.

    **Note:** Remind students that they had to consult the Plotly documentation for this activity, and that Plotly's documentation is straightforward to use. Plotly has a wide breadth of functionality beyond the scope of this class, but students can rely on Plotly's documentation for their own self-directed learning.

  * Explain that we can set the size of the margins in the `layout` object to accommodate for the name lengths.

  * Ask the students if they have any questions.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Sorting+and+Slicing&lessonpageTitle=Functional+Programing+for+Data+Processing&lessonpageNumber=14.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F14-Interactive-Web-Visualizations%2F2%2FLessonPlan.md)</sub>

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.

