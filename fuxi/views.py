from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

class Query(View):
    def get(self, request, method):
        if method == 'getdata':
            resp = [
            { "dbname": "Foo", "tables": ["table1", "table2"] },
            { "dbname": "Bar", "tables": ["table1", "table2", "table2"] }
          ]
            return HttpResponse(json.dumps(resp), content_type="application/json")

def index(request):
    return render(request,'pages/index.html')

