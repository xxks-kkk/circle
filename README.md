# circle
A code snippet management tool that meant to be extreme lightweight, powerful, and portable

## Why circle?

**In short: I hate GUI, and how commerical tool handle my snippet data: hiding it inside the app**

This is a hobby project when I started my career as a *professional* programmer at IBM. I should have but never used a code snippet management tool before, and I think it is time to develop my own code base in order to improve work efficiency. I tired some code snippet management tools but I was bugged out by their program size, GUI, and incapibility to meet my needs. So, I want to develop one on my own, and at the same time, hone my programming skills.

## What is target for circle?

Circle is a code snippet management tool that designed to work under UNIX-like system. It will *NOT* provide any GUI, and meant to be used under terminal. It aims to be open: provide a complete tree snippet file structure that can be manipulated easily without hiding all your snippets inside the software.

---------------------------------------------------------------------------------------------------------------------------------------------

## Scratch

The incomplete feature list includes:

- Auto line count about source code files, it will provide statistics to give you some stuff to brag about on the resume:
      
      shell: 2500L
      python: 3000L

- Working easily with Vim: 

      allow you to export the snippet directly from Vim without interrupting your workflow (ie. close vim, open vim, paste the 
      snippet, then back to vim to continue working)

- Intuitive text-based interface
      
      Title, Labels, Related URL, Snippet code

- Rich syntax highlight

- Include a DB for better performance, and organization? Maybe?

- Allow sync with Github or specified server

- Build a search engine on top of it with interface like google ( called "search my code base")

- CRAZY: Be a startup, built a community forum, reward top contributor, mainly like google but restricted to "search for code"
