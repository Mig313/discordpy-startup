# インストールした discord.py を読み込む
import discord
import os
import asyncio

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/yaju':
        await message.channel.send('ｲｷｽｷﾞｨ!!ｲｸｯｲｸｯ...ﾍｯﾍｯﾍｯ...ﾝｱｰｯ!!')
    if message.content == "/op":
        member = message.autho
        role = member.guild.get_role(722022742123348020)
        await member.add_roles(role)
        #role = guild.get_role(722022742123348020)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)