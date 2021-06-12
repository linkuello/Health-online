from django.shortcuts import render, redirect
from .forms import ProfileForm, ContactForm
from healthprofile import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

#def profile(request):
#    all=profile.objects.all()
#    return render(request,"home.html",{"item":all,})

#def profile_detail(request,food_id):
#	profiles=profile.objects.get(pk=profile_id)
#	return render(request,"profile.html",{"profile":profiles,"title":profiles.title})

#def add_profile(request):
#	if request.method=="POST":
#            title=request.POST["title"]
#            selfintroduction=request.POST["selfintroduction"]
#            country=request.POST["country"]
#            image_url=request.POST["image_url"]
#            phone_number=request.POST["phone_number"]
#            email=request.POST["email"]
#            byear=request.POST["byear"]
#            expertise=request.POST["expertise"]
#            prep_method=request.POST["prep_method"]
#            upload_date=request.POST["upload_date"]
#            new_profile=profile.objects.create(
#            	title=title,
#            	selfintroduction=selfintroduction,
#            	country=country,
#            	phone_number=phone_number,
#            	email=email,
#            	image_url=image_url,
#            	byear=byear,
#            	expertise=expertise,
#            	prep_method=prep_method,
#            	upload_date=upload_date,)
#            return redirect("/")
#	return render(request,"addprofile.html")



# Create your views here.


@login_required
def profile(request):
    user = request.user
    user_profile = models.Profile.objects.get(user=user)
    user_contact = models.Contact.objects.get(user=user)

    return render(request, "profile/profile.html", locals())


@login_required
def update_profile(request):
    user = request.user
    user_profile = models.Profile.objects.get(user=user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Update Success')
        else:
            messages.warning(request, 'To modify the personal information, each field must be filled in')
    else:
        profile_form = ProfileForm(instance=user_profile)
        messages.warning(request, 'Update Failed')

    return render(request, 'profile/update_profile.html', locals())


@login_required
def update_contact(request):
    user = request.user
    user_contact = models.Contact.objects.get(user=user)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, instance=user_contact)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Update Success')
        else:
            messages.warning(request, 'To modify the personal information, each field must be filled in')
    else:
        contact_form = ContactForm(instance=user_contact)
        messages.warning(request, 'Update Failed')

    return render(request, 'profile/update_contact.html', locals())



# @login_required
# def userinfo(request):
#     user=User.objects.get(name=name)
#     try:
#         profile=profile.objects.get(user=user)
#     except:
#         profile=Profile(user=user)
#
#     if request.method=='POST':
#         profile_form=ProfileForm(request.POST,instance=profile)
#         if profile_form.is_valid():
#             messages.add_message(request,messages.INFO,"Personal information has been saved")
#             profile_form.save()
#             return HttpResponseRedirect('/userinfo')
#         else:
#             messages.add_message(request,messages.INFO,'To modify the personal information, each field must be filled in')
#     else:
#         profile_form=ProfileForm()
#     return render(request, 'healthprofile/userinfo.html', locals())


# @login_required
# def contact(request):
#     user=User.objects.get(name=name)
#     contact=Contact.objects.get(user=user)
#     try:
#         contact=Contact.objects.get(user=user)
#     except:
#         contact=Contact(user=user)
#
#     if request.method=='POST':
#         contact_form=ContactForm(request.POST,instance=contact)
#         if contact_form.is_valid():
#             messages.add_message(request,messages.INFO,"Personal information has been saved")
#             contact_form.save()
#             return HttpResponseRedirect('/contact')
#         else:
#             messages.add_message(request,messages.INFO,'To modify the personal information, each field must be filled in')
#     else:
#         contact_form=ContactForm()
#     return render(request, 'healthprofile/contact.html', locals())

