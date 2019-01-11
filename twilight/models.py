from django.db import models


# todo log
# user_id + session_id + message_id + in + out


class TTSSpr(models.Model):
    """Справочник произношения слов"""
    word = models.CharField('Слово', max_length=64)
    speech = models.CharField('Произношение', max_length=64)

    def __str__(self):
        return '%s: %s' % (self.word, self.speech)
