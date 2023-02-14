from django.http import JsonResponse
from .models import Drink
from .serializer import DrinkSerializer

def drink_list(request):
    
    #get all drinks
    #serialize them 
    #return jason list of the drinks

    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)

    return JsonResponse({'drinks' : serializer.data})