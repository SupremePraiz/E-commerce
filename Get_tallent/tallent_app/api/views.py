from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from tallent_app.models import Contractor, Employer, JobPost, Comment
from .serializers import ContactorSerializer, EmployerSerializer, JobPostSerializer, CommentSerializer


'''Contractor Api'''
class ContractorList(generics.ListCreateAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContactorSerializer
    permission_classes = [IsAuthenticated]
    
class ContractorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContactorSerializer
    permission_classes =[IsAuthenticated,IsAdminOrReadOnly]

'''Employer Api'''
class EmployerList(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes =[IsAuthenticated]
    
class EmployerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes =[IsOwnerOrReadOnly]   
    
'''JobPost Api'''
class JobPostList(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    # permission_classes =[IsAuthenticated]
    
class JobpostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes =[IsOwnerOrReadOnly]
    

'''comment Api'''
class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    # permission_classes =[IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(jobpost=pk)
    
    
class CommentCreate(generics.CreateAPIView):
    
    serializer_class = CommentSerializer
    # permission_classes =[IsAuthenticated]
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        jobpost = JobPost.objects.get(pk=pk)
        serializer.save(jobpost=jobpost, user=self.request.user)

    

    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =[IsAdminOrReadOnly]
    
    