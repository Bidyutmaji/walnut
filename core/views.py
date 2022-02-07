import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Age:
    def __init__(self, y, m, d):
        self.y = int(y)
        self.m = int(m)
        self.d = int(d)
    
    def calculate(self):
        today = datetime.date.today()
        dob = datetime.date(self.y, self.m, self.d)
        age = int((today-dob).days / 365.25)
        return age



class AgeView(APIView):

    def post(self, request, format=None):
        day = request.data['day']
        month = request.data['month']
        year = request.data['year']

        age = Age(year, month, day)
        age = age.calculate()

        return Response(age)

def home(request):
    return render(request, 'core/index.html')