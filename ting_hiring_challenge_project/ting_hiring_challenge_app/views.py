from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth import login, logout, authenticate
from ting_hiring_challenge_app.models import PlayerRegistration,PlayerWinnings,CustomUser
# Create your views here.

def user_login(request):
    """Logs in a user if the credentials are valid and the user is active,
    else redirects to the same page and displays an error message."""
    if request.method == 'POST':
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('ting_hiring_challenge_app:all_players'))  
        else:
            return render(request, 'ting_hiring_challenge_app/login.html',{'error_message': 'Username or Password Incorrect!'})
    else:
        return render(request, 'ting_hiring_challenge_app/login.html')

def user_sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('ting_hiring_challenge_app:Login'))

def all_players(request):
    player_list = PlayerRegistration.objects.all()
    data={'player_list':player_list}
    return render(request, 'ting_hiring_challenge_app/player_table.html',data)

def all_winners(request):
    winners_list=PlayerWinnings.objects.all()
    data={'winners_list':winners_list}
    return render(request, 'ting_hiring_challenge_app/winning_table.html',data)

def all_users(request):
    users_list=CustomUser.objects.all()
    data={'users_list':users_list}
    return render(request, 'ting_hiring_challenge_app/user_table.html',data)


def email_validation(request):
    """This view is for taking email input from user
    parameter : request
    returns : Html Template
    on page "email_validation.html" """
    data={}
    return render(request, 'ting_hiring_challenge_app/email_validation.html',data)

def email_exists(request):
    """This view is for taking email input from user
    parameter : request
    returns : Html Template
    on page "email_validation.html" """
    data={}
    return render(request, 'ting_hiring_challenge_app/email_validation.html',data)

def form(request):
    """This view is for taking email input from user
    parameter : request
    returns : Html Template
    on page "email_validation.html" """
    if request.method == "POST":
        player_email = request.POST['player_email']
    data={'player_email':player_email}
    return render(request, 'ting_hiring_challenge_app/form.html',data)

def form_submit(request):
    if request.method == "POST":
        player_email = request.POST['player_email']
        player_name = request.POST['player_name']
        player_gender= request.POST['player_gender']
        player_mobile_no = request.POST['player_mobile_no']
        player_address = request.POST['player_address']
        Player_object = PlayerRegistration.objects.get(player_email=player_email)
        Player_object.player_name = player_name
        Player_object.player_gender = player_gender
        Player_object.player_mobile_no = player_mobile_no
        Player_object.player_address = player_address
        Player_object.save()
        return HttpResponseRedirect(reverse('ting_hiring_challenge_app:success_page'))


def success_page(request):
    return render(request, 'ting_hiring_challenge_app/success_form.html')


def failed_page(request):
    if request.method == "POST":
        player_email = request.POST['player_email1']
        Player_object = PlayerRegistration.objects.get(player_email=player_email)
        if Player_object.player_retry == True:
            data={'player_email':player_email}
            return render(request,'ting_hiring_challenge_app/failed.html',data)
        else:
            data={}
            return render(request,'ting_hiring_challenge_app/no_retry.html',data)
                        
def questions(request):
    """This view is for taking email input from user
    parameter : request
    returns : Html Template
    on page "questions.html" """
    if request.method == "POST":
        player_email = request.POST['player_email1']
        data={'player_email':player_email}
        return render(request, 'ting_hiring_challenge_app/questions.html',data)

def question_submit(request):
    if request.method == "POST":
        player_email = request.POST['player_email']
        ans1 = request.POST['question1']
        ans2 = request.POST['question2']
        Player_object = PlayerRegistration.objects.get(player_email=player_email)
        Player_object.player_retry = False
        Player_object.save()
        if ans1=="250+" and ans2=="Delhi":
            data={'player_email':player_email}
            return render(request, 'ting_hiring_challenge_app/spin.html',data)
        else:
            data={}
            return render(request,'ting_hiring_challenge_app/last_failure.html')

def email_form_submit(request):
    """This view is for taking email input from user
    parameter : request
    returns : Html Template
    on page "email_validation.html" """
    if request.method == "POST":
        player_email = request.POST['player_email']
        if PlayerRegistration.objects.filter(player_email=player_email).exists():
            return render(request, 'ting_hiring_challenge_app/email_validation.html',{'error_message':"User Exists"})
        else :
            PlayerRegistration.objects.create(player_email=player_email)
            data={'player_email':player_email}
            return render(request, 'ting_hiring_challenge_app/spin.html',data)
    data={}
    return render(request, 'ting_hiring_challenge_app/email_validation.html')

def spin_submit(request):
    """This view is for taking email input from user
    parameter : request
    returns : Html Template
    on page "email_validation.html" """
    if request.method == "POST":
        player_winning = request.POST.get('player_winning')
        player_email = request.POST.get('player_email')
        Player_object = PlayerRegistration.objects.get(player_email=player_email)
        PlayerWinnings.objects.create(player_name=Player_object,player_winning=player_winning)
        # return HttpResponse('ting_hiring_challenge_app:email_validation')
        return HttpResponseRedirect(reverse('ting_hiring_challenge_app:email_validation'))

    # def spin_submit(request):
    # """This view is for taking email input from user
    # parameter : request
    # returns : Html Template
    # on page "email_validation.html" """
    # if request.method == "POST":
    #     player_email = request.POST.get('player_email1')
    #     Player_object = PlayerRegistration.objects.get(player_email=player_email)
    #     PlayerWinnings.objects.create(player_name=Player_object,player_winning=player_winning)
    #     # return HttpResponse('ting_hiring_challenge_app:email_validation')
    #     return HttpResponseRedirect(reverse('ting_hiring_challenge_app:email_validation'))    