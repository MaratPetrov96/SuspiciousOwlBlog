from .models import Record
from django.forms import ModelForm,TextInput,Textarea,DateTimeInput,ImageField

class AddForm(ModelForm):
    class Meta:
        model=Record
        fields=['title','text','anons','picture']
        widgets={'title':TextInput(attrs={'name':'link'}),
                 'anons':Textarea(attrs={'name':'anons','rows':'2','cols':'20'}),
                 'text':Textarea(attrs={'name':'title',
                                        'rows':'8','cols':'40'}),
                 'picture':ImageField()}
