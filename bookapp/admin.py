from django.contrib import admin
from . models import Book, Author, Period, Text

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Period)
admin.site.register(Text)
