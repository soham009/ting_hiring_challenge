#--- Ting Hiring Challenge - Imported Packages List ----

#------Django Internal Packages-----
from django.urls import include, path,re_path
from django.contrib.auth import views as auth_views
#<------Django Internal Packages-----

#------ Ting Hiring Challenge Importing Project Files -----
#Ting Hiring Challenge - Our Application Views
from ting_hiring_challenge_app import views

#</--- Ting Hiring Challenge Importing Project Files ----

#Ting Hiring Challenge - Application Name for URL Calling from Templates
app_name = 'ting_hiring_challenge_app'

#--- Ting Hiring Challenge Data Management URL List ----
urlpatterns = [

#<------ Ting Hiring Challenge Index Form URLs -----

#Ting Hiring Challenge  - Index Form
path("", views.email_validation, name="email_validation"),

path('Login',views.user_login,name='Login'),

path('logout',views.user_sign_out,name='logout'),

path('all_players',views.all_players,name='all_players'),

path('all_winners',views.all_winners,name='all_winners'),

path('all_users',views.all_users,name='all_users'),
#Ting Hiring Challenge  - Index Form
path("exists", views.email_exists, name="email_exists"),

#Ting Hiring Challenge  - Index Form
path("form", views.form, name="form"),

path('form_submit',views.form_submit,name="form_submit"),

path('success_page',views.success_page,name='success_page'),

path("failed_page",views.failed_page,name="failed_page"),

#Ting Hiring Challenge  - Index Form
path("questions", views.questions, name="questions"),

path('question_submit',views.question_submit,name='question_submit'),

#Ting Hiring Challenge  - Index Form
path("email_form_submit", views.email_form_submit, name="email_form_submit"),
#Ting Hiring Challenge  - Survey Form Submit
#path("leads/form/submit", views.home_form_submit, name="home_form_submit"),
#Ting Hiring Challenge  - Index Form
path("spin_submit", views.spin_submit, name="spin_submit"),
#</------ Ting Hiring Challenge Index Form URLs -----

]