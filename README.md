# Автопост из ВК в телеграм канал.
Пошаговая установка "для чайников" в конце.
## Быстрый старт
```
git clone https://github.com/Widowan/vkToTelegram
pip install -r requirements.txt
```

Дальше в файле **config.yml** настройте параметры согласно комментариям.
Не забудьте добавить бота в администраторы канала.

### Запуск
Запуск из файла **vi.py**, следовательно:
```
python vi.py
```  


## Как получить chatid приватного канала:
1. Войдите в веб-версию телеграма [здесь](https://web.telegram.org)
2. Найдите ваш канал. Посмотрите на ссылку, она должна выглядеть примерно так: https://web.telegram.org/#/im?p=c1055587116_11052224402541910257
3. Вытащите "**1055587116**" из ссылки и добавьте "**-100**" в начало.

Другой вариант можно найти [здесь](https://stackoverflow.com/questions/33858927/how-to-obtain-the-chat-id-of-a-private-telegram-channel)

## Вывод
![Пример #1](https://i.imgur.com/KMjERfQ.png)
![Пример #2](https://i.imgur.com/rqoMHAx.png)

## Внимание! Бот:
Взаимодействует только с _первым_ аттачментом поста, и только если это видео, картинка или гифка


_TODO: Починить вышеуказанный пункт_


## Инструкция по установке для хлебушков:  
Все команды, конечно, прописываются в командной строке/терминале.  
**Причем командную строку нужно запускать от имени администратора!**  

1. Устанавливаем Python:  
   Для Linux:  
   ```
   sudo apt install python3
   sudo pip install setuptools
   ```
   Для Windows нужно вручную скачать клиент с [официального сайта Python](https://www.python.org/)  

2. Устанавливаем git:  
   Для Windows:  
   скачать клиент [здесь](https://git-scm.com/download/win)  
   Для Linux:
   ```
   sudo apt install git
   ```

3. Из команд pip3 и python3 убирается цифра '3' если вы на Windows (И, конечно же, sudo)  
   (Не забудьте перейти в директорию в которую хотели бы сохранить скрипт!)  
   ```
   git clone https://github.com/Widowan/vkToTelegram && cd vkToTelegram
   sudo pip3 install -r requirements.txt
   ```
4. Создаем бота в телеграме:  
   Идем к [@botFather](https://t.me/botfather) и создаем у него бота, следуя инструкциям.  
   Добавьте этого бота в администраторы чата/канала, в который будут поститься сообщения.  
 
5. Дальше настройте конфиг в файле config.yml:
   1. Первые 2 строки это ваши логин и пароль, соответсвенно. Они нужны для работы с API вк.
   2. Третья строка - ссылка на группу/стену человека. ТОЛЬКО циферный формат.
      Узнать id группы/юзера с пользовательской ссылкой вам поможет [гугл](lmgtfy.com/?q=Как+узнать+id+группы+вконтакте).  
      Вкратце: можете зайти в фото/видео/аудио записи группы/человека - в ссылке и будет id (_id групп всегда идет со знаком '-'_).
   3. Четвертая строка это пользовательская ссылка на страницу: т.е. из группы vk.com/vkmusic строка domain будет 'vkmusic'.
   4. Пятая - токен вашего бота.
   5. Последняя - ссылка на канал/чат в который бот будет постить сообщения.
6. Запуск:
   ```
   python3 vi.py
   ```
