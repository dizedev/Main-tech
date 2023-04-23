import asyncio
import random
import disnake
from disnake.ext import commands


class Coins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="монетка", description='Команда, которая возвращает орла или решку.')
    async def coins(self, ctx: disnake.ApplicationCommandInteraction):
        coin = ["Орел", "Решка"]
        result = random.choice(coin)

        await ctx.send(f"Орел или решка? Угадайте! Результат будет через 3 секунды...")
        await asyncio.sleep(3)
        await ctx.edit_original_response(f"Результат: {result}!")


def setup(bot):
    bot.add_cog(Coins(bot))
