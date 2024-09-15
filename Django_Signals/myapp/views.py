from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def create_new_user(request):
    print("Initiating user creation...")
    
    # Create a new user to trigger the post_save signal
    new_user = User.objects.create(username='sample_user')
    
    print("User creation complete, signal will now be processed.")
    
    return HttpResponse("User has been successfully created!")


