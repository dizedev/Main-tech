from disnake.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_any_role(1091637465858715648)
    @commands.slash_command()
    async def ping(self, interaction):
        await interaction.response.send_message("Понг!")


def setup(bot):
    bot.add_cog(Ping(bot))