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
        day = int(request.data['day'])
        month = int(request.data['month'])
        year = int(request.data['year'])

        # age = Age(year, month, day)
        # age = age.calculate()
        today = datetime.date.today()
        try:
            dob = datetime.date(year, month, day)
            age = int((today-dob).days / 365.25)
            return Response(age)

        except ValueError:
            error = "please enter your DOB correctly."

            return Response(error)
            

        
        

def home(request):
    return render(request, 'core/index.html')