from django.http import request
from django.shortcuts import render

# Create your views here.
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')
