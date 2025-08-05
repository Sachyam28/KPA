from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer, BogieChecksheetSerializer
from .models import BogieChecksheet

# Create your views here.


@api_view(['POST'])
def create_wheel_spec(request):
    serializer = WheelSpecificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "submittedBy": serializer.data['submittedBy'],
                "submittedDate": serializer.data['submittedDate'],
                "status": "Saved"
            }
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_bogie_checksheet(request):
    serializer = BogieChecksheetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "inspectionBy": serializer.data['inspectionBy'],
                "inspectionDate": serializer.data['inspectionDate'],
                "status": "Saved"
            }
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_wheel_spec_filtered(request):
    formNumber = request.GET.get('formNumber')
    submittedBy = request.GET.get('submittedBy')
    submittedDate = request.GET.get('submittedDate')

    filters = {}
    if formNumber:
        filters['formNumber'] = formNumber
    if submittedBy:
        filters['submittedBy'] = submittedBy
    if submittedDate:
        filters['submittedDate'] = submittedDate

    qs = WheelSpecification.objects.filter(**filters)
    serializer = WheelSpecificationSerializer(qs, many=True)
    return Response({
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": serializer.data
    })