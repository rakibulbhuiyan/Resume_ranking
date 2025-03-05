
from django.contrib import admin
from django.urls import path
from checkresume.views import JobDescriptionApi,AnalyzeResumeAPI

urlpatterns = [
    path('api/job-description/', JobDescriptionApi.as_view()),
    path('api/analyze-resume/', AnalyzeResumeAPI.as_view()),
    path('admin/', admin.site.urls),
]
