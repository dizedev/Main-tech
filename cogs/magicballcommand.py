import random
import disnake
from disnake.ext import commands


class MagicBallCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="шар", description="Даёт верные ответы на все ваши вопросы.")
    async def ball(self, ctx: disnake.AppCommandInteraction, *, question):
        answers = [
            "Я не знаю.",
            "Да.",
            "Нет.",
            "Возможно.",
            "Спроси позже.",
            "Иди нахуй."
        ]
        await ctx.send(f"Ваш вопрос: {question}\nМой ответ: {random.choice(answers)}")


def setup(bot):
    bot.add_cog(MagicBallCommand(bot))
