<h1> TeachersPetBot Previous Features </h1>

<h2> Iteration I </h2>

### Initialization

When Teacher's Pet has been added to a new server as a bot, it will do the following:

* Create a new role called Instructor with Administrative permissions if one does not already exist
* Add the owner of the guild to the Instructor role
* Create a #q-and-a channel if one doesn't already exist
* Create a #calendar channel if one doesn't already exist

In addition to this auto-set up, there is also a command which allows a user with the Instructor role to give the same role to another user. This command will only work for users with the Instructor role already (for example, the guild owner).

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/bot_join.png)

### Q&A
The Q&A functionality allow students to ask and answer questions anonymously. The questions are numbered and when answers are sent, they are combined with the question so they can be easily found. Answers are also marked with `Student Ans` and `Instructor Ans` to distinguish between the sources.  
To ask a question, type `!ask "Question"` in the #q-and-a channel. Example: `!ask "When is the midterm?"`.  
![image](https://user-images.githubusercontent.com/32313919/135383816-430792aa-b8c3-4d6b-8176-1621293d089e.png)  
To answer a question type `!answer <question_number> "Answer"` in the #q-and-a channel. Example: `!answer 1 "Oct 12"`.  
Student answer:  
![image](https://user-images.githubusercontent.com/32313919/135383913-4a7431c3-9e14-466b-9a07-683df39bc1bc.png)  
Instructor answer:  
![image](https://user-images.githubusercontent.com/32313919/135383932-551850ef-6f6c-4349-b3a4-d36ce583de14.png)

### Events/Calendar
Events are items relevant to a class that are time-sensitive. Currently, the types of events include office hours, exams, and assignments. Events in a class are kept track of, and assignments/exams are displayed in a calendar for students and instructors to see.

Events can be created by instructors. Creation of an event can be initiated in the private `instructor-commands` channel with the `!create` command. The bot will ask the instructor about various details for the event. Once the event is created, it should exist persistently within the system and will be added to the event list.

The calendar is updated at the creation of any new event that gets displayed on the calendar. Everything is ordered by date and sorted into two categories, past events and future events. Links attached to assignments are displayed in the calendar as well. The footer of the calendar is tagged with the last time it was updated.

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/calendar.png)

### Office Hours
The bot contains functionality for handling TA office hours. After a TA office hour event is added and it is time for a TA's office hour to open, the bot will automatically create office hour channels in the server, allowing students to enter the office hour queue and instructors to help students based on the queue. Once the closing time for the office hour is reached, the channels related to the TA's office hour are automatically deleted.

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_channels.png)

##### Entering an office hour (as a student)
Students may wish to receive individual help from a TA or they may want to join other students for help as a group (when they need help with a group project, etc); TeachersPetBot supports both of these use cases. A student may enter the queue as an individual using the `!oh enter` command within the text channel for an ongoing office hour. Upon doing so, a new group will be created and the student will become the sole member of that group. Student may enter existing groups by inputting `!oh enter <group_id>`, where `group_id` is the ID of the group the student wishes to join (group IDs will be displayed in the queue). Once it is an individual's (or group's) turn to be helped by the instructor, all members of the group will be invited into a voice channel where they will be able to talk with the TA.

Upon entering this command in an office hour channel:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_enter.png)

The queue will look like this:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_lone.png)

Upon entering an existing group, say group '000':

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_enter_grp.png)

The queue will look like this:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_group.png)

##### Exiting the office hour queue (as a student)
A student may wish to exit the office hour queue for whatever reason; they may do so by typing `!oh exit` in the channel they are in the queue for.

If a student exists in the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_lone.png)

And enters this command:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_exit.png)

The student will be wiped from the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_empty.png)

##### Traversing the queue (as an instructor)
Once the instructor is ready to help the next student in the queue, they may enter `!oh next` in the office hour text channel. Upon doing so, DMs will be sent to all group members next in the queue notifying them that it is their turn, and they will be able to enter the office hour voice channel.

If a student exists in the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_lone.png)

And an instructor wishes to help the next student in the queue:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_next.png)

The student will be invited to the instructor's voice channel and the queue will be advanced:

![image](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/oh_empty.png)


### Profanity Censoring 

Using the Python package better-profanity, Teacher's Pet will catch profane words sent by members of the guild, delete the message, and re-send the exact message with the bad word(s) censored out. It will also catch profane words in messages which have been edited to incude bad words. This package supports censoring based off any non-alphabetical word dividers and swears with custom characters. NOTE: Currently the Bot does not censor swears which have had extra alphabetical characters added.

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/profanity_example.PNG)

<br>
<h2> Iteration II </h2>

### New Member joining channel

Upon a new member joining the channel the BOT send the member a welcome message to the member in a private chat:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/member_addition.jpeg)

### Instructor view/modification

The remove instructor command can only be used by an instructor in the instructor commands channel. I removes a existing instructor from the role of an instructor and revokes the members permission to access the instructor commands channel.

When the remove instructor command is used:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/remove_Instructor.png)

The getInstructor command can be used in any channel and list outs the members in the guild who have Instructor role.

When the get instructor command is used:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/get_Instructor.png)

### Attendance

This functionality can be used only by the instructor. instructor-commands is the channel used. The command checks the total students in the guild with the students currently available in the General voice channel. It then generates the number of attendees and absentees. Then the students list is pushed to the instructor-commands channel.

When the attendance is requested by the instructor in the correct channel:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/attendance.png)

When the attendance is requested by the instructor in the wrong channel:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/attendance_wrong_channel.png)

### Help

This is a custom help command which is describes the command and on demand of a specific command, it provides syntax of the command, permitted users and channels. This command can be executed in any channel and by anyone.

General Help:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/help.png)

Help for a specific command:

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/help_command.png)


### Custom Profanity Censoring 
Building upon the existing python package better-profanity, Teacher's pet, in addition to catching the existing profane words, will now give an option to declare custom words as profane. This adds them to the list of words to be filtered and any further use of said word would cause it to be censored. 
NOTE: Currently the Bot does not censor swears which have had extra alphabetical characters added.
Working : 
Use the below syntax to include the custom word to the profane list:
![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/custom_profanity1.png)

Whenever the above word is used the below flow is triggered : 
![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/custom_profanity2.png)

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/custom_profanity3.png)


### Detecting Close Calls (Upcoming Assignments and Exams)
This task runs in the background, once a day it checks if there are any assignments and exams coming up and reminds students. It works as follows : 

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/close_calls2.png)

Whenever there is nothing to remind : 

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/close_calls1.png)

### Poll Command
This command allows the Instructors to create a custom poll for the class. The command takes the following as inputs - Duration of the poll, Topic on focus, Options . Once the poll duration is complete the the command ends and displays the result of the poll. Note: A student can only vote for single option.<br />
Example: `!poll 2 "Topic for Tmrw's class" Physics chemistry biology maths`

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/poll_command.png)

### Utility Commands

#### Ping Command
Since the bot is hosted on cloud ( In this case Heroku ). Its crucial to know the latency of the bot. This command  `!ping` returns the ping and the corresponding response time.

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/ping_command.png)


#### Status Command
For the purpose of Debugging and maintaining the bot `!stats` command has been added to keep track of CPU usage, Bot up time, Bot version, No. of users and Memory usage.

![alt text](https://github.com/Ashwinshankar98/TeachersPetBot/blob/main/images/stats_command.png)
