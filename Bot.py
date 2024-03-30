import os
import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Token do bot gerado pelo BotFather
TOKEN = "6792089785:AAEuIj9Z7k_pxRn8ldS4uC8ECpzTKRkVMI4"

# ID do grupo para onde o bot enviará as mensagens
GROUP_ID = "-1002144325445"

# @ do grupo do jogo
GAME_GROUP_USERNAME = "@cybertaticsweb3game"

# Função para enviar mensagem para o grupo a cada 30 minutos
def send_periodic_message(context: CallbackContext):
    gas_prices = get_gas_prices() # Função para obter os preços do gás da rede Polygon
    matic_price = get_matic_price() # Função para obter o preço atual da Matic
    message = f'Gas prices on the Polygon network:\n\n'
    for speed, price in gas_prices.items():
        message += f'{speed.capitalize()}: {price} Gwei\n'
    message += f'\nCurrent Matic price: ${matic_price}\n\n'
    message += f'🚀 **Join our Web3 Game - Compete to Earn!** 🎮\n'
    message += f'Play as many matches as you want and earn unlimited rewards in Matic directly!\n'
    message += f'Join our 3D FPS Web3 game at {GAME_GROUP_USERNAME} and visit our website at [Cybertatics](https://cybertatics.com)!'
    context.bot.send_message(chat_id=GROUP_ID, text=message, parse_mode='MarkdownV2')

# Função para enviar mensagem para o grupo em resposta ao comando /send
def send_message(update, context):
    gas_prices = get_gas_prices() # Função para obter os preços do gás da rede Polygon
    matic_price = get_matic_price() # Função para obter o preço atual da Matic
    message = f'Gas prices on the Polygon network:\n\n'
    for speed, price in gas_prices.items():
        message += f'{speed.capitalize()}: {price} Gwei\n'
    message += f'\nCurrent Matic price: ${matic_price}\n\n'
    message += f'🚀 **Join our Web3 Game - Compete to Earn!** 🎮\n'
    message += f'Play as many matches as you want and earn unlimited rewards in Matic directly!\n'
    message += f'Join our 3D FPS Web3 game at {GAME_GROUP_USERNAME} and visit our website at [Cybertatics](https://cybertatics.com)!'
    context.bot.send_message(chat_id=update.message.chat_id, text=message, parse_mode='MarkdownV2')

# Função para obter os preços do gás da rede Polygon
def get_gas_prices():
    url = 'https://gasstation-mainnet.matic.network'
    response = requests.get(url)
    data = response.json()
    gas_prices = {
        'aggressive': data['fast'],
        'medium': data['standard'],
        'slow': data['safeLow']
    }
    return gas_prices

# Função para obter o preço atual da Matic em dólares
def get_matic_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data['matic-network']['usd']

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("send", send_message))
    dp.add_handler(CommandHandler("start", send_message))  # To allow /start
    updater.start_polling()

    # Send message every 30 minutes
    updater.job_queue.run_repeating(send_periodic_message, interval=1800)

    updater.idle()

if __name__ == '__main__':
    main()
