NOTE: This is my first seriously-treated spec, that follows 
spec writing philosophy by Joel on Software: 
http://www.joelonsoftware.com/articles/fog0000000035.html


------------------------------------------------------------

                    circle
            Functional Specification

                   Zeyuan Hu
             Last Updated: 10/18/15

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
best of understanding, is a chunck of code that serves as a guide/template for future
development.


***** Scenarios *****

Scenario 1: David

David is a geeky software developer who refuses to use copyright software 
unless he has to. During the day work, he deals with code a lot. 
Most of the time, he connects his windows laptop with company's server, and start
typing code on it. When he is done with googling and experiments with new code,
he wants a way to keep them future reference in an organized fashion. 
But he feels laborsome to switch back to windows, and copy-paste his 
just-typed code into a GUI-based snippet management software. He 
feels this slow down his pace and drags him out of his "zone". Also, he doesn't 
seem to trust the copyright snippet management tool because the tool hideout his
snippets, and only gives him a option to export them. 

David now starts to use circle. Whenever he wants to save a piece of code, he simply
into visual mode, highlight them, and press a key, a new window will split out. It
will ask him entering title, tags, and snippet code. Once he is finished, he simply
press the same key, the window will close, and he can then back to work. 

In some cases, David may want to directly save the code he finds on web. He don't need
to open Vim. He can start circle as an independent program as well. Similarly, he can
enter title, tags, snippet code, and url. 

When he wants to reference the code, he can get a list-view by label or type key word
to search. Also, when he wants to see the actual code snippet not through circle, he 
can directly go to his specified circle snippet store location, and play around with
the snippet as he wishes. 


Scenario 2: Zeke

Zeke is not as geeky as David but he still needs to do the work under Unix environment
most of the time. Zeke has no preference on what text editor he wants to use because
he doesn't care about that as long as he can get job done. However, he still needs a tool to
better manage his code snippet. He wishes a tool that allows him to enter "Title" "tag" "url"
"content" in command-line fashion, and provides some basic functionality to allow him browse
the entries. Maybe like a list? Maybe ... He doesn't know. One thing he particularly doesn't like
the previous code snippet management tool is that there is no separated interface for editing and viewing.
Previous tool merge two interfaces into one. Zeke consider himself as a careless guy. He usually messes up his
precious code snippets when he simply just want to lookup. He really wishes "circle" could fix this.


***** Non goals *****

This version will not support the following features:
    
    1. GUI. Definitely no!

    2. Sophisticated search engine. I don't mean to build a search engine powerful like
    google. As long as it can search result for exactly David typing, it will be good.
    Later, if I have time, I can improve this a bit.
    
    3. Sync. No interest to allow user to sync with Dropbox, Google Drive, OneDrive. Only support github for now.
    
    4. syntax highlight. Not the right time to figure out what is good syntax color
    for each code snippet.
    
    5. Customize tree file structure import. This feature is cool but not gonna do it now
    
    6. Database to manage entries. High chance not do it now. Maybe nice to implement this when I seriously consider 2) search engine
    
    7. Integration with text editor. I like to satisfy Zeke's wishes, and later move on to David's.

    8. No backup feature support yet. Definitely future.

***** Commands overview  *****

More like a command line tool. Everything starts with `circle ...`, where `...` represents some command line options

Note: <options> means placeholder for some options, --options means command option with name "options" exactly

# show all tags 
circle --tag

# show all entries
circle

# show entries under certain tag
circle --tag <tag>

# create a new entry
circle --new [-f |--file]

# view the entry
circle --view <entry_num>

# edit the entry
circle --edit <entry_num>
circle --edit <entry_num> [--title <new_title> | --tag <new_tag> | --url <new_url> | --content <content>]

# help
circle --help

# download locally
circle --download

# upload to github
circle --upload

# support config
circle --config <key> <value>

***** Details spec *****

1. install
    prompt user to specify where he wants to store his snippets. Then create a snippet directory under the previously specified
    directory

2. show all tags
    list all tags like this:

    shell
    c++
    Java
    ...

3. show all entries
    like this:

    shell
        <entry_num> <title1> [...]
        <entry_num> <title2> [...]
        <entry_num> <title3> [...]
    c++
        <entry_num> <title4> [...]
        <entry_num> <title5> [...]
        <entry_num> <title6> [...]
    Java
        <entry_num> <title7> [...]
        <entry_num> <title8> [...]
        <entry_num> <title9> [...]

    Note:
        3.1 [...] contains some stats about the file: for now, I think "number of open times" is the most important one
            because it tells how often user will use the file, and sort the file under each tag based upon this stat in 
            descending order.

4. show entries under certain tag
    the format will keep consistent with (3) show all entries.

5. create a new entry

    5.1 circle --new 
        
        after this one entered, a series of prompts will show up:

        - Title?
        - Tag?
        - Url?
        - Content?

        Those four prompts basically ask user to input the thing. User
        should have option to switch back and forth among these four prompts
        using arrow keys. 

        Note about each prompt will be following:

        - Title?

            User can enter anything they want

        - Tag?

            This is the place user enters the tag. Possible autocompletion will need.
            Here, "Shell" is same as "shell", "SHELL",... In other words, cases are ignored.

        - Url?

            This is for user to indicate where this code snippet comes from?

        - Content?

            This will open up editor that allow user to input their code snippet. Or, just let them
            input directly under the prompt? THINK!

            Pro editor: enjoys syntax highlight, and other great features comes with editor
            Con editor: separate interface, user may need to take extra effort memorizing what "Title" "Tag" ... they just input
    
    5.2 circle --new [-f | --file]

        -f or --file format indicates that user want to edit the file directly. This will open up a file with format much like 6) view
        the entry except the "stats area" will not be included.

6. view the entry
    
    6.1 format out nicely about "Title" "Tag" "Url" "Content". 
    6.2 add some stats info at the very beginning (like, directory of this code
        snippet, when first time created, when last time modified, number of times viewed, ...)
    6.3 automatically copy the "content" into clipboard and ready to use
    6.4 allow Zeke/David enters the <entry_num> to lookup without typing the long "title" or ...
    
    format like:

    ----------------------
    Stats area
    ----------------------
    Title, 
    Tag,
    Url
    ----------------------
    Content
    ----------------------

7. edit the entry

    This supports two types of commands:

        7.1 circle --edit <entry_num>

            This will prompt up the entry file to allow user to edit. The entry file will look much similar to 6) view the entry format except that
            there will be no stats area.

        7.2 circle --edit <entry_num> [--title <new_title> | --tag <new_tag> | --url <new_url> | --content <content>]

            This provide a quick way for user to modify the entry.

8. help

    Nothing new but please do format nicely.
	
9. download locally

	circle will download the code snippet from code snippet files to a local user-specified directory. The file will be compressed into tar.gz before
    downloading.

9. upload to github

    circle will upload code snippets to github. This allows both Zeke/David to enjoy some cloud feature: they can add code
    snippet from different machine, and get a copy of his own code snippets whenever he wants.

10. support config
    
    Mimic git. This will allow user to config circle with key-value pair. Alternatively, user can directly modify ~/.circleconfig file
    
