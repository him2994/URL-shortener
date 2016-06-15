from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import *
from django.http import *
from django.shortcuts import *
from django.core.urlresolvers import reverse

# Create your views here.
@csrf_exempt
def index(request):
	if request.method == 'GET':
		print 'here2'
		return render(request,'index.html',{'status':''})

	if request.method == 'POST':
		print request
		url = 'http://localhost:9000/api/'
		u = request.POST.get('url')
		print u
		data = {'url':u}
		print data
		r = requests.post(url,data=data)
		if r.status_code == 200 :
			result = r.json()
			print result
			return render(request,'index.html',{'url':result,'status':''})
		else :
			return render(request,'index.html',{'status':'Something wrong happen. Try again later.'})


@csrf_exempt
def rdirect(request,u):
	if request.method == 'GET':
		print 'here'
		print u
		url = 'http://localhost:9000/api/?q='+u
		r = requests.get(url)
		result = r.json()
		print result
		if r.status_code == 200 and result['status'] == 'Success':
			return	HttpResponseRedirect(result['furl'])
		else :
			data={'status':'Shorted url does not exist.'}
			return HttpResponseRedirect(reverse('index'),data)  #bsbvbdvbdooooooooo