
from django.contrib import admin
from django.urls import path
from app.views import TransactionView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TransactionView, name='transaction')
]
