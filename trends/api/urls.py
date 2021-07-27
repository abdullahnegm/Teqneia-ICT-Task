from django.urls import path


from .views import TrendsView

urlpatterns = [
    path('trends/', TrendsView.as_view())
]
