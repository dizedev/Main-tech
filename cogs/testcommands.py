import asyncio

import disnake
from disnake.ext import commands


class MuteCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="мут", description="Заглушает пользователя по всему серверу на указанное время.")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx: disnake.AppCommandInteraction, member: disnake.Member, time: int, *, reason=None):
        if disnake.utils.get(ctx.author.roles, id=):
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
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли <>.')

    @commands.slash_command(name="унмут", description="Снимает мут с указанного пользователя.")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx: disnake.AppCommandInteraction, member: disnake.Member):
        if disnake.utils.get(ctx.author.roles, id=):
            muted_role = disnake.utils.get(ctx.guild.roles, name="Muted")

            if muted_role not in member.roles:
                await ctx.send(f"{member.mention} не замучен.")
                return

            await member.remove_roles(muted_role)
            await ctx.send(f"{member.mention} больше не замучен.")
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли <@>.')


def setup(bot):
    bot.add_cog(MuteCommands(bot))
