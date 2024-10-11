from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def SendEmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = "Welcome!"
        from_email = 'jaynishdhanani8@gmail.com'
        to_email = [email]
        
       # Render the HTML content for the email
        html_content = render_to_string('wlcemail.html', {'message': message})
        text_content = f"Welcome to our site, {message}!"  # Plain text fallback

        # Create the email with both plain text and HTML versions
        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")  # Attach HTML version
        
        # Send the email
        msg.send(fail_silently=False)

    return render(request, 'MyEmail.html')