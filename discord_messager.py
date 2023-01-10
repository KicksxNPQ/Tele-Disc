import asyncio

import yaml
import sys
import logging
import discord
import aiohttp
import os
import discordM

''' 
------------------------------------------------------------------------
    DISCORD CLIENT - Init the client
------------------------------------------------------------------------
'''

discord_client = discordM.DiscordManual().get()
with open('config.yml', 'rb') as f:
    config = yaml.safe_load(f)

''' 
------------------------------------------------------------------------
    MESSAGE AS WE RECIEVE FROM FORWARDGRAM SCRIPT
------------------------------------------------------------------------
'''

message = sys.argv[1]

send_channel_id = sys.argv[2]
index_of_channel = int(sys.argv[3])
path_image = sys.argv[4]

''' 
------------------------------------------------------------------------
    DISCORD SERVER START EVENT - We will kill this immaturely
------------------------------------------------------------------------
'''
# when discord is initalized, it will trigger this event. 
# we quickly send messages to our discord channels and quit the script prematurely.
# this gets trigged again when a new message is sent on channel from telegram

except_ids = ["1672577148", "1718929369"]


def isAddEveryone(mess, send_channel_id):
    if (not (send_channel_id in except_ids)):
        return mess + "\n @everyone"
    return mess


async def sendMessage():
    async with aiohttp.ClientSession() as session:
        try:
            webhook = discord.Webhook.from_url(config["discord_webhooks"][index_of_channel], session=session)
            mess = message.replace("@LeakNhomAD", "")
            if path_image != "":
                await webhook.send(content=isAddEveryone(mess, send_channel_id), file=discord.File(path_image))
                os.remove(path_image)
            else:
                await webhook.send(content=isAddEveryone(mess, send_channel_id))
        except Exception as e:
            print(e)
        finally:
            quit()

@discord_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(discord_client))
    print('Awaiting Telegram Message')
    await sendMessage()

if discord_client.is_closed():
    discord_client.connect(config["discord_bot_token"])
else:
    asyncio.run(sendMessage())

