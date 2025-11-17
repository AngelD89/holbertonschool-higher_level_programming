This project introduces fundamental concepts of JavaScript and the DOM (Document Object Model). You will learn how to dynamically access, modify, and interact with HTML documents using JavaScript from the browser.

📚 Learning Objectives

By the end of this project, you should be able to explain:

🔹 General

What the DOM is and why it is important

What document, window, and element objects are

How to select HTML elements in JavaScript

How to modify an element’s attributes, classes, and content

How to listen and respond to events

How to create, append, and remove elements

How to load external data using Fetch API

What JSON is and how to use it

How to update the page dynamically without reloading

🛠️ Requirements
Files

All files must end with a new line.

You are not allowed to use var.

Use only Vanilla JavaScript (no jQuery).

Scripts

Must be executed in the browser.

Must be included in the HTML using:

<script src="filename.js"></script>

Code Style

Follow Holberton’s style guide.

Semistandard encouraged.

📂 Project Structure
.
├── 0-script.js
├── 1-script.js
├── 2-script.js
├── 3-script.js
├── 4-script.js
├── 5-script.js
├── 6-script.js
├── 7-script.js
├── 8-script.js
└── README.md

🧪 How to Test

Use the provided HTML files with each script. Example:

cat 7-main.html


Then open it in your browser:

file:///path/to/7-main.html


Scripts must update the DOM exactly as specified.

📝 Tasks Summary
0. Color me red!

Change the color of the <header> element to red using document.querySelector.

1. Click and turn red

Add an event listener that turns the <header> text red when clicking the #red_header element.

2. Add .red class

When clicking #red_header, add the class red to <header>.

3. Add a class on click

When clicking #toggle_header, toggle the classes red and green.

4. List of elements

When clicking #add_item, add a new <li> element to <ul class="my_list">.

5. Change the text

When clicking #update_header, update <header> to “New Header!!!”.

6. Star Wars character

Fetch the Star Wars API:
https://swapi-api.hbtn.io/api/people/5/?format=json

Display the character name in the element with id character.

7. Star Wars movies

Fetch all movies from:
https://swapi-api.hbtn.io/api/films/?format=json

Display each movie title in the <ul id="list_movies">.

8. Say Hello to Everybody!

Fetch the translation of “hello” from:
https://hellosalut.stefanbohacek.com/?lang=fr

Display the result inside the element with id hello.

This script must work when included in <head> — meaning it must wait for the DOM to load.

💡 Tips

Use DOMContentLoaded when scripts run from the <head> tag.

Always handle errors in fetch.

Test everything directly in the browser console.

👨‍💻 Author: Angel D. Bayo Torres

Project developed as part of Holberton School curriculum
JavaScript - DOM Manipulation
