from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'ishan',
        'rohan',
        'mukesh'
    ]
    return JsonResponse(friends,safe=False)