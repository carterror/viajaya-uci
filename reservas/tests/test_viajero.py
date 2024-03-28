from django.test import TestCase, Client
from django.urls import reverse
from reservas.models.viajero import Viajero
from usuarios.models import Usuario

# lista_viajeros
# agregar_viajero
# editar_viajero
# eliminar_viajero
    
class ViajeroUnitTest(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create_superuser(
            'admin', 'admin@test.com', 'admin', ci = '00110367543'
        )
        
        self.viajero = Viajero.objects.create(
            nombre = 'Carlos Brayan',
            ci = '00110367543',
            user = usuario,
        )
    
    def test_model(self):
        # Configura el objeto de prueba
        viajero = Viajero.objects.first()
        self.assertEqual(viajero.nombre, 'Carlos Brayan')
        self.assertEqual(viajero.ci, '00110367543')
        self.assertEqual(viajero.user.username, 'admin')

class ViajeroTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.client = Client()
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

        Viajero.objects.create(
            nombre = 'Carlos Brayan',
            ci = '00110367543',
            user = self.usuario,
        )
        Viajero.objects.create(
            nombre = 'Javier Gonzalez',
            ci = '00110367543',
            user = self.usuario,
        )
        
    def test_get_ok(self):
        self.client.login(username='admin', password='admin')
        
        # Obtener la URL de la vista
        url = reverse('lista_viajeros')
        # Realizar la solicitud GET a la vista
        response = self.client.get(url)
        # Verificar que la respuesta es 200 OK
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se esté utilizando
        self.assertTemplateUsed(response, 'viajeros/lista_viajeros.html')
        # Verificar que los usuarios estén en el contexto de la respuesta
        viajeros_en_contexto = response.context['viajeros']
        self.assertEqual(len(viajeros_en_contexto), 2)
        # Verificar que los datos de los usuarios estén en el contenido de la respuesta
        self.assertContains(response, 'Carlos Brayan')
        self.assertContains(response, 'Javier Gonzalez')
        
    def test_form_post(self):
        self.client.login(username='admin', password='admin')
        
        # Aquí debes definir los datos que enviarás en la petición POST
        data = {
            'ci': '01210598724',
            'nombre': 'Alejandro Santana',
        }
        
        # Utiliza reverse para obtener la URL basada en el nombre de la vista
        url = reverse('agregar_viajero')
        urlr = reverse('lista_viajeros')
        
        # Realiza la petición POST con el cliente de prueba
        response = self.client.post(url, data)
        
        # Aquí verificar la respuesta
        # Verificar que la respuesta redirige a la URL correcta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, urlr)
        
        # Verifica que se creo correctamente en la base de datos
        objeto_creado = Viajero.objects.filter(ci='01210598724', nombre='Alejandro Santana').exists()
        self.assertTrue(objeto_creado)