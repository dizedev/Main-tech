import disnake
from disnake.ext import commands


class BanCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="бан", description="Изгоняет указанного участника с сервера навсегда.")
    async def ban(self, ctx: disnake.AppCommandInteraction, member: disnake.Member, *, reason=None):
        if disnake.utils.get(ctx.author.roles, id=):
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} был забанен. Причина: {reason}')
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли .')

    @commands.has_any_role()
    @commands.slash_command(name="унбан", description="Снимает блокировку")
    async def unban(self, ctx: disnake.AppCommandInteraction, *, user: disnake.User):
        if disnake.utils.get(ctx.author.roles, id=):
            await ctx.guild.unban(user)
            if (user.name, user.discriminator) == (user.name, user.discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} был разбанен.')
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли.')


def setup(bot):
    bot.add_cog(BanCommands(bot))
