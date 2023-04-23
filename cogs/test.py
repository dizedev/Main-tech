import asyncio

import disnake
from disnake.ext import commands


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: disnake.Member, time: int, *, reason=None):
        guild = ctx.guild
        muted_role = disnake.utils.get(guild.roles, name="Muted")

        if not muted_role:
            muted_role = await guild.create_role(name="Muted")

            # Проверка роли на каждый чат
            for channel in guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False)

        await member.add_roles(muted_role, reason=reason)
        await ctx.send(f"{member.mention} был замучен на {time} секунд. Причина: {reason}.")
        await asyncio.sleep(time)
        await member.remove_roles(muted_role)
        await ctx.send(f"{member.mention} больше не замучен.")


def setup(bot):
    bot.add_cog(Mute(bot))
