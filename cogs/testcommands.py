import asyncio

import disnake
from disnake.ext import commands


class MuteCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Заглушает по всему серверу на указанное время.")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx: disnake.AppCommandInteraction, member: disnake.Member, time: int, *, reason=None):
        if disnake.utils.get(ctx.author.roles, id=1060541642450411560):
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
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли <@&1060541642450411560>.')

    @commands.slash_command(description="Снимает мут с указанного пользователя.")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx: disnake.AppCommandInteraction, member: disnake.Member):
        if disnake.utils.get(ctx.author.roles, id=1060541642450411560):
            mutedRole = disnake.utils.get(ctx.guild.roles, name="Muted")

            if mutedRole not in member.roles:
                await ctx.send(f"{member.mention} не замучен.")
                return

            await member.remove_roles(mutedRole)
            await ctx.send(f"{member.mention} больше не замучен.")
        else:
            await ctx.send(f'{ctx.author.mention}, у вас нет роли <@&1060541642450411560>.')


def setup(bot):
    bot.add_cog(MuteCommands(bot))
