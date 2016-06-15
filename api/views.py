from django.shortcuts import render
from models import *
import json
from django.http import *
from config import *
import time
import hashlib
from django.views.decorators.csrf import *

# Create your views here.
@csrf_exempt
def surl(request):
	
	if request.method == 'GET':
		key = request.GET['q']
		try:
			u = Main.objects.get(surl=key)
			print u
			response = {
				'status' : 'Success',
				'message': 'Found in database.',
				'baseurl': BASE_URL,
				'surl'	 : str(u.surl),
				'id'	 : int(u.id),
				'furl'	 : str(u.furl)
			}
			return HttpResponse(json.dumps(response))
		except:
			response = {
				'status'	:	'Failed',
				'message'	:	"Sorry url doesn't exist. Please get the shorten url."
			}
			return HttpResponse(json.dumps(response))



	if (request.method == 'POST'):
		print request.POST.get('url')
		url = request.POST.get('url')
		print url
		dict = []
		for_check = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
		string = ''
		try:
			u=Main.objects.get(furl=url)
			print u
			response = {
				'status' : 'Success',
				'message': 'Already exist in database.',
				'baseurl': BASE_URL,
				'surl'	 : str(u.surl),
				'id'	 : int(u.id),
				'furl'	 : str(u.furl)
			}
			return HttpResponse(json.dumps(response))
		except:
			try:
				u = Main.objects.create(furl=url)
				u.save()
				print u
				u = Main.objects.get(furl=url)
				id = int(u.id)
				print id
			except:
				response = {
					'status'	:	'Failed',
					'message'	:	"Sorry internal error. Try again later."
				}
				return HttpResponse(json.dumps(response))
			while id :
				r = id%62
				dict.append(r)
				id = id/62
			dict = dict[::-1]
			for i in dict:
				string = string + str(for_check[i])
			print string
			try :
				u.surl = string
				u.save()
				response = {
					'status' : 'Success',
					'message': 'Added to the database.',
					'baseurl': BASE_URL,
					'surl'	 : str(u.surl),
					'id'	 : int(u.id),
					'furl'	 : str(u.furl)
				}
				return HttpResponse(json.dumps(response))
			except:
				response = {
					'status'	:	'Failed',
					'message'	:	"Sorry internal error. Try again later."
				}
				return HttpResponse(json.dumps(response))
