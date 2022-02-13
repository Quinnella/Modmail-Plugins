import discord
from discord.ext import commands, tasks
import asyncio

class ChangeStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.first = None
        self.second = None
        self.third = None
        self.fourth = None
        self.fifth = None

    @tasks.loop(seconds=10)
    async def start_the_status(self):
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=f"{self.first}"))
        await asyncio.sleep(10)
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{self.second}"))
        await asyncio.sleep(10)
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{self.third}"))
        await asyncio.sleep(10)
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.competing, name=f"{self.fifth}"))
        await asyncio.sleep(10)

    @commands.group(name="statusy", invoke_without_command=True)
    async def status_group(self, ctx):
        embed = discord.Embed(
            title="Change the Bot's Status!",
            description=f"Change the Bot's Status to make it change every 10 Seconds!\n\n One = Playing, Two = Watching, Three = Listening to, Fourth = Competing in\n\nAvailable Commands:\n`{self.bot.prefix}statusy start`: Start the Status Changing Process\n`{self.bot.prefix}statusy stop`: Stop the bot's looping status & activity\n\n`{self.bot.prefix}statusy one`: Set the first status of the bot!\n`{self.bot.prefix}statusy two`: Set the second status of the bot!\n`{self.bot.prefix}statusy three`: Set third first status of the bot!\n`{self.bot.prefix}statusy four`: Set the fourth status of the bot!\n`{self.bot.prefix}statusy five`: Set the Fifth status of the bot!",
            color=self.bot.main_color
        )
        await ctx.send(embed=embed)

    @status_group.command(name="start")
    async def statusy_start(self, ctx):
        if self.first == None or self.second == None or self.third == None:
            await ctx.send("Please set the 3 Status's first!")
        else:
            self.start_the_status.start()
            await ctx.send("Successfully set rotating presence!")

    @status_group.command(name="one")
    async def first_set(self, ctx, *, first):
        if first == None:
            await ctx.send("Please choose something to set!")
        else:
            self.first = first
            await ctx.send(f"Set `{first}` as the first status!")

    @status_group.command(name="two")
    async def second_set(self, ctx, *, two):
        if two == None:
            await ctx.send("Please choose something to set!")
        else:
            self.second = two
            await ctx.send(f"Set `{two}` as the second status!")

    @status_group.command(name="three")
    async def third_set(self, ctx, *, three):
        if three == None:
            await ctx.send("Please choose something to set!")
        else:
            self.third = three
            await ctx.send(f"Set `{three}` as the third status!")
            
    @status_group.command(name="four")
    async def fourth_set(self, ctx, *, four):
        if four == None:
            await ctx.send("Please choose something to set!")
        else:
            self.fourth = four
            await ctx.send(f"Set `{four}` as the fourth status!")

    @status_group.command(name="stop")
    async def statusy_stop(self, ctx):
        if self.first == None or self.second == None or self.third == None or self.fourth == None
             await ctx.send("There are no rotating activity / status.")
        else:
             self.start_the_status.cancel()
             await self.bot.change_presence(status=None, activity=None)
             await ctx.send("**Successfully Stopped all Rotating presence!**")
             

def setup(bot):
    bot.add_cog(ChangeStatus(bot))
