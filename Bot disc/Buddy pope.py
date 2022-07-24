
import discord
from discord.ext import commands, tasks

bp = commands.Bot("*")

@bp.event
async def on_ready():
    print(f"Estou pronto {bp.user}")
    # nargas.start()


@bp.event
async def on_message(message):
    if message.author == bp.user:
        return

    if "vadia" in message.content:
        await message.channel.send(
            f"{message.author.name} Para com essa porra ae, fudido"
        )

        await message.delete()
    await bp.process_commands(message)

@bp.command(name = 'eae')
async def send_hi(ctx):
    name = ctx.author.name
    res = "Fala tu " + name
    await ctx.send(res)


@bp.command(name = 'cutuca')
async def mul(ctx):
    name = ctx.author.name
    re = f"*{bp.user.name} esta Transando*, não ta disponivel vadia!!"
    await ctx.send(re)

@bp.command(name = 'nft')
async def nft(ctx):
    re = f'NFT = Não Fode Truta'
    await ctx.send(re)

@bp.command(name = 'vtnc')
async def vtn(ctx):
    name = ctx.author.name
    ree = f'{name} Sua mãe é minha'
    await ctx.send(ree)

@bp.command(name = 'lolo')
async def lolo(ctx):
    name = ctx.author.name
    ree = f'{name}😜😜 \nCADE O LOLÓ🤔🤔??\n HEIN🤨 ??\n CADE O LOLÓ??🤪🤪'
    await ctx.send(ree)


@bp.command(name = 'teste')
async def tst(ctx):
    name = ctx.author.name
    tt = 'Teste para ver se lembro dos comandos'
    await ctx.send(tt)


# @tasks.loop(seconds=3)
# async def nargas():
#     id_channel = bp.get_channel(990367554713301073)
#
#     await id_channel.send(f"Cade o nargas o {bp.user.name} quer bufar um nargas")


bp.run("")















