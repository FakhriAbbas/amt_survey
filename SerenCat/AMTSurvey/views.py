from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    context = {
    }
    return render(request, 'AMTSurvey/index.html', context)

def pre_survey_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/pre_survey.html', context)

def mental_model_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/mental_model.html', context)

def part_3_directions_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/part_3_directions.html', context)

def session_1_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/session_1.html', context)

def session_2_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/session_2.html', context)

def post_survey_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/post_survey.html', context)

def thank_you_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/thank_you.html', context)
