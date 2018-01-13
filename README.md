# Автопост из ВК в телеграм канал.
## Установка
```
git clone https://github.com/Widowan/vkToTelegram
pip install -r requirements.txt
```

Дальше в файле **config.yml** настройте параметры согласно комментариям.
Не забудьте добавить бота в администраторы канала.

## Запуск
Запуск из файла **vi.py**, следовательно:
```
python vi.py
```
### Вот и все!


### Как получить chatid приватного канала:
1. Войдите в веб-версию телеграма [здесь](web.telegram.org)
2. Найдите ваш канал. Посмотрите на ссылку, она должна выглядеть примерно так: https://web.telegram.org/#/im?p=c1055587116_11052224402541910257
3. Вытащите "**1055587116**" из ссылки и добавьте "**-100**" в начало.

Другой вариант можно найти [здесь](https://stackoverflow.com/questions/33858927/how-to-obtain-the-chat-id-of-a-private-telegram-channel)

## Вывод
[**первая** картинка из поста]  

[новое сообщение]  

[текст поста]  


[ссылка на пост]  
ИЛИ:
[текст поста]  


[ссылка на пост]  

[прикрепленное как превью видео]  

## Внимание! Бот:
1) Взаимодействует только с _первым_ аттачментом поста, и только если это видео или картинка



2) Не умеет отправлять только видео/картинки без текста (т.е. в посте обязательно должен быть текст с картинкой)

_TODO: Починить вышеуказанные 2 пункта_
