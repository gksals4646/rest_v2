from django import forms
from .models import Customer
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required':'이름을 입력해주세요'
        },
        max_length=64, label ='이름'
    )
    phone = forms.CharField(
        error_messages={
            'required':'전화번호를 입력해주세요'
        },
        max_length=64, label ='전화번호'
    )
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요'
        },
        widget = forms.PasswordInput, label = '비밀번호'
    )
    repassword = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요'
        },
        widget = forms.PasswordInput, label = '비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')

        if password and repassword:
            if password != repassword:
                self.add_error('password','비밀번호가 서로 다릅니다.')
                self.add_error('repassword','비밀번호가 서로 다릅니다.')
            else:
                customer = Customer(
                    name = name,
                    phone = phone,
                    password = password
                )
                customer.save()

class LoginForm(forms.Form):
    phone = forms.CharField(
        error_messages={
            'required':'전화번호를 입력해주세요'
        },
        max_length=64, label ='전화번호'
    )
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요'
        },
        widget = forms.PasswordInput, label = '비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password')
        

        if phone and password:
            try:
                customer = Customer.objects.get(phone=phone)
            except Customer.DoesNotExist:
                self.add_error('phone','등록되지않은 전화번호 입니다.')
                return
            
            if password != customer.password:
                self.add_error('password','비밀번호를 틀렸습니다.')

            else:
                self.name = customer.name
                self.phone = customer.phone

