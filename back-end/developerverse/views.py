from rest_framework import generics
from rest_framework import permissions
from .models import Project, Website
from .serializers import ProjectSerializer, WebsiteSerializer

# Create your views here.

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # Only Users that are authenticated and have the the requisite permissions 
    # defined in Django's standrard model permissions will be able to edit the
    # entry 
    permission_classes = (permissions.DjangoModelPermissions, )