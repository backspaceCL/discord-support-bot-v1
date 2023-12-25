import discord #모듈 불러오기
token = "token" #봇 토큰 설정하기
client = discord.Client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready(): #봇이 준비되었을 때 뜨는 메시지입니다.
    print("봇 준비 완료!")
    print(client.user)
    print("===========================")

client.run(token)
