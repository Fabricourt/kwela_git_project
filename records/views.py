from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from .models import balance
from django.contrib.auth.models import User

def records(request):
   
    msg=""
    if request.method == "POST":
        try:
            username = request.POST["username"]
            amount = request.POST["amount"]
            senderUser = User.objects.get(username=request.user.username)
            receiverrUser =  User.objects.get(username=username)
            sender = balance.objects.get(user = senderUser)
            receiverr = balance.objects.get(user = receiverrUser)
            sender.balance = sender.balance - int(amount)
            receiverr.balance = receiverr.balance - int(amount)
            sender.save()
            receiverr.save()
            msg = "Transaction Success"
        except Exception as e:
            print(e)
            msg = "Transaction Failure, Please check and try again"
    user = balance.objects.get(user=request.user)
    return render(request,'records/records.html',{"balance":user.balance,"msg":msg}, )

