TOKEN = TELEGRAM_TOKEN
ADMINS = []
MAP_API = MAP_API_TOKEN
WEATHER_TOKEN = YANDEX_WEATHER_API_TOKEN
PROFILE_MESSAGE = '''Профиль пользователя %user_mention%
<b>Твой город:</b> %user_town%
<b>Кол-во раз получения погоды:</b> %user_weather_requests%
<b>Дата и время регистрации</b> %register_date%
'''

GET_WEATHER_MESSAGE = '''Прогноз для города %town% на %forecast%:
<b>Температура:</b> %temp_now%°C
<b>Ощущается как:</b> %feels_like%°C
<b>Давление:</b> %pressure% мм.рт.ст.
<b>Влажность:</b> %humidity%%
<b>Ветер:</b> %wind_speed% м/c
<b>Порывы ветра до:</b> %wind_gust% м/c'''

WEATHER_CONDITIONS_URLS = {'clear': 'sunny.png',
                            'partly-cloudy': 'partly_cloudy.png',
                            'cloudy': 'cloudy.png',
                            'overcast': 'cloudy.png',
                            'overcast-and-light-rain': 'rain_light.png',
                           'partly-cloudy-and-rain': 'rain.png',
                            'light-rain': 'rain_light.png',
                            'cloudy-and-light-rain': 'rain_light.png',
                            'cloudy-and-rain': 'rain.png',
                            'rain': 'rain.png',
                            'drizzle': 'rain_light.png',
                            'moderate-rain': 'rain.png',
                            'heavy-rain': 'rain.png',
                            'continuous-heavy-rain': 'rain.png',
                            'showers': 'rain.png',
                            'wet-snow': 'snow_s_rain.png',
                            'light-snow': 'snow_light.png',
                            'snow': 'snow.png',
                            'snow-showers': 'snow_light.png',
                            'hail': 'hail.png',
                            'thunderstorm': 'thunderstorm.png',
                            'thunderstorm-with-rain': 'thunderstorm-with-rain.png',
                            'thunderstorm-with-hail': 'thunderstorm-with-hail.png'}

WEATHER_SHORTCUTS = {'monday': 'пн',
                      'tuesday': 'вт',
                      'wednesday': 'ср',
                      'thursday': 'чт',
                      'friday': 'пт',
                      'saturday': 'сб',
                      'sunday': 'вс'}

SAD_ART = '''
⣿⣿⣿⣿⠿⢋⣩⣤⣴⣶⣶⣦⣙⣉⣉⣉⣉⣙⡛⢋⣥⣶⣶⣶⣶⣶⣬⡙⢿⣿
⣿⣿⠟⣡⣶⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙
⣿⢋⣼⣿⠟⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣧
⠃⣾⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡈⢿⣿⣿⣿⣿
⢰⣶⣼⣿⣷⣿⣽⠿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣷⡀⠛⢿⣿⣿
⢃⣺⣿⣿⣿⢿⠏⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⣿⣿⣷⢹⣿⣷⣄⠄⠈⠉
⡼⣻⣿⣷⣿⠏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⠸⣿⣿⣿⣿⣶⣤
⣇⣿⡿⣿⠏⣸⣎⣻⣟⣿⣿⣿⢿⣿⣿⣿⣿⠟⣩⣼⢆⠻⣿⡆⣿⣿⣿⣿⣿⣿
⢸⣿⡿⠋⠈⠉⠄⠉⠻⣽⣿⣿⣯⢿⣿⣿⡻⠋⠉⠄⠈⠑⠊⠃⣿⣿⣿⣿⣿⣿
⣿⣿⠄⠄⣰⠱⠿⠄⠄⢨⣿⣿⣿⣿⣿⣿⡆⢶⠷⠄⠄⢄⠄⠄⣿⣿⣿⣿⣿⣿
⣿⣿⠘⣤⣿⡀⣤⣤⣤⢸⣿⣿⣿⣿⣿⣿⡇⢠⣤⣤⡄⣸⣀⡆⣿⣿⣿⣿⣿⣿
⣿⣿⡀⣿⣿⣷⣌⣉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣌⣛⣋⣴⣿⣿⢣⣿⣿⣿⣿⡟⣿
⢹⣿⢸⣿⣻⣶⣿⢿⣿⣿⣿⢿⣿⣿⣻⣿⣿⣿⡿⣿⣭⡿⠻⢸⣿⣿⣿⣿⡇⢹
⠈⣿⡆⠻⣿⣏⣿⣿⣿⣿⣿⡜⣭⣍⢻⣿⣿⣿⣿⣿⣛⣿⠃⣿⣿⣿⣿⡿⠄⣼
⣦⠘⣿⣄⠊⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⡿⠁⠄⠟
'''

HELP_MESSAGE = '''
Привет, %username%! Это справка, и вы уже разобрались с первой кнопкой \U0001F609. У нашего бота есть функции: 
1) Получение погоды на текущий день
2) Узнать ссылку на github-репозиторий с исходным кодом
3) Запланировать получение погоды каждый определённый промежуток времени
4) Получить погоду на неделю картинкой
5) Получить график температуры
6) Изменить город для прогноза погоды
7) Посмотреть свой профиль

<b>Схема использования бота:</b>
‣ Сперва выберите свой город с помощью кнопки
<b> \U0001F3D9 Сменить город </b>. По умолчанию выбрана Москва.
‣ Далее можете нажать кнопку 
<b> \U0001F326 Узнать погоду </b>. Бот отправит вам погоду на сегодняшний день

<b>Дополнительные функции</b>
‣ У бота можно попросить прислать график температуры на сегодня, завтра или послезавтра. 
Для этого нажмите кнопку
<b>\U0001F4C8 График температуры</b>, а затем выберите, на сколько дней вперёд вам нужно получить график.

‣ Также у бота можно попросить запланировать получение погоды(т.е. попросить автоматически присылать погоду каждый некоторый промежуток времени)
Для этого нажмите кнопку <b>\U0001F514 Уведомления</b>. 
Затем нажмите кнопку 
<b>\U0001F514 Включить уведомления</b>. 
По умолчанию прогноз будет присылаться каждый час. Чтобы изменить период отправки, нажмите <b>\U0001F514 Уведомления</b>. 
Затем нажмите кнопку
<b>\U000023F0 Изменить период отправки</b>. 
Затем выберите период отправки. Также можно получать прогноз на неделю, а не на день. 
Для этого нажмите <b>\U0001F514 Уведомления</b>. 
Затем нажмите кнопку
<b>\U0001F4D2 Изменить тип уведомления</b>. 
Выберите пункт 
<b>\U0001F4D2 На неделю</>. 

‣ У бота есть функция получения погоды картинкой. Для этого нажмите кнопку
<b>\U0001F326 Погода на неделю</b>. Бот пришлёт вам картинку с прогнозом на 7 дней (включая сегодня).

‣ У бота можно попросить выслать ссылку на github-репозиторий с исходным кодом. Для этого нажмите на кнопку 
<b>\U0001F4C1 Репозиторий</b>

‣ У бота существует возможность выслать вам свой профиль. Для этого нажмите кнопку 
<b>\U0001F464 Профиль</b>. Бот вышлет вам информацию о вас: количество раз получения погоды, время/дата вашей регистрации и т.д.
'''

NOTIFICATIONS_WEATHER_MENU_MESSAGE = '''<b>Статус уведомлений:</b> %notifications_status%
<b>Период отправки уведомлений:</b> %notifications_period%
<b>Тип уведомлений:</b> %notifications_type%
'''