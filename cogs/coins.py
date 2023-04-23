from disnake.ext import commands
import random
import asyncio


class coins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def coins(self, ctx):
        coin = ["Орел", "Решка"]
        result = random.choice(coin)
        await ctx.send(f"Орел или решка? Угадайте! Результат будет через 3 секунды...")
        await asyncio.sleep(3)
        await ctx.send(f"Результат: {result}!")


def setup(bot):
    bot.add_cog(coins(bot))