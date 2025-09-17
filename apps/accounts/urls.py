from django.urls import path
from apps.accounts.views import RegisterCreateView, LoginFormView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    # path('profile/', RegisterCreateView.as_view, name='register'),
    # path('verification/', RegisterCreateView.as_view, name='register'),
    # path('resend/code/', RegisterCreateView.as_view, name='register'),
    # path('forget/password', RegisterCreateView.as_view, name='register'),
    # path('update/password', RegisterCreateView.as_view, name='register'),
]