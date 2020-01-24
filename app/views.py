from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from app import models, serializers


class ImageGallery(viewsets.ModelViewSet):
    queryset = models.ImageGallery.objects.all()
    serializer_class = serializers.ImageGallery


class Image(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.Image


class Hotel(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.Hotel


class HotelRoom(viewsets.ModelViewSet):
    queryset = models.HotelRoom.objects.all()
    serializer_class = serializers.HotelRoom


class RentingCenter(viewsets.ModelViewSet):
    queryset = models.RentingCenter.objects.all()
    serializer_class = serializers.RentingCenter


class Rental(viewsets.ModelViewSet):
    queryset = models.Rental.objects.all()
    serializer_class = serializers.Rental


class MedicalFacility(viewsets.ModelViewSet):
    queryset = models.MedicalFacility.objects.all()
    serializer_class = serializers.MedicalFacility


class MedicalService(viewsets.ModelViewSet):
    queryset = models.MedicalService.objects.all()
    serializer_class = serializers.MedicalService


class Trip(viewsets.ModelViewSet):
    queryset = models.Trip.objects.all()
    serializer_class = serializers.Trip


class Activity(viewsets.ModelViewSet):
    queryset = models.Activity.objects.all()
    serializer_class = serializers.Activity


class Order(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.Order


class OrderedActivity(viewsets.ModelViewSet):
    queryset = models.OrderedActivity.objects.all()
    serializer_class = serializers.OrderedActivity


def search(request):
    """Search API
    This query is supposed to use an NLP-based engine to parse user's query and look for services that would match that.
    However, our professor deemed the analysis and design of such a section too complicated for the purposes of this
    course and therefore, the call was reduced to a simple database search.
    """
    query = request.GET.get('query', None)
    if query is None:
        response = HttpResponse(status=200)
        response.write('To search within the available trips, send your query as a <b>GET</b> request to this page.<br>')
        response.write('The response contains a JSON object containing an attribute by the key <b>trips</b>. ')
        response.write('The attribute contains the primary keys of the trips matching your query.')
        return response
    trips = models.Trip.objects.filter(description__contains=query, available=True).values_list('id', flat=True)
    return JsonResponse({'trips': list(trips)})
