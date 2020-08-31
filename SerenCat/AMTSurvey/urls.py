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


]