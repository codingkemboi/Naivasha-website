from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			new_user = authenticate(request, username=username, password=password)
			if new_user is not None:
				login(request, new_user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("kongoni_web:home")
			
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="users/login.html", context={"login_form":form})


def logoutUser(request):
    """Log the user out."""
    logout(request)
    return redirect('kongoni_web:home')






def register_request(request):	
	if request.method != "POST":
		form = NewUserForm()
	else:
		# process completed form
		form = NewUserForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			authenticated_user = authenticate(username=new_user.username,
										password=request.POST['password1'])
			login(request, authenticated_user)
			messages.success(request, "Registration successful." )
			return redirect("users:login")

		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	

	context = {'register_form': form}
	return render (request=request, template_name="users/register.html", context={"register_form":form})