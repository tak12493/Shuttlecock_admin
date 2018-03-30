import telepot

token = "590053987:AAFxLwN2NqoNHopqdA6im9Kbvmwq3IClXGs"
TelegramBot = telepot.Bot(token)
print(TelegramBot.getUpdates())
