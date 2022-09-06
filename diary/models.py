from django.db import models
# djangoでは datetime.nowの代わりに timezone.now で現在日付・時刻を取得
from django.utils import timezone


# models.Modelクラスを継承した独自クラス
class Day(models.Model):
    # CharField 1行で終わる文章
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
