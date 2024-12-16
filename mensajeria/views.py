from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'mensajeria/inbox.html', {'messages': messages})

# Create your views here.
from django.shortcuts import render, redirect
from .forms import MessageForm

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'mensajeria/send_message.html', {'form': form})

from django.shortcuts import render
from .models import Message

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'mensajeria/inbox.html', {'messages': messages})
