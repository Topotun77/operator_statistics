from django.db import models


class Call(models.Model):
    """ Модель таблицы Звонок """
    id = models.AutoField(primary_key=True)
    campaign = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    operator = models.CharField(max_length=100, null=True, blank=True)
    processed = models.BooleanField(default=False)
    status = models.CharField(max_length=250, null=True, blank=True)
    # Видимо, следующее поле д.б. связано с таблицей Base, но для базы в ТЗ не указана
    # уникальность поля Идентификатор и тип указан текстовый. Т.е. не совсем понятно,
    # что такое "база" и "кампания"? Связь, все-таки, идет по "кампании" или по "базе"?
    # Если по "база", то почему поле м.б. пустым?
    base = models.CharField(max_length=300, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    success = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонок'
        db_table = 'call'

    def __str__(self):
        return f"{self.operator} ({self.number}, {self.campaign})"


class Base(models.Model):
    """ Модель таблицы заданий """
    id = models.CharField(max_length=300, unique=True, primary_key=True)
    campaign = models.CharField(max_length=100)
    received_date = models.DateField()
    parameters = models.JSONField()
    task = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'База'
        verbose_name_plural = 'База'
        db_table = 'base'

    def __str__(self):
        return f"{self.task} ({self.received_date})"

