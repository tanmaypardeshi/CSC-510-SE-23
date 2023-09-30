###########################
# Tests Spam
###########################
from time import sleep
import discord
###########################
# Function: test
# Description: runs each test
# Inputs:
#      - testing_bot: bot that sends commands to test TeachersPetBot
#      - guild_id: id of the guild that is using the TeachersPetBot
# Outputs: None
###########################
async def test(testing_bot, guild_id):
    await test_spam(testing_bot)

async def test_spam(testing_bot):
    qna_channel = discord.utils.get(testing_bot.get_all_channels(), name='q-and-a')
    await qna_channel.send('shit')
    await ctx.send("message 1")
    await ctx.send("message 2")
    await ctx.send("message 3")
    await ctx.send("message 4")
    await ctx.send("message 5")
    await ctx.send("message 6")
    messages = await qna_channel.history(limit=1).flatten()
    





