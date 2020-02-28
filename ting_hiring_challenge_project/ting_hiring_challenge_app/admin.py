#<------Django Internal Packages-----
from django.contrib import admin
#</------Django Internal Packages-----

#<------Importing My Models from Models.py-----
from ting_hiring_challenge_app.models import PlayerRegistration, PlayerWinnings, CustomUser
#</------Importing My Models from Models.py-----

# My Models
class PlayerRegistrationAdmin(admin.ModelAdmin):
    search_fields = ["player_name"]
    list_display = [
        "pk",
        "player_name",
        "player_gender",
        "player_mobile_no",
        "player_email",
        "created_at",
        "updated_at",
    ]
    list_editable = ["player_name",
        "player_gender",
        "player_mobile_no",
        "player_email"]

class PlayerWinningsAdmin(admin.ModelAdmin):
    search_fields = ["player_name"]
    list_display = [
        "pk",
        "player_name",
        "player_winning",
        "created_at",
        "updated_at",
    ]

class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ["pk","name"]
    list_display = [
        "pk",
        "role",
        "name",
    ]
    list_editable = ["role","name"]

#<------Registering My Models to display on Admin Site-----
admin.site.register(PlayerRegistration,PlayerRegistrationAdmin)
admin.site.register(PlayerWinnings,PlayerWinningsAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
#</------Registering My Models to display on Admin Site-----

#<------ Customizing the Django Admin Dashboard -----
admin.site.site_header = "Ting Hiring Challenge"
admin.site.site_title = "Ting Hiring Challenge"
admin.site.index_title = "Welcome to Ting Hiring Challenge"
#</------Customizing the Django Admin Dashboard-----