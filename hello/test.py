from models import Sight


sights = Sight.objects.get(country = "Германия")
print(sights)