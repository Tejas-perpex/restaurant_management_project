from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('feedback')  # reload page after saving
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})
