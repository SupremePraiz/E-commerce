from rest_framework import serializers

from tallent_app.models import Contractor, Employer, JobPost, Comment

class ContactorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Contractor
        fields = "__all__"
        

class EmployerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Employer
        fields = "__all__"
        
class JobPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = JobPost
        fields = "__all__"
        
        
        
class CommentSerializer(serializers.ModelSerializer):
    comments = JobPostSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    jobpost = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = "__all__"
        