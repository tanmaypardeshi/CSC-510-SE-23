"""
This file defines tests for email address configuration functions.
"""

import discord
from utils import wait_for_msg


async def test_create_email_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!remove_email')

    await commands_channel.send('!create_email no-reply-test@example.com')
    await wait('Email has been configured successfully!')

    await commands_channel.send('!remove_email')
    await wait('Email address has been deleted successfully')


async def test_update_email_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create_email no-reply-test@example.com')
    await wait('Email has been configured successfully!')

    await commands_channel.send('!update_email no-reply-test1@example.com')
    await wait('Email address has been updated successfully')

    await commands_channel.send('!remove_email')
    await wait('Email address has been deleted successfully')


async def test_view_email_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create_email no-reply-test@example.com')
    await wait('Email has been configured successfully!')

    await commands_channel.send('!view_email')
    await wait('Configured email address : no-reply-test@example.com')

    await commands_channel.send('!remove_email')
    await wait('Email address has been deleted successfully')


async def test_view_email_invalid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!view_email')
    await wait('There is no configured email address')


async def test_create_email_invalid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!create_email no-reply-test@example.com')
    await wait('Email has been configured successfully!')

    await commands_channel.send('!create_email no-reply-test@example.com')
    await wait('There is already an email address configured for this user. '
               'Please update it using update_email command')

    await commands_channel.send('!remove_email')
    await wait('Email address has been deleted successfully')


async def test_remove_email_invalid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!remove_email')
    await wait('There is no configured email address')


async def test(testing_bot, guild_id):
    commands_channel = discord.utils.get(testing_bot.get_all_channels(), name='q-and-a')
    guild = testing_bot.get_guild(guild_id)
    role = discord.utils.get(guild.roles, name="Instructor")
    member = guild.get_member(testing_bot.user.id)
    await member.add_roles(role)

    await test_create_email_valid(testing_bot, commands_channel)
    await test_view_email_valid(testing_bot, commands_channel)
    await test_update_email_valid(testing_bot, commands_channel)

    await test_remove_email_invalid(testing_bot, commands_channel)
    await test_view_email_invalid(testing_bot, commands_channel)
    await test_create_email_invalid(testing_bot, commands_channel)

    await member.remove_roles(role)
