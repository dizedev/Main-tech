import disnake
from disnake.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="commands")
    async def commands(self, ctx: disnake.AppCommandInteraction):
        embed = disnake.Embed(title="Помощь по командам", description="Вот список всех моих команд и их описания:")
        embed.add_field(name="/help", value="Показывает список всех доступных команд.")
        embed.add_field(name="/ping", value="Проверка работоспособности бота.")
        embed.add_field(name="/coins", value="Игра Орел и Решка.")
        embed.add_field(name="/ball", value="Даёт верные ответы на все ваши вопросы.")
        embed.add_field(name="/math", value="Можно решить любые математические примеры.")
        embed.add_field(name="/ticket", value="Создает тикет")
        embed.add_field(name="/dog", value="Показывает фото случайной собаки.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
