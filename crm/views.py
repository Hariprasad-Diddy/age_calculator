from os import times
from django.shortcuts import render
from datetime import datetime,timedelta,date
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from decimal import Decimal
# Create your views here.

@api_view(['POST'])
def age_calculator(request):
    if request.method == "POST":
        start_year = request.data.get("start_year")
        start_month = request.data.get("start_month")
        start_date = request.data.get("start_date")
        end_year = request.data.get("end_year")
        end_month = request.data.get("end_month")
        end_date = request.data.get("end_date")

        days_in_year = 365.2425
        hm_years = int((date(int(end_year),int(end_month),int(end_date)) - date(int(start_year),int(start_month),int(start_date))).days / days_in_year)
        hm_months = round(int((date(int(end_year),int(end_month),int(end_date)) - date(int(start_year),int(start_month),int(start_date))).days) / 30.5)
        hm_days = int((date(int(end_year),int(end_month),int(end_date)) - date(int(start_year),int(start_month),int(start_date))).days)
        months = int(hm_months - 12*hm_years)
        days = int(end_date)-int(start_date)
        weeks = str(int(hm_days) * 0.142857)
        hours = int(hm_days)*24
        minutes = int(hm_days)*24*60
        seconds = int(hm_days)*24*60*60
        dec = Decimal(weeks)%1
        b = round(float(dec) / 0.142857)
        return HttpResponse("{} Years {} months {} days \n or {} Months {} days \n {} weeks {} days \n or {} days \n or {} Hours \n or {} Minutes \n or {} Seconds".format(
            hm_years,months,days,
            hm_months,days,
            weeks.split('.')[0],b,
            hm_days,
            hours,
            minutes,
            seconds))