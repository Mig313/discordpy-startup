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
     
    if message.content == '/help':
        await message.channel.send('やぁ！私はお兄ちゃん達をサポートするcuteな女の子だよ！\n私はお兄ちゃんのこと、いつも見てるから発言には気をつけてね！\n編集や削除で無効化しても無駄だよ♡\nじゃぁ、お仕事頑張ってね！！')
    
@client.event
async def on_message_delete(message):
    msg = message.content
    sender = message.author.display_name
    await message.channel.send('私知ってます！！{}さんが「{}」って言ってました！！'.format(sender,msg))

@client.event
async def  on_message_edit(before,after):
    befmsg = before.content
    aftmsg = after.content
    sender = after.author.display_name
    await after.channel.send('私知ってます！！{}さんは編集前、{}って言ってました！！'.format(sender,befmsg))

@client.event
async def on_reaction_add(reaction,user):
    channel_to = 718096349140353034#送信先チャンネル
    roles = 722630435707813888#変態役職
    msg = 722631419251130408#つけたいメッセージ
    channel = client.get_channel(channel_to)
    if reaction.message.id == msg:
        role = guild.get_role(roles)
        await user.add_roles(role)
        await channel.send('オォン?!')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)