import discord


class DiscordManual:
    client = None
    intents = None
    bot_token = ""

    def __init__(self):
        if self.client is None:
            self.intents = discord.Intents(members=True, guilds=True)
            self.client = discord.Client(intents=self.intents)

    def connect(self, bot_token):
        self.client.run(bot_token, reconnect=True)
        self.bot_token = bot_token

    def get(self):
        return self.client
