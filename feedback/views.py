from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Feedback
from datetime import datetime
from os import mkdir, path
from pytz import timezone

from .forms import FeedbackForm


def get_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            time = timezone('Europe/Moscow').localize(datetime.now())
            Feedback.objects.create(text=text, created_at=time)
            if not path.exists('send_mail'):
                mkdir('send_mail')
            with open(f'send_mail/{time}', 'w') as f:
                f.write(text)
        return HttpResponseRedirect('/feedback/')
    else:
        form = FeedbackForm()

    return render(request, 'feedbackform.html', {'form': form})