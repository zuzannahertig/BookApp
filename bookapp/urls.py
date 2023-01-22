from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('teksty', views.texts, name='teksty'),
    path('teksty/<int:text_id>', views.texts_details, name='teksty_szczegol'),
    path('teksty/new', views.texts_new, name='teksty_nowy'),
    path('teksty/update/<int:text_id>', views.texts_update, name='teksty_modyfikuj'),
    path('teksty/delete/<int:text_id>', views.texts_delete, name='teksty_kasuj'),

    path('ksiazki', views.books, name='ksiazki'),
    path('ksiazki/<int:book_id>', views.books_details, name='ksiazki_szczegol'),
    path('ksiazki/new', views.books_new, name='ksiazki_nowy'),
    path('ksiazki/update/<int:book_id>', views.books_update, name='ksiazki_modyfikuj'),
    path('ksiazki/delete/<int:book_id>', views.books_delete, name='ksiazki_kasuj'),

    path('epoki', views.periods, name='epoki'),
    path('epoki/<int:period_id>', views.periods_details, name='epoki_szczegol'),
    path('epoki/new', views.periods_new, name='epoki_nowy'),
    path('epoki/update/<int:period_id>', views.periods_update, name='epoki_modyfikuj'),
    path('epoki/delete/<int:period_id>', views.periods_delete, name='epoki_kasuj'),

    path('autorzy', views.authors, name='autorzy'),
    path('autorzy/<int:author_id>', views.authors_details, name='autorzy_szczegol'),
    path('autorzy/new', views.authors_new, name='autorzy_nowy'),
    path('autorzy/update/<int:author_id>', views.authors_update, name='autorzy_modyfikuj'),
    path('autorzy/delete/<int:author_id>', views.authors_delete, name='autorzy_kasuj'),

    path('wykresy/<int:text_id>', views.get_image, name='get_image'),
    path('predictions/<int:book_id>', views.get_predictions, name='predictions'),

    path('projekt', views.project, name='projekt'),
]
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
