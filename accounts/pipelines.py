from .models import User

def save_profile(backend,user,details,response,*args,**kwargs):
    if backend.name == "google-oauth2":
        profile=user
        if profile is None:
            profile = User(id=user.id)

        profile.nome= details['fullname']
        profile.save()