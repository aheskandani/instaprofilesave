import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from instaloader import Instaloader, Profile

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
PORT = int(os.environ.get('PORT', 5000))
bot_token = '5449413191:AAHq9zYO6Zj23lj2vNY8jRmhHXC2VNTHeMc'

def start(update, context):
	welcome_text = 'Hello friend to instagram profile save bot 🌹\n
		        Please enter the username or url and wait to download 🙏🏻\n\n
			Developed by @eskandani'
	update.message.reply_text(welcome_text)

def id(update, context):
	update.message.reply_text(f'Chat ID: {update.message.chat_id}')

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
	
def url_to_username(url):
	if len(url) > 30:
		website = 'instagram.com/'
		start_idx = url.find(website) + len(website)
		end_idx = url.find('?')
		return url[start_idx:end_idx]
	else:
		return url

def download_pic(update, context):
    try:
        insta = Instaloader()
        username = url_to_username(update.message.text)
        profile = Profile.from_username(insta.context, username)
        url = profile.get_profile_pic_url()
        cap = profile.full_name + '\n\n' + profile.biography + '\n\n' + '@instaprofilesave_bot'
        update.message.reply_photo(photo=url, caption=cap)
    except:
	    update.message.reply_text('User not found!')

updater = Updater(bot_token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('id', id))
updater.dispatcher.add_handler(MessageHandler(Filters.text, download_pic))
updater.dispatcher.add_handler(MessageHandler(Filters.command, download_pic))
updater.dispatcher.add_handler(MessageHandler(Filters.text, download_pic))

dp.add_error_handler(error)
updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
updater.bot.setWebhook('https://obscure-chamber-30229.herokuapp.com/' + bot_token)
updater.idle()
