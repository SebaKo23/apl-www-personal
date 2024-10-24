## Demonstracja działania serializerów 
### Listing do wykorzystania w shellu Pythona:

```python
from polls.models import Osoba, Stanowisko
from polls.serializers import OsobaSerializer, StanowiskoModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# ///
# Test serializera nr 1
# ///
osoba = Osoba.objects.get(id=1)
serializer = OsobaSerializer(osoba)
serializer.data # weryfikacja danych

# Serializacja do JSON

content = JSONRenderer().render(serializer.data)
content

# Przesłanie obiektu i deserializacja
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = OsobaSerializer(data=data)
deserializer.is_valid() # Walidacja danych

# Zwróciło True, zatem wyświetlamy dane i zapisujemy:
deserializer.validated_data
deserializer.save()

# ///
# Test serializera nr 2
# ///
stanowisko = Stanowisko.objects.get(id=1)
serializer = StanowiskoModelSerializer(stanowisko)
serializer.data # weryfikacja danych

# Serializacja do JSON

content = JSONRenderer().render(serializer.data)
content

# Przesłanie obiektu i deserializacja
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = StanowiskoModelSerializer(data=data)
deserializer.is_valid() # Walidacja danych

# Zwróciło True, zatem wyświetlamy dane i zapisujemy:
deserializer.validated_data
deserializer.save()
```