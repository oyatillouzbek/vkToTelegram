from twx.botapi import TelegramBot
import cfg
from retry import retry

token = cfg.readcfg('config.yml')['token']
channel = cfg.readcfg('config.yml')['channel']
bot = TelegramBot(token)
bot.update_bot_info()

@retry(tries=10, delay=18)
def sendtextonly(message):
    bot.send_message(channel, message, disable_web_page_preview=True)


@retry(tries=10, delay=18)
def sendtextandphoto(photourl, message):
    bot.send_photo(channel, photourl).wait()
    bot.send_message(channel, message, disable_web_page_preview=True)


@retry(tries=10, delay=18)
def sendtextandvideo(message):
    bot.send_message(channel, message, parse_mode='HTML')

@retry(tries=10, delay=18)
def sendtextandgif(gifurl, message):
    bot.send_video(channel, gifurl).wait()
    bot.send_message(channel, message)
