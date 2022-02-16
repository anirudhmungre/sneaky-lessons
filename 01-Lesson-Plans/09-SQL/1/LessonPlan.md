# 9.1 Introduction to SQL

## Overview

In today's class, students will be introduced to SQL databases and will learn how to create tables and simple queries.

## Class Objectives

By the end of class, students will be able to:

- Install and run Postgres and pgAdmin on their computers.
- Create a database and tables using pgAdmin.
- Define SQL data types, primary keys, and unique values.
- Load CSV files into a database and query the data.
- Articulate the four basic functions of persistent storage (CRUD) and apply this set of functions to a database.
- Combine data from multiple tables using JOINs.

## Instructor Prep

<details>
  <summary><strong>Instructor Notes</strong></summary>

* **Important:** Before today's class, send out [instructions](../Supplemental/InstallationGuides) for installing PostgreSQL and pgAdmin. Students should install these before class (these are the same guides that were shared prior to class last week).

* Today's class will be challenging. In this lesson, a series of activities will introduce students to programming with SQL using Postgres and pgAdmin. The pace of today's class will be quick as students absorb learning a new UI and programming language simultaneously.

* Because this lesson introduces more than one new concept, circulate through the class during student activities to assist those who appear frustrated or stuck. Some students may already have experience with SQL; embrace these students' knowledge of the language and have them assist students who are not yet familiar with SQL.

* This lesson introduces new content rapidly. Students may express frustration at learning a new interface and programming language simultaneously. Explain to students that while the learning curve may be steep at first, SQL experience is highly sought-after and well worth the effort required to become comfortable with it.

