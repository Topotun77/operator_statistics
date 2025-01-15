from datetime import datetime

from django import forms

from .models import Base


class QueryStatForm(forms.ModelForm):
    """
    Форма для запроса статистики
    """
    operator = forms.CharField(label='Оператор:', max_length=100)
    from_date = forms.DateField(label='Дата начала периода:',
                                initial=datetime.now().date().replace(day=1))
    to_date = forms.DateField(label='Дата окончания периода:',
                              initial=datetime.now().date())

    class Meta:
        model = Base
        fields = ['operator', 'from_date', 'to_date']
