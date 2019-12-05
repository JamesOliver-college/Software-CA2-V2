from django.shortcuts import render



from .email import Email

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_email = form.cleaned_data['email']
            signup_user = User.objects.get(name='Customer')
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            Email.sendSignUpConfirmation(request, username, user_email)