'''


This views will be used as API 
to retreive data from Heroku DB which contains 
info about users. 

The reasons is simple. Free Heroku does not allow
cross DB data sharing.


'''

from rest_framework import generics
from all_apps.User.models import CustomUser
from .merit_serializers import TeacherInfoSerializer
from rest_framework.response import Response


class GetTeacherInfoAPIView(generics.GenericAPIView):

    queryset = CustomUser.objects.all()
  
    serializer_class = TeacherInfoSerializer
    permission_classes = []
    authentication_classes = []
    
    def get(self, request, *args, **kwargs):

        teacherId = kwargs.get("id")
        
        qs = CustomUser.objects.get(id=teacherId)    
        
        serialized_data = TeacherInfoSerializer(qs, many=False) 
        
        return Response(serialized_data.data)

