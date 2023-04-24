import disnake
import requests
from disnake.ext import commands


class DogCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="dog")
    async def dog(self, ctx: disnake.AppCommandInteraction):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        img_url = response.json()['message']
        embed = disnake.Embed(title='Случайная собака', color=0x00ff00)
        embed.set_image(url=img_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(DogCommands(bot))
