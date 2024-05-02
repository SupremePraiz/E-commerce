from django.urls import path
from .views import (ContractorList, ContractorDetail, EmployerList, EmployerDetail, JobPostList, JobpostDetail,
                    CommentList, CommentDetail)


urlpatterns = [
  path("contractor/", ContractorList.as_view(), name="contractor_list"),
  path("contractor/<int:pk>/", ContractorDetail.as_view(), name="contractor_detail"),
  
  path("employer/", EmployerList.as_view(), name="employer_list"),
  path("employer/<int:pk>/",EmployerDetail.as_view(), name="employer_detail"),
  
  path("job/",JobPostList.as_view(), name="job_list"),
  path("job/<int:pk>/",JobpostDetail.as_view(), name="job_detail"),
  
  path("comment/",CommentList.as_view(), name="comment_list"),
  path("comment/<int:pk>",CommentDetail.as_view(), name="comment_detail")
]



