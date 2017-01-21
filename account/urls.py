from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # login view
    # url(r'^login/$', views.user_login, name='login'),

    # login / logout urls

    url(r'^login/$',
        auth_views.login,
        {'template_name': 'account/login.html'},
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'account/logged_out.html'},
        name='logout'),
    url(r'^logout-then-login/$',
        auth_views.logout_then_login,
        {'template_name': 'account/login.html'},
        name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),

]
