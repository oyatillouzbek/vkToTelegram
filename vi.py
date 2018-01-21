import vk_api
import datetime
import cfg
from eventlet import sleep
import send
import socket
import traceback

login = cfg.readcfg('config.yml')['login']
password = cfg.readcfg('config.yml')['password']
wallid = cfg.readcfg('config.yml')['wallid']
domain = cfg.readcfg('config.yml')['domain']
vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth()
    print('[{}] Auth Succesful!'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
except vk_api.AuthError as e:
    print('[{}] Auth Error!\nTraceback:\n'.format(datetime.strftime("%Y-%m-%d %H:%M:%S", datetime.gmtime())))
    print(e)
api = vk_session.get_api()

def is_pinned(): #searching for pinned post and skipping it via offset parameter if found
    data = api.wall.get(owner_id=wallid, domain=domain, offset='0', count='1', filter='all', extended='0', v='5.69')
    try:
        if data['items'][0]['is_pinned']:
            return 1
    except KeyError:
        return 0

def wallget(): #using wallget api
    wallget = api.wall.get(owner_id=wallid, domain=domain, offset=is_pinned(), count='1', filter='all', extended='0', v='5.69')
    return wallget

def attachments(): #analyzing attachments
    try:
        if walldata['items'][0]['attachments']: #looking if there any attachment
            if walldata['items'][0]['attachments'][0]['type'] == 'photo': #if attachment is photo
                photosize = ['photo_1280', 'photo_807', 'photo_604', 'photo_130', 'photo_75']
                for size in photosize:
                    try:
                        url = walldata['items'][0]['attachments'][0]['photo'][size] #searching for maximum size
                        attachmentType = 'photo'
                        return url, attachmentType
                    except KeyError as e:
                        continue
            if walldata['items'][0]['attachments'][0]['type'] == 'video': #if attachment is video
                videoid = walldata['items'][0]['attachments'][0]['video']['id'] #video's id is needed to generate link to the video
                videoOwner = walldata['items'][0]['attachments'][0]['video']['owner_id']
                url = 'vk.com/video{}_{}'.format(videoOwner, videoid)
                attachmentType = 'video'
                return url, attachmentType
            if walldata['items'][0]['attachments'][0]['type'] == 'doc':
                if walldata['items'][0]['attachments'][0]['doc']['ext'] == 'gif':
                    url = walldata['items'][0]['attachments'][0]['doc']['url']
                    attachmentType = 'gif'
                    return url, attachmentType
                else:
                    a = 'a'
                    b = 'b'
                    return a, b
            else:
                a = 'a'
                b = 'b'
                return a, b
    except Exception as e: #if no attachments returning useless values
        a = 'a'
        b = 'b'
        return a, b

getcurrid = lambda: walldata['items'][0]['id']
getwalltext = lambda: walldata['items'][0]['text']
getpostlink = lambda: 'vk.com/{}?w=wall{}_{}'.format(domain, wallid, getcurrid()) #generating link to the post

lastid = 0
walldata = wallget()

while 1==1:
    currid = getcurrid()

    while currid == lastid:
        print('>{}< No new posts found'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        sleep(45)
        del(currid, walldata)
        walldata = wallget()
        currid = getcurrid()

    print('[{}] New post found'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

    url = attachments()[0]
    lastid = currid
    message = '{}\n\n{}'.format(getwalltext(), getpostlink()) #final message that will be sent to channel
    attachmentType = attachments()[1]

    if attachmentType == 'photo':
        send.sendtextandphoto(url, message)
    elif attachmentType == 'video':
        hiddenvideo = '<a href="{}"> </a>'.format(url) #hiding link to video into  'alt+255' synmbol. Telegram wont show it in message, but still link will be avaliable on preview
        tempmsg = '{}{}'.format(hiddenvideo, message)
        send.sendtextandvideo(tempmsg)
        del(hiddenvideo, tempmsg)
    elif attachmentType == 'gif':
        send.sendtextandgif(url, message)
    else:
        send.sendtextonly(message)
    print('[{}] Post sent to telegram'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
