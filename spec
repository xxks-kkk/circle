NOTE: This is my first seriously-treated spec, that follows 
writing philosophy by Joel on Software: 
http://www.joelonsoftware.com/articles/fog0000000035.html


------------------------------------------------------------

                    circle
            Functional Specification

                   Zeyuan Hu
             Last Updated: 10/14/15

------------------------------------------------------------


***** DISCLAIMER *****

This spec is not, by any stretch of the imagination,
complete. All of the wording will need to be revised several times 
before it is finalized. The layout of the screens is 
shown here merely to illustrate the underlying functionality. 
The actual look and feel will be developed over time with the input 
of iterative user feedback.

This spec does not discuss the algorithms used by tool,which will be 
discussed elsewhere. It simply discusses what the user sees when 
they interact with circle.


***** Overview *****

circle is a code snippet management tool that allows user to write and 
manage their code snippet in a terminal-based environment. Snippet, to my
understanding, is a chunck of code that serves as a guide/template for future
development.


***** Scenarios *****

Scenario 1: David
David is a geeky software developer who refuses to use copyright software 
unless he has to. During the day work, he deals with code a lot. 
Most of the time, he connects his windows laptop with company's server, and start
typing code on it. When he is done with googling and experiments with new code,
he wants to keep them future reference. 
But he feels laborsome to switch back to windows, and copy-paste his 
just-typed code into a GUI-based snippet management software. He 
feels this slow down his pace and drags him out of his "zone". Also, he doesn't 
seem to trust the copyright snippet management tool because the tool hideout his
snippets, and only gives him a option to export them. 

David now starts to use circle. Whenever he wants to save a piece of code, he simply
into visual mode, highlight them, and press a key, a new window will split out. It
will ask him entering title, labels, and snippet code. Once he is finished, he simply
press the same key, the window will close, and he can then back to work. 

In some cases, David may want to directly save the code he finds on web. He don't need
to open Vim. He can start circle as an independent program as well. Similarly, he can
enter title, labels, snippet code, and url. 

When he wants to reference the code, he can get a list-view by label or type key word
to search. Also, when he wants to see the actual code snippet not through circle, he 
can directly go to his specified circle snippet store location, and play around with
the snippet as he wishes. 


***** Non goals *****

This version will not support the following features:
    1. GUI
    2. Sophisticated search engine. I don't mean to build a search engine powerful like
    google. As long as it can search result for exactly David typing, it will be good.
    Later, if I have time, I can improve this a bit.
    3. Sync. Leave it here for now. Come back later.
    4. syntax highlight. Not the right time to figure out what is good syntax color
    for each code snippet.

