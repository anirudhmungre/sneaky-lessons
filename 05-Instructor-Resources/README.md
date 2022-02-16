# Instructional Staff Resources

Welcome to the Data Boot Camp! We're happy that you will be leading our classes and want to prepare you for successful sessions. Consider this a resource that will cover known issues, frequently asked questions, and more!

## Known Issues

* [MacOS Catalina Update](resources/catalina.md)

- - -

# Student FAQ

We know how many different questions can pop up during the course of this class, especially with such a scope of technologies covered. This FAQ is intended to answer many common questions asked by students during this course. We hope you find it useful!

If you think of other potential questions to add, please let us know! We are always looking for more feedback. Feel free to log an issue or a pull request with your desired additions.

## Table of Contents

[Unit 01 - Excel](#unit-01-excel) <br>
[Unit 02 - VBA Scripting](#unit-02-vba-scripting) <br>
[Unit 03 - Python](#unit-03-python) <br>
[Unit 04 - Pandas](#unit-04-pandas) <br>
[Unit 05 - Matplotlib](#unit-05-matplotlib) <br>
[Unit 06 - Python APIs](#unit-06-python-APIs) <br>
[Unit 07 - Project 1](#unit-07-project-1) <br>
[Unit 09 - SQL](#unit-09-sql) <br>
[Unit 10 - Advanced Data Storage and Retrieval](#Unit-10-advanced-data-storage-and-retrieval) <br>
[Unit 11 - Web](#unit-11-web) <br>
[Unit 12 - Web Scraping and Document Databases](#Unit-12-web-scraping-and-document-databases) <br>
[Unit 13 - ETL Project](#unit-13-etl-project) <br>

[Unit 15 - Mapping Web](#unit-15-mapping-web) <br>
[Unit 16 - R](#unit-16-r) <br>
[Unit 18 - Tableau](#unit-18-tableau) <br>

[Unit 21 - Machine Learning](#unit-21-machine-learning) <br>
[Unit 22 - Big Data](#unit-22-big-data)

## Unit 01: Excel

#### What's the relevance of Excel?

Many Enterprise-level organizations still use Excel in their day-to-day operations and expect new employees to be comfortable working with their legacy data in their preferred software.

We also want everyone to start off on the same footing. Later in class we will be diving even deeper into data software, so we want to make sure that we all have a strong and solid foundation. We will be starting VBA next week and having a good understanding of Excel will make it easier for everyone to stay on the same page.

- - -

## Unit 02: VBA Scripting

#### What's the relevance of VBA?

You can consider VBA to be an introduction into the basics of programming that will become more relevant later in the course. VBA is also a great tool you can use to automate the data manipulation that we do in Excel.

VBA is also prevalent in many older companies and in the financial industry. Many of these companies will value your ability to manipulate their legacy data in Excel with VBA.

- - -

## Unit 03: Python

#### What's up with this crazy indentation?

With Python, indentation is more than just organization and readability. Python's functionality actually depends on proper indentation!

In this snippet, we're using indentation to tell our code where our for loops begin and end. In Python, indenting creates blocks of code that work together. Similarly, indenting backwards tells the program when to end a loop.

```python
for x in range(10):
    print(x)

for x in range(20, 30):
    print(x)
```

The code you will write in Python will eventually be seen by someone else. Focusing on organization and readability is important because you want colleagues to be able to read your code. If your code is poorly organized it will be difficult to read later on.

- - -

## Unit 04: Pandas

#### When should we use Pandas versus just using Python?

Python is a scripting language, while Pandas is a library that works on top of Python and makes data manipulation easier.

Libraries are pre-written chunks of code that make it easier to unlock the capabilities of a programming language. Someone else already did a ton of hard work to create these libraries and make your life easier and your workflow more efficient.

It would be a slog to manually go through all of your data with vanilla Python. Pandas makes this process much quicker.

You can think of it like what it's like using Excel vs using VBA with Excel.

- - -

## Unit 05: Matplotlib

#### I'm having trouble picking up on this new syntax...

Luckily, there is documentation for that! Whenever we work with a library, we are using code that is already pre-written. We always need to reference the documentation when using a new library. Think of documentation as a set of detailed instructions. Without looking at the instructions, you will never know how to use a new piece of technology.

We recognize this may be your first time looking at a library that is less semantic, or readable, but this will be a constant for the future. You will see a lot of new technology throughout the course, and each time you will need to dive into the documentation. The documentation quality and organization will be different for each new technology, so learning how to read general documentation is a skill in itself.

- - -

## Unit 06: Python APIs

#### How do I differentiate between the client and the server?

The web applications we build in class (and all other web apps) will live on a server, which is basically a gigantic computer or network of computers. When a user goes into their browser and types in an address, the server sends information to the user's computer, or the client.

Basically: Clients request from the server, and the server returns a response.

#### Where can I find more information on how to use these APIs?

Each API is a pre-written set of code that helps you interact with somebody elses information. Every API will come with its own set of documentation, and much like with a library, you will have to dive into it! There should be a developer section on each site that will explain the service and any potential limitations.

Any time we work with an API, it's a good idea to have the documentation ready and refer to it frequently. This is all part of the process when it comes to picking up and familiarizing yourself with new technologies.

- - -

## Unit 07: Project 1

#### I'm not feeling confident with Git... What are some resources that could help?

Start with our pre-work, which has two modules with video tutorials and activities that can help out with the foundations of working with Git:
[Bootcamp Pre-work](https://coding-bootcamp-dataviz-prework.readthedocs-hosted.com/en/latest )

Conveniently, GitHub has their own set of guides to help break down how to use the program:
[GitHub Guides](https://guides.github.com/)

Additionally, if you find videos helpful in your learning process, this is roughly an hour of video designed to cover the fundamentals of Git and GitHub:
[No Nonsense Github Videos](https://github.com/Multishifties/No-Nonsense-Github-Project)

Finally, we have a handy visual Git reference guide located here:
[Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-en.html)

#### How will this project beneficial?

Each project that we tackle in this class serves multiple purposes, and they will all be highly critical in your development as a data professional. First, group projects allow you to start developing a collaborative workflow that is very similar to the workflow you would encounter at many jobs in the field. Good teamwork is an essential real-world skill. Working in a group also allows you to accomplish more and create more impressive projects than you would be able to alone! Take advantage of it!

This project will be your first opportunity to build a data presentation from the ground up. This is something you will do many times as a data professional, so the more you practice and reinforce these skills, the better off you will be in the field!

Finally, this project is going to be featured in your resume and portfolio. Having strong examples of your work in your professional materials increases the chances to wow a potential employer and ultimately get hired!

- - -
  
## Unit 09: SQL

#### What's the relevance of PostgreSQL?

PostgreSQL, or Postgres, is a really cool free, open-source object-relational database management system. Databases are going to be crucial in our work as data professionals! PostgreSQL is also most popular with some of the careers that our course is helping prepare you for.

Remember how we discussed the relationship between client and server earlier? We can think of our database as the third part of that relationship. Essentially, the client sends a request to the server, the server grabs the associated data from the database, and then the retrieved data is returned to the client by the server.

#### But what does SQL mean?

SQL stands for Structured Query Language. Put simply, SQL is the language that we use to interact with our database. SQL is the most widely used database language, is incredibly effective at manipulating data, and is one of the easier languages to learn! Learning SQL is also great for employability - There are thousands of jobs that look for candidates with SQL experience!

- - -

## Unit 10: Advanced Data Storage and Retrieval

#### What is SQLite and why use it?

SQLite is a dialect for using an SQL database. The syntax is very similar to the PostgreSQL syntax, with the main difference between the two being that SQLite is entirely serverless. SQLite allows for the power of database storage but with a tiny footprint. SQLite is also conveniently part of the standard Python library, so no additional setup is needed to get it up and running.

SQLite is not comparable with PostgreSQL or any other SQL language, rather it focuses on providing local data storage for individual applications.

#### What does ORM mean?
ORM stands for Object-Relational Mapper. Object-relational mapping allows us to write SQL queries using the object-oriented paradigm of the language with which you prefer to work. In other words, for our purposes in class, it allows us to interact with our database using Python.

#### How are classes relevant?
As you already know, Python is an "Object-Oriented Programming (OOP) language", which means that it is highly concerned with organization and reusability. Classes are crucial to OOP in that they allow us to group related things and keep them together.

A class is essentially a template that allows us to create objects, which have variables and behaviors associated with them. It helps streamline our code and create efficiencies whenever something needs to be used various times.

- - -

## Unit 11: Web

#### What's the relevance of using web technologies like HTML and CSS?

Learning these web technologies teaches us an entirely new way to present our data: in a beautiful web application! Having an impressive GUI with which to present your findings can truly take your work to the next level, and looks great to employers and stakeholders!

- - -

## Unit 12: Web Scraping and Document Databases

#### Why are we using Mongo now? I thought SQL was the best!

While SQL is an extremely powerful language for defining and manipulating data, it can actually be restrictive. SQL requires you to use predefined schemas to determine your data structure, and requires that all of your data follow the same structure.

A NoSQL database has a dynamic schema for unstructured data and can store data in a variety of ways. This gives it much more flexibility in practice as not all data will come structured in the same way.

- - -

## Unit 13: ETL Project

#### Why are we doing this project?

ETL, or Extract, Transform, Load, is a critical aspect of working with data. With ETL, we are essentially pulling in data from various sources, cleaning and restructuring it, and then writing it into a database for storage. This workflow is something you will see time and time again as a data professional. It will be an opportunity to see everything built from the ground up in class.

- - -

## Unit 14: Intro to JavaScript

#### Oh no! More new syntax that I don't understand!?

Don't be afraid! Learning new syntax can certainly feel like learning a whole new language. And that's what we're doing! We don't expect you to be JavaScript masters! All of this information is iterative and your skills will only improve with time and practice. If it becomes overwhelming take advantage of office hours to spend time with the instructional staff to help get you over the hill. Please don't be afraid to reach out for help! We are all here for your success.

#### Why do we need to learn JavaScript? I thought this was a Python course...

Learning how to build functional web applications with HTML, CSS, and JavaScript is going to open up a world of possibilities for presenting our data! Many of the libraries that we will be using for impressive visualizations are JavaScript libraries, making it an essential skill for some of our more interactive visualizations.

Learning JavaScript also gives you another real world skill to add on to your resume that employers love!

#### Why would I use Plotly instead of Matplotlib or another library?

While Plotly.js is not necessarily "better" than Matplotlib or another plotting library, it is useful for a variety of reasons! Plotly is also incredibly popular in the data community.

Plotly.js uses both D3.js and WebGL to render graphics, works with JSON schema, and supports a large variety of map charts, including basic, statistical, financial, and scientific!

- - -

## Unit 15: Mapping Web

#### Why is it useful to map out data geographically?

Your datasets should be visualized and explained in different ways depending on the background context of the data and what your stakeholders are most interested in learning. Oftentimes, the geography in the data is highly relevant. For example, a marketing stakeholder would be interested to know the popularity of their product in specific states to understand how to best move forward with their campaigns.

- - -

## Unit 16: R

#### What is the relevance of R?

R is a programming language used for statistical computing, commonly used in data analysis and by data miners. It’s also used for its strength in graphics.

While you don’t need to walk away with a mastery of this language, it’s helpful to gain exposure to multiple languages and technologies throughout this course to gain some familiarity with their core concepts.

- - -

## Unit 18: Tableau

#### How is this different than Excel or the other ways I’ve learned to make a chart?

While Excel and VBA allow you to be very flexible in how you manipulate your data, Tableau allows you to more easily discover visualizations to which you want to apply your data, even ones that aren’t readily available in Excel, like world maps.

Tableau also allows for high flexibility in changing data sources for creating charts, changing your mind on what kind of chart you want to use, and allows you to add data and change scenarios on the fly without much overhead. The drag-and-drop abilities of Tableau make it incredibly simple to integrate more data (and it can handle **a lot** of data, more so than Excel).

Different tools for different uses makes it easier for you to adapt and adjust, giving your stakeholders what they want.

#### Why are we using the public version and not student?

Typically, you’ll find that a lot of platforms that offer student discounts or trials do not extend this to students of continuing education programs or students without university email addresses. Please ask your SSM about your university policies on this.

#### What is the difference between public and pro?

Tableau Public is a free version of the software that provides all the same tools as Pro. However, because it’s free, it requires all data that is input to be freely accessible to everyone, and has a limit of 1 million rows. This version should not be used if you’re dealing with any sensitive or privileged datasets. This version also does not allow saving to your machine and you must save to their server.

- - -

## Unit 21: Machine Learning

#### What is the relevance of machine learning?

Machine Learning is one kind of data analysis that automates model building leading us into the creation of systems that can identify patterns, make decisions, and learn without much human intervention. It's an exciting realization of the growth of artificial intelligence as a computer learns from previous computations and produces reliable and repeatable results from their decisions.

While Machine Learning has been around for a while, there's been a spike in its popularity in more recent years. You can hear about it used more by marketing professionals through Twitter, in the recommendation system that Netflix, Hulu, and Amazon use, and even within self-driving cars. The purpose of Machine Learning here is to analyze more data in less time, delivering accurate results every time.

This branch of data analytics is going to continue growing in various areas including the financial sector to identify investment opportunities, government work to detect fraud, and the further advancement of wearable healthcare devices.

#### How much Machine Learning knowledge will I walk away with?

Machine learning is a very deep well of knowledge. We could have an entire course dedicated to Machine Learning and still walk away wanting to know more. This course is meant to provide you with an introduction into Machine Learning and give you the tools and familiarity to continue this education on your own. Take advantage of in-class time, office hours, and your network of peers to continue learning more about Machine Learning.

- - -

## Unit 22: Big Data

#### What is the relevance of Big Data?

Our methods of data collection have grown quite a bit in the past few years. We now have a massive amount of data available, but adequately parsing, processing, and analyzing this data is difficult to do using our traditional applications. 2.3 trillion gigabytes of new data is created each day in both structured and unstructured formats. Knowing how to process and analyze this data is a very in-demand skill.

Using Big Data, businesses can gain understanding in where, when, and why their customers buy their product. They can provide targeted advertisement in a more efficient way. They can predict market trends and anticipate future production needs. They can have an edge on the competition or their own future improvement. They can identify new sources of revenue. Big Data can be a game changer to a company.

#### How much Big Data knowledge will I walk away with?

Similar to Machine Learning, Big Data is a very deep well of knowledge. We could have an entire course dedicated to understanding how to handle Big Data effectively and still walk away wanting to know more. This course is meant to provide you with an introduction into Big Data and give you the tools and familiarity to continue this education on your own. Take advantage of in-class time, office hours, and your network of peers to continue learning more about Big Data and its real world use cases.
