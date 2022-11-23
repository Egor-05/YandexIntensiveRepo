from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FeedbackForm


def get_feedback(request):
    if request.method == 'POST':
        print(request.POST)
        text = request.POST.get('text')
        print(text, '--------------------')
        return HttpResponseRedirect('/123')
    else:
        form = FeedbackForm()

    return render(request, 'feedbackform.html', {'form': form})