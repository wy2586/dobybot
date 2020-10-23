import discord
import os
import random


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("도비가 가동되었어!")
    game = discord.Game("10/21 ~ ")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("/도움말"):
        embed = discord.Embed(title="도움말", description="만드는 놈이 개발을 안해서 명령어가 안늘어남", color=0x000000)
        embed.set_author(name="도움말", icon_url="https://media.istockphoto.com/vectors/information-placeholder-with-exclamation-vector-icon-on-transparent-vector-id1013473976")
        embed.add_field(name=f"/골라 [이름들]", value=f"대충 결정장애 생겼을때 쓰는 명령어입니다. 그게 다임", inline=False)
        embed.add_field(name=f"/팀나누기 [유저들]:[팀]", value=f"내전 등을 할 때 팀을 만들기 위해 사용합니다\n 이때 팀 목록에 팀은 유저수만큼 써야합니다", inline=False)
        embed.add_field(name=f"/봇정보", value=f"이 응아덩어리가 왜 생겼는지 알 수 있음", inline=False)
        embed.set_footer(text="도비 설명 끝")
        await message.channel.send(embed=embed)
        print("도움말이 출력되었어!")

    if message.content.startswith("/말하기"):
        msg = message.content[5:]
        await client.get_channel(712667198795153509).send(msg)
        print("말하기 기능이 사용되었어!")

    if message.content.startswith("/공지"):
        msg = message.content[4:]
        embed = discord.Embed(title="공지", description=msg, color=0x000000)
        await client.get_channel(712667198795153509).send(embed=embed)
        print("공지 기능이 사용되었어!")

    if message.content.startswith("/골라"):
        choice = message.content.split(" ")
        choicenunber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenunber]
        await message.channel.send(choiceresult)
        print("골라 기능이 사용되었어!")

    if message.content.startswith("/팀나누기"):
        team = message.content[6:]
        peopleteam = team.split(":")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "====>" + teamname[i])
        print("팀나누기 기능이 사용되었어!")

    if message.content.startswith("/봇정보"):
        embed = discord.Embed(title="봇정보", color=0x000000)
        embed.set_author(name="도움말", icon_url="https://mblogthumb-phinf.pstatic.net/MjAxODA2MjJfMjY2/MDAxNTI5NjQ0NTg1ODg0.4Ta-cCQwQOUUcZvII1U54fNOSLrE4ffjl6Owo0ECpdYg.-J_7mw_BVCzSdCbgLo18aNWozpSsE6uJnQi8NBarb4Ug.PNG.sabuek/%EB%8F%84%EB%B9%843.PNG?type=w800")
        embed.add_field(name=f"이름", value=f"도비", inline=False)
        embed.add_field(name=f"만들어진 이유", value=f"파이썬 교육 받은적없는 놈이 심심해서 싸재낌", inline=False)
        embed.add_field(name=f"개발시기", value=f"2020.10.21 ~ 현재진행중", inline=False)
        embed.add_field(name=f"이거 만든놈", value=f"discord : 민규#3269 \n필요한 기능 말해도 추가 안해줌", inline=False)
        await message.channel.send(embed=embed)
        print("봇정보 기능이 사용되었어!")
        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
