import discord
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("testmsg")
    

    @commands.command()
    async def testembed(self, ctx):
        embed = discord.Embed(title="TestEmbed")
        embed.add_field(name="Test", value="Embed", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(test(bot))