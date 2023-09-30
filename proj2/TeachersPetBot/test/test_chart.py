"""
This file defines tests for chart configuration functions.
"""

import discord
from utils import wait_for_msg


async def test_chart_valid(testing_bot, commands_channel):
    async def wait(content):
        await wait_for_msg(testing_bot, commands_channel, content)

    await commands_channel.send('!chart grades pie A B C 5 4 3')
    await wait("Here is your chart:")

    await commands_channel.send('!check_chart grades')
    await wait("Your requested chart:")


async def test(testing_bot, guild_id):
    commands_channel = discord.utils.get(testing_bot.get_all_channels(), name='q-and-a')
    guild = testing_bot.get_guild(guild_id)
    role = discord.utils.get(guild.roles, name="Instructor")
    member = guild.get_member(testing_bot.user.id)

    await member.add_roles(role)

    await test_chart_valid(testing_bot, commands_channel)
