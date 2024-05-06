from rest_framework import serializers

from api.models import Jobs,JobCard


class JobSerializer(serializers.ModelSerializer):



    class Meta:

        model=Jobs

        fields =  "__all__"

        read_only_fields=["id","job_card_object"]




class JobCardSerializer(serializers.ModelSerializer):

    
    class Meta:

        model = JobCard

        fields = "__all__"

        read_only_fields = ["id","status","created_date","job"]
    
    jobs=JobSerializer(many=True,read_only=True)

    total_amount=serializers.CharField(read_only=True)


