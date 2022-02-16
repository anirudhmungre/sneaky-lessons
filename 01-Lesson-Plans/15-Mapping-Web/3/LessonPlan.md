# 15.3 Citi Bike Project with Leaflet and Intro to Projects

## Overview

In today's class, the students will further develop their Leaflet skills by working on a mini project. This will consist of mapping Citi Bike data and then deploying the mini project to GitHub Pages. During the rest of the class, you'll assign the students to project groups, and they'll brainstorm Project 3 proposals.

## Class Objectives

By the end of today's class, students will be able to:

* Complete an in-class group project using Leaflet.js.
* Deploy data visualizations to GitHub Pages.
* Draft a project proposal with your team.

## Instructor Prep

<details>
    <summary><strong>Instructor Priorities</strong></summary>

* The students should have the time to further develop their Leaflet skills by creating a map of all the Citi Bike stations in New York.

</details>

<details>
    <summary><strong>Instructor Notes</strong></summary>

* Your project week might have been shifted because of a holiday. This means that the students will have less time to work on projects today. Consider the following:

  * Remind the students that office hours exist before and after the class that they can use for extended project work.

  * Alternatively, students can coordinate with team members to work on their projects outside of class.

* At the start of the class, you'll reintroduce the students to the career services support that's available to them during their job search. If possible, take a moment to go through the [short slideshow](https://docs.google.com/presentation/d/18inCMR9TB47q3yEY-YflqA-96cBqXheM9X0BrD0Gk9Y/edit#slide=id.p7) at that time.

* Keep in mind that a large portion of time during the beginning of the class is dedicated to the students working on a Leaflet project. During that time, make sure that you and the TAs check in with the students individually and offer help to any students who are stuck.

* The final part of today's class will consist of forming the Project 3 groups and drafting the Project 3 proposals. This will provide a great chance for the students to finalize any last-minute questions before they start their projects.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-17-geojson-and-leaflet) for answers to questions that students of this program frequently ask. If you have recommendations for more questions, feel free to log an issue or create a pull request with the additions that you'd like.

</details>

- - -

# Class Activities

## 1. Welcome and Use the Python HTTP Server

| Activity Time:       0:30 |  Elapsed Time:      0:30  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 1.1 Instructor Do: Welcome the Class and Reintroduce the available career services (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slides 1 - 3 to go over class objectives, welcome the class, and ask students if they're actively engaged in a job search or intend to engage in one by the end of the program.

* Remind the class that, now that they are over two-thirds of the way through the program, this is a great time to start thinking about their job search and engaging with the many career services options provided as part of the program.

* Go through slides 4 - 10 about [career services](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit#slide=id.gc6057a243e_0_7383).

* If any questions arise, advise the students to reach out to their Student Success Manager.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Use the Python HTTP Server (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slides 11 and 12 to set the ground to assist you with this live code with the class.
* Use the following files:

  * [remote-example/index.html](Activities/01-Ins_Python_HTTP_Server/Solved/remote-example/index.html)

  * [local-example/index.html](Activities/01-Ins_Python_HTTP_Server/Solved/local-example/index.html)

  * [CORS.md](Activities/01-Ins_Python_HTTP_Server/CORS.md)

* In your browser, go to [Citi Bike System Data](https://www.citibikenyc.com/system-data). Then let the students know that we'll use the Citi Bike real-time data for our next activity. Specifically, we'll use the [Citi Bike API station information endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json). Go to the endpoint in your browser, and then show students that it's a regular JSON file, which we're used to.

* In Visual Studio Code, open [remote-example/index.html](Activities/01-Ins_Python_HTTP_Server/Solved/remote-example/index.html). Show that this is a simple file. Mention that we'll request the data by using `d3.json()` and log the data to the console. However, a problem exists. In your browser, open [remote-example/index.html](Activities/01-Ins_Python_HTTP_Server/Solved/remote-example/index.html). (Be sure to directly open this HTML file. Don't run it from Visual Studio Code.) Show that in the console, we get the following error:

  ```text
  Access to fetch at 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
  ```

* Mention that this is a Cross-Origin Resource Sharing (CORS) error, and this more commonly occurs when we load local JSON files. But, as we can see here, it sometimes happens with remote APIs, as well.

* If time allows, open [local-example/index.html](Activities/01-Ins_Python_HTTP_Server/Solved/local-example/index.html) in Visual Studio Code. Show that it loads a local JSON file with `d3.json()`. Then open `index.html` in your browser again, and show that we get the following, different error. But, the error still relates to CORS:

  ```text
  Fetch API cannot load file:///path/to/Activities/01-Ins_Python_HTTP_Server/Solved/local-example/data/data.json. URL scheme must be "http" or "https" for CORS request.
  ```

* Mention that to avoid these CORS errors, we need to run a local web server.

* Explain servers at a high level, as follows:

  * A **server** is a program or device that performs actions such as processing and sharing data.

  * For example, when a user logs in to a website, the server receives the user's information, compares it against information in its database, and then sends a response back to the user (e.g. a successful login, an error, etc.).

  * This is called the **request-response model**. The user, also known as the client, sends a request to the webpage server. The webpage server  then sends back the requested data in response.

* Explain why a browser can't directly read the JSON file, as follows:

  * For security reasons, browsers heavily restrict reading and writing to local files.

  * If they allowed access to local files, remote sites could read and manipulate our private data. Or, simply opening a local file with the browser could trigger a malicious script.

  * However, Python provides a lightweight server for testing. We can run it with the `python -m http.server` command. We then avoid this restriction&mdash;because the browser won't consider the local file or the remote API call as part of a cross-origin request.

* Explain that the Python HTTP server provides a web address for the file and for the HTML page and thus avoids security issues.

  **Note:** Students who are curious about CORS can read the [included guide](Activities/01-Ins_Python_HTTP_Server/CORS.md) for more information.

* From the [remote-example](Activities/01-Ins_Python_HTTP_Server/Solved/remote-example) directory, run `python -m http.server` in your terminal. Navigate to `localhost:8000`, and then open the console to show that the data now correctly loads.

* Go back to your terminal, and show the students that pressing CTRL+C ends the server.

* Navigate to the [local-example](Activities/01-Ins_Python_HTTP_Server/Solved/local-example) directory, and then run `python -m http.server` again. Navigate to `localhost:8000` again, and then show that the server is serving files, that it returns no CORS error, and that Plotly can create the box plots.

* Emphasize that `index.html` must reside in the directory where we  run `python -m http.server`.

* Open `plot.js`, and then explain the following:

  * D3 sends a request to the `data/data.json` route, as the following code shows:

    ```js
    d3.json("data/data.json").then((data) => {}
    ```

  * Previously, the script returned a CORS error, because it tried to access the local JSON data without a server.

  * With a server, the data is retrieved from its own URL.

* Navigate to `localhost:8000/data/data.json` to display the requested JSON data, as the following image shows:

  ![A screenshot depicts the JSON data.](Images/data_json.png)

* Answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+and+Use+the+Python+HTTP+Server&lessonpageTitle=Citi+Bike+Project+with+Leaflet+and+Intro+to+Projects&lessonpageNumber=15.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F3%2FLessonPlan.md)</sub>

## 2. Create Citi Bike Maps

| Activity Time:       0:55 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 2.1 Instructor Do: Introduce Citi Bike (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slides 13 - 15 to introduce this lesson to the class.

* Inform the students that they'll use the Citi Bike API to create a Leaflet map displaying the locations of Citi Bike stations in New York. The activity includes two versions: a basic version and an advanced version. The latter requires two datasets from separate Citi Bike API endpoints. At a minimum, the students should work to complete the basic version.

* Open [index.html](Activities/02-Stu_CitiBike_Leaflet/Solved/Basic/index.html). In the terminal, run `python -m http.server`. In the browser, navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to show the students the basic version of the map, which uses only the first dataset. The following image shows this map:

  ![A screenshot depicts the basic map.](Images/44-Citibike_basic.png)

* Point out the following on the map:

  * Each marker resides at the latitude and longitude that the request received.

  * When someone clicks a marker, a popup appears that displays the station name and capacity.

* Take a moment to show the students the response that the [Citi Bike API station information endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json) gave back. This is the response that we used to create this map. Go back and forth between this data and the map to illustrate how the returned data is used. Be sure to mention the following:

  * This data is not GeoJSON data, because it doesn't include any features.

  * This response does, however, include the longitude and latitude for each bike station, which is the data that we use to place our markers.

  * The response also includes other useful information, such as the `name`, `station_id`, and `capacity` of each bike station.

* After answering any questions about the basic version of the map, shut down the server, open [index.html](Activities/02-Stu_CitiBike_Leaflet/Solved/Advanced/index.html), and then restart the server with `python -m http.server`. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/), and then show the class the advanced version of the map that they'll work toward. Be sure to highlight the following functionality:

  * This solution groups markers into layers according to the station status&mdash;such as "Out of Order", "Coming Soon", and "Empty".

  * By using a Leaflet plugin, different custom markers are used for the different status groups.

  * Like with the basic map, a popup appears when someone clicks a marker. Additionally, we see the number of available bikes at each station along with the station name and total capacity.

  * This version of the activity uses a map legend to display the quantities of markers for each status, their colors, and the last time the API was updated.

* Stress that the students should complete the basic version of the map before moving on to this more advanced version. The following image shows an example of the advanced map:

  ![A screenshot depicts an advanced version of the map.](Images/44-Citibike_advanced.png)

* Remind the students that they need to perform a second API call to get all the data that they need to build this advanced map. The first was to the [Citi Bike API station information endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json), which we demonstrated with the basic map.

* Show the students the response that the [Citi Bike API station status endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_status.json) gives back. Be sure to highlight the following:

  * This endpoint supplies information about the status of each bike station, including the number of available bikes and whether the station is currently installed and renting bikes.

  * However, this endpoint doesn't supply the coordinates of each bike station. We must still get this information from the first endpoint that we discussed, the [Citi Bike API station information endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json).

  * The stations in both API responses have corresponding `station_id` properties. This should ease matching up and using the data from both datasets.

* Encourage the students to get creative with this activity. This might mean using a different type of base map or using vector layers instead of markers.

* Explain that all these instructions and additional suggestions exist in the [Unsolved](Activities/02-Stu_CitiBike_Leaflet/Unsolved) directory for this activity.

</details>

<details>
    <summary><strong>✏️ 2.2 Groups Do: Create Citi Bike maps (30 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slides 16 - 19 to present this activity to the class.

* In this activity, the students will work in groups. They'll work with the Citi Bike API to build a map of all the Citi Bike stations and each one's status.

* For the activity instructions, go to the [README](Activities/02-Stu_CitiBike_Leaflet/README.md) file for this activity.

</details>

<details>
    <summary><strong>⭐ 2.3 Review: Create Citi Bike maps (15 mins)</strong></summary>

* Send out the [Solved](Activities/02-Stu_CitiBike_Leaflet/Solved) directory for this activity, and then go over the solutions as a class.

* Let the students know that this was an ambitious project to fully complete in the allotted time. But, it provided good practice with both Leaflet and traversing data structures with JavaScript. Encourage them to continue working on it outside of class if they haven't already finished. The reason is that it would make an impressive addition to their portfolios.

* Answer any further questions about the solution.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Create+Citi+Bike+Maps&lessonpageTitle=Citi+Bike+Project+with+Leaflet+and+Intro+to+Projects&lessonpageNumber=15.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F3%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:40 |  Elapsed Time:      2:05  |
|---------------------------|---------------------------|

⏰ **Three-Hour Adjustment:** Change the break to 15 minutes.

- - -

## 3. Deploy a Project to GitHub Pages

| Activity Time:       0:45 |  Elapsed Time:      2:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: Deploy a Project to GitHub Pages (15 mins)</strong></summary>

* ⏰**Three-Hour Adjustment**: Reduce the activity time to 10 minutes.

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slides 22 - 27 to assist you to present this lesson to the class.

* For the activity files, go to the [Solved](Activities/03-Ins_Github_Pages/Solved) directory.

* Inform the students that they'll deploy the Citi Bike project to GitHub Pages. Also, tell them the following:

  * They'll use the `d3.json()` method to get data from the JSON file and visualize it.

  * In addition to uploading the HTML and JavaScript script files to GitHub, they'll need to upload the JSON file.

* Explain the following benefits of deploying a Plotly visualization with a data file:

  * It makes a data visualization available to the public that's far more visually appealing than a published Jupyter notebook.

  * The ability to read data from local files means that data sources aren't limited to those that we get from placing API calls.

* Navigate to the `Solved` directory, and then show the Plotly project structure. Note the following:

  * A JSON file contains the data. The following image shows where to find this file:

    ![A screenshot depicts that data.json exists in the data directory. That directory, index.html, and plots.js exist at the same level.](Images/github07.png)

  * Because `data.json` is an external file, we can't pull the data that it contains directly into the JavaScript file.

  * Instead, we must get it from a server.

* Take a moment to explain the relative path of the `data.json` file, as follows:

  * Because `plotly.js` must access the contents of `data.json`, it must navigate to the `data` directory and then to `data.json`.

  * In `plotly.js`, the file path is entered as the argument of the `json` method as follows: `d3.json("data/data.json")`.

* From the command-line interface (CLI), navigate to the `Solved` directory, and then start a local server with `python -m http.server`. Then in your browser, go to `localhost:8000`. The following image shows the resulting plot:

    ![A screenshot depicts a plot of the Greek gods search results.](Images/github08.png)

* Demonstrate how to deploy an existing project to GitHub Pages by completing the remaining steps. (The students should find these steps familiar, but we'll supply them for future reference.)

* Create a new repository in GitHub as follows:

  1. Go to the GitHub website, and then create a new repository by clicking New, as the following image shows:

      ![A screenshot depicts the New button.](Images/github01.png)

  2. Note that the repository must be public to be deployed to GitHub Pages. Make sure that Public option is selected, as the following image shows:

      ![A screenshot depicts the Public option selected and the Private option cleared.](Images/github03.png)

  3. Clone the repository by copying the URL and then entering `git clone <url>` in the CLI. The following image shows where you can copy the URL:

      ![A screenshot depicts the URL box.](Images/github02.png)

* Push the project to GitHub as follows:

  1. Navigate to the directory of the repository.

  2. Copy the HTML, JavaScript, and JSON files from the `Solved` directory to the repository.

  3. Enter the following commands:

      1. `git add .`

      2. `git commit -m "<your message here>"`

      3. `git push origin main`

* Configure the project for deployment by completing the following steps:

  1. In GitHub, go to the project page, and then click Settings, as the following image shows:

      ![A screenshot depicts the Settings tab.](Images/github04.png)

  2. Under Settings, go to `Pages`, and then in the **Select source** list, select **main branch**, as the following image shows:

      ![A screenshot depicts selecting main branch.](Images/github05.png)

  3. Click **Save**.

* The project should now be deployed to GitHub Pages, as the following image shows:

  ![A screenshot depicts the plot of the Greek gods search results on GitHub Pages.](Images/github06.png)

* Be aware of the following:

  * The URL of the deployed page is `<account name>.github.io/<project name>`.

  * The deployment should be quick but might take up to several minutes.

</details>

<details>
  <summary><strong>✏️ 3.2 Students Do: Deploy the Citi Bike Project (20 mins)</strong></summary>

* ⏰**Three-Hour Adjustment**: Reduce the activity time to 15 minutes.

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slides 28 and 29 to present this activity to the class.

* For the activity files, go to the [Unsolved](Activities/04-Stu_Github_Pages/Unsolved) directory.

* For the activity instructions, go to the [README.md](Activities/04-Stu_Github_Pages/README.md) file for this activity.

* In this activity, the students will deploy the Citi Bike project to GitHub Pages.

  **Note:** As the students work on the activity, you and your TAs should identify and help any students who are struggling.

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Deploy the Citi Bike Project (10 mins)</strong></summary>

* Briefly walk through the steps of deployment to GitHub Pages, as follows:

  1. Create a project repository in GitHub.

  2. Clone the repository on the local computer.

  3. Add the project files to the repository.

  4. Push the changes to GitHub.

  5. In the repository settings,  under Source, select **main branch**, and then click **Save**. The following image shows selecting **main branch**:

      ![A screenshot depicts selecting **main branch** in the Select source list.](Images/github10.png)

* If time allows, take a moment to highlight the following elements of the code:

  * In the HTML file, we read the c3 library from a content delivery network (CDN), as the following code shows:

    ```html
    <script src="https://d3js.org/d3.v5.min.js"></script>
    ```

  * In the JavaScript file, we use a d3 method to read the data from the JSON file, as the following code shows:

    ```js
    d3.json("data/data.json").then((incomingData) => {}
    ```

  * After reading in the JSON file, we arbitrarily refer to its data as `incomingData`. However, we can give this argument any other name, such as `data` or `jsonData`.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Deploy+a+Project+to+GitHub+Pages&lessonpageTitle=Citi+Bike+Project+with+Leaflet+and+Intro+to+Projects&lessonpageNumber=15.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F3%2FLessonPlan.md)</sub>

## 4. Intro to Project 3

| Activity Time:       1:10 |  Elapsed Time:      4:00  |
|---------------------------|---------------------------|

<details>
    <summary><strong>📣 4.1 Instructor Do: Introduce Project 3 (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slides 31 - 40 to assist you to introduce Project 3 to the class.

  * Remind students that they will need to submit their preferred project track (finance, healthcare, or custom topic) to their instructor prior to forming groups.

</details>

<details>
    <summary><strong>🎉 4.2 Everyone Do: Assign Project 3 Teams and Brainstorm Proposals (1:00)</strong></summary>

* ⏰**Three-Hour Adjustment**: If today's class occurs on a weekday, reduce the project work time to 25 minutes.

* Open the [slideshow](https://docs.google.com/presentation/d/1y7fp7LQFEcMtuyhDj5FQqZL_scBs93k5o73qioUxoww/edit?usp=sharing) and use slide 41 for this activity.

* Use the rest of the class to assign Project 3 teams of three to five students each and to have the students brainstorm and draft their Project 3 proposals.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Intro+to+Project+2&lessonpageTitle=Citi+Bike+Project+with+Leaflet+and+Intro+to+Projects&lessonpageNumber=15.3&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F15-Mapping-Web%2F3%2FLessonPlan.md)</sub>

- - -
© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
