import random2
import string
from django.utils.text import slugify


def random_string_generator(size=None, chars=string.ascii_letters + string.digits):
    return ''.join(random2.choice(chars) for i in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    klass = instance.__class__

    if klass.objects.filter(slug=slug).exists():
        new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


