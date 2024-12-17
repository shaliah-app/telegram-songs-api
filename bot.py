from telethon import TelegramClient, events

API_ID = '24989859'
API_HASH = '70851b288050ecc9a5202bafda72ff77'
TOKEN = '7462718254:AAFuRdDo3j3e9Vxhr9ZlNbDkivGygTEcbV0'
CHANNEL_TESTE_ID = -1002488198462
CHANNEL_ShaliahSongs_ID = -1002357778672

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=TOKEN)

@bot.on(events.NewMessage(chats=CHANNEL_TESTE_ID))
async def message_handler(event):
    await bot.send_message(CHANNEL_ShaliahSongs_ID,event.message.message)

bot.run_until_disconnected()