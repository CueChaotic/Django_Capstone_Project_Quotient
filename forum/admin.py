from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Forum)
admin.site.register(Discussion)

"""The above are used to register the Forum and Discussion models, from the
'models.py' file, in the admin console of the site.

:param Forum: Pertains to the Forum model
:param Discussion: Pertains to the Discussion model
"""
