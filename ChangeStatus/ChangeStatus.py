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
        await self.bot.change_presence(activity=discord.Game(name=f"{self.first}"))
        await client.change_presence(status=discord.Status.dnd)
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{self.second}"))
        await client.change_presence(status=discord.Status.dnd)
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{self.third}"))
        await client.change_presence(status=discord.Status.dnd)
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Streaming(name=f"{self.fourth}", url="https://www.twitch.tv/somechannel"))
        await asyncio.sleep(10)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=f"{self.fifth}"))
        await asyncio.sleep(10)

    @commands.group(name="statusy", invoke_without_command=True)
    async def status_group(self, ctx):
        embed = discord.Embed(
            title="Change the Bot's Status!",
            description=f"Change the Bot's Status to make it change every 10 Seconds!\n\nAvailable Commands:\n`{self.bot.prefix}statusy start`: Start the Status Changing Process\n`{self.bot.prefix}statusy one`: Set the first status of the bot!\n`{self.bot.prefix}statusy two`: Set the second status of the bot!\n`{self.bot.prefix}statusy three`: Set third first status of the bot!\n`{self.bot.prefix}statusy four`: Set the fourth status of the bot!\n`{self.bot.prefix}statusy five`: Set the Fifth status of the bot!",
            color=self.bot.main_color
        )
        await ctx.send(embed=embed)

    @status_group.command(name="start")
    async def statusy_start(self, ctx):
        if self.first == None or self.second == None or self.third == None or self.fourth == None or self.fifth == None:
            await ctx.send("Please set the 5 Statuses first!")
        else:
            self.start_the_status.start()
            await ctx.send("Done! If you experience any problems just run this command again!")

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

    @status_group.command(name="five")
    async def fifth_set(self, ctx, *, five):
        if five == None:
            await ctx.send("Please choose something to set!")
        else:
            self.fifth = five
            await ctx.send(f"Set `{fifth}` as the fourth status!")


def setup(bot):
    bot.add_cog(ChangeStatus(bot))
