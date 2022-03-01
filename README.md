# QuizMe
_A Google Docs add-on that empowers reading comprehension through generated quizzes._

## Inspiration
Many teachers assign long readings to their students that are typically ungraded, so students can be tempted to skim through. This results in low memory retention and a poor understanding of the content. Quiz materials are a great solution but are difficult to find and do not always cover the content you’re interested in. That’s where QuizMe comes in, an easy-to-use, accessible tool that generates quizzes based on any text for students and teachers.

## What it does
QuizMe is a Google Docs Add-on, so it will appear in the sidebar of any Google Doc. Click on it, and a side panel opens asking you to select text to generate questions for and to enter a few parameters (# of questions, whether to create a Google Form from the questions / answers). Once you do, click "Quiz Me!", and the panel will present the questions and answers for the user to attempt. If the user decided to create a Google Form, buttons will appear to let the user take the Form as a quiz or to further edit the Form.

## How we built it
We used Apps Script, a cloud-based JavaScript platform that lets you integrate with and automate tasks across Google products, to build the front-end (the QuizMe side panel). From the front-end, we made a POST request containing the user's selected text and additional parameters to an API endpoint. This endpoint we created by setting up a Linux server using NGINX on Google Cloud; we then used Flask to handle the POST request in Python. 

In the Python code, we pass the selected text to a question generator [model](https://github.com/AMontgomerie/question_generator) and return the questions & answers to the front-end. The front-end formats and renders those questions & answers, and (optionally) it creates a Google Form quiz programmatically from them.

## What's next for QuizMe
The model currently generates only multiple-choice questions, so we would eventually add support for True/False, short answer questions, etc. In addition, the maximum number of words the back-end can process before timing out is around 512. If we can increase this capacity, our application would be able to generate questions over entire chapters of text at a time. Lastly, our server that hosts the model currently does not have a GPU; running question/answer generation on a GPU would reduce the speed by 50%, thereby improving user experience. 

