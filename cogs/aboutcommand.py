import disnake
from disnake.ext import commands


class AboutCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="бот", description="Показывает информацию о боте и их разработчиках")
    async def about(self, ctx: disnake.AppCommandInteraction):
        embed = disnake.Embed(title='О боте', description="" color=0x00ff00)
        embed.set_author(name='Main Tech')
        embed.add_field(name='Автор', value='n')
        embed.add_field(name='Версия', value='v1.02.')
        embed.add_field(name='Дата выпуска', value='23.04.2023')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AboutCommand(bot))
