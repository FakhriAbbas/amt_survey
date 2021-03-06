from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pre_survey', views.pre_survey_view, name='pre_survey'),
    path('mental_model', views.mental_model_view, name='mental_model'),
    path('part_3_directions', views.part_3_directions_view, name='part_3_directions'),
    path('session_1', views.session_1_view, name='session_1'),
    path('session_2', views.session_2_view, name='session_2'),
    path('post_survey', views.post_survey_view, name='post_survey'),
    path('thank_you', views.thank_you_view, name='thank_you'),
    path('save_pre_survey', views.save_pre_survey, name='save_pre_survey'),
    path('save_mental_model', views.save_mental_model, name='save_mental_model'),
    path('save_session_1', views.save_session_1, name='save_session_1'),
    path('save_session_2', views.save_session_2, name='save_session_2'),
    path('save_post_survey', views.save_post_survey, name='save_post_survey'),

    path('mental_model_1', views.mental_model_1_view, name='mental_model_1'),
    path('save_mental_model_1', views.save_mental_model_1, name='save_mental_model_1'),
    path('mental_model_2', views.mental_model_2_view, name='mental_model_2'),
    path('save_mental_model_2', views.save_mental_model_2, name='save_mental_model_2'),
    path('mental_model_3', views.mental_model_3_view, name='mental_model_3'),
    path('save_mental_model_3', views.save_mental_model_3, name='save_mental_model_3'),
    path('mental_model_4', views.mental_model_4_view, name='mental_model_4'),
    path('save_mental_model_4', views.save_mental_model_4, name='save_mental_model_4'),
    path('mental_model_5', views.mental_model_5_view, name='mental_model_5'),
    path('save_mental_model_5', views.save_mental_model_5, name='save_mental_model_5'),

    path('get_book_details', views.get_book_details, name='get_book_details'),


]