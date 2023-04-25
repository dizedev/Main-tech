import disnake
from disnake.ext import commands


class MathCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="калькулятор", description="Помогает решить любой пример")
    async def math(self, ctx: disnake.AppCommandInteraction, *, equation):
        try:
            result = eval(equation)
            await ctx.send(f'Задача: {equation} = {result}')
        except:
            await ctx.send('Ошибка при выполнении вычислений.')


def setup(bot):
    bot.add_cog(MathCommands(bot))
