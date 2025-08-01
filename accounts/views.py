from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Volunteer
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.conf import settings
from paystackapi.transaction import Transaction
from django.shortcuts import render, redirect
from .models import Donation
from .models import Event
from django.utils import timezone


def home(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'accounts/index.html', {'upcoming_events': upcoming_events})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'accounts/signup.html')
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        login(request, user)
        messages.success(request, "You are signed in!")
        return redirect('profile')  # Redirect to profile after signup
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are signed in!")
            return redirect('home')  # Redirect to profile after signin
        else:
            error = "Invalid username or password."
            return render(request, 'accounts/login.html', {'error': error})
    return render(request, 'accounts/login.html')

def signout_view(request):
    logout(request)
    messages.success(request, "You have been signed out.")
    return redirect('login')

def donate_view(request):
    context = {
        'PAYSTACK_PUBLIC_KEY': settings.PAYSTACK_PUBLIC_KEY,
        # ... other context ...
    }
    return render(request, 'accounts/donate.html', context)

# Profile view to display user information
def volunteer_view(request):
    context = {}
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if Volunteer.objects.filter(user=request.user).exists():
            context['volunteer_message'] = "Thank you for volunteering! You are already registered as a volunteer."
        else:
            Volunteer.objects.create(user=request.user, phone_number=phone_number)
            context['volunteer_message'] = "Thank you for signing up as a volunteer! Our team will contact you soon."
    return render(request, 'accounts/volunteer.html', context)

@login_required
def profile_view(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'accounts/profile.html', {'upcoming_events': upcoming_events})

def verify_payment(request):
    reference = request.GET.get('reference')
    response = Transaction.verify(reference)
    print(response)  # Debug: See Paystack response in your terminal
    if response['status'] and response['data']['status'] == 'success':
        amount = response['data']['amount'] / 100
        email = response['data']['customer']['email']
        donation = Donation.objects.create(
            amount=amount,
            reference=reference,
            email=email,
            user=request.user if request.user.is_authenticated else None
        )
        print(donation)  # Debug: Confirm donation is created
        return render(request, 'accounts/payment_success.html', {'reference': reference})
    else:
        return render(request, 'accounts/payment_failed.html', {'reference': reference})