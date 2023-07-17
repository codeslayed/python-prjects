# Set up the OpenAI API endpoin
import requests

import json
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

api_url = "https://api.openai.com/v1/chat/completions"
api_key = "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"

# Set up the Telegram bot
bot = telegram.Bot(token="5950923308:AAEig5zp2S5eb80hZnArFFj8koNij1eqyM4")

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the user's message
    message = update.message.text

    # Set up the OpenAI API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": message,
        "max_tokens": 50,
        "temperature": 0.5
    }

    # Send the request to the OpenAI API
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_data = json.loads(response.text)

    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_data["choices"][0]["text"])

# Set up the Telegram bot's handlers
updater = Updater(token="5950923308:AAEig5zp2S5eb80hZnArFFj8koNij1eqyM4", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
updater.idle()