from django.shortcuts import render

def index(request):
	return render(request, 'artist/index.html')

def gallery(request):
	return render(request, 'artist/gallery.html')

def about(request):
	return render(request, 'artist/about.html')

def contact(request):
	return render(request, 'artist/contact.html')
