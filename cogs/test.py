import asyncio

import disnake
from disnake.ext import commands

class mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: disnake.Member, time: int, *, reason=None):
        guild = ctx.guild
        mutedRole = disnake.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            # Проверка роли на каждый чат
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"{member.mention} был замучен на {time} секунд. Причина: {reason}.")
        await asyncio.sleep(time)
        await member.remove_roles(mutedRole)
        await ctx.send(f"{member.mention} больше не замучен.")


def setup(bot):
    bot.add_cog(mute(bot))