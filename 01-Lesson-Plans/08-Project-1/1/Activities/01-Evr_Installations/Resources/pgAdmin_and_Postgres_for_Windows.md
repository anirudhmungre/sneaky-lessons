# Installing pgAdmin and Postgres on Windows

Similar to coding with Python using Visual Studio Code, SQL requires a code editor with the ability to execute the scripts developers (you!) create.

## Before you Begin

* Remember to choose the installation package specific to your operating system and download the latest version.

* Be prepared to record a password, this will be needed later!

## Download Link(s)

* [PostgreSQL](https://www.enterprisedb.com/downloads/postgresql)

* [Installation Instructions](https://www.enterprisedb.com/edb-docs/d/postgresql/installation-getting-started/installation-guide-installers/12/index.html)

## Instructions

* **Note:** You will be prompted to create a free account prior to downloading the software.

* After downloading the latest version of PostgreSQL 12.7, double click on the `postgresql-12.7-2-windows-x64.exe` file.

* **Note:** exact file version may be slightly different.

  ![postgresql-12.7-2-windows-x64.png](../Images/postgresql-12.7-2-windows-x64.png)

* Go through the Setup Wizard and install PostgreSQL. Keep the default location as: `/Library/PostgreSQL/12`.

* Select the components to be installed. **Un-check the option to install Stack Builder.

  ![stack_builder.png](../Images/stack_builder_pc.png)

* Next, add your Data Directory. Keep the default location as: `/Library/PostgreSQL/12/data`.

* Next, enter `postgres` as the password. **Be sure to record this password for future use.**

* Keep the default port as `5432` and in the Advanced Options, set locale as as `[Default locale]`.

* The final screen will be the `Pre Installation Summary`.

* When you are done, the `Postgres 12` folder can be accessed from the start menu of your computer.

  * This folder contains the `pgAdmin 4` application, which will be used throughout this unit.

  * To confirm the installation, start `pgAdmin` (this will open in a new browser window) and connect to the default server by clicking on it and entering the password if prompted.
