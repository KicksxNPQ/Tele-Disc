import yaml
import sys
import logging
import discord
import aiohttp
import os
''' 
------------------------------------------------------------------------
    DISCORD CLIENT - Init the client
------------------------------------------------------------------------
'''

intents = discord.Intents(members=True, guilds=True)
discord_client = discord.Client(intents=intents)
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
    if (not(send_channel_id in except_ids)):
        return mess + "\n @everyone"
    return mess

@discord_client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(discord_client))
    print('Awaiting Telegram Message')
    # My channels are for RTX card drops and PS5
    #channel_1 = discord_client.get_channel(int(send_channel_id))
    #print(config["input_channel_ids"])
    #id_of_channel = config["input_channel_ids"].index(send_channel_id)
    #channel_name = config["input_channel_ids"][id_of_channel]
    async with aiohttp.ClientSession() as session:
        try:
            webhook = discord.Webhook.from_url(config["discord_webhooks"][index_of_channel], session = session)
            mess = message.replace("@LeakNhomAD", "")
            if (path_image != ""):
                await webhook.send(content=isAddEveryone(mess, send_channel_id), file=discord.File(path_image))
                os.remove(path_image)
            else:
                await webhook.send(content=isAddEveryone(mess, send_channel_id))
        except:
            print('Error')
        finally:    
            discord_client.close()
            quit()

discord_client.run(config["discord_bot_token"])

