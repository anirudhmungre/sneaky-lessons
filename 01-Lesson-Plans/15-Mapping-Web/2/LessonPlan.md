# 15.2 GeoJSON and Leaflet Plugins

## Overview

We'll spend today's class furthering our knowledge of GeoJSON and learning about the wonders of Leaflet plugins.

## Class Objectives

By the end of today's class, students will be able to:

* Leverage Leaflet.js plugins and other third-party libraries.
* Differentiate between maps and map elements for visualizing different datasets.
* Create and deploy custom interactive dashboards.

## Instructor Prep

<details>
    <summary><strong>Instructor Priorities</strong></summary>

By the end of today's class, students will be able to:

* Create maps using GeoJSON.
* Use Leaflet plugins and third-party libraries. 
* Apply different map styles based on the data type. 

</details>

<details>
    <summary><strong>Instructor Notes</strong></summary>

* Today, we'll do many exercises and move fairly quickly. If you want, you can allow the students to work in pairs on the student exercises.

* Make sure to look over the exercises before coming to class!

</details>

- - -

# Class Activities

## 1. Welcome and Map the NYC Neighborhoods

| Activity Time:       0:25 |  Elapsed Time:      0:25  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 1.1 Instructor Do: Welcome the Students</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slides 3 and 4 to welcome your students to the class, and address any lingering questions that they might have from the last class. Also, take this opportunity to give your students an overview of today's class using slide 2.

* Today, we'll continue our discussion of GeoJSON and learn how to extend the functionality of Leaflet with third-party plugins!

</details>

<details>
    <summary><strong>📣 1.2 Instructor Do: Review GeoJSON (0:05)</strong></summary>
    
* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slides 5 and 6 to assist you with this review.

* Open the [earthquake GeoJSON data](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson) from the last class.

* Once again, note that this link shows us all the earthquakes that have occurred during the past hour across the globe.

* Reiterate that the GeoJSON data includes a `features` array that contains both geographic data (`geometry`) and descriptive information (`properties`). In this case, each earthquake is a feature. In addition to the geographical data about where it occurred, the time, magnitude, and other information are present about each earthquake.

</details>

<details>
    <summary><strong>🎉 1.3 Everyone Do: Map the NYC Neighborhoods (0:20)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slides 7 and 8 to live code this lesson with the class.

* Let's dive right into an example that uses advanced Leaflet and GeoJSON functionality.

* We'll build a map of New York City that's broken down by boroughs and neighborhoods. The students will first make a basic map of the data. We'll then learn to enrich the map as a class by using the [BasicNYCBoroughs activity code](Activities/01-Evr_BasicNYCBoroughs). The following image shows the basic map:

    ![A screenshot depicts the starting map of the NYC boroughs and neighborhoods.](Images/Boroughs_Start.png)

    **Important:** We'll work with four JavaScript files. To access the different steps, modify your HTML file to use a different `logic.js` file.

