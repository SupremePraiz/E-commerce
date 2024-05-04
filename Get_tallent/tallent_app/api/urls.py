from django.urls import path
from .views import (ContractorList, ContractorDetail, EmployerList, EmployerDetail, JobPostList, JobpostDetail,
                    CommentList, CommentDetail, CommentCreate)


urlpatterns = [
  path("contractor/", ContractorList.as_view(), name="contractor_list"),
  path("contractor/<int:pk>/detail/", ContractorDetail.as_view(), name="contractor_detail"),
  
  path("employer/", EmployerList.as_view(), name="employer_list"),
  path("employer/<int:pk>/detail/",EmployerDetail.as_view(), name="employer_detail"),
  
  path("job/",JobPostList.as_view(), name="job_list"),
  path("job/<int:pk>/detail/",JobpostDetail.as_view(), name="job_detail"),
  
  path("comment-list/<int:pk>/",CommentList.as_view(), name="comment_list"),
  path("job/<int:pk>/comment-create/",CommentCreate.as_view(), name="comment_create"),
  path("comment/<int:pk>/detail/",CommentDetail.as_view(), name="comment_detail")
]



