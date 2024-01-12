import asyncio
import config
from amiyabot import AmiyaBot, Message, Chain
from amiyabot.adapters.mirai import mirai_api_http

adapter_service = mirai_api_http(host='localhost', ws_port=8060, http_port=8080)
bot = AmiyaBot(appid='******', token='******', adapter=adapter_service)


@bot.on_message(keywords='hello')
async def _(data: Message):
    return Chain(data).text(f'hello, {data.nickname}')


asyncio.run(bot.start())
