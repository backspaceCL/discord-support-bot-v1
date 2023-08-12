import discord #모듈 불러오기
token = "MTEzOTU0MjkwMzQ1OTQxNDE1Ng.GNC_W_.0VPt6uhEaHjazj_DCvCGlRH-_bhHiwjR-Pk-TA" #봇 토큰 설정하기
client = discord.Client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready(): #봇이 준비되었을 때
    print("봇 준비 완료!")
    print(client.user)
    print("===========================")

@client.event
async def on_message(message): #사용자가 메시지를 입력했을 때
    if message.content == "! 컴퓨터 견적": #만일 사용자가 "! 컴퓨터 견적" 라고 입력했을 때
        await message.channel.send("! NEX에게 개인 DM 해주세요.") #봇이 "! NEX에게 개인 DM 해주세요." 라고 답한다.
    if message.content == "! 컴퓨터 문제점": #만일 사용자가 "! 컴퓨터 문제점" 라고 입력했을 때
        await message.channel.send("! NEX에게 어떤 종류의 문제이고, 먼저 충분히 검색 해보시고 개인 DM 해주세요.") #봇이 "! NEX에게 어떤 종류의 문제이고, 먼저 충분히 검색 해보시고 개인 DM 해주세요." 라고 답한다.
    if message.content == "! 커스텀 키보드 견적": #만일 사용자가 "! 커스텀 키보드 견적" 라고 입력했을 때
        await message.channel.send("! NEX에게 선호하시는 축, 사용 용도 등 작성해서 개인 DM 해주세요.") #봇이 "! NEX에게 선호하시는 축, 사용 용도 등 작성해서 개인 DM 해주세요." 라고 답한다.

client.run(token)