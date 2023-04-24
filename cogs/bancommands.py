import disnake
from disnake.ext import commands


class BanCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Изгоняет указанного участника с сервера навсегда.")
    async def ban(self, ctx: disnake.AppCommandInteraction, member: disnake.Member, *, reason=None):
        if disnake.utils.get(ctx.author.roles, id=1060542125621649458):
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} был забанен. Причина: {reason}')
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли <@&1060542125621649458>.')

    @commands.has_any_role(1060542125621649458)
    @commands.slash_command()
    async def unban(ctx: disnake.AppCommandInteraction, *, user: disnake.User):
        if disnake.utils.get(ctx.author.roles, id=1060542125621649458):
            await ctx.guild.unban(user)
            if (user.name, user.discriminator) == (user.name, user.discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} был разбанен.')
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли <@&1060542125621649458>.')


def setup(bot):
    bot.add_cog(BanCommands(bot))
