from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
	score=5
	return render(request, 'play.html')
