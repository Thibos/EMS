from django.shortcuts import render
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.contrib import messages


import requests



from django.utils import timezone

# Create your views here.
def post_list(request):

    return render(request,'homeApp/loging.html')

def loging(request):
    """1.get the token from the server using login credetials
        2.on login successful then open the dashboard with employees data"""
    if request.method =='POST':
        print "its a post"
        uname= request.POST.get('uname')
        psw=request.POST.get('psw')
        print uname

        credetials={'username':uname,'password':psw}

        #get the token from the server
        response = requests.post("http://staging.tangent.tngnt.co/api-token-auth/",data=credetials)
        token=response.json()
        print response.status_code
        if response.status_code == 200:
           # messages.success(request,"Login successful")


            return render(request,'homeApp/graph.html')
        else:
            messages.error(request,"Login credetials are wrong")




    return render(request,'homeApp/loging.html')




def profile(request):
    """1.get the token from the server using login credetials
        2.on login successful then open the dashboard with employees data"""


    return render(request,'homeApp/loging.html')


def graph(request):
    heade = {'Authorization': 'token {}'.format('2a3d1af2f3f6d1cddaa3012c1c465fcbdffa3678')}
    url = "http://staging.tangent.tngnt.co/api/employee/"
    employeers = requests.get(url, headers=heade)
    print employeers.json()


    return render(request, 'homeApp/graph.html')

def getUser():
    heade = {'Authorization': 'token {}'.format('2a3d1af2f3f6d1cddaa3012c1c465fcbdffa3678')}
    url = "http://staging.tangent.tngnt.co/api/user/me/"
    user = requests.get(url, headers=heade)
    print user.json()

    return user

def getEmployeers():
    heade = {'Authorization': 'token {}'.format('2a3d1af2f3f6d1cddaa3012c1c465fcbdffa3678')}
    url = "http://staging.tangent.tngnt.co/api/employee/"
    employeers = requests.get(url, headers=heade)
    print employeers.json()
    return employeers

def getMyProfile():
    heade = {'Authorization': 'token {}'.format('2a3d1af2f3f6d1cddaa3012c1c465fcbdffa3678')}
    url = "http://staging.tangent.tngnt.co/api/employee/me/"
    profile = requests.get(url, headers=heade)
    print profile.json()
    return profile


