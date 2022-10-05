from xml.etree.ElementInclude import include
from django.urls import path
from .merit_views import(
    MeritMainPageView,
    ManageClassesView,
    ManageScoresView,
    ManageStudentsView,
    MeritExplanationView,
    ManageRecordsView,
    ViewScoresView,
    ClassStudentsView,
)

from .merit_api_views import ( 
    GetTeacherInfoAPIView,
    

)
urlpatterns = [

    path('', MeritMainPageView.as_view(), name='merit-main-page'),
    path('manage_classes/',ManageClassesView.as_view(), name='manage-classes'),
    path('manage_scores/',ManageScoresView.as_view(), name='manage-scores'),
    path('manage_students/',ManageStudentsView.as_view(), name='manage-students'),
    path('merit_explanation/', MeritExplanationView.as_view(), name='merit-explanation'),
    path('manage_records/', ManageRecordsView.as_view(), name="my-records"),
    path('manage_students/<int:id>', ViewScoresView.as_view(), name='view-scores'),
    

    
    path('manage_students/class_students/<int:id>', ClassStudentsView.as_view(), name="class-students"),

    path('api/get_teacher_info', GetTeacherInfoAPIView.as_view(), name='get-teacher-info'),
    path('api/get_teacher_info/<int:id>', GetTeacherInfoAPIView.as_view(), name='get-teacher-info-id'),
]