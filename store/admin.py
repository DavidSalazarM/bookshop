from django.contrib import admin
from .models import Author, Publisher, Book

models = [Author, Publisher, Book]

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

