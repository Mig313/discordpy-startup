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

# メッセージ受信時に動作する処理
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
 #       oppageta_role = discord.utils.get(message.guild.roles, id=722022742123348020) #おっぱげた
        await message.author.add_roles(722022742123348020)
        await message.channel.send('やっほー')
async def 
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)