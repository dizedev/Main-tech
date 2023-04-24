import disnake
from disnake.ext import commands


class AboutCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="about")
    async def about(self, ctx: disnake.AppCommandInteraction):
        embed = disnake.Embed(title='О боте', description='Многофункциональный бот.', color=0x00ff00)
        embed.set_author(name='Hyper Tech')
        embed.add_field(name='Автор', value='<@795901895666434070> а так же <@662994219794956298>\n')
        embed.add_field(name='Версия', value='v1.01.')
        embed.add_field(name='Дата выпуска', value='23.04.2023')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AboutCommand(bot))
