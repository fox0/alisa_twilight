import traceback
from json import JSONDecoder, JSONEncoder
from django.http import HttpResponse
import pymorphy2

json_decoder = JSONDecoder()
json_encoder = JSONEncoder()
morph = pymorphy2.MorphAnalyzer()


def alisa_api(func):
    def wrap(request):
        if not request.method == 'POST':
            return HttpResponse('Error: only POST')

        json = json_decoder.decode(request.read().decode())
        # noinspection PyBroadException
        try:
            text = func(json['request']['nlu']['tokens'])
        except Exception:
            text = traceback.format_exc()
        r = {
            'response': {
                'text': text,
                'tts': text,  # todo
                # 'buttons': []
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

    return wrap


@alisa_api
def api(tokens):
    # for word in re.findall(r'\w+', s.replace('+', '')):
    #     for i in m.parse(word):
    #         print(i.tag.cyr_repr, i)
    #         if i.score > 0.33:
    #             break
    #     print()
    #
    # print(m.parse('стол')[0].inflect({m.cyr2lat('рд')}))
    return ' '.join(tokens)
