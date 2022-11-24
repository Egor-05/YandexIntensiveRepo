from datetime import datetime
from os import mkdir, path

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pytz import timezone

from .forms import FeedbackForm
from .models import Feedback


def get_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            time = timezone("Europe/Moscow").localize(datetime.now())
            Feedback.objects.create(text=text, created_at=time)

            # Здесь сделал условную отправку

            send_mail(
                "Обратная связь",
                text,
                "user@example.com",
                ["reciever@example.com"],
                fail_silently=True,
            )
        return HttpResponseRedirect("/feedback/")
    else:
        form = FeedbackForm()

    return render(request, "feedbackform.html", {"form": form})
