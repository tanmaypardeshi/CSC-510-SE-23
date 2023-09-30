###########################
# Tests Event creation functionality
###########################
import discord
from utils import wait_for_msg

async def test_create_assignment_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('assignment')
    
    await wait('What would you like the assignment to be called')
    await commands_channel.send('test')
    
    await wait('What is the due date of this assignment?')
    await commands_channel.send('01-01-1999')

    await wait('What time is this assignment due?')
    await commands_channel.send('13:37')

    await wait('Link associated with submission? Type N/A if none')
    await commands_channel.send('N/A')

    await wait('Extra description for assignment? Type N/A if none')
    await commands_channel.send('Some stuff')

    await wait('Assignment successfully created')


async def test_create_assignment_invalid_url(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('assignment')
    
    await wait('What would you like the assignment to be called')
    await commands_channel.send('test')
    
    await wait('What is the due date of this assignment?')
    await commands_channel.send('01-01-1999')

    await wait('What time is this assignment due?')
    await commands_channel.send('13:37')

    await wait('Link associated with submission? Type N/A if none')
    await commands_channel.send('Oops')

    await wait('Invalid URL. Aborting')


async def test_create_assignment_invalid_date(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('assignment')
    
    await wait('What would you like the assignment to be called')
    await commands_channel.send('test')
    
    await wait('What is the due date of this assignment?')
    await commands_channel.send('Oops')

    await wait('Invalid date')


async def test_create_assignment_invalid_time(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('assignment')
    
    await wait('What would you like the assignment to be called')
    await commands_channel.send('test')
    
    await wait('What is the due date of this assignment?')
    await commands_channel.send('01-01-1999')

    await wait('What time is this assignment due?')
    await commands_channel.send('Oops')
    
    await wait('Invalid Time format')


async def test_create_exam_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('exam')

    await wait('What is the title of this exam?')
    await commands_channel.send('test')

    await wait('What is the start date of this exam?')
    await commands_channel.send('01-01-1999')

    await wait('What is the start time for the exam?')
    await commands_channel.send('12:01')

    await wait('What is the end date of this exam?')
    await commands_channel.send('01-03-1999')

    await wait('What is the end time for the exam?')
    await commands_channel.send('12:01')

    await wait('What is the duration of the exam?')
    await commands_channel.send('85 minutes')

    await wait('description of the exam')
    await commands_channel.send('Some desc')

    await wait('Exam successfully created')


async def test_create_exam_invalid_start_date(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)
    
    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('exam')

    await wait('What is the title of this exam?')
    await commands_channel.send('test')

    await wait('What is the start date of this exam?')
    await commands_channel.send('Oops')

    await wait('Invalid date')


async def test_create_exam_invalid_start_time(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('exam')

    await wait('What is the title of this exam?')
    await commands_channel.send('test')

    await wait('What is the start date of this exam?')
    await commands_channel.send('01-01-1999')

    await wait('What is the start time for the exam?')
    await commands_channel.send('Oops')

    await wait('Invalid Time format')

async def test_create_exam_invalid_end_date(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)
    
    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('exam')

    await wait('What is the title of this exam?')
    await commands_channel.send('test')

    await wait('What is the start date of this exam?')
    await commands_channel.send('01-01-1999')

    await wait('What is the start time for the exam?')
    await commands_channel.send('12:01')

    await wait('What is the end date of this exam?')
    await commands_channel.send('Oops')

    await wait('Invalid date')


async def test_create_exam_invalid_end_time(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('exam')

    await wait('What is the title of this exam?')
    await commands_channel.send('test')

    await wait('What is the start date of this exam?')
    await commands_channel.send('01-01-1999')

    await wait('What is the start time for the exam?')
    await commands_channel.send('12:01')

    await wait('What is the end date of this exam?')
    await commands_channel.send('01-03-1999')

    await wait('What is the end time for the exam?')
    await commands_channel.send('Oops')
    
    await wait('Invalid Time format')

async def test_create_oh_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('office-hour')

    await wait('Which instructor will this office hour be for?')
    await commands_channel.send('Apollo')

    await wait('Which day would you like the office hour to be on')
    await commands_channel.send('Mon')

    await wait('What is the start time of the office hour?')
    await commands_channel.send('12:01')

    await wait('What is the end time of the office hour?')
    await commands_channel.send('12:01')

    await wait('Office hour successfully created')


async def test_create_oh_invalid_start_time(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('office-hour')

    await wait('Which instructor will this office hour be for?')
    await commands_channel.send('Apollo')

    await wait('Which day would you like the office hour to be on')
    await commands_channel.send('Mon')

    await wait('What is the start time of the office hour?')
    await commands_channel.send('Oops')
    
    await wait('Invalid Time format')

async def test_create_oh_invalid_end_time(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('office-hour')

    await wait('Which instructor will this office hour be for?')
    await commands_channel.send('Apollo')

    await wait('Which day would you like the office hour to be on')
    await commands_channel.send('Mon')

    await wait('What is the start time of the office hour?')
    await commands_channel.send('12:01')

    await wait('What is the end time of the office hour?')
    await commands_channel.send('Oops')
    
    await wait('Invalid Time format')


async def test_create_project_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('project')

    await wait('What is the title of this project?')
    await commands_channel.send('test')

    await wait('Please enter the due date of this project along with the time')
    await commands_channel.send('01-01-1999 12:45')

    await wait('Link associated with submission? Type N/A if none')
    await commands_channel.send('N/A')

    await wait('Extra description for project? Type N/A if none')
    await commands_channel.send('test project')

    await wait('Project successfully created!')


async def test_create_project_invalid_link(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('project')

    await wait('What is the title of this project?')
    await commands_channel.send('test')

    await wait('Please enter the due date of this project along with the time')
    await commands_channel.send('01-01-1999 12:45')

    await wait('Link associated with submission? Type N/A if none')
    await commands_channel.send('project_test_link')

    await wait('Invalid URL. Aborting, Please try again!.')


async def test_create_project_invalid_due_date(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('project')

    await wait('What is the title of this project?')
    await commands_channel.send('test')

    await wait('Please enter the due date of this project along with the time')
    await commands_channel.send('01-01-19 12:45')

    await wait('Invalid date format. Aborting, Please try again!.')


async def test_create_project_invalid_due_time(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create')
    await wait('Which type of event')
    await commands_channel.send('project')

    await wait('What is the title of this project?')
    await commands_channel.send('test')

    await wait('Please enter the due date of this project along with the time')
    await commands_channel.send('01-01-1999 1234:45')

    await wait('Invalid date format. Aborting, Please try again!.')


async def test(testing_bot, guild_id):
    commands_channel = next(ch for ch in testing_bot.get_guild(guild_id).text_channels if ch.name == 'instructor-commands')

    # Add instructor role to bot
    guild = testing_bot.get_guild(guild_id)
    role = discord.utils.get(guild.roles, name="Instructor")
    member = guild.get_member(testing_bot.user.id)
    await member.add_roles(role)

    await test_create_assignment_valid(testing_bot, commands_channel)
    await test_create_assignment_invalid_url(testing_bot, commands_channel)
    await test_create_assignment_invalid_date(testing_bot, commands_channel)
    await test_create_assignment_invalid_time(testing_bot, commands_channel)

    await test_create_exam_valid(testing_bot, commands_channel)
    await test_create_exam_invalid_start_date(testing_bot, commands_channel)
    await test_create_exam_invalid_start_time(testing_bot, commands_channel)
    await test_create_exam_invalid_end_date(testing_bot, commands_channel)
    await test_create_exam_invalid_end_time(testing_bot, commands_channel)

    await test_create_oh_valid(testing_bot, commands_channel)
    await test_create_oh_invalid_start_time(testing_bot, commands_channel)
    await test_create_oh_invalid_end_time(testing_bot, commands_channel)

    # test cases for project create event
    await test_create_project_valid(testing_bot, commands_channel)
    await test_create_project_invalid_link(testing_bot, commands_channel)
    await test_create_project_invalid_due_date(testing_bot, commands_channel)
    await test_create_project_invalid_due_time(testing_bot, commands_channel)


    # remove instructor role from bot
    await member.remove_roles(role)
