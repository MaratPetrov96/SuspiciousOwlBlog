class AddForm(ModelForm):
    class Meta:
        model=Record
        fields=['title','text','anons','picture']
        widgets={'title':TextInput(attrs={'name':'link','placeholder':''}),
                 'anons':Textarea(attrs={'name':'anons','rows':'2','cols':'20',
                                         'placeholder':''}),
                 'text':Textarea(attrs={'name':'title','rows':'10','cols':'60'
                                        ,'placeholder':''})}
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Optional.')
    last_name = forms.CharField(max_length=30, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets={'content':Textarea(attrs={'name':'title','rows':'10','cols':'60'
                                        ,'placeholder':'Ваш комментарий'})}
