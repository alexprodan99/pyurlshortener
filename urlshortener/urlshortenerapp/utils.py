from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, 'MAXIMUM_URL_CHARS', 7)

AVAILABLE_CHARS = ascii_letters + digits

def _create_random_code(chars=AVAILABLE_CHARS):
    return ''.join([choice(chars) for _ in range(SIZE)])

def create_short_url(model):
    random_code = _create_random_code()

    model_class = model.__class__
    
    # if short url was already generated rerun create_short_url to generate a new one random code
    if model_class.objects.filter(short_url=random_code).exists():
        return create_short_url(model)

    return random_code

