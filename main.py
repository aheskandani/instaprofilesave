from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from instaloader import Instaloader, Profile

bot_token = '5449413191:AAHq9zYO6Zj23lj2vNY8jRmhHXC2VNTHeMc'
admin_chat_id = '37087739'
updater = Updater(bot_token, use_context=True)

def url_to_username(url):
	if len(url) > 30:
		website = 'instagram.com/'
		idx_1 = url.find(website) + len(website)
		idx_2 = url.find('?')
		return url[idx_1:idx_2]
	else:
		return url

# Bot commands
def start(update: Update, context: CallbackContext):
	update.message.reply_text('Hello friend to instagram profile save bot 🌹\nPlease enter the username or url and wait to download 🙏🏻')

def id(update: Update, context: CallbackContext):
	update.message.reply_text(f'Chat ID: {update.message.chat_id}')

def download_pic(update: Update, context: CallbackContext):
    try:
        insta = Instaloader()
        username = url_to_username(update.message.text)
        profile = Profile.from_username(insta.context, username)
        url = profile.get_profile_pic_url()
        cap = profile.full_name + '\n\n' + profile.biography + '\n\n' + '@instaprofilesave_bot'
        update.message.reply_photo(photo=url, caption=cap)
    except:
	    update.message.reply_text('User not found!')

if __name__ == '__main__':
	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('id', id))
	updater.dispatcher.add_handler(MessageHandler(Filters.text, download_pic))
	updater.dispatcher.add_handler(MessageHandler(Filters.command, download_pic))
	updater.dispatcher.add_handler(MessageHandler(Filters.text, download_pic))
	updater.start_polling()
