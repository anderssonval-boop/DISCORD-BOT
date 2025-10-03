import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

id_do_servidor = 1346919403689611314

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=id_do_servidor))
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='Testando')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estou funcionando!", ephemeral = True)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dm', description='Envia uma mensagem no DM do usuário selecionado')
@app_commands.describe(
    usuario='usuario que vai receber a msg',
    msg='mensagem a ser enviada para o usuário selecionado'
)
async def dm_command(interaction: discord.Interaction, usuario: discord.User, msg: str):
    try:
        if not interaction.user.guild_permissions.manage_messages:
            return await interaction.response.send_message(
                "⚠️Você precisa fazer parte da STAFF para poder usar esse comando⚠️.",
                ephemeral=True
            )
        
        embed = discord.Embed(description=msg)
        
        await usuario.send(embed=embed)
        await interaction.response.send_message(
            "✅Mensagem enviada com sucesso!✅",
            ephemeral=True
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌Não foi possível enviar a mensagem. O usuário pode ter DMs desativadas.❌",
            ephemeral=True
        )
    except Exception as error:
        print(f"Erro ao enviar DM: {error}")
        await interaction.response.send_message(
            "❌Ocorreu um erro ao enviar a mensagem.❌",
            ephemeral=True
        )

token = os.getenv('DISCORD_BOT_TOKEN')
if not token:
    print("⚠️ ERRO: Token do bot não encontrado! Configure a variável DISCORD_BOT_TOKEN")
else:
    aclient.run(token)
