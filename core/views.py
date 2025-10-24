from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from news.models import Information, Category
from django.db.models import Q
from Reports.models import Relatoriu
from django.core.paginator import Paginator
from django.utils import timezone
from django.conf import settings

# Create your views here.

def Index(request):
    categories = Category.objects.all()
    latest_reports = Relatoriu.objects.order_by('-data')[:3]

    q = request.GET.get('q', '').strip()
    if q:
        infos_qs = Information.objects.select_related('category').filter(
            Q(title__icontains=q) | Q(excerpt__icontains=q) | Q(content__icontains=q)
        ).distinct()
    else:
        infos_qs = Information.objects.select_related('category').all()
    
    paginator = Paginator(infos_qs, 6)  # 6 news items per page
    page_number = request.GET.get('page')
    infos = paginator.get_page(page_number)

    # Provide both 'infos' (new) and 'info' (legacy) to avoid breaking existing templates
    context = {
        'infos': infos,
        'info': infos,  # legacy key used in some templates
        'categories': categories,
        'latest_reports': latest_reports,
        'page': page_number,
        'query': q,
        'results_count': infos.paginator.count if hasattr(infos, 'paginator') else None,
    }

    # Handle contact form POST
    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        email = (request.POST.get('email') or '').strip()
        subject = (request.POST.get('subject') or '').strip()
        message = (request.POST.get('message') or '').strip()

        # Basic validation
        if not all([name, email, subject, message]):
            messages.error(request, "Please fill out all fields.")
            return render(request, 'home/index.html', context)

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address.")
            return render(request, 'home/index.html', context)

        # Prepare email content
        full_message = f"New message received from your website contact form:\nFrom: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}"
        try:
            # Send message to admin
            send_mail(
                subject=f"New Contact Message: {subject}",
                message=full_message,
                from_email='no-reply@yourdomain.com',  # Replace with your domain email or configured sender
                recipient_list=['abraaodejesusximenes@gmail.com'],
                fail_silently=False,
            )

            # Optionally send an auto-reply to the user (non-blocking)
            try:
                send_mail(
                    subject="Thank you for contacting ANCT - TL",
                    message=(f"Hi {name},\n\nThank you for reaching out to ANCT - TL.\nWe have received your message and will get back to you soon.\n\n--\n{message}"),
                    from_email='no-reply@yourdomain.com',
                    recipient_list=[email],
                    fail_silently=True,
                )
            except Exception:
                # Don't fail the whole request if auto-reply fails
                pass

            messages.success(request, "Your message has been sent. Thank you!")
            return redirect('index')

        except BadHeaderError:
            messages.error(request, "Invalid header found.")
        except Exception as e:
            messages.error(request, f"An error occurred while sending your message: {e}")

    return render(request, 'home/index.html', context)





