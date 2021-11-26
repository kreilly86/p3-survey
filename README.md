<img src="assets/personality-profiler.png">

# Personality Profiler

The Personality Profiler is a terminal based personality survey using Python 3, which will capture and analyse data of the personality traits of extroversion , introversion and ambiversion.
<br>

## UX
<hr>

### User Stories
<hr>

    i. As a user I want to easily understand the terminal commands
    ii. As a user I want to answer questions that are concise and engaging
    iii. As a user I want feedback on my inputs and for any errors to be handled without much disruption
    iv. As a user I want to receive analysis of my survey answers
<br>

## APPLICATION FEATURES
<hr>
<br>

### BUGS AND ERRORS
<hr>
<br>
<img src="assets/error1.png">
<br>
When creating the run_survey function I encountered an error "Index Error: List index out of range" On closer expection I realised I had failed to seperate each question item with a comma, so the indexing was invalid. Once I added commas, the function ran as expected and generated feedback for the user.
<br>
<br>
<img src="assets/error2.png">
<br>
<br>
After I made the function to run the personality survey questions, I created a function called "calculate_trait()" that would take the "score" of the questions and give a value out of 10. By default I have the answers set to equate to an extrovert tendancy. Anything above 70% returns that the user is an extrovert, anything below 40% returns that the user is an introvert, and in between returns that the user is an ambivert. In the run_survey function I have a concatenated string giving the result value / the length of questions which equates to 10. I tried the code to state'" if result > 7/10, print message to user that they are an extrovert. And if "result < 4/10, print message to user that they are an introvert, else print they are an ambivert. Because the values are string values thus didn't work, so instead I changed the conditions and just took the result > 7, or < 4, as the result variable is a number this works, and because the length or questions is 10 it is easy to translate that as a percentage.
<br>
<br>

## CREDITS
<hr>

### CONTENT

The questions and info for the survey were taken from this TED.com article:
<br>
https://ideas.ted.com/quiz-are-you-an-extrovert-introvert-or-ambivert/
<br>
<br>

<br>
Canva for project logo creation
<br>
<br>

### CODE
<hr>

[Code Institute "Love Sandwiches" Project:](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode)

<br>
I used the the Love Sandwiches walkthrough project steps to link to Google Sheets.

#### TUTORIALS
<br>

[Mike Dane]("https://www.youtube.com/watch?v=SgQhwtIoQ7o") 
<br>
This tutorial helped me to create a Question Class instance and build the main survey questions to find out the users' personality type.








