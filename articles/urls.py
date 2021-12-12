from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path("", views.articles, name="all"),
    path("create-article", views.create_article, name='create'),
    path("delete/<int:id>/", views.delete_article, name='delete'),
    path("<int:id>/", views.article_details, name="details"),
]
