from rest_framework import viewsets, mixins
from core import models
from core import serializers
from django.db.utils import IntegrityError
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status

class IpGeoEntryViewset(viewsets.GenericViewSet,
                                mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin):
    queryset = models.IpGeoEntry.objects.all()
    serializer_class = serializers.IPGeoEntrySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IntegrityError:
            raise APIException("Host already exists")
        except KeyError:
            raise APIException("Wrong input data")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
