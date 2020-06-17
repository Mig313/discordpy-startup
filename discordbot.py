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

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
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
async def on_message_edit(before,after):
    befmsg = before.content
    aftmsg = after.content
    sender = after.author.display_name
    await after.channel.send('私知ってます！！{}さんは編集前、「{}」って言ってました！！'.format(sender,befmsg))

@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(692774588995731530)
    channel = guild.get_channel(718096349140353034)
    if not payload.message_id == 722631419251130408 and payload.emoji == "🔞":
        return
    role = guild.get_role(722630435707813888)
    user = guild.get_member(payload.user_id)
    if role in user.roles:
        await channel.send('おまわりさん！！{}は変態願望の塊です！！'.format(user.display_name))
    else:
        await user.add_roles(role)
        await channel.send('おまわりさん！！{}は変態です！！'.format(user.display_name))

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)