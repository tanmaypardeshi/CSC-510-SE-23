<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 0.208 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Mon Sep 18 2023 14:23:55 GMT-0700 (PDT)
* Source doc: Project 1 Difficulties
----->


<h1>Project 1 Difficulties and Lessons Learned</h1>

The purpose of this text is to go over what was hard about getting the Teacher’s Pet Bot to run. Additionally, we will discuss how those hardships could have been avoided, and most importantly what practices our group will commit to, in order to make sure others don’t face these hardships in the future. 

The first thing that should be noted is that the installation guide wasn’t explicitly clear on how to install the software. For example, there are some details clearly missing from the instructions on the .env file. For instance, the installation guide doesn’t explain what the .env file is/what it does, or where in the directory path it should be located. What’s worse is that the .env file example references things such as “test-bot-application-id” and “custom bot version”, without explaining what those are. All of this led to some extra pain spent figuring out what the original creators intended with the .env file. The issues the group faced will working with the .env file could have been quickly circumvented had the installation guide been rigorous in its explanations. We also noticed that the installation guide hadn’t actually been updated by the last group to work on the bot, which also shows the last group didn’t take the time to make sure the installation guide was in peak condition. Had the last group simply updated the installation guide at all, we are sure the .env file instructions would have been more clear. With all that in mind, the group has committed to making sure we are very rigorous and detailed in any guides we upload to GitHub, so that working together will be easier, but also so that when future groups try to work with our code it will be easier for them as well. Also we commit to making sure we update all the instruction guides on the GitHub that are not already up to par with how they should be, as had the last group done this, it would have saved us a lot of wasted time. 

The second set of issues we ran into were versioning errors. These errors led to the most trouble and took quite some time to figure out. For example, the first issue we ran into after following the installation instructions was the discord-components module from requirements.txt not even existing anymore. Or at least that’s what we thought, until we eventually found that “discord-components” had a name change a few years back and is now “discord-ui”. Of course, installing the most recent version of discord-ui led to even more problems as then some of the code was throwing errors. In particular, we found that some of the code used by the bot referencing discord-components was no longer apart of discord-ui. With this new knowledge, the group had to make a few updates to the code to account for the fact that some commands from discord-components were no longer apart of discord-ui. And to what should be no surprise to anyone, even once we fixed the initial code errors we still ran into errors when attempting to run. The last set of errors were especially tricky to figure out, but we eventually discovered that discord-ui stopped being updated fom some reason during 2022, meaning that discord-ui was no longer compatible with the newest version of discord.py (another package that is significantly important for the bot). In order to fix this issue we then had to depreciate the discord.py package we were using, to a version before it’s 2.0 era. Then, we tested the code, and finally things were working fine. To avoid the pains felt from this second set of issues, it would have taken quite a bit of effort. Number one, it would have helped a lot had the original team included information on when the required packages would no longer be available. Of course this may not have been information they had access to, but our team is committed to including that info on our GH if we have it. Another thing that definitely would have helped would have been if the code written by the original team had better comments explaining how things worked. Our group had to change the code significantly since the discord-components package was no longer the same, however it was hard to know what to change when certain functions such as “Select” needed a replacement from discord-ui but there was not given explanation as to what “Select” was doing in the first place. Because of this, the group has committed to writing standardized comments for functions that may not be clear be clear to users who have not worked with the software much before. 
