import json
import os

import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)


# Функция сохранения данных пользователя в JSON
def save_data(user, data):
    with open(f'./users/{user.id}.json', 'w') as file:
        json.dump(data, file)


# Функция загрузки данных пользователя из файла JSON
def load_data(user):
    try:
        with open(f'./users/{user.id}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.command(name="super_secret_command")
async def secret(ctx):
    await ctx.message.delete()
    await ctx.send(f'Привет, {ctx.author.mention}. Это тайное сообщение!')


@bot.command(name="news")
async def news(ctx):
    # Ваш код для получения новостей
    page_news = [
        {'title': 'В России началась вакцинация от COVID-19', 'description': 'Правительство России объявило о начале '
                                                                             'кампании по вакцинации людей от '
                                                                             'COVID-19.'},
        {'title': 'Космический корабль SpaceX вернулся на Землю', 'description': 'Космический корабль SpaceX Crew '
                                                                                 'Dragon вернулся на Землю после '
                                                                                 'успешного запуска в космос.'},
        {'title': 'Главный тренер "Манчестер Юнайтед" уволен', 'description': 'Главный тренер "Манчестер Юнайтед" был '
                                                                              'уволен после непродолжительной карьеры'
                                                                              ' в этой команде.'}
    ]

    # Создание встроенного сообщения с новостями
    embed = disnake.Embed(title='Новости', color=0xff8800)
    for i, new in enumerate(page_news):
        embed.add_field(name=f'{i + 1}. {new["title"]}', value=f'{new["description"]}\n\u200b', inline=False)

    # Отправка сообщения с встроенным сообщением
    await ctx.send(embed=embed)


@bot.command(name="setmoderator")
@commands.has_guild_permissions(administrator=True)
async def set_moderator(ctx: disnake.AppCommandInteraction, member: disnake.Member):
    member = member or ctx.message.author
    guild = bot.get_guild(1060537877982887957)
    role = guild.get_role(1060541642450411560)

    await member.add_roles(role)
    await ctx.send(f"Пользователю {member.mention} была выдана роль {role.mention}")


@bot.command(name="deletemoderator")
@commands.has_guild_permissions(administrator=True)
async def delete_moderator(ctx: disnake.AppCommandInteraction, member: disnake.Member):
    member = member or ctx.message.author
    guild = bot.get_guild(1060537877982887957)
    role = guild.get_role(1060541642450411560)

    await member.remove_roles(role)
    await ctx.send(f"Пользователю {member.mention} была снята роль {role.mention}")


# Создание команды регистрации
@bot.command(name="register")
async def register(ctx: disnake.AppCommandInteraction, name):
    # Проверка, был ли пользователь уже зарегистрирован
    data = load_data(ctx.author)
    if data is not None:
        await ctx.send('Вы уже зарегистрированы')
        return

    # Создание данных пользователя и сохранение их в файл JSON
    data = {'name': name, 'coins': 0}
    save_data(ctx.author, data)

    await ctx.send(f'{ctx.author.mention}, вы были зарегистрированы')


# Создание команды для просмотра баланса
@bot.command(name="balance")
async def balance(ctx):
    # Загрузка данных пользователя из файла JSON
    data = load_data(ctx.author)

    # Проверка, зарегистрирован ли пользователь
    if data is None:
        await ctx.send(f'{ctx.author.mention}, вы не зарегистрированы')
        return

    await ctx.send(f'{ctx.author.mention}, ваш текущий баланс: {data["coins"]}')


@bot.command(name="pay")
async def pay(ctx: disnake.AppCommandInteraction, recipient: disnake.User, amount: int):
    # Загрузка данных отправителя из файла JSON
    sender_data = load_data(ctx.author)

    # Проверка, зарегистрирован ли отправитель
    if sender_data is None:
        await ctx.send(f'{ctx.author.mention}, вы не зарегистрированы')
        return

    # Проверка, что у отправителя достаточно средств
    if sender_data['coins'] < amount:
        await ctx.send(f'{ctx.author.mention}, недостаточно средств')
        return

    # Загрузка данных получателя из файла JSON
    recipient_data = load_data(recipient)

    # Проверка, зарегистрирован ли получатель
    if recipient_data is None:
        await ctx.send(f'{recipient.mention} не зарегистрирован')
        return

    # Обновление баланса отправителя и получателя
    sender_data['coins'] -= amount
    recipient_data['coins'] += amount

    # Сохранение данных отправителя и получателя в файлах JSON
    save_data(ctx.author, sender_data)
    save_data(recipient, recipient_data)

    await ctx.send(f'{ctx.author.mention} перевел {recipient.mention} {amount} монет!')


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(settings.DISCORD_TOKEN)
