import random

from disnake.ext import commands


class MagicBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ask_a_ball(self, ctx, *, question):
        answers = [
            "Я не знаю.",
            "Да.",
            "Нет.",
            "Возможно.",
            "Спроси позже."
        ]
        await ctx.send(f"Ваш вопрос: {question}\nМой ответ: {random.choice(answers)}")


def setup(bot):
    bot.add_cog(MagicBall(bot))
