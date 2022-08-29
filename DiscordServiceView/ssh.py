import asyncio
import nextcord
import os
from dotenv import load_dotenv
from nextcord.ext import commands

load_dotenv()

TOKEN = os.getenv('TOKEN')
z1 = os.getenv('z1')
z2 = os.getenv('z2')
z3 = os.getenv('z3')
channel1 = int(os.getenv('channel1'))
channel2 = int(os.getenv('channel2'))
channel3 = int(os.getenv('channel3'))
restartt = int(os.getenv('restartt'))
stopt = int(os.getenv('stopt'))
startt= int(os.getenv('startt'))
service1 = os.getenv('service1')
service2 = os.getenv('service2')
service3 = os.getenv('service3')
send = os.getenv('send')
import subprocess

class View1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="Start", style=nextcord.ButtonStyle.green, custom_id="persistent_view:green1"
    )
    async def green(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Starting",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service1} start", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(startt)
            getVersion =  subprocess.Popen(f"service {service1} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await asyncio.sleep(startt)
        await interaction.message.edit(content=z1, view=View1())

    @nextcord.ui.button(
        label="Stop", style=nextcord.ButtonStyle.red, custom_id="persistent_view:red1"
    )
    async def red(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Stopping",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service1} stop", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(stopt)
            getVersion =  subprocess.Popen(f"service {service1} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await asyncio.sleep(startt)
        await interaction.message.edit(content=z1, view=View1())

    @nextcord.ui.button(
        label="Restart", style=nextcord.ButtonStyle.blurple, custom_id="persistent_view:blurple1"
    )
    async def grey(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Restarting",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service1} restart", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(restartt)
            getVersion =  subprocess.Popen(f"service {service1} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await interaction.message.edit(content=z1, view=View1())
    
    @nextcord.ui.button(
        label="Status", style=nextcord.ButtonStyle.gray, custom_id="persistent_view:status1"
    )
    async def status(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        try:
            getVersion =  subprocess.Popen(f"service {service1} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)


class View2(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="Start", style=nextcord.ButtonStyle.green, custom_id="persistent_view:green2"
    )
    async def green(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Starting",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service2} start", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(startt)
            getVersion =  subprocess.Popen(f"service {service2} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await asyncio.sleep(startt)
        await interaction.message.edit(content=z2, view=View2())

    @nextcord.ui.button(
        label="Stop", style=nextcord.ButtonStyle.red, custom_id="persistent_view:red2"
    )
    async def red(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Stopping",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service2} stop", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(stopt)
            getVersion =  subprocess.Popen(f"service {service2} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await asyncio.sleep(startt)
        await interaction.message.edit(content=z2, view=View2())

    @nextcord.ui.button(
        label="Restart", style=nextcord.ButtonStyle.blurple, custom_id="persistent_view:blurple2"
    )
    async def grey(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Restarting",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service2} restart", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(restartt)
            getVersion =  subprocess.Popen(f"service {service2} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await interaction.message.edit(content=z2, view=View2())
    
    @nextcord.ui.button(
        label="Status", style=nextcord.ButtonStyle.gray, custom_id="persistent_view:status2"
    )
    async def status(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        try:
            getVersion =  subprocess.Popen(f"service {service2} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)


class View3(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label="Start", style=nextcord.ButtonStyle.green, custom_id="persistent_view:green3"
    )
    async def green(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Starting",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service3} start", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(startt)
            getVersion =  subprocess.Popen(f"service {service3} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await asyncio.sleep(startt)
        await interaction.message.edit(content=z3, view=View3())

    @nextcord.ui.button(
        label="Stop", style=nextcord.ButtonStyle.red, custom_id="persistent_view:red3"
    )
    async def red(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Stopping",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service3} stop", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(stopt)
            getVersion =  subprocess.Popen(f"service {service3} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await asyncio.sleep(startt)
        await interaction.message.edit(content=z3, view=View3())

    @nextcord.ui.button(
        label="Restart", style=nextcord.ButtonStyle.blurple, custom_id="persistent_view:blurple3"
    )
    async def grey(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        for x in self.children:
            x.disabled = True
        await interaction.message.edit(content="Restarting",view=self)
        try:
            getVersion =  subprocess.Popen(f"service {service3} restart", shell=True, stdout=subprocess.PIPE).stdout
            await asyncio.sleep(restartt)
            getVersion =  subprocess.Popen(f"service {service3} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)
        await interaction.message.edit(content=z3, view=View3())
    
    @nextcord.ui.button(
        label="Status", style=nextcord.ButtonStyle.gray, custom_id="persistent_view:status3"
    )
    async def status(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.defer()
        try:
            getVersion =  subprocess.Popen(f"service {service3} status", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(View1())
            self.add_view(View2())
            self.add_view(View3())
            self.persistent_views_added = True
            if send:
                await (bot.get_channel(channel1).send(z1, view=View1()))
                await (bot.get_channel(channel2).send(z2, view=View2()))
                await (bot.get_channel(channel3).send(z3, view=View3()))
        print(f"Logged in as {self.user} (ID: {self.user.id})")
bot = Bot(command_prefix="$")

import threading
import psutil

@bot.slash_command(name="threadds", description="Monitor time and when it last ran", default_member_permissions=8)
async def threadds(interaction: nextcord.Interaction):
    await interaction.response.defer()
    hdd = psutil.disk_usage('/')
    await interaction.followup.send(('RAM memory % used:', psutil.virtual_memory()[2],' The CPU usage is: ', psutil.cpu_percent(4),"Free: %d GiB" % (hdd.free // (2**30))))
    # Linux only can't test on windows
    #data = psutil.sensors_temperatures()
    #print(data)


@bot.slash_command(name="add", description="add", default_member_permissions=8)
async def remove(interaction: nextcord.Interaction, arg: int):
        await interaction.response.defer()
        try:
            getVersion =  subprocess.Popen(f"./add.sh {arg}", shell=True, stdout=subprocess.PIPE).stdout
            version =  getVersion.read()
            await interaction.send(version.decode(),ephemeral=True)
        except Exception as e:
            await interaction.send(f"Action failed expection: {e.args}, Please try again",ephemeral=True)

bot.run(TOKEN)
