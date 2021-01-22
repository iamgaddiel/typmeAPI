from django.urls import path
from rest_framework import routers
from api.views import( 
    UserCreateView, 
    PrescriptionView, 
    UserPrescriptionList,
    UserPrescriptionDetail,
)

router = routers.DefaultRouter(trailing_slash=True)
router.register("drugs", PrescriptionView, "prescription")

urlpatterns = [
    path("user/", UserCreateView.as_view(), name='user'),
    path("user/<int:user_id>/drugs/", UserPrescriptionList.as_view(), name="user_drug"),
    path("user/<int:user_id>/drugs/<int:pk>/", UserPrescriptionDetail.as_view(), name="user_drug_detail"),
]

urlpatterns += router.urls


'''
api/user/(GET) (POST)
api/user/:id (GET) (PUT) (DELETE)

api/user/:user_id/drugs/ (GET) (POST)
api/user/:user_id/drugs/:prescription_id (GET) (DELETE)
'''

