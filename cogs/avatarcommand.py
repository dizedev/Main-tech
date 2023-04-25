import disnake
from disnake.ext import commands


class AvatarCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="аватар", description="Показывает аватар указанного пользователя")
    async def avatar(self, ctx: disnake.AppCommandInteraction, member: disnake.Member = None):
        if not member:
            member = ctx.author
        embed = disnake.Embed(title=f'Аватар пользователя: {member}', color=0x00ff00)
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AvatarCommand(bot))
