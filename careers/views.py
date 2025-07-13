

from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application
from django.http import HttpResponse


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_listings.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})




def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']
        Application.objects.create(job=job, name=name, email=email, resume=resume)
        # return HttpResponse("Application submitted successfully!")
        return redirect('success')

    return render(request, 'apply.html', {'job': job})

def success(request):
    return render(request, 'success.html')

from django.shortcuts import render

def chatbot(request):
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []

    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        response = generate_response(user_message)

        # Update chat history
        chat = request.session['chat_history']
        chat.append({'user': user_message, 'bot': response})
        request.session['chat_history'] = chat

    return render(request, 'chatbot.html', {'chat_history': request.session.get('chat_history', [])})


# Simple logic to simulate chatbot replies
def generate_response(message):
    message = message.lower()
    if "apply" in message:
        return "You can apply by clicking the 'Apply' button on the job listing."
    elif "job" in message or "openings" in message:
        return "Check our homepage to see all current job openings."
    elif "hello" in message or "hi" in message:
        return "Hi! How can I assist you with your job application today?"
    else:
        return "Sorry, I didn't understand that. Please ask about jobs, application status, or how to apply."
    
def landing(request):
    return render(request, 'landing.html')    
