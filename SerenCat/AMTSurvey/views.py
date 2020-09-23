from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .services import *
from django.core.cache import cache
from django.conf import settings

def index(request):
    if 'USER_ID' not in request.session:
        no_users = len(default_storage.listdir('./data/results')[0])
        if (no_users % 2) == 0:
            request.session['APP_MODE'] = 0
        else:
            request.session['APP_MODE'] = 1
        request.session['USER_ID'] = get_random_string(20) + str(request.session.get('APP_MODE'))

    context = {
    }
    return render(request, 'AMTSurvey/index.html', context)

def pre_survey_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/pre_survey.html', context)

def save_pre_survey(request):
    q1 = request.POST.get("q1", "")
    q2 = request.POST.get("q2", "")
    q3 = request.POST.get("q3", "")

    # save q1, q2, q3
    save_pre_survey_data(request,q1,q2,q3)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_1') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_view(request):
    context = {
    }
    # book_list = get_books_mental_model(request)
    # print(book_list)
    context['books'] = None
    return render(request, 'AMTSurvey/mental_model.html', context)

def save_mental_model(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result)
    response = { 'status' : 1 , 'redirect-url' : reverse('part_3_directions') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def part_3_directions_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/part_3_directions.html', context)

def session_1_view(request):
    context = {
    }
    familiar_list = get_familiar_cluster(request)
    interest_list = get_interest_cluster(request)

    if ( len(familiar_list) == 0 ) | (len(interest_list) == 0 ):
        return render(request, 'AMTSurvey/cant_proceed.html', context)

    if request.session.get('APP_MODE') == 0:
        book_list = get_familiar_book(request, familiar_list)
    else:
        book_list = get_interest_book(request, interest_list)

    context['books'] = book_list
    return render(request, 'AMTSurvey/session_1.html', context)

def session_2_view(request):
    context = {}
    # handle error if familiar and interest are empty

    familiar_list = get_familiar_cluster(request)
    interest_list = get_interest_cluster(request)

    if ( len(familiar_list) == 0 ) | (len(interest_list) == 0 ):
        return render(request, 'AMTSurvey/cant_proceed.html', context)

    if request.session.get('APP_MODE') == 1:
        book_list = get_familiar_book(request, familiar_list)
    else:
        book_list = get_interest_book(request, interest_list)

    context['books'] = book_list
    return render(request, 'AMTSurvey/session_2.html', context)

def post_survey_view(request):
    context = {
    }
    return render(request, 'AMTSurvey/post_survey.html', context)

def thank_you_view(request):
    context = {
        'user_id' : request.session.get('USER_ID')
    }
    del request.session['USER_ID']
    return render(request, 'AMTSurvey/thank_you.html', context)

def save_session_1(request):
    result = request.POST.get("response" , '')
    save_curiosity_session(request, result, 1)
    response = { 'status' : 1 , 'redirect-url' : reverse('session_2') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def save_session_2(request):
    result = request.POST.get("response" , '')
    save_curiosity_session(request, result, 2)
    response = { 'status' : 1 , 'redirect-url' : reverse('post_survey') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def save_post_survey(request):
    q1 = request.POST.get("q1", "")
    q2 = request.POST.get("q2", "")
    q3 = request.POST.get("q3", "")

    # save q1, q2, q3
    save_post_survey_data(request,q1,q2,q3)
    response = { 'status' : 1 , 'redirect-url' : reverse('thank_you') }

    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_1_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 1)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_1.html', context)

def save_mental_model_1(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 1)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_2') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_2_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 2)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_2.html', context)

def save_mental_model_2(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 2)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_3') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_3_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 3)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_3.html', context)

def save_mental_model_3(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 3)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_4') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_4_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 4)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_4.html', context)

def save_mental_model_4(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 4)
    response = { 'status' : 1 , 'redirect-url' : reverse('mental_model_5') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def mental_model_5_view(request):
    context = {
    }
    book_list = get_books_mental_model_per_page(request, 5)
    context['books'] = book_list
    return render(request, 'AMTSurvey/mental_model_5.html', context)

def save_mental_model_5(request):
    result = request.POST.get("response" , '')
    save_mental_model_response(request, result, 5)
    response = { 'status' : 1 , 'redirect-url' : reverse('part_3_directions') }
    return HttpResponse(json.dumps(response), content_type="application/json")

def get_book_details(request):
    isbn = request.POST.get("ISBN", '')
    books_dict = pickle.load(default_storage.open('./data/pickles/books_space_dict.pkl', mode='rb'))
    book = books_dict[isbn]

    response = { 'status' : 1 , 'book_details' : book }
    return render(request, 'AMTSurvey/includes/book_detail_modal.html', {'title' : book['title'], 'desc': book['desc'] , 'image_url': book['image_url']})

