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
    url(r'^password-change/$',
        auth_views.password_change,
        {'template_name': 'account/password_change.html'},
        name='password_change'),
    url(r'^password-change/done/$',
        auth_views.password_change_done,
        {'template_name': 'account/password_change_done.html'},
        name='password_change_done'),
    url(r'^password-reset/$',
        auth_views.password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name='password_reset'),
    url(r'^password-reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)$',
        auth_views.password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^register/$',
        views.register,
        # {'template_name': 'registration/register.html'},
        name='register'),
]
