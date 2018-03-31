# -*- coding: utf8 -*-
from django.db import models

# Models are the truth of your data inside the application.
# They represent the entities inside your application, the database.

# Product Model:
# This represents a a product for all the application
# from this class, django builds the database table.

class Product(models.Model):
    id_user = models.CharField(max_length=10, verbose_name=u'Id Usuario ')
    name = models.CharField(max_length=120, verbose_name=u'Nombre del Producto ')
    description = models.TextField(max_length=240, help_text=(u'Escriba en menos de 240'
                                                              + u' carácteres la descripción del producto.'), verbose_name=u'Descripción ')



    def __string__(self):
        return (self.name
                + "\nDescripción: " + self.description
                + "\nCantidad: " + self.stock)
