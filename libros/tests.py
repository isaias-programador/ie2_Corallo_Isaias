from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import libros

class LibroEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.libro = libros.objects.create(titulo='Libro de prueba', genero='Género de prueba')

    def test_obtener_detalles_libro(self):
        url = reverse('libros-detail', args=[self.libro.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Revisa que los datos del libro que trae sean iguales a los datos del libro creado.

    def test_agregar_libro(self):
        url = reverse('libros-list')
        data = {'titulo': 'Nuevo libro', 'genero': 'Nuevo género'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Revisa que el libro se haya creado correctamente en la base de datos

    def test_actualizar_libro(self):
        url = reverse('libros-detail', args=[self.libro.id])
        data = {'titulo': 'Título actualizado', 'genero': 'Género actualizado'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Revisa que el libro se hayan actualizado las modificaciones correctamente en la base de datos

    def test_eliminar_libro(self):
        url = reverse('libros-detail', args=[self.libro.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Revisa que el libro se haya borrado correctamente de la base de datos