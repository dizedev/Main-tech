import disnake
from disnake.ext import commands


class Help1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def commands(self, ctx):
        embed = disnake.Embed(title="Помощь по командам", description="Вот список всех моих команд и их описания:")
        embed.add_field(name="$help", value="Показывает список всех доступных команд.")
        embed.add_field(name="$ping", value="Проверка работоспособности бота.")
        embed.add_field(name="$coins", value="Игра Орел и Решка.")
        embed.add_field(name="$mute", value="Выдает мут участнику на определенное время.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help1(bot))
