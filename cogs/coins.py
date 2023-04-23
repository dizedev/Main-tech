import asyncio
import random

from disnake.ext import commands


class Coins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="супер", description='Команда, которая возвращает орла или решку.')
    async def coins(self, ctx):
        coin = ["Орел", "Решка"]
        result = random.choice(coin)

        info = await ctx.send(f"Орел или решка? Угадайте! Результат будет через 3 секунды...")
        await asyncio.sleep(3)
        await ctx.send(f"Результат: {result}!")


def setup(bot):
    bot.add_cog(Coins(bot))
