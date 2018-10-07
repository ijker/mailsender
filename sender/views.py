from common.mymako import render_mako_context
from django.http import HttpResponse
from blueking.component.shortcuts import get_client_by_request
import json

# Create your views here.

def home(request):
	return render_mako_context(request,'sendmail/home.html')

def sendmail(request):
	text={}
	text["title"]=request.POST.get("title")
	text["receiver"]=request.POST.get("receiver")
	text["content"]=request.POST.get("content")
	client=get_client_by_request(request)
	result=client.cmsi.send_mail(**text)
	return HttpResponse(json.dumps(result),content_type="application/json")
