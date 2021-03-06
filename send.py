from twx.botapi import TelegramBot
import cfg

token = cfg.readcfg('config.yml')['token']
channel = cfg.readcfg('config.yml')['channel']
bot = TelegramBot(token)
bot.update_bot_info()

def sendtextonly(message):
    try:
        bot.send_message(channel, message, disable_web_page_preview=True)
    except Exception:
        sendtextonly(message)

def sendtextandphoto(photourl, message):
    try:
        bot.send_photo(channel, photourl).wait()
        bot.send_message(channel, message, disable_web_page_preview=True)
    except Exception:
        sendtextandphoto(photourl, message)

def sendtextandvideo(message):
    try:
        bot.send_message(channel, message, parse_mode='HTML')
    except Exception:
        sendtextandvideo(message)

def sendtextandgif(gifurl, message):
    try:
        bot.send_video(channel, gifurl).wait()
        bot.send_message(channel, message)
    except Exception:
        sendtextandgif(gifurl, message)
