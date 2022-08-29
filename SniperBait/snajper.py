import nextcord
import os
from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()

TOKEN = os.getenv('TOKEN')
allowedmembers=[]
send = os.getenv('send')

class View1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="Reserve Qualification", style=nextcord.ButtonStyle.green, custom_id="persistent_view:green"
    )
    async def green(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        print(interaction.user.name, "pressed the green button")
        if interaction.user.id in allowedmembers:
            button.disabled=True
            await interaction.response.edit_message(content=f'Sniper Qualification 0/1 slots left. Reserved by <@{interaction.user.id}>', view=self)
        else:
            await bot.get_channel(994994089441361981).send(f"Jabaited {interaction.user.mention} for Sniper Qualification")
            await interaction.send("An error has accured try again later!",ephemeral=True)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(View1())
            self.persistent_views_added = True
            if send:
                await (bot.get_channel(994994089441361981).send('Sniper Qualification 1/1 slots left', view=View1()))
        print(f"Logged in as {self.user} (ID: {self.user.id})")



bot = Bot(command_prefix="$")

bot.run(TOKEN)
