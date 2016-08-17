from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import NameForm,ContactForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
     
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
           
            return render(request,'testform/thanks.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'testform/name.html', {'form': form, 'ContactForm': ContactForm})

def send_mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return render(request,'testform/thanks.html')