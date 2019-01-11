import logging
from json import JSONDecoder, JSONEncoder
from django.http import HttpResponse
from twilight.core import prosess

log = logging.getLogger(__name__)

json_decoder = JSONDecoder()
json_encoder = JSONEncoder()


def webhook(request):
    if not request.method == 'POST':
        return HttpResponse('Error: only POST')

    json = json_decoder.decode(request.read().decode())
    # todo parse type
    tokens = json['request']['nlu']['tokens']
    if tokens:
        # noinspection PyBroadException
        try:
            text = prosess(tokens)
        except Exception as e:
            log.exception('error')
            text = 'Внутренняя ошибка. Прости.'
    else:
        text = 'Привет'
        # todo
        # "Давно не виделись" - проверять дату последней активности
        # "Привет, меня зовут Твайлайт Спаркл. А тебя?" - новый пользователь
    return render(json, text)


def render(json, text):
    r = {
        'response': {
            'text': text,
            'tts': tts(text),
            # 'buttons': []  # todo 'ты неправильно произнесла слово'
            'end_session': False,
        },
        'session': {
            'session_id': json['session']['session_id'],
            'message_id': json['session']['message_id'],
            'user_id': json['session']['user_id'],
        },
        'version': json['version'],
    }
    return HttpResponse(json_encoder.encode(r), content_type='application/json')


def tts(text):
    # todo расстановка ударений
    return text
