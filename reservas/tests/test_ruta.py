from django.test import TestCase, Client
from django.urls import reverse
from reservas.models.ruta import Ruta
from usuarios.models import Usuario

class RutaUnitTest(TestCase):
    def setUp(self):
        Ruta.objects.create(
            lugar = 'La Habana',
        )
    
    def test_model(self):
        # Configura el objeto de prueba
        viajero = Ruta.objects.first()
        self.assertEqual(viajero.lugar, 'La Habana')

class ViajeroTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.client = Client()
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')
        
        Ruta.objects.create(
            lugar = 'La Habana',
        )
        
        Ruta.objects.create(
            lugar = 'Las Villas',
        )
                
    def test_get_ok(self):
        self.client.login(username='admin', password='admin')
        
        # Obtener la URL de la vista
        url = reverse('lista_rutas')
        # Realizar la solicitud GET a la vista
        response = self.client.get(url)
        # Verificar que la respuesta es 200 OK
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se esté utilizando
        self.assertTemplateUsed(response, 'ruta/lista_ruta.html')
        # Verificar que los usuarios estén en el contexto de la respuesta
        rutas_en_contexto = response.context['rutas']
        self.assertEqual(len(rutas_en_contexto), 2)
        # Verificar que los datos de los usuarios estén en el contenido de la respuesta
        self.assertContains(response, 'La Habana')
        self.assertContains(response, 'Las Villas')
        
    def test_form_post(self):
        self.client.login(username='admin', password='admin')
        
        # Aquí debes definir los datos que enviarás en la petición POST
        data = {
            'lugar': 'Matanzas'
        }
        
        # Utiliza reverse para obtener la URL basada en el nombre de la vista
        url = reverse('agregar_ruta')
        urlr = reverse('lista_rutas')
        
        # Realiza la petición POST con el cliente de prueba
        response = self.client.post(url, data)
        
        # Aquí verificar la respuesta
        # Verificar que la respuesta redirige a la URL correcta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, urlr)
        
        # Verifica que se creo correctamente en la base de datos
        objeto_creado = Ruta.objects.filter(lugar='Matanzas').exists()
        self.assertTrue(objeto_creado)