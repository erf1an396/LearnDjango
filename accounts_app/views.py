from django.shortcuts import render, HttpResponse
from django.http import Http404


users = [
    {
        'username':'amir',
        'name':'amirhossein',
        'lastname':'amir',
        'phone':'09391231245',
        'city':'ahwaz'
    },
       {
        'username':'milad',
        'name':'shahparast',
        'lastname':'dodoli',
        'phone':'09391231245',
        'city':'ahwaz'
    },
       {
        'username':'mehdi',
        'name':'navamisi',
        'lastname':'parandeh',
        'phone':'09391231245',
        'city':'ahwaz'
    },
]

def userslist(request):
    user_list = users
    return render (request, 'accounts_app/user_list.html', context={'users_list':users})


def profile(request, username):
    for user in users:
        if user['username'] == username:
            return render(request,'accounts_app/profile.html', context={"user":user})
    
    raise Http404("this is not found")
    
def info(request):
    return render(request, 'accounts_app/info.html')


