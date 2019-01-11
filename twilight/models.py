from django.db import models


class Log(models.Model):
    """Лог запросов к боту"""
    user_id = models.CharField(max_length=64)
    session_id = models.CharField(max_length=64)
    message_id = models.IntegerField()
    ask = models.CharField(max_length=1024)
    ans = models.CharField(max_length=1024)


class TTSSpr(models.Model):
    """Справочник произношения слов"""
    word = models.CharField('Слово', max_length=64)
    speech = models.CharField('Произношение', max_length=64)

    def __str__(self):
        return '%s: %s' % (self.word, self.speech)
