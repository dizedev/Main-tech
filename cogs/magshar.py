import random

from disnake.ext import commands

class shar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def шар(self,ctx, *, question):
        answers = [
            "Я не знаю.",
            "Да.",
            "Нет.",
            "Возможно.",
            "Спроси позже."
        ]
        await ctx.send(f"Ваш вопрос: {question}\nМой ответ: {random.choice(answers)}")

def setup(bot):
    bot.add_cog(shar(bot))