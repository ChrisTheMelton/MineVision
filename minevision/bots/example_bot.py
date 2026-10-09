from javascript import require, On, Once, AsyncTask, once, off
import sys

# import javascript library
mineflayer = require("mineflayer")

# global bot parameters
server_host = "localhost"
server_port = 25565
server_version = "1.16.5"
reconnect = True

class MCBot:

    def __init__(self, bot_name):
        self.bot_args = {
            "username": bot_name,
            "host": server_host,
            "port": server_port,
            "version": server_version,
            "hideErrors": False
        }
        self.reconnect = reconnect
        self.bot_name = bot_name
        self.start_bot()

    # start mineflayer bot
    def start_bot(self):
         self.bot = mineflayer.createBot(self.bot_args)

         self.start_events()

    # attach mineflayer events to the bot
    def start_events(self):

        # login event (bot logged in)
        @On(self.bot, "login")
        def login(this):
            bot_socket = self.bot._client.socket
            print(f"Logged in to {bot_socket.server if bot_socket.server else bot_socket._host}")

        # chat event (bot got a msg in chat)
        @On(self.bot, "messagestr")
        def messagestr(this, message, messagePosition, jsonMsg, sender=None, verified=None):
            if messagePosition == "chat" and "kys" in message:
                self.reconnect = False
                this.quit()

        # kicked event (bot was kicked)
        @On(self.bot, "kicked")
        def kicked(this, reason, loggedIn):
            if loggedIn:
                print(f"Kicked from the server: {reason}")
            else:
                print(f"Kicked while trying to connect: {reason}")

        # end events (bot disconnected from the server)
        @On(self.bot, "end")
        def end(this, reason):
                    print(f"Disconnected: {reason}")

                    #turn off event listeners
                    off(self.bot, "login", login)
                    off(self.bot, "kicked", kicked)
                    off(self.bot, "end", end)
                    off(self.bot, "messagestr", messagestr)
                    if self.reconnect:
                        print("Restarting bot...")
                        self.start_bot()

# start any number of bots
num_bots = 10
bots = []
for i in range(1, num_bots + 1):
     bots.append(MCBot(f"bot-{i}"))


