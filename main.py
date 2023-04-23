import os
import settings
import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.command()
@commands.has_guild_permissions(
    administrator=True)  # administrator=True - значит что использовать команду может человек только с правом администратора
async def setmoderator(ctx, member: disnake.Member):
    member = member or ctx.message.author
    guild = bot.get_guild(1060537877982887957)
    role = guild.get_role(1060541642450411560)

    await member.add_roles(role)
    await ctx.send(f"Пользователю {member.mention} была выдана роль {role.mention}")


@bot.command()
@commands.has_guild_permissions(
    administrator=True)  # administrator=True - значит что использовать команду может человек только с правом администратора
async def dellmoderator(ctx, member: disnake.Member, moder_level: int):
    member = member or ctx.message.author
    guild = bot.get_guild(1060537877982887957)
    role = guild.get_role(1060541642450411560)

    await member.remove_roles(role)
    await ctx.send(f"Пользователю {member.mention} была снята роль {role.mention}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(settings.discord_token)
