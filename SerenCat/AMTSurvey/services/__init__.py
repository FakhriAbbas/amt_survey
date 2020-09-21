from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string
import pickle
from django.templatetags.static import static
import json, requests
from django.core.cache import cache
import numpy

def save_pre_survey_data(request, q1, q2, q3):
    user_id = request.session.get('USER_ID')
    content = q1 + ';' + q2 + ';' + q3
    default_storage.save('./data/results/' +  str(user_id) + '/pre_survey' , ContentFile(content))

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = result_str.upper()
    return result_str

def get_books_mental_model(request):
    user_id = request.session.get('USER_ID')
    pkl_file = default_storage.open('./data/pickles/clusters_to_isbn.pkl' , mode='rb')
    cluster_isbn_dict = pickle.load(pkl_file)
    books_dict = pickle.load(default_storage.open('./data/pickles/books_dict.pkl', mode='rb'))
    book_list = dict()
    for i in range(0,20):
        isbn_ = random.choice(cluster_isbn_dict[i])
        title, description, url = get_isbn_details(isbn_, books_dict)
        book_list[i] = {
                        'isbn' : isbn_ ,
                        'title' : title,
                        'description' : description,
                        'image_url' : url
                        }
    return book_list

def get_isbn_details(isbn, books_dict):
    image_url = get_book_url(isbn)
    title = books_dict[isbn][0]
    description = books_dict[isbn][1]
    return title, description, image_url

def get_book_url(isbn):
    default_image_url = 'default'
    return default
    google_api_url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + str(isbn)
    r = requests.get(google_api_url)
    data = json.loads(r.text)
    image_url = default_image_url
    if ('totalItems' in data) and (data['totalItems'] == 0):
        pass
    else:
        if 'items' in data:
            if len(data['items']) > 0:
                if 'volumeInfo' in data['items'][0]:
                    if 'imageLinks' in data['items'][0]['volumeInfo']:
                        if 'smallThumbnail' in data['items'][0]['volumeInfo']['imageLinks']:
                            image_url = data['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']
    return image_url

def save_mental_model_response(request, result, page):
    user_id = request.session.get('USER_ID')
    tokens = result.split(';')[:-1]
    cluster_interest_list = list()
    cluster_familiar_list = list()
    for resp in tokens:
        if len(resp.split('-')) > 1:
            values = resp.split('-')
            cluster_id = values[0]
            cluster_v = values[1]
            if cluster_v == 'interest':
                cluster_interest_list.append(cluster_id)
            elif cluster_v == 'familiar':
                cluster_familiar_list.append(cluster_id)
            cluster_isbn = values[2]
    default_storage.save('./data/results/' +  str(user_id) + '/mental_model_response_' + str(page), ContentFile(result))
    if 'familiar_cluster' in request.session:
        request.session['familiar_cluster'].append(cluster_familiar_list)
    else:
        request.session['familiar_cluster'] = cluster_familiar_list
    if 'interest_cluster' in request.session:
        request.session['interest_cluster'].append(cluster_interest_list)
    else:
        request.session['interest_cluster'] = cluster_interest_list

def get_familiar_book(request, familiar_list):
    user_id = request.session.get('USER_ID')
    relevance_book_dict = pickle.load(default_storage.open('./data/pickles/relevance_books.pkl', mode='rb'))
    book_list = list()
    for element in range(0,10):
        cluster_idx = element % len(familiar_list)
        cluster_id = int(familiar_list[cluster_idx])
        relevance_book_dict[cluster_id][element]['cluster_id'] = cluster_id
        book_list.append(relevance_book_dict[cluster_id][element])
    return book_list

def get_interest_cluster(request):
    return parse_response(request, 'interest')

def parse_response(request, condition):
    user_id = request.session.get('USER_ID')
    c_list = list()
    for i in range(1,6):
        c_file = default_storage.open('./data/results/' + str(user_id) + '/' + 'mental_model_response_' + str(i), mode='r')
        c_response = c_file.readline()
        response = c_response.split(';')[:-1]
        for r in response:
            if r.split('-')[1] == condition:
                c_list.append(r.split('-')[0])
        c_file.close()
    return c_list

def get_familiar_cluster(request):
    return parse_response(request, 'familiar')

def get_interest_book(request, interest_list):
    user_id = request.session.get('USER_ID')
    interest_book_dict = pickle.load(default_storage.open('./data/pickles/interest_books.pkl', mode='rb'))
    book_list = list()
    for element in range(0,10):
        cluster_idx = element % len(interest_list)
        cluster_id = int(interest_list[cluster_idx])
        interest_book_dict[cluster_id][element]['cluster_id'] = cluster_id
        book_list.append(interest_book_dict[cluster_id][element])
    return book_list


def save_curiosity_session(request, result, session_number):
    user_id = request.session.get('USER_ID')
    # tokens = result.split(';')[:-1]
    # # for resp in tokens:
    # #     if len(resp.split('-')) > 1:
    # #         values = resp.split('-')
    # #         cluster_id = values[0]
    # #         cluster_v = values[1]
    # #         isbn_ = values[2]
    default_storage.save('./data/results/' +  str(user_id) + '/save_session_' + str(session_number) , ContentFile(result))

def save_post_survey_data(request, q1, q2, q3):
    user_id = request.session.get('USER_ID')
    content = q1 + ';' + q2 + ';' + q3
    default_storage.save('./data/results/' +  str(user_id) + '/post_survey' , ContentFile(content))

def get_books_mental_model_per_page(request, page):
    user_id = request.session.get('USER_ID')
    cluster_books_dict = pickle.load(default_storage.open('./data/pickles/clusters_book.pkl', mode='rb'))
    result = {}
    for counter, element in enumerate(cluster_books_dict.items()):
        if ( counter >= (8*(page-1)) ) & ( counter < (page*8) ):
            key, value = element[0] , element[1]
            result[key] = value
        else:
            continue

    print( len(list(result.keys())) )
    print(page)
    return result