* We will be using a [static version of the data](https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/15-Mapping-Web/nyc.geojson) originally from [BetaNYC](https://data.beta.nyc/dataset/pediacities-nyc-neighborhoods). A live version can be accessed from [this direct link](https://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson)

* Use D3 to retrieve our data like we did during the last class. 

* Just like in the last example, we have an array of features. Each feature is an object that contains properties (in this case, neighborhood information) and geometry (where it fits on the map).

* We now have our map! It's not particularly descriptive, however, so let's add custom styling. To do so, complete the following steps:

  1. Open [logic2.js](./Activities/01-Evr_BasicNYCBoroughs/Solved/static/js/logic2.js) to get the logic for the next version of the map, and then review the code.

  2. We can style features by passing a style object. We can change the border, fill, color, opacity, and more. (For sample stylings, refer to the [Leaflet Path options](https://leafletjs.com/reference-1.6.0.html#path).) Take a moment to change the style a bit.

* Be aware that another way exists to set the style of a feature. Open [logic3.js](./Activities/01-Evr_BasicNYCBoroughs/Solved/static/js/logic3.js) to get the next version of the map logic, and then note the following:

  * In this version, we pass in a function that can style individual features based on their properties.

  * If we look back at the GeoJSON, we can see that each feature has the `borough` property, which we can access through `feature.properties.borough`.

  * We have written a function that uses `if-else` statements to return different colors based on the borough that the neighborhood belongs to.

  * Each feature is styled by using this function, so all our boroughs will be color coded! The following image shows this map of the NYC boroughs and neighborhoods:

    ![A screenshot depicts the map.](Images/Boroughs.png)

* For the last step in completing our map, we'll add some interaction. Specifically, we'll add mouse events by using the [`onEachFeature`](https://leafletjs.com/reference-1.6.0.html#geojson-oneachfeature) option. You can find the code that includes this option in [logic4.js](./Activities/01-Evr_BasicNYCBoroughs/Solved/static/js/logic4.js). Notice the following:

  * The `onEachFeature` option will call the supplied function on every feature&mdash;essentially, looping through all the neighborhoods. This is useful because we want to bind some mouse events to all our neighborhoods.

  * We also have access to several events that we can subscribe to. We set events that will trigger on `mouseover`, `mouseout`, and `click`. On `mouseover` and `mouseout`, we want to change the opacity of the feature so that it has a nice highlight effect.

  * Our `click` function calls the [fitBounds()](https://leafletjs.com/reference-1.6.0.html#map-fitbounds) function on our clicked feature.

  * Finally, we want to bind a popup so that when someone clicks a neighborhood, its name and the borough that it belongs to display.

* Check with your students to see if they have any questions. Answer them all to the best of your ability before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+and+Map+the+NYC+Neighborhoods&lessonpageTitle=GeoJSON+and+Leaflet+Plugins&lessonpageNumber=15.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F2%2FLessonPlan.md)</sub>

## 2. Intro to Plugins

| Activity Time:       0:15 |  Elapsed Time:      0:40  |
|---------------------------|---------------------------|

<details>
    <summary><strong>🎉 2.1 Everyone Do: Create a Heat Map of Crime in San Francisco (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slides 9 and 10 to live code this lesson with the class.

* Explain the Leaflet is designed to be a lightweight and fast library. It focuses on only a core set of features. Through the use of plugins, however, we can add functionality to Leaflet.

  **Note:** A **plugin** is a third-party library that integrates with Leaflet to add one or more features. We can create heat maps, map our data as a function of time, and so much more!

* Point the students to the [Leaflet Plugins](https://Leafletjs.com/plugins.html) documentation, and let them spend a few minutes looking at the possibilities that plugins can offer.

* Our next activity as a class will focus on plotting some basic data with vanilla Leaflet and then adding a third-party plugin to make a marvelous (and insightful) map!

  **Note:** You can find all the solution files for this activity in the [Solved](./Activities/02-Evr_CrimeHeatmap/Solved) folder, but do your best to code this activity live.

* In this exercise, we'll visualize historical crime data for San Francisco. All this information and more is available on [DataSF](https://data.sfgov.org/), which is an open data site for San Francisco. Complete the following steps:

  * Find our specific dataset at [Police Department Incident Reports: Historical 2003 to May 2018](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry). Distribute this link, and make sure that your class is following along with you!

  * Click `API` to reveal the API endpoint.

  * Although we're using JSON, the data can be exported in other formats, such as comma-separated values (CSV) and XML. Today, however, we'll use only JSON.

* Explain that the next step is to use D3 to get this data and then plot it. The following image shows the resulting map of crime in San Francisco with vanilla markers:

  ![A screenshot depicts the map.](Images/Crime_Before.png)

* It's now time to add our plugin! For this activity, we'll use [Leaflet.heat](https://github.com/Leaflet/Leaflet.heat) to make a heat map. Distribute this link to your students, or have them find it on the plugin page. Then complete the following steps:

  1. As stated in the documentation, all we have to do to use the Leaflet.heat plugin is download the `Leaflet.heat.js` file and then link to it in our project HTML file.

  2. In `index.html`, comment out the `just-crime.js` script, and then uncomment the `heatmap.js` script.

  3. The documentation tells us that we need to create a new type of layer, a `heatLayer`, and pass it an array of points. Consider asking the students how to implement this plugin by looking at its repository. Reading and parsing documentation is an important skill for any developer!

  4. Instead of adding a marker to the map, we loop through the data and push it to an array. We pass that array of points along with some options into the `heatLayer`, and then we add it to the map.

  5. Point out that in the finished file, we made additional changes by modifying `radius` and `blur` while also increasing the record count to 10,000! (Refer to [The $limit Parameter | Socrata](https://dev.socrata.com/docs/queries/limit.html).) Ask the students what other options we could have modified, according to the [Socrata documentation](https://dev.socrata.com/docs/queries/).

  6. The following image shows our heat map of crime in San Francisco!

      ![A screenshot depicts the heat map.](Images/Heatmap.png)

* Check with your students to find out if they have any questions. Answer them all to the best of your ability before moving on.
  
</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Intro+to+Plugins&lessonpageTitle=GeoJSON+and+Leaflet+Plugins&lessonpageNumber=15.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F2%2FLessonPlan.md)</sub>

## 3. Map Rodent Clusters

| Activity Time:       0:40 |  Elapsed Time:      1:20  |
|---------------------------|---------------------------|

<details>
    <summary><strong>✏️ 3.1 Students Do: Map Rodent Clusters (0:30)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slides 11 and 12 to present this activity to the class.

* In this activity, the students will be working solo. They'll get data from the ([NYC Open Data](https://data.cityofnewyork.us/)) website and then plot it with the help of a Leaflet plugin. Feel free to let them work in pairs, because this topic can be challenging.

* Consider spending a few minutes demonstrating how to build a URL on the NYC Open Data website with the needed endpoints.

* For the starter files, go to the [Unsolved](./Activities/03-Stu_MarkerClusters/Unsolved) folder for this activity.

* For the activity instructions, go to the [README](./Activities/03-Stu_MarkerClusters/README.md) file for this activity.

  **Hint:** The students might want to spend time studying both the [NYC Open Data API](https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9) and Socrata queries, such as those that use the [$where parameter](https://dev.socrata.com/docs/queries/where.html).

</details>

<details>
    <summary><strong>⭐ 3.2 Review: Map Rodent Clusters (0:10)</strong></summary>

* Distribute the [solution files](./Activities/03-Stu_MarkerClusters/Solved) to the class, and then review the previous activity, making sure to answer any questions that your class might have.

* Be sure to point out that debugging on a small batch of data points can save a lot of time, especially when using a new library.

* Mention that the pattern for this exercise resembles the one that they used in the previous exercises with Leaflet. This pattern is as follows:

  * We create the map object before importing any data. Because JavaScript is an asynchronous language, it uses some of the time spent waiting for the data to build the map.

  * We import the data with `d3.json()`. Once we have the data, an anonymous function goes through that data with a `for` loop and adds a marker to the marker cluster group for each data point. Once the `for` loop finishes, we add the marker group to the map.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Map+Rodent+Clusters&lessonpageTitle=GeoJSON+and+Leaflet+Plugins&lessonpageNumber=15.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F2%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:35  |
|---------------------------|---------------------------|

- - -

## 4. Create a Choropleth Map

| Activity Time:       0:40 |  Elapsed Time:      2:15  |
|---------------------------|---------------------------|

<details>
    <summary><strong>👥 4.1 Partners Do: Create a Choropleth Map (0:30) </strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slides 15 and 16 to present this activity to the class and the following slides to present each step of the activity: [step 1 - slide 17](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit#slide=id.gc6f1757a7d_0_14225), [step 2 - slide 19](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit#slide=id.gc6f1757a7d_0_14239), [step 3 - slide](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit#slide=id.gc6f1757a7d_0_14252) and [step 4 - slide 23](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit#slide=id.gc6f1757a7d_0_14264).

* Note that for every step slide there is a review slide following.

* The following image shows the median income choropleth map:

  ![A screenshot depicts the map.](Images/Choropleth.png)

* In this activity, the students will work together with their partners to create a [choropleth map](https://en.wikipedia.org/wiki/Choropleth_map). The map will visualize the median household incomes of Los Angeles and the surrounding counties.

* Be aware that we haven't covered choropleth maps as a class, so this activity will take place as a series of steps. The class will reconvene after each step to review what they did before moving on.

* For the starter files, go to the [Unsolved](./Activities/04-Par_MoneyChoropleth/Unsolved) folder for this activity.

* For the activity instructions, go to the [README](./Activities/04-Par_MoneyChoropleth/README.md) file for this activity.

</details>

<details>
    <summary><strong>⭐ 4.2 Review: Creating a Choropleth Map (0:10)</strong></summary>

### Review Step 1

* Open [logic-step1.js](Activities/04-Par_MoneyChoropleth/Solved/static/js/logic-step1.js), and point out the following new code:

    ```js
    // Get the data with d3.
    d3.json(geoData).then(function(data) {

      console.log(data);

      // Create a new choropleth layer.

        // Define which property in the features to use.

        // Set the color scale.

        // The number of breaks in the step range

        // q for quartile, e for equidistant, k for k-means

        // Binding a popup to each layer

      // Set up the legend.

        // Add the minimum and maximum

      // Adding the legend to the map.

    });
    ```

* Reiterate to the students that this will load the data and then log it to the console, where we can inspect it.

* In Google Chrome, open [index.html](Activities/04-Par_MoneyChoropleth/Unsolved/index.html), open **Developer tools**, navigate to the Console tab, and then expand the data object that we logged to the console. Expand the `features` array, expand one of the features, and then point out that `properties` holds data about the specified location&mdash;so it's a good place to find the Median Household Income data.

  **Note:** The first six entries have `null` values for `MHI2016`. Be prepared for the students to ask about this. The [original data source](https://maps.scag.ca.gov/scaggis/rest/services/ATDB/ATDB_ATP_Requirements/MapServer/0) doesn't specify why some values are null. Let the students know that many possibilities exist for why the data is null. Perhaps the data was insufficient, not recorded, invalidated, or even corrupted.)

* Let the students return to the activity.

- - -

### Review Step 2

* Go to the [leaflet-choropleth](https://github.com/timwis/leaflet-choropleth/) repository page, and then scroll down to **Installation**. Point out to the students that the installation steps apply to JavaScript developers, so it's not necessary to install NPM or Bower. Note that it does say to include `dist/choropleth.js` from this repository&mdash;and we do need this. Navigate to the `dist` folder in the repository, and then click **choropleth.js**. The [choropleth.js page](https://github.com/timwis/leaflet-choropleth/blob/gh-pages/dist/choropleth.js) displays. Mention that the code on this page is intentionally compact and difficult to read but that we don't need to understand it to use it. Get the code in one of the following two ways:

  * Clone the repository, and then copy `choropleth.js` to your `static/js/` folder.

  * Copy the raw text from GitHub, and then paste it into a new `choropleth.js` file.

* In Microsoft Visual Studio Code, open [index.html](Activities/04-Par_MoneyChoropleth/Solved/index.html), and then point out the following code (which imports the file):

    ```html
    <!-- Step 2 -->
    <!-- leaflet-choropleth JavaScript -->
    <script type="text/javascript" src="static/js/choropleth.js"></script>
    ```

* Distribute the code to the students if necessary, and then return to the [leaflet-choropleth repository](https://github.com/timwis/leaflet-choropleth). Scroll down to **Usage**, and then point out that the students should follow the Usage instructions for the upcoming Step 3.

- - -

### Review Step 3

* Open [logic-step3.js](Activities/04-Par_MoneyChoropleth/Solved/static/js/logic-step3.js). Go over the following code with students, comparing each line to the Usage example in the [leaflet-choropleth repository](https://github.com/timwis/leaflet-choropleth):

  ```js
  // Create a new choropleth layer.
  geojson = L.choropleth(data, {

    // Define which property in the features to use.
    valueProperty: "MHI2016",

    // Set the color scale.
    scale: ["#ffffb2", "#b10026"],

    // The number of breaks in the step range
    steps: 10,

    // q for quartile, e for equidistant, k for k-means
    mode: "q",
    style: {
      // Border color
      color: "#fff",
      weight: 1,
      fillOpacity: 0.8
    },

    // Binding a popup to each layer
    onEachFeature: function(feature, layer) {
      layer.bindPopup("Zip Code: " + feature.properties.ZIP + "<br>Median Household Income:<br>" +
        "$" + feature.properties.MHI2016);
    }
  }).addTo(myMap);
  ```

* Open [index.html](Activities/04-Par_MoneyChoropleth/Solved/index.html), comment out the call to `logic-step1.js`, and then uncomment the call to `logic-step3.js`, as follows:

  ```html
  <!-- Our JavaScript -->
  <!-- <script type="text/javascript" src="static/js/logic-step1.js"></script> -->
  <script type="text/javascript" src="static/js/logic-step3.js"></script>
  <!-- <script type="text/javascript" src="static/js/logic-step4.js"></script> -->
  ```

* In Chrome, open [index.html](Activities/04-Par_MoneyChoropleth/Solved/index.html) to display the choropleth map.

* Let the students finish the activity before moving on to Step 4.

- - -

### Review Step 4

* Go to the [leaflet-choropleth legend example](https://github.com/timwis/leaflet-choropleth/tree/gh-pages/examples/legend), and then open `demo.js`. Point out that we'll use the following code from the example as a starting point for our choropleth map:

    ```js
    // Add legend (don't forget to add the CSS from index.html)
    var legend = L.control({ position: 'bottomright' })
    legend.onAdd = function (map) {
      var div = L.DomUtil.create('div', 'info legend')
      var limits = choroplethLayer.options.limits
      var colors = choroplethLayer.options.colors
      var labels = []

      // Add min & max
      div.innerHTML = '<div class="labels"><div class="min">' + limits[0] + '</div> \
  			<div class="max">' + limits[limits.length - 1] + '</div></div>'

      limits.forEach(function (limit, index) {
        labels.push('<li style="background-color: ' + colors[index] + '"></li>')
      })

      div.innerHTML += '<ul>' + labels.join('') + '</ul>'
      return div
    }
    legend.addTo(map)
  })
  ```

* The first comment directs us to the CSS from `index.html`. Navigate to [index.html](https://github.com/timwis/leaflet-choropleth/blob/gh-pages/examples/legend/index.html), and then add the following code to [style.css](Activities/04-Par_MoneyChoropleth/Solved/static/css/style.css):

  ```css
  .legend {
    color: #555;
    padding: 6px 8px;
    font: 12px Arial, Helvetica, sans-serif;
    font-weight: bold;
    background: white;
    background: rgba(255,255,255,0.8);
    box-shadow: 0 0 15px rgba(0,0,0,0.2);
    border-radius: 5px;
  }
  .legend ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
    clear: both;
  }
  .legend li {
    display: inline-block;
    width: 30px;
    height: 22px;
  }
  .legend .min {
    float: left;
    padding-bottom: 5px;
  }
  .legend .max {
    float: right;
  }
  ```

* Open [index.html](Activities/04-Par_MoneyChoropleth/Solved/index.html), comment out the call to `logic-step1.js` and then uncomment the call to `logic-step3.js`, as follows:

  ```html
  <!-- Our JavaScript -->
  <!-- <script type="text/javascript" src="static/js/logic-step1.js"></script> -->
  <!-- <script type="text/javascript" src="static/js/logic-step3.js"></script> -->
  <script type="text/javascript" src="static/js/logic-step4.js"></script>
  ```

* In Chrome, open [index.html](Activities/04-Par_MoneyChoropleth/Solved/index.html) to display the choropleth map with the legend.

* Open [logic-step4.js](Activities/04-Par_MoneyChoropleth/Solved/static/js/logic-step4.js), and then go over the following lines of code with the students:

  ```js
  // Set up the legend.
  var legend = L.control({ position: "bottomright" });
  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");
    var limits = geojson.options.limits;
    var colors = geojson.options.colors;
    var labels = [];

    // Add the minimum and maximum.
    var legendInfo = "<h1>Median Income</h1>" +
      "<div class=\"labels\">" +
        "<div class=\"min\">" + limits[0] + "</div>" +
        "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
      "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function(limit, index) {
      labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;
  };

  // Adding the legend to the map
  legend.addTo(myMap);
  ```

* Compare and contrast our code to that in the [leaflet-choropleth legend example](https://github.com/timwis/leaflet-choropleth/tree/gh-pages/examples/legend). Point out that `L.control()` is a base method that creates a generic control and that it's not specific to creating legends.

* Note that overwriting the `onAdd()` method is where the control becomes a legend. The `L.DomUtil.create` method handles creating a `div` with `info` and `legend` classes for us.

* Go back to the choropleth map in your browser, and then inspect the legend. Show how the JavaScript code creates each element.

* Finally, point out that Leaflet still needs to know where to put this legend*mdash;which `legend.addTo(myMap)` accomplishes. Answer any remaining questions that the students have before moving on to the next activity.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Create+a+Choropleth+Map&lessonpageTitle=GeoJSON+and+Leaflet+Plugins&lessonpageNumber=15.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F2%2FLessonPlan.md)</sub>

## 5. Create a Map of Your Own

| Activity Time:       0:45 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
    <summary><strong>✏️ 5.1 Groups Do: Create a Map of Your Own (0:30)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slides 25 and 26 to present this activity to the class.

* Have students get into small groups. They'll create a map of their own from scratch. They'll find a dataset, map it, then use a [new plugin](https://leafletjs.com/plugins.html) to visualize the data in an interesting way.

* Tell them that they'll share their map with the class and give a brief presentation on it at the end of the day.

  **Note:** This assignment focuses on getting a working map. So, also tell them that the presentations are secondary to making a splendid map.

</details>

<details>
    <summary><strong>🎉 5.2 Everyone Do: Mini-Presentations on Maps (0:15)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1xt7i7U39ai25oOcIfnOrJ7ErRFDeamdm13YTIs5Ggf4/edit?usp=sharing) and use slide 27 to present this activity to the class.

* Bring the class back together, and then call on the groups one at a time to present their newest maps to the class. Have them explain at a high level how they made their maps, and answer any questions that arise during the presentations.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Create+a+Map+of+Your+Own&lessonpageTitle=GeoJSON+and+Leaflet+Plugins&lessonpageNumber=15.2&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F2%2FLessonPlan.md)</sub>

- - -
© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
