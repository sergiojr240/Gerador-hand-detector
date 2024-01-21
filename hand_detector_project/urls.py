"""
URL configuration for hand_detector_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from hand_detector.controllers import HandLandmarksRestController
from hand_detector.views import SelectMethodView

urlpatterns = [    
    path('detect_hand_landmarks/', HandLandmarksRestController.as_view(), name='detect_hand_landmarks'),
    path('select_method/', SelectMethodView.as_view(), name='select_method'),
    
]

