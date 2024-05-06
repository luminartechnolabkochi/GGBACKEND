from django.shortcuts import render

from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.generics import CreateAPIView

from rest_framework import status

from rest_framework.decorators import action


from api.serializers import JobSerializer,JobCardSerializer

from api.models import JobCard,Jobs




class JobCardViewSet(viewsets.ModelViewSet):

    serializer_class=JobCardSerializer

    queryset=JobCard.objects.all()


    @action(methods=["post"],detail=True)
    def add_job(self,request,*args,**kwargs):

        job_card_object=self.get_object()

        serializer_instance= JobSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(job_card_object=job_card_object)

            return Response(data=serializer_instance.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    

