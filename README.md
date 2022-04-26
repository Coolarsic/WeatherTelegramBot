Добрый день, $username! Это краткое руководство по погодному боту. Можно его не читать, так как в боте всё сделано максимально понятно, однако есть некоторые нюансы. Именно они здесь и освещаются. Приятного чтения!</br></br>
<div align="center"><b>Основные функции бота для пользователей</b></div><br>

1) <b>Выбор своего города</b><br>
Чтобы сменить свой город, нажмите на клавиатуре кнопку <br><-Сменить город->(по умолчанию бот отправляет погоду для Москвы). После данного действия бот предложит вам ввести название своего
города. Вводить название необязательно с большой буквы. Далее, вы можете отправить сообщение с названием города. Бот сообщит вам, что ваш город выбран. После того, как вы выбрали свой город, проверьте, правильно ли вы ввели название города. Если вы допустили ошибку, просто нажмите кнопку <-Сменить город-> ещё раз и введите название города корректно.
2) <b>Получение погоды</b><br>
Чтобы получить погоду просто нажмите кнопку <br><-Узнать погоду->. Бот пришлёт вам погоду на сегодня, в сообщении будут основные данные о погоде: температура, ощущаемая температура, влажность, скорость ветра и скорость порывов ветра.
3) <b>Получение погоды на неделю вперёд картинкой</b><br>
Чтобы получить погоду на неделю вперёд картинкой, нажмите кнопку <br><-Красивая погода->. Бот вышлет вам картинку с погодой на неделю вперёд, на которой также будут основные данные о погодк на неделю вперёд.
4) <b>Получение графика температуры</b><br>
Чтобы получить график температуры, нажмите кнопку <br><-График температуры->. Бот спросит у вас, на какое количество дней вперёд вам нужен график(на данный момент получить график тепературы можно получить максимум на два дня вперёд). Введите количество дней и отправьте сообщение. Бот вышлет вам картинку с графиком температуры.
5) <b>Получение информации о себе</b><br>
Бот хранит информацию о количестве ваших запросов и времени вашей регистрации. Чтобы узнать эту информацию, нажмите кнопку <-Профиль->. Бот вышлет вам вышеперечисленную информацию.
6) <b>Получение cсылки на github-репозиторий</b><br>
Чтобы получить ссылку на github-репозиторий с ботом, нажмите кнопку<br> <-Репозиторий->. Бот вышлет вам ссылку на github-репозиторий с ботом.
7) <b>Выбрать расписание получения погоды</b><br>
Если вы хотите, чтобы бот автоматически отправлял вам погоду через определённый промежуток времени, нажмите кнопку <-Расписание->. Бот запросит у вас промежуток времени, через который вам будет приходить погода(в днях). Введите его и отправьте сообщение боту. После этого бот будет присылать вам погоду каждый данный промежуток времени.
8) <b>Получить погоду в inline-режиме</b><br>
Если вы хотите отправить кому-либо погоду, полученную с помощью бота, то вы можете сделать это прямо в inline-режиме. Для этого перейдите в чат с тем человеком, которому вы хотите отправить погоду. Напишите сообщение вида: <i>@seweather_bot <-city-> </i>, где <i><-city-></i> - город, для которого нужно получить погоду. После отправки сообщения текст вашего сообщения заменится на сообщение с погодой для того города, который вы ввели.
<br><br>
<div align="center"><b>Для разработчиков</b></div>
Список всех используемых библиотек и их версий находится в файле requirements.txt. Бот был написан для интерпретатора python версии 3.9.2. Сперва склонируйте репозиторий командой <br>
git clone https://github.com/goldbocman/weather_telegram_bot
<br>Далее перейдите в папку с проектом. Чтобы запустить бота необходимо получить API-токены telegram и yandexweatherapi. В файле config.py находятся 4 переменные, которые необходимо заполнить для запуска бота: TOKEN - api-ключ telegram, WEATHER_TOKEN - api-ключ yandexweatherapi, ADMINS - список администраторов(их id в telegram), которым придёт уведомление о запуске бота, MAP_API - api-ключ яндекс карт. После этого можно установить необходимые библиотеки(сперва вам нужно установить интерпретатор python и пакетный менеджер pip). Чтобы установить библиотеки, отдайте команду<br> pip install -r requirements.txt<br> После окончания процесса установки библиотек можно запускать бота.
<br><br>

Спасибо, если дочитали до конца.<br>
<div align="right">Бота делали<br>goldbocman<br>Coolarsic<br></div><br>
<div align="center">2022</div>