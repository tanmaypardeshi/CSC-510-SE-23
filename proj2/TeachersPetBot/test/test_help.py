###########################
# Tests help module
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
    commands_channel = discord.utils.get(testing_bot.get_all_channels(),
                                         name='q-and-a')
    guild = testing_bot.get_guild(guild_id)
    role = discord.utils.get(guild.roles,
                             name="Instructor")

    member = guild.get_member(testing_bot.user.id)
    await member.add_roles(role)

    print('testing main help')
    await commands_channel.send('!help')
    sleep(5)
    mess = await commands_channel.history(limit=1).flatten()
    for m in mess:
        assert 'help' in m.content
        await m.delete()

    async def answer():
        await commands_channel.send('!help answer')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'answer' in m.content
            await m.delete()

    async def ask():
        await commands_channel.send('!help ask')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'ask' in m.content
            await m.delete()

    async def attend():
        await commands_channel.send('!help attendance')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'attendance' in m.content
            await m.delete()

    async def begin():
        await commands_channel.send('!help begin-tests')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'begin-tests' in m.content
            await m.delete()

    async def create():
        await commands_channel.send('!help create')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'create' in m.content
            await m.delete()

    async def end():
        await commands_channel.send('!help end-tests')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'end-tests' in m.content
            await m.delete()

    async def oh():
        await commands_channel.send('!help oh')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'oh' in m.content
            await m.delete()

    async def ping():
        await commands_channel.send('!help ping')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'ping' in m.content
            await m.delete()

    async def poll():
        await commands_channel.send('!help poll')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'poll' in m.content
            await m.delete()

    async def setIns():
        await commands_channel.send('!help setInstructor')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'setInstructor' in m.content
            await m.delete()

    async def stats():
        await commands_channel.send('!help stats')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'stats' in m.content
            await m.delete()

    async def regrade_request():
        await commands_channel.send('!help regrade-request')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'regrade-request' in m.content
            await m.delete()

    async def update_request():
        await commands_channel.send('!help update-request')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'update-request' in m.content
            await m.delete()

    async def display_requests():
        await commands_channel.send('!help display-requests')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'display-requests' in m.content
            await m.delete()

    async def remove_request():
        await commands_channel.send('!help remove-request')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'remove-request' in m.content
            await m.delete()

    async def create_email():
        await commands_channel.send('!help create_email')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'create_email' in m.content
            await m.delete()

    async def update_email():
        await commands_channel.send('!help update_email')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'update_email' in m.content
            await m.delete()

    async def view_email():
        await commands_channel.send('!help view_email')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'view_email' in m.content
            await m.delete()

    async def remove_email():
        await commands_channel.send('!help remove_email')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'remove_email' in m.content
            await m.delete()

    async def test_end():
        await commands_channel.send('!help test')
        sleep(5)
        msg = await commands_channel.history(limit=1).flatten()
        for m in msg:
            assert 'test' in m.content
            await m.delete()

    await answer()
    await ask()
    await attend()
    await begin()
    await create()
    await end()
    await oh()
    await ping()
    await poll()
    await setIns()
    await stats()
    await test_end()
    await regrade_request()
    await update_request()
    await display_requests()
    await remove_request()
    await create_email()
    await update_email()
    await view_email()
    await remove_email()
