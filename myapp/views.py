from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, SnippetForm, SignUpForm

# Create your views here.
def contact(request):

	if request.method == 'POST':

		form = ContactForm(request.POST)
		if form.is_valid():
			name= form.cleaned_data['name']
			email=form.cleaned_data['email']

			print(name, email)
	
	form = ContactForm(request.POST)
	return render(request, 'form.html', {'form':form})

	#return HttpResponse('Contact View')

def snippet_details(request):

	if request.method == 'POST':

		form = SnippetForm(request.POST, request.FILES)
		if form.is_valid():

			a=form.save(commit=False)
			a.save()

			print("Valid")
			return render(request, 'welcome.html')
		
	form = SnippetForm(request.POST,request.FILES)
	return render(request, 'form.html', {'form':form})


def login_details(request):

	if request.method == 'POST':

		form =  SignUpForm(request.POST)
		if form.is_valid():

			a=form.save(commit=False)
			a.save()

			print("Valid Login")
			return render(request, 'welcome.html')
		else:
			return render(request, 'welcome.html')

	
	form = SignUpForm(request.POST,request)
	return render(request, 'login.html', {'form':form})