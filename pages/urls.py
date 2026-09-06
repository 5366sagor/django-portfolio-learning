from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('portfolio/', views.portfolio, name="portfoilo"),
    path('portfolio/<int:skill_id>/', views.portfolio_detail, name='portfolio_detail')
]