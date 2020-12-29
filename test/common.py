'''
Created on 15-May-2020

@author: Aman_
'''

def success_Response(request):
   return {'status':"0",'statusMessage':"success","data": request}

def failure_Response(request):
    return {'status':"1",'statusMessage':"failure","data": request}
