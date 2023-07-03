import uuid

import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.utils import json

from location.locationserializer import LocationSerializer

accesstoken = 'fsq38jf5s6BtxsM5GasJ/3pdhr7HlOSL2O6cjpiwegCvd90='


@api_view(['POST'])
def create_location(request):
    try:
        locations = get_locations_from_four_square(request)
        response = []

        # Parse the JSON data
        data = json.loads(locations.content.decode('utf-8'))
        # Access the "results" array
        locations = data.get('results', [])
        for location in locations:
            model_data = four_json_to_location_data(location)
            serializer = LocationSerializer(data=model_data)
            if serializer.is_valid():
                serializer.save()
                response.append(serializer.data)
        return JsonResponse(response, safe=False)
    except APIException as e:
        print(f"APIException: {str(e)}")
        return JsonResponse({'error': 'Error occurred while fetching data from FourSquare.'}, status=500)


def four_json_to_location_data(four_json):
    model_data = {
        'fsq_id': uuid.uuid4(),
        'latitude': float(four_json['geocodes']['main']['latitude']),
        'longitude': float(four_json['geocodes']['main']['longitude']),
        'address': four_json['location']['address'],
        'country': four_json['location']['country'],
        'region': four_json['location']['region'],
        'name': four_json['name'],
    }
    return model_data


def get_locations_from_four_square(request):
    url = "https://api.foursquare.com/v3/places/search"

    params = {
        "ll": request.data.get("latitude") + ',' + request.data.get("longitude"),
    }

    headers = {
        "Accept": "application/json",
        "Authorization": accesstoken
    }

    response = requests.request("GET", url, params=params, headers=headers)

    return response
