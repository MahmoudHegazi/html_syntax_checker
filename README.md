# html_syntax_checker
Python function to check if there is syntax errors in html code made it for my code editor

it has many problems like with when you use operator like < or > or / in code 
to reprsent less than or greater than 

# i search and found the best way to do that is by :
To check html, or any other language, you will have to make a proper parser. You need to go through the input text character by character and interpret everything. Your program will have to understand the different tags and the rules for them. There are several tags, like <pre> and <! --> that can contain anything, including broken html, so when you encounter those you have to suspend any parsing. And so on.
