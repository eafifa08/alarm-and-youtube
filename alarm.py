"""
Приложение-будильник. Открытие определенной страницы в интернете в определенное время.
"""
import configparser
import webbrowser
import datetime
import time


def get_settings():
    """
    Получение настроек из ini файла
    :return: Словарь настроек
    """
    config = configparser.ConfigParser()
    config.read('settings.ini')
    if not config.sections():
        set_default_settings()
        config.read('settings.ini')
    return {'url': config['alarm']['url'], 'time': config['alarm']['time']}


def set_default_settings():
    """Установка настроек по умалочанию"""
    config = configparser.ConfigParser()
    config['alarm'] = {'url': 'https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy',
                       'time': '11:42:00'}
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


def run_browser(url):
    """Запуск браузера"""
    webbrowser.open(url)


def run_waiting():
    """Основной цикл приложения"""
    settings = get_settings()
    time_alarm = settings.get('time')
    url = settings.get('url')
    while True:
        time.sleep(0.2)
        if check_time(time_alarm):
            run_browser(url)
            time.sleep(2)


def check_time(time_alarm):
    """Проверка времени"""
    today = datetime.datetime.now()
    time_now = today.time().strftime('%H:%M:%S')
    if time_now == time_alarm:
        return True
    else:
        return False


if __name__ == '__main__':
    run_waiting()
