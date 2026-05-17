from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SupportTicket
from .forms import SupportTicketForm


@login_required
def support_list(request):
    tickets = SupportTicket.objects.filter(user=request.user)
    return render(request, 'support/list.html', {'tickets': tickets})


@login_required
def support_create(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Ticket submitted successfully.')
            return redirect('support_list')
    else:
        form = SupportTicketForm()
    return render(request, 'support/create.html', {'form': form})


@login_required
def support_detail(request, pk):
    ticket = get_object_or_404(SupportTicket, pk=pk, user=request.user)
    return render(request, 'support/detail.html', {'ticket': ticket})


def help_center(request):
    return render(request, 'support/help_center.html')


def privacy_policy(request):
    return render(request, 'support/privacy_policy.html')


def terms_of_service(request):
    return render(request, 'support/terms_of_service.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        messages.success(request, 'Thank you! Your message has been sent successfully. We will get back to you soon.')
        return redirect('contact_us')
    return render(request, 'support/contact_us.html')
