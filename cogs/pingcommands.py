import disnake
from disnake.ext import commands


class PingCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_any_role(1091637465858715648)
    @commands.slash_command(name="ping", description="Показывает состояние бота")
    async def ping(self, ctx: disnake.AppCommandInteraction):
        if disnake.utils.get(ctx.author.roles, id=):
            if ctx.channel.id == :
                await ctx.send("Понг!")
            else:
                await ctx.send('Вы не можете использовать эту команду в текущем канале.')
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли .')


def setup(bot):
    bot.add_cog(PingCommands(bot))
