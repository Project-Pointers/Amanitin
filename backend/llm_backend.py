import asyncio

from amiyabot import AmiyaBot, Message, Chain

bot = AmiyaBot(appid='******', token='******')


@bot.on_message(keywords='hello')
async def _(data: Message):
    return Chain(data).text(f'hello, {data.nickname}')


asyncio.run(bot.start())