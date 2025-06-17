from django.http import HttpResponse
from .tasks import send_welcome_email

def trigger_email(request):
    send_welcome_email.delay("22eg506b03@anurag.edu.in")
    return HttpResponse("Email task triggered.")
