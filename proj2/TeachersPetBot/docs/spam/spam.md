
# Location of Codehttps:
The code that implements the above commands is located [here](https://github.com/chandur626/TeachersPetBot/blob/main/src/bot.py)


# Code Description
## Functions
on_message(message):

This function takes as arguments the message in context and performs spam detection. It keeps track of the number of messages a user sent in a file called [spam.txt](https://github.com/chandur626/TeachersPetBot/blob/main/src/spam.txt). This file keeps track of the number of message a user sent in the channel. Once the limit is hit, the file auto clears. 

# How to run it? (Small Example)
This code runs everytime a message is sent in the channel. 

## An example 
### Send the following messages in the channel:
#### message1
#### message2
#### message3
#### message4
#### message5
#### message6
The channel will now give a warning saying too many messages.

When a user tries to send more than 5 (current threshold) messages in a channel, it gives a warning message saying that the user is trying to send too many messages. This functinality is specific to users. It doesn't stop the user from sending messages even it they hit their limit. 




