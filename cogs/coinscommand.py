import asyncio
import random
import disnake
from disnake.ext import commands


class CoinsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def coins(self, ctx: disnake.AppCommandInteraction):
        coin = ["Орел", "Решка"]
        result = random.choice(coin)
        await ctx.send("Орел или решка? Угадайте! Результат будет через 3 секунды...")
        await asyncio.sleep(3)
        await ctx.edit_original_response(content=f"Результат: {result}!")


def setup(bot):
    bot.add_cog(CoinsCommand(bot))
