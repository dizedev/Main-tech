import disnake
from disnake.ext import commands


class TicketsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ticket_channel = None

    @commands.slash_command(name="ticket")
    @commands.has_permissions(manage_channels=True)
    async def ticket(self, ctx: disnake.AppCommandInteraction):
        global ticket_channel
        overwrites = {
            ctx.guild.default_role: disnake.PermissionOverwrite(read_messages=False),
            ctx.author: disnake.PermissionOverwrite(read_messages=True),
            ctx.guild.me: disnake.PermissionOverwrite(read_messages=True)
        }
        try:
            ticket_channel = await ctx.guild.create_text_channel(name=f'ticket-{ctx.author.display_name}',
                                                                 overwrites=overwrites)
            await ctx.send(f'{ctx.author.mention}, тикет создан: {ticket_channel.mention}')
        except:
            await ctx.send('Ошибка при создании канала. Пожалуйста, попробуйте позже.')

    @commands.slash_command(name="close_ticket")
    @commands.has_permissions(manage_channels=True)
    async def close_ticket(self, ctx: disnake.AppCommandInteraction):
        global ticket_channel
        if ticket_channel:
            await ticket_channel.delete()
            await ctx.send('Тикет закрыт.')
        else:
            await ctx.send('Тикет не был создан.')


def setup(bot):
    bot.add_cog(TicketsCommand(bot))
