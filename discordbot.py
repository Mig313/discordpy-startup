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

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行 

    if message.content == '/debug':
        await message.channel.send('---デバッグデータ---')

    if message.content == '/hi':
        await message.channel.send('Hi!')

    if message.content == 'おっｐ':
        await message.channel.send('おっぱげた...')
        role1 = discord.utils.get(message.guild.roles, id=722022742123348020)
        await message.author.add_roles(role1)
    
@client.event
async def on_typing(channel,user,when):
    usersan = user.name
    await channel.send('{}さんが喋ろうとしている...!'.format(usersan))

@client.event
async def on_message_delate(messages):
    await messages.channel.send('消え失せろ！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)