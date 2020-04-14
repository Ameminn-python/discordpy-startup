import discord
import os
import traceback
client=discord.client()
token = os.environ['DISCORD_BOT_TOKEN']


@client.event
async def on_message(message):
    if message.content == '/ch':
        await message.channel.send(str(message.channel.name)+':'+str(message.channel.id))
    if message.content == '/guild':
        await message.channel.send(str(message.guild.name)+':'+str(message.guild.id))
    if message.content.startswith('/role'):
        for role in message.role_mentions:
            await message.channel.send(str(role.name)+';'+str(role.id))
    
bot.run(token)
