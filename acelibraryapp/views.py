from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
	
	return render(request,'fbauth/index.html',{'user': request.user,'user': request.user})
