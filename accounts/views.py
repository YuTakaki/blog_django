from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signUp(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('articles:all')
  else:
    form = UserCreationForm()
  return render(request, "accounts/signup.html", {'form': form})

def signIn(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      # form.save()
      user = form.get_user()
      login(request, user)
      if "next" in request.POST:
        return redirect(request.POST.get('next'))
      return redirect('articles:all')
  else:
    form = AuthenticationForm()
  return render(request, "accounts/signin.html", {'form': form})

def logoutview(request):
  logout(request)
  return redirect('articles:all')