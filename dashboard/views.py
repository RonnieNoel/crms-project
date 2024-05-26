from django.shortcuts import render,redirect
from login.models import Crime,User,Charge,Evidence,Investigation,Suspect,Victim,Witness
from django.contrib.auth.decorators import login_required,user_passes_test
from dashboard.Reportcase import CrimeForm
from django.contrib import messages
from email.message import EmailMessage
import ssl
import smtplib
from django.urls import reverse


def staff_required(view_func):
    """
    Decorator to restrict access to staff users only.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse('login'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@login_required
def UserDashView(request):
    # Count occurrences for each related model
    charge_count = Charge.objects.count()
    evidence_count = Evidence.objects.count()
    investigation_count = Investigation.objects.count()
    suspect_count = Suspect.objects.count()
    victim_count = Victim.objects.count()
    witness_count = Witness.objects.count()
    user_count=User.objects.count()
    crime_count=Crime.objects.count()

    female_crime_count = Suspect.objects.filter(gender='female').count()
    male_crime_count = Suspect.objects.filter(gender='male').count()

    # Pass the counts to the template
    return render(request, 'UserDash.html', {
        'charge_count': charge_count,
        'evidence_count': evidence_count,
        'investigation_count': investigation_count,
        'suspect_count': suspect_count,
        'victim_count': victim_count,
        'witness_count': witness_count,
        'user_count':user_count,
        'female_crime_count': female_crime_count,
        'male_crime_count': male_crime_count,
        'crime_count':crime_count
    })

@staff_required
def DashView(request):
    crime_count = Crime.objects.count()
    user_count = User.objects.count()
    suspect_count = Suspect.objects.count()
    evidence_count = Evidence.objects.count()
    investigation_count = Investigation.objects.count()
    
    data = Crime.objects.all().order_by('-reference')[:5]
    suspects=Suspect.objects.all().order_by('-id')[:5]
    return render(request, 'Dashboard.html', {
        'suspect_data':suspects,
        'passed_data': data,
        'crime_count': crime_count,
        'user_count': user_count,
        'suspect_count': suspect_count,
        'evidence_count': evidence_count,
        'investigation_count': investigation_count,
    })

@staff_required
def StatView(request):
    # Count occurrences for each related model
    charge_count = Charge.objects.count()
    evidence_count = Evidence.objects.count()
    investigation_count = Investigation.objects.count()
    suspect_count = Suspect.objects.count()
    victim_count = Victim.objects.count()
    witness_count = Witness.objects.count()
    user_count=User.objects.count()
    crime_count=Crime.objects.count()

    female_crime_count = Suspect.objects.filter(gender='female').count()
    male_crime_count = Suspect.objects.filter(gender='male').count()

    # Pass the counts to the template
    return render(request, 'statistics.html', {
        'charge_count': charge_count,
        'evidence_count': evidence_count,
        'investigation_count': investigation_count,
        'suspect_count': suspect_count,
        'victim_count': victim_count,
        'witness_count': witness_count,
        'user_count':user_count,
        'female_crime_count': female_crime_count,
        'male_crime_count': male_crime_count,
        'crime_count':crime_count
    })


@login_required
def ReportCase(request):
    return render(request,'Reportcrime.html')

@login_required
def SubmitView(request):
    if request.method == "POST":
        form = CrimeForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            instance = form.save()

            # Get the email address from the form
            email_sender ='your email'
            email_password = 'your password' 

            # Send email notification
            email_receiver = form.cleaned_data['email']

            subject = 'Crime Reported'
            body = f"Crime Name : {instance.name}\nDescription: {instance.description}\nLocation: {instance.location}"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            messages.success(request, "Crime reported successfully")
            return redirect("home")
        else:
            messages.error(request, "Something went wrong")
    else:
        form = CrimeForm()
    return render(request, "Reportcrime.html", {'form': form})
