from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def client(request):
    if request.method == 'GET':
        client_info = {
            'id': 1,
            'first_name': 'John',
            'last_name': 'Doe',
            'address': '123 Main St',
            'phone_number': '555-1234',
            'email': 'john.doe@example.com',
        }
        return JsonResponse(client_info)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(["GET", "POST"])
def cleaner(request):
    if request.method == 'GET':
        cleaner_info = {
            'id': 1,
            'first_name': 'Jane',
            'last_name': 'Smith',
            'gender': 'F',
            'age': 30,
            'experience': '5 years',
        }
        return JsonResponse(cleaner_info)
    else:
        return HttpResponseBadRequest('Invalid request method')


@require_http_methods(["GET", "POST"])
def apartment(request):
    if request.method == 'GET':
        apartment_info = {
            'id': 1,
            'address': '123 Main St',
            'size': '1000 sqft',
            'bedrooms': 2,
            'bathrooms': 1.5,
            'occupants': ['John Doe', 'Jane Smith'],
        }
        return JsonResponse(apartment_info)
    else:
        return HttpResponseBadRequest('Invalid request method')