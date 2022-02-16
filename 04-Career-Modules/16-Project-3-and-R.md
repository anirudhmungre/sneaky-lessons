# Career Connection

Welcome back to another Career Connection! This week you explored the R programming language and software environment that is commonly used for statistical computing. In fact, the R language is so widely used among data scientists that as of November 2019, R ranks 16th in the [TIOBE Index](https://www.tiobe.com/tiobe-index/), a measure of coding language popularity.

So what? Who cares?

You do! Because R is so popular, there is a decent chance that you’ll come across platforms using the R language or you’ll need to do some work with it in your data career. As with any platform or language, there are both opponents and evangelists of using R in enterprise organizations. It has traditionally been very popular in the academic setting, but it has recently gained traction in the commercial scenes because it can do almost anything that you want it to do.

**Did You Know?**

> Facebook uses a technique called power analysis, which allows the company to figure out whether it has collected enough data when studying user interactions with its online platform ([source](https://www.fastcompany.com/3030063/why-the-r-programming-language-is-good-for-business)). Research data scientists developed these statistical tools in R and made them available across the company.

## Look to the Future

Now that you have gotten your feet in the world of R, let’s make sure those who come across your profile know that. Let’s implement some Employer Competitive strategies.

- Build Your Visibility

  - Attend one or two local Meetups/Eventbrite events in the next couple of weeks. You can find groups that are R specific or that discuss data visualization topics in general.
  - Aim to make at least two or three meaningful connections—have conversations and exchange contact details.
    Reach out to those contacts within 48 hours of the meetup.

- Improve Your Skills

  - We spent a week learning R, but there is so much more to learn. Find an online tutorial on YouTube, Udemy, PluralSight, or another site and practice something we learned in class—or look up something new.

## Technical Interview

This week’s technical interviewing preparation section will be slightly different from other weeks. Instead of a few questions to give special consideration to, we are providing a larger list of questions you might face during an interview around the R programming language.

We strongly recommend you review each of the questions and the answers—practice them with somebody from your cohort, one to one, outside of class. One of you could be the interviewer while the other acts as the interviewee.

You might know the answer to those questions we discussed in class, but others you’ll need to research. Either way, try to discover the answers for yourself before looking at our answer key. This will aid you in remembering the answers.

1. What are the different data structures in R?
2. What is RMarkdown?
3. How do you install a package in R?
4. What is shinyR?
5. What does `cbind()` do?
6. How would you join multiple strings together?
7. How do you import and read a CSV file into R?
8. Name three functions that can be used for debugging in R.
9. How would you extract one particular word from a string?
10. Write a for loop in R to print a list of fruits.

### Answer Key

1. Vector, list, matrix, and data frame
2. RMarkdown is reporting tool provided by R
3. `install.packages(“<package_name>”)`
4. `shinyR` is a package that allows you to build interactive web applications using R. It can be extended with CSS themes, htmlwidgets, and JavaScript.
5. `cbind()` binds two columns together.
6. `string_c()`
7. `read.csv()`
8. Possible answers: `traceback()`, `debug()`, `browser()`, `trace()`, `recover()`
9. `string_extract_all()`
10. Answer:

```py
    fruits<-c(“orange”, “grapes”,”kiwi”)
    for(i in fruits) {
        print(i)
    }
```

### Case Study

> AirFly is a new global budget aviation company that has seen tremendous success in offering long-haul budget flights, imitating successful European models like EasyJet and Ryanair. However, AirFly executives recently felt that their statistical analysis system was not providing them enough data in a uniform manner—in fact, each department had its only individual reporting system, which in turn required a heavy contribution from the IT and accounting departments in time and finances to bring together the reports for analysis.
>
> Because AirFly is focused on providing low-cost service across the globe, cutting costs in areas that do not affect personnel is given the highest priority. Executives realized that reporting was being done manually in many areas, and was thus time-consuming and prone to mistakes. What AirFly needs is a central statistical tool that can collect, analyze, and visualize data from multiple sources that can be prepared quickly and allow for almost-instant report generation.
>
> Convinced by work done at other companies, AirFly has decided to create a new tool using R. You have been successful in obtaining an interview at the company to be one of the new engineers being brought on to create the tool.
>
> The hiring manager would like you to put together a one-page overview of how you might tackle this system, including any packages you might use. Feel free to get creative!

## Continue to Hone Your Skills

If you're interested in learning more about the technical interviewing process and practicing algorithms in a mock interview setting, check out our [upcoming workshops](https://careernetwork.2u.com/?utm_medium=Academics&utm_source=boot_camp).
