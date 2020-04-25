import vk
import datetime
import cfg
from time import sleep
import send

login = cfg.readcfg('config.yml')['login']
password = cfg.readcfg('config.yml')['password']
wallid = cfg.readcfg('config.yml')['wallid']
domain = cfg.readcfg('config.yml')['domain']
vk_session = vk.AuthSession('6309796', login, password, scope='wall,groups,offline')

try:
    api = vk.API(vk_session)
    print('[{}] Auth Succesful!'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
except Exception as e:
    print('[{}] Auth Error!\nTraceback:\n'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
    print(e)

#searching for pinned post and skipping it via offset parameter if found
def is_pinned():
    try:
        data = api.wall.get(owner_id=wallid, domain=domain, offset='0', count='1', filter='all', extended='0', v='5.69')
    except Exception:
        is_pinned()
    try:
        if data['items'][0]['is_pinned']:
            return 1
    except KeyError:
        return 0

#using wallget api
def wallget():
    try:
        _wallget = api.wall.get(owner_id=wallid, domain=domain, offset=is_pinned(), count='1', filter='all', extended='0', v='5.69')
        if _wallget == None:
            _wallget = wallget()
        else:
            return _wallget
    except Exception:
        sleep(10)
        wallget()

#analyzing attachments
def attachments():
    try:
        #looking if there any attachment
        if walldata['items'][0]['attachments']:
            #if attachment is photo
            if walldata['items'][0]['attachments'][0]['type'] == 'photo':
                photosize = ['photo_1280', 'photo_807', 'photo_604', 'photo_130', 'photo_75']
                for size in photosize:
                    try:
                        #searching for maximum size
                        url = walldata['items'][0]['attachments'][0]['photo'][size]
                        attachmentType = 'photo'
                        return url, attachmentType
                    except KeyError as e:
                        continue
            #if attachment is video
            if walldata['items'][0]['attachments'][0]['type'] == 'video':
                #video's id is needed to generate link to the video
                videoid = walldata['items'][0]['attachments'][0]['video']['id']
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
    #if no attachments returning useless values
    except Exception as e:
        a = 'a'
        b = 'b'
        return a, b

getcurrid = lambda: walldata['items'][0]['id']
getwalltext = lambda: walldata['items'][0]['text']
#generating link to the post
getpostlink = lambda: 'vk.com/{}?w=wall{}_{}'.format(domain, wallid, getcurrid())

lastid = 0
walldata = wallget()

while 1==1:
    while walldata == None:
        walldata = wallget()
    currid = getcurrid()

    while currid == lastid:
        print('>{}< No new posts found'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        sleep(45)
        del(currid, walldata)
        walldata = wallget()
        while walldata == None:
            walldata = wallget()
        currid = getcurrid()

    print('[{}] New post found'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

    url = attachments()[0]
    lastid = currid
    #final message that will be sent to channel
    message = '{}\n\n{}'.format(getwalltext(), getpostlink())
    attachmentType = attachments()[1]

    if attachmentType == 'photo':
        send.sendtextandphoto(url, message)
    elif attachmentType == 'video':
        #hiding link to video into  'alt+255' synmbol.
        #Telegram wont show it in message, but still link will be avaliable on preview
        hiddenvideo = '<a href="{}"> </a>'.format(url)
        tempmsg = '{}{}'.format(hiddenvideo, message)
        send.sendtextandvideo(tempmsg)
        del(hiddenvideo, tempmsg)
    elif attachmentType == 'gif':
        send.sendtextandgif(url, message)
    else:
        send.sendtextonly(message)
    print('[{}] Post sent to telegram'.format(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