* Please reference our [Student FAQ](../../../05-Instructor-Resources/README.md#unit-09-sql) for answers to questions frequently asked by students of this program. If you have any recommendations for additional questions, feel free to log an issue or a pull request with your desired additions.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

* Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then send out the PDF file.

</details>

- - -

# Class Activities

## 1. Welcome & Create a Database

| Activity Time:       0:15 |  Elapsed Time:      0:15  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 1.1 Instructor Do: Welcome Class (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 1-4 to welcome students to this lesson.

* Welcome students to class and congratulate them on making it through the project week. They have come very far since the beginning of the course and should feel proud of what they have accomplished so far!

* Go over the learning outcomes for the SQL unit and today's class objectives. (Slides 3-4)

* Tell students that today's lesson will introduce them to one of the most popular programming languages used when working with databases: SQL. SQL programmers are in high demand, so this is an important language to understand. SQL allows us to manipulate and mine data as well as access large amounts of data with ease.

</details>

<details>
  <summary><strong>📣 1.2 Instructor Do: Introduction to SQL (5 mins)</strong></summary>

* Before diving into the lesson's activities, open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 5-8 to go over the purpose of SQL.

  * SQL (often pronounced "sequel") stands for Structured Query Language. It is a powerful programming tool designed to allow programmers to create, populate, manipulate, and access databases, as well as provide programmers with an easy method for dealing with server-side storage.

  * Data using SQL is stored in tables on the server, much like spreadsheets you would create in Microsoft Excel. This makes the data easy to visualize and search.

  * PostgreSQL (usually referred to as "Postgres") is an object-relational database system that uses the SQL language.

  * pgAdmin is the management tool used for working with Postgres. It simplifies creation, maintenance, and use of database objects.

* Send out the [Student Guide](../StudentGuide.md) containing this week's objectives as well as resource links.

* Send out the [SQL Reference Guide](../Supplemental/SQL_reference_guide.pdf) for students to use as a reference during the activities this week.

</details>

<details>
  <summary><strong>🎉 1.3 Everyone Do: Create a Database (5 mins)</strong></summary>

* Begin by verifying that everyone has successfully installed pgAdmin and Postgres. Everyone should have completed this step prior to today's class.

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 9-10 to show students how to create a database in pgAdmin.

  * Open pgAdmin in a new browser window and ensure that everyone is able to follow along and view their new server in the browser.

    ![browser-view.png](Images/browser-view.png)

* Walk the class through the steps to create a database using pgAdmin.

  * In the pgAdmin editor, right-click the newly established server to create a new database.

  * From the menu, select **Create**, and then select **Database** to create a new database.

  ![create_database.png](Images/create_database.png)

  * Enter **animals_db** as the database name. Make sure the owner is set as the default postgres, and then click **Save**.

  ![animals_db.png](Images/animals_db.png)

* At this point, show students that there is a new database listed in the left-hand menu. Explain that the new database, `animals_db`, is not yet connected to the server. Simply clicking on the database will create a connection to Postgres.

  ![new_db.png](Images/new_db.png)

* Answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=1+-+Welcome+%26+Create+a+Database&lessonpageTitle=Introduction+to+SQL&lessonpageNumber=9.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F09-SQL%2F1%2FLessonPlan.md)</sub>

- - -

## 2. Creating Tables

| Activity Time:       0:30 |  Elapsed Time:      0:45  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 2.1 Instructor Do: Create a Table (10 mins)</strong></summary>

* Now that there is a database on the server, it's time to dig into the real meat of SQL and start creating tables within the new database!

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 11-16 to assist students to understand how to create tables in SQL.

* From the left-hand menu in pgAdmin, right-click **animals_db** and select **Query Tool**.

  **Note:** You can also select **Query Tool** from the Tools drop-down menu at the top of the screen. (See second screenshot below.)

  ![query_tool.png](Images/query_tool.png)

  ![tools_dropdown.png](Images/tool_dropdown.png)

* Explain to students that this is how to access the code editor.

* Type the following lines of code, explaining each line:

  ```sql
  CREATE TABLE people (
    name VARCHAR(30) NOT NULL,
    has_pet BOOLEAN DEFAULT false,
    pet_type VARCHAR(10) NOT NULL,
    pet_name VARCHAR(30),
    pet_age INT
  );
  ```

  * `CREATE TABLE people (<COLUMNS>);` creates a table called `people` with the columns listed within the parentheses.

  * `name VARCHAR(30) NOT NULL` creates a  `name` column, which can hold character strings of up to 30 characters and will not allow null fields.

  * The `NOT NULL` constraint requires the name field to have a value specified.

  * `pet_type VARCHAR(10) NOT NULL,` creates a `pet_type` in the same manner as the `name` column is created. The only difference is the number of characters allowed in the column.

  * `has_pet BOOLEAN DEFAULT false` creates a `has_pet` column that holds either true or false values, though the default value is now set as false.

  * `pet_name VARCHAR(30)` creates a `pet_name` column, which can hold character strings of up to 30 characters and will allow null fields.

  * `pet_age INT` creates a`pet_age` column, which can hold whole numbers.

  * **Note:** Be sure to point out the semicolon at the end of the statement, which tells pgAdmin that this line of code has concluded.

* After reviewing the code, click the play icon to run the script. Make a note of the Messages tab at the bottom of the screen.

  ![lightning_bolt.png](Images/lightning_bolt.png)

* Demonstrate that the structure of a table can be visualized using `SELECT * FROM <table name>;`.  Point out the error message that now appears at the bottom of the page.

  * Explain that SQL data is persistent; it is not deleted or overwritten when identical commands are run unless specifically commanded. This means that when a database or table is created with a  name identical to one that already exists, an error will occur telling the user that the database or table already exists.

  * Ask the class how to avoid this kind of error. Students may respond that they can simply delete the offending line of code and then run the commands again. Explain that while this method would work, deleting working code is not a best practice.

  * Show the class an alternative method: Highlight the lines of code to run, and then click the play icon to run only the highlighted selection. This method of running SQL code is preferable to deleting previous code.

    ![Select.png](Images/Select.png)

* Point out that the structure of a table can be visualized using `SELECT * FROM <table name>;`.

  * Explain that using the asterisk in this manner tells pgAdmin to select all fields from the table.

  * In the future, students will be able to view the structure of their table, and all of the values contained within it, using this same line of code.

* Type the following code while explaining what it does line by line.

  ```sql
  INSERT INTO people (name, has_pet, pet_type, pet_name, pet_age)
  VALUES ('Jacob', true, 'dog', 'Misty', 10),
    ('Ahmed', true, 'rock', 'Rockington', 100),
    ('Peter', true, 'cat', 'Franklin', 2),
    ('Dave', true, 'dog', 'Queso', 1);

  SELECT *
  FROM people;
  ```

  * This code operates as it reads: it inserts data into the `people` table and then specifies the columns in which data will be entered.

  * The `VALUES` line places the data contained in the parentheses into the corresponding columns listed after the `INSERT INTO` statement.

  * Note: Single quotations must be used for insert strings; otherwise, an error will result.

* Use the following code to query the table, extracting only the `pet_name`.

  ```sql
  SELECT pet_name
  FROM people;
  ```

  * Explain that specifying a column name in the `SELECT` statement will return only the data contained in that field.

* Filter the queried data to display only dogs younger than 5.

  ```sql
  SELECT pet_type, pet_name
  FROM people
  WHERE pet_type = 'dog'
  AND pet_age < 5;
  ```

* Explain the following points:

  * The `SELECT` clause can specify more than one column.

  * Data is filtered by using additional clauses such as `WHERE` and `AND`.

  * The `WHERE` clause will extract only the data that meets the condition specified. `AND` adds a second condition to the original clause, further refining the query.

</details>

<details>
  <summary><strong>✏️ 2.2 Student Do: Creating Tables (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 17-19 to present this activity to the class.

* In this activity, students will use pgAdmin to recreate and query a table from an image provided.

**Instructions:** [README.md](Activities/03-Stu_Creating_Tables/README.md)

</details>

<details>
  <summary><strong>⭐ 2.3 Review: Creating Tables (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slide 20 to assist you to review the activity.

* **File:** [stu_creating_tables.sql](Activities/03-Stu_Creating_Tables/Solved/stu_creating_tables.sql)

* Create a new database named `city_info` in pgAdmin. Then use the query tool to copy and paste, or live code, the solution from `stu_creating_tables.sql`.

  * To create a new table, remind students to specify the data type for each column.

    ```sql
    CREATE TABLE cities (
      city VARCHAR(30) NOT NULL,
      state VARCHAR(30) NOT NULL,
      population INT
    );
    ```

* Insert multiple rows of data into the new table.

  * Point out to students that each column is specified in the `INSERT INTO` clause, and the values are inserted in the same order.

  * To make the code easier to read, each row of values is on its own line, separated by a comma.

    ```sql
    INSERT INTO cities (city, state, population)
    VALUES ('Alameda', 'California', 79177),
      ('Mesa', 'Arizona', 496401),
      ('Boerne', 'Texas', 16056),
      ('Anaheim', 'California', 352497),
      ('Tucson', 'Arizona', 535677),
      ('Garland', 'Texas', 238002);
    ```

* Create a query to view the data using the `SELECT` clause.

  ```sql
  SELECT *
  FROM cities;
  ```

  * Point out the syntax here. Even though the code can fit on a single line, it's good practice to split it up over two lines instead. This way, the code is easier to read when more advanced queries are created.

* Using the `SELECT` clause again, query the data to return only the cities in the table.

  ```sql
  SELECT city
  FROM cities;
  ```

* Explain to students that the first bonus question incorporates a `WHERE` clause, which further filters the data.

  * The `WHERE` clause is used to search for specific data within a database. In this case, we are extracting only the records that meet the specified condition.

  * In the line `WHERE state = 'Arizona';` we are specifying Arizona in the state column.

    ```sql
    SELECT city, state
    FROM cities
    WHERE state = 'Arizona';
    ```

* Demonstrate the solution to the second bonus question.

  * Point out to students that the `WHERE` clause is highly customizable, such as with the use of the `<` operator.

    ```sql
    SELECT *
    FROM cities
    WHERE population < 100000;
    ```

* Walk through the solution to the third and final bonus question.

  * Explain to students that queries can be filtered even further with the `AND` clause. This clause allows users to specify more than one condition in their query.

    ```sql
    SELECT *
    FROM cities
    WHERE population < 100000
    AND state = 'California';
    ```

* Answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=2+-+Creating+Tables&lessonpageTitle=Introduction+to+SQL&lessonpageNumber=9.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F09-SQL%2F1%2FLessonPlan.md)</sub>

- - -

## 3. Making and Using an ID

| Activity Time:       0:25 |  Elapsed Time:      1:10  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 3.1 Instructor Do: The Value of Unique Values (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 21-24 to present the class to Unique Values.

* **File:** [values_of_uniques.sql](Activities/04-Ins_Values_of_Uniques/Solved/values_of_uniques.sql)

* Using the `people` table from the `animals_db` database, insert the duplicate data below into the table and then visualize the table with the new information.

  ```sql
  INSERT INTO people (name, has_pet, pet_type, pet_name, pet_age)
  VALUES ('Ahmed', true, 'rock', 'Rockington', 100);

  SELECT *
  FROM people;
  ```

  * Duplicate data is a real-world occurrence (and an eyesore). Demonstrate how to remove the rows containing the string `Ahmed` in the `name` column.

    ```sql
    DELETE FROM people
    WHERE name = 'Ahmed';
    ```

  * The duplicate was deleted, but so was the original row. That's a little annoying. Make sure the class understands why this happened.

  * Because the name Ahmed appears twice in the table, SQL assumes that the user wants to delete every column containing that name; it doesn't understand that the user is simply trying to remove the duplicate row.

  * To prevent this kind of thing from occurring, programmers will often want to create a column that automatically populates each new row with unique data. This allows them to select and modify that row more easily.

* Remove the `people` table by running the following line of code:

  ```sql
  -- Delete the table "people"
  DROP TABLE people;
  ```

* Copy the following code from the `values_of_uniques.sql` file and paste it in the pgAdmin editor.

  ```sql
  -- Re-create the table "people" within animals_db
  CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    has_pet BOOLEAN DEFAULT false,
    pet_type VARCHAR(10) NOT NULL,
    pet_name VARCHAR(30),
    pet_age INT
  );

  -- Insert data into the table
  INSERT INTO people (name, has_pet, pet_type, pet_name, pet_age)
  VALUES ('Jacob', true, 'dog', 'Misty', 10),
    ('Ahmed', true, 'rock', 'Rockington', 100),
    ('Ahmed', true, 'rock', 'Rockington', 100),
    ('Peter', true, 'cat', 'Franklin', 2),
    ('Dave', true, 'dog', 'Queso', 1),
    ('Dave', true, 'dog', 'Pringles', 7);

  -- Query all fields from the table
  SELECT *
  FROM people;
  ```

  * Explain that a *primary key* uniquely identifies a row.

  * `SERIAL` generates a new value for each inserted record in the table. By default, the starting value is 1, and it will increase by 1 for each new record. When using `SERIAL` with our unique `PRIMARY KEY`, we automatically get unique, incrementing values for each table row.

  * Point out that because values will automatically increment, each row's ID is guaranteed to be unique. This ensures that SQL does not identify and update the wrong row when CRUD—Create, Read, Update, Delete—statements are implemented.

  * Point out that the `INSERT` statements have not changed, as they do not need to insert data specifically into the `id` column. SQL automatically provides a value for this column, fulfilling the uniqueness constraint by automatically incrementing the last value used as an ID.

  * The data type for the `id` column is automatically assigned as an integer.

* One entry in the table is incorrect: one of the Daves has the wrong `pet_name` and `pet_age`. We need to update the `pet_name` from Pringles to Rocket and the `pet_age` from 7 to 8.

  * To avoid issues with updating multiple rows, it's best to update by ID. First, query by name to find the ID for the row we want to update.

    ```sql
    SELECT id, name, pet_name, pet_age
    FROM people
    WHERE name = 'Dave';
    ```

  * This will return all rows that contain the name Dave, including the `id`, `pet_name`, and `pet_age` columns.

  * Next, we can select and update the `pet_name` from Pringles to Rocket and the `pet_age` from 7 to 8 based on the row's unique ID.

    ```sql
    UPDATE people
    SET has_pet = true, pet_name = 'Rocket', pet_age = 8
    WHERE id = 6;
    ```

  * Note that, similar to a query, the `WHERE` statement is used to pinpoint the data we want to change. In this case, the `id` column is used to select the unique row we want to affect.

  * Duplicate data is also easier to remove with the use of a unique ID. With the following code, remove the duplicate data.

    ```sql
    DELETE FROM people
    WHERE id = 3;
    ```

  * This does precisely what was desired: duplicate data is deleted, and original data is preserved.

* Answer any remaining questions before moving on.

</details>

<details>
  <summary><strong>✏️ 3.2 Student Do: Making and Using an ID (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 25-26 to present this activity to the class.

In this activity, students will recreate a table and then query, insert, and update data.

**Instructions:** [README.md](Activities/05-Stu_Making_IDs/README.md)

</details>

<details>
  <summary><strong>⭐ 3.3 Review: Making and Using an ID (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slide 27 to assist you to review the activity.

* **File:** [making_ids.sql](Activities/05-Stu_Making_IDs/Solved/making_ids.sql)

* Open `making_ids.sql` and copy the code into pgAdmin.

* Go over the lines of code used to create the ID and set it as the primary key. Make sure the class understands how this works, and explain how useful this will be in this week's homework.

* Review how to create a new column using the `ALTER TABLE` and `ADD COLUMN` statements. Explain that adding the column name and data type is completed in the same manner as creating a new table.

* Answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=3+-+Making+and+Using+an+ID&lessonpageTitle=Introduction+to+SQL&lessonpageNumber=9.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F09-SQL%2F1%2FLessonPlan.md)</sub>

- - -

## Break

| Activity Time:       0:15 |  Elapsed Time:      1:25  |
|---------------------------|---------------------------|

- - -

## 4. Hide and Seek

| Activity Time:       0:25 |  Elapsed Time:      1:50  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 4.1 Instructor Do: Import Data (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 29-32 to introduce how to import data to the class.

* **Files:**

  * [birdsong.csv](Activities/06-Ins_Importing_Data/Resources/birdsong.csv)

  * [importing_data.sql](Activities/06-Ins_Importing_Data/Solved/importing_data.sql)

* So far, the class has created their own tables and values manually using SQL code. As one might imagine, this process can be tedious when translating large datasets from external sources. Thankfully, pgAdmin includes a built-in import tool that can take CSV files and easily import their data into tables.

* Return to pgAdmin and create a new database called `Miscellaneous_DB`.

* Open the CSV file within an integrated development environment, such as Excel, to show the dataset that will be imported. Be sure to point out that the first row of this dataset includes headers.

  * Open a query tool within `Miscellaneous_DB` and create a table named `bird_song`.

  * Using the code from `importing_data.sql`, create the columns necessary to import the data. Point out that the columns created match the data in the CSV file.

  * Once the table and columns have been created, right-click **Miscellaneous_DB** from the left-hand menu and select **Refresh**.

  * Scroll down to Schemas and expand that menu, and then expand the Tables menu.

    ![table-expand.png](Images/table-expand.png)

  * Right-click the new table and select **Import/Export** from the menu.

    ![import-export.png](Images/import-export.png)

* In the Options tab, complete the following steps:

  * Slide the Import/Export tab to **Import**.

  * Click on the dot menu to navigate to the `birdsong.csv` file on your computer.

  * Slide the Header tab to **Yes**.

  * Select the comma from the drop-down menu to set it as the Delimiter.

  * Leave the other fields as they are, and then click **OK**.

  ![import.png](Images/import.png)

* In the query tool, rerun `SELECT * FROM birdsong` to verify that data has been imported.

* Let the class know that the bigger a dataset is, the longer it will take for pgAdmin to import values.

</details>

<details>
  <summary><strong>✏️ 4.2 Student Do: Hide and Seek (10 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 33-34 to present this activity to the class.

In this activity, students will create a new table and import data from a CSV file.

* **Files:**

  * [WordAssociation_AC.csv](Activities/07-Stu_Hide_and_Seek/Resources/WordAssociation_AC.csv)

  * [WordAssociation_BC.csv](Activities/07-Stu_Hide_and_Seek/Resources/WordAssociation_BC.csv)

* **Instructions:** [README.md](Activities/07-Stu_Hide_and_Seek/README.md)

</details>

<details>
  <summary><strong>⭐ 4.3 Review: Hide and Seek (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slide 35 to assist you to review the activity.

* **File:** [hide_and_seek.sql](Activities/07-Stu_Hide_and_Seek/Solved/hide_and_seek.sql)

* Open pgAdmin and paste the code from `hide_and_seek.sql` into the editor. Explain the following:

  * Although the CSV data does not contain an `id` column, when we specify `SERIAL PRIMARY KEY` while creating the table, IDs will automatically be assigned to each row.

  * To view a range of data, we can use a combination of `WHERE` and `AND` statements.

  * To collect data that exists in either one column or another, the `OR` statement is included in the query.

* Walk through the solutions to the bonus questions, touching on the following points:

  * After importing the second table, we can specify a source with the `WHERE` statement.

  * `AND` statements can be used more than once for more specific results.

* Answer any questions before moving on.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=4+-+Hide+and+Seek&lessonpageTitle=Introduction+to+SQL&lessonpageNumber=9.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F09-SQL%2F1%2FLessonPlan.md)</sub>

- - -

## 5. Using CRUD

| Activity Time:       0:30 |  Elapsed Time:      2:20  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 5.1 Instructor Do: CRUD (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 36-38 to introduce CRUD to the class.

* Return to the slideshow and begin to explain CRUD operations.

  * CRUD, while an unusual acronym, is a set of tools that are persistently used throughout programming. CRUD stands for Create, Read, Update, and Delete.

* Engage the class in a discussion by asking them to provide examples of CRUD operations.

* In today's class, each of the operations has been in use. Students have:

  * Created data in a table with the `INSERT` statement.

  * Read data with the use of `SELECT`.

  * Updated a table's data using `UPDATE`.

  * Deleted data using `DELETE`.

* Introduce the class to an additional method of reading the data: wildcards.

  * A wildcard is a character—either a percentage sign or an underscore—that takes the place of one or more characters in a query.

  * The keyword `LIKE` indicates the use of a wildcard in a query.

  * The percentage sign (%) signifies that zero, one, or multiple characters will be substituted in a query.

    * For example, in the query `WHERE last_name LIKE 'Will%';` all names in the database beginning with "Will" will be returned, no matter the length.

  * When using the underscore as a wildcard, only a single character is replaced in the query.

  * In the line `WHERE first_name LIKE '_AN';`, only three-lettered names ending with "an" will be returned.

* Answer any questions before moving on.

</details>

<details>
  <summary><strong>✏️ 5.2 Student Do: Using CRUD (20 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 39-40 to present this activity to the class.

* In this activity, students will utilize CRUD operations (Create, Read, Update, Destroy) on the provided data.

* **Files:**
  * [schema.sql](Activities/08-Stu_CRUD/Resources/schema.sql)

  * [GlobalFirePower.csv](Activities/08-Stu_CRUD/Resources/GlobalFirePower.csv)

* **Instructions:** [README.md](Activities/08-Stu_CRUD/README.md)

* Let the class know that they will be using the `WHERE` clause in this activity.

* This activity will require students to do some research. Links are provided to help them search for solutions to problems they are likely to encounter.

</details>

<details>
  <summary><strong>⭐ 5.3 Review: Using CRUD (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slide 41 to assist you to review the activity.

* **Files:**

  * [schema.sql](Activities/08-Stu_CRUD/Resources/schema.sql)

  * [using_crud.sql](Activities/08-Stu_CRUD/Solved/using_crud.sql)

  * [GlobalFirePower.csv](Activities/08-Stu_CRUD/Resources/GlobalFirePower.csv)

* Open a query tool in `Miscellaneous_DB` and copy and paste the code from `schema.sql` to create a new table named `firepower`. Go over the following:

  * Refresh the table list, and then import the data from `GlobalFirePower.csv` into the new table.

  * First, alter the table to add an `id`.

  * Deletions and updates are made where the conditions are met.

  * Multiple averages can be selected at once.

  * Values can be inserted into the table even though not every value is filled out.

  * Finally, select all values to show the newly added country.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=5+-+Using+CRUD&lessonpageTitle=Introduction+to+SQL&lessonpageNumber=9.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F09-SQL%2F1%2FLessonPlan.md)</sub>

- - -

## 6. Joining the NBA

| Activity Time:       0:40 |  Elapsed Time:      3:00  |
|---------------------------|---------------------------|

<details>
  <summary><strong>📣 6.1 Instructor Do: Joins (15 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 42-44 to introduce joins to the class.

* **Files:**

  * [joins.sql](Activities/09-Ins_Joins/Solved/joins.sql)

  * [players.csv](Activities/09-Ins_Joins/Resources/players.csv)

  * [matches.csv](Activities/09-Ins_Joins/Resources/matches.csv)

* Students may recall working with merges and joins to combine datasets during the Pandas module. While SQL is a vastly different language than Python, it also includes the functionality to merge tables.

* Create two new tables in `Miscellaneous_DB` in pgAdmin named `players` and `matches`.

  * Copy the code from `joins.sql` to create the tables, and then import the corresponding data from `players.csv` and `matches.csv`.

  * Remember to refresh the database; newly created tables will not immediately appear.

  * Point out that both tables have matching values within the `player_id` column of the `players` table and the `loser_id`/`winner_id` columns of the `matches` table.

  * Because there are common values, it is possible to join these tables together. For example:

    ```sql
    INNER JOIN players ON
    players.player_id=matches.loser_id;
    ```

  * From the `joins.sql` file, copy and paste the code performing an `inner join` on the two tables:

    ```sql
    SELECT players.first_name, players.last_name, players.hand, matches.loser_rank
    FROM matches
    INNER JOIN players ON
    players.player_id=matches.loser_id;
    ```

  * Note: Some students may have advanced knowledge of SQL queries and use aliases in their solutions. Using aliases is not necessary for today's activities; they will be covered more comprehensively in the next class.

    ```sql
    -- Advanced INNER JOIN solution
    SELECT p.first_name, p.last_name, p.hand, m.loser_rank
    FROM matches AS m
    INNER JOIN players AS p ON
    p.player_id=m.loser_id;
    ```

  * Point out one significant difference between SQL joins and Python joins: in SQL joins, the columns that should be viewed after the join must be declared in the initial `SELECT` statement.

    ![inner-join.png](Images/inner-join.png)

* There are five primary types of joins that can be used with PostgreSQL:

  * `INNER JOIN` returns records that have matching values in both tables.

  * `LEFT JOIN` returns all records from the left table and the matched records from the right table.

  * `RIGHT JOIN` returns all records from the right table and the matched records from the left table.

  * `CROSS JOIN` returns records that match every row of the left table with every row of the right table. This type of join has the potential to make very large tables.

  * `FULL OUTER JOIN` places null values within the columns that do not match between the two tables, after an inner join is performed.

* Send out the link to this explanation of Postgres [joins](https://www.tutorialspoint.com/postgresql/postgresql_using_joins.htm) for students to study.

* Demonstrate a couple of different joins that can be performed. Then answer any questions before moving on to the next activity.

</details>

<details>
  <summary><strong>✏️ 6.2 Student Do: Joining the NBA (20 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slides 45-47 to present this activity to the class.

* In this activity, students will be using joins to query NBA player seasonal statistics.

* **Files:**

  * [Players.csv](Activities/10-Stu_Joins/Resources/Players.csv)

  * [Seasons_Stats.csv](Activities/10-Stu_Joins/Resources/Seasons_Stats.csv)

  * [schema.sql](Activities/10-Stu_Joins/Resources/schema.sql)

* **Instructions:** * [README.md](Activities/10-Stu_Joins/README.md)

</details>

<details>
  <summary><strong>⭐ 6.3 Review: Joining the NBA (5 mins)</strong></summary>

* Open the [slideshow](https://docs.google.com/presentation/d/1IhtPr1-L0J-AAToJeO8THcFPQhCwO2XlWkDJt7cXoKo/edit?usp=sharing) and use slide 48 to assist you to review the activity.

* **File:** [joining_the_nba.sql](Activities/10-Stu_Joins/Solved/joining_the_nba.sql)

* Using the schema.sql file and the query tool, create two new tables named `players` and `seasons_stats` using the data in `Players.csv` and `Seasons_Stats.csv`.

* Open `joining_the_nba.sql` and copy the code. Then open a new query tool and paste the solution into the editor. Review the solution, explaining the following:

  * Since the selected data comes from two different tables, the naming convention is `table_name.column_name`.

  * Next, determine which table to select from and which table to `INNER JOIN` with. Remember, the inner join only selects data that has matching values in both tables.

  * Finally, determine the key both tables will join on. For example, to join the two tables by using the `id` and an `INNER JOIN`, select the data columns to be viewed from both tables, and then specify which columns the tables will be connected by.

    ```sql
    SELECT players.id,
      players.player,
      players.height,
      players.weight,
      players.college,
      players.born,
      seasons_stats.position,
      seasons_stats.tm
    FROM players
    INNER JOIN seasons_stats ON
    players.id = seasons_stats.player_id;
    ```

* Answer any questions before ending class.

</details>

<sub>[Having issues with this activity? Report a bug!](https://form.jotform.com/200705887599168?activityOr=6+-+Joining+the+NBA&lessonpageTitle=Introduction+to+SQL&lessonpageNumber=9.1&whereIs=DataViz-Lesson-Plans+GitHub&typeA18=https%3A%2F%2Fgithub.com%2Fcoding-boot-camp%2FDataViz-Lesson-Plans%2Fblob%2Fv1.1%2FDataviz-Lesson-Plans%2F01-Lesson-Plans%2F09-SQL%2F1%2FLessonPlan.md)</sub>

- - -

### End Class

- - -

## References

Stowell, Dan and Xeno Canto contributors. (2014). Bird Sound Recordings. [https://archive.org/details/xccoverbl_2014](https://archive.org/details/xccoverbl_2014)

Loes, Anne. (2020). Wordgame: English word associations. Version 3. [https://www.kaggle.com/anneloes/wordgame](https://www.kaggle.com/anneloes/wordgame)


Global Firepower. (2017). Global Firepower. Initially compiled by Global Firepower [Global Firepower](https://www.globalfirepower.com) Edited and compiled by Blitzer. [https://www.kaggle.com/blitzr/gfp2017](https://www.kaggle.com/blitzr/gfp2017)

Sports Reference LLC. (2018). NBA Players stats since 1950. Version 2. Data initially compiled by [Sports Reference LLC](https://www.basketball-reference.com). Edited and compiled by Omri Goldstein. [https://www.kaggle.com/drgilermo/nba-players-stats](https://www.kaggle.com/drgilermo/nba-players-stats)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
