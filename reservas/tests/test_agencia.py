from django.test import TestCase, Client
from django.urls import reverse
from reservas.models.agencia import Agencia
from usuarios.models import Usuario


class AgenciaUnitTest(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create_superuser(
            'admin', 'admin@test.com', 'admin', ci = '00110367543'
        )

        self.agencia = Agencia.objects.create(
            nombre = 'Agencia test',
            provincia = 'provincia test',
            telefono = '11036743',
            direccion = 'direccion test',
        )
    
    def test_model(self):
        # Configura el objeto de prueba
        agencia = Agencia.objects.first()
        self.assertEqual(agencia.nombre, 'Agencia test')
        self.assertEqual(agencia.telefono, '11036743')

class agenciaTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.client = Client()
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

        Agencia.objects.create(
            nombre = 'Agencia test',
            provincia = 'provincia test',
            telefono = '11036743',
            direccion = 'direccion test',
        )
        Agencia.objects.create(
            nombre = 'Agencia test 2',
            provincia = 'provincia test 2',
            telefono = '11036741',
            direccion = 'direccion test 2',
        )
        
    def test_get_ok(self):
        self.client.login(username='admin', password='admin')
        
        # Obtener la URL de la vista
        url = reverse('lista_agencias')
        # Realizar la solicitud GET a la vista
        response = self.client.get(url)
        # Verificar que la respuesta es 200 OK
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se esté utilizando
        self.assertTemplateUsed(response, 'agencias/lista_agencias.html')
        # Verificar que los usuarios estén en el contexto de la respuesta
        agencias_en_contexto = response.context['agencias']
        self.assertEqual(len(agencias_en_contexto), 2)
        # Verificar que los datos de los usuarios estén en el contenido de la respuesta
        self.assertContains(response, 'Agencia test 2')
        self.assertContains(response, 'Agencia test')
        
    def test_form_post(self):
        self.client.login(username='admin', password='admin')
        
        # Aquí debes definir los datos que enviarás en la petición POST
        data = {
            'nombre': 'Agencia test 4',
            'provincia': 'provincia test 4',
            'telefono': '11036741',
            'direccion': 'direccion test 4',
        }
        
        # Utiliza reverse para obtener la URL basada en el nombre de la vista
        url = reverse('agregar_agencia')
        urlr = reverse('lista_agencias')
        
        # Realiza la petición POST con el cliente de prueba
        response = self.client.post(url, data)
        
        # Aquí verificar la respuesta
        # Verificar que la respuesta redirige a la URL correcta
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, urlr)
        
        # Verifica que se creo correctamente en la base de datos
        objeto_creado = Agencia.objects.filter(telefono='11036741').exists()
        self.assertTrue(objeto_creado)
        
    def test_form_put(self):
        self.client.login(username='admin', password='admin')
        
        # Aquí debes definir los datos que enviarás en la petición POST
        data = {
            'nombre': 'Agencia test 3',
            'provincia': 'provincia test 3',
            'telefono': '11036748',
            'direccion': 'direccion test 3',
        }
        
        # Utiliza reverse para obtener la URL basada en el nombre de la vista
        url = reverse('editar_agencia', args=[1])
        urlr = reverse('lista_agencias')
        
        # Realiza la petición POST con el cliente de prueba
        response = self.client.post(url, data)
        
        # Aquí verificar la respuesta
        # Verificar que la respuesta redirige a la URL correcta
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, urlr)
        
        # Verifica que se creo correctamente en la base de datos
        objeto_creado = Agencia.objects.filter(telefono='11036748').exists()
        self.assertTrue(objeto_creado)
        
        
    def test_delete(self):
        self.client.login(username='admin', password='admin')
        
        objeto_creado = Agencia.objects.filter(telefono='11036743').first()
        self.assertTrue(objeto_creado)
        
        # Utiliza reverse para obtener la URL basada en el nombre de la vista
        url = reverse('eliminar_agencia', args=[objeto_creado.id])
        urlr = reverse('lista_agencias')
        
        
        # Realiza la petición POST con el cliente de prueba
        response = self.client.post(url)
        
        # Aquí verificar la respuesta
        # Verificar que la respuesta redirige a la URL correcta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, urlr)
        
        # Verifica que se creo correctamente en la base de datos
        objeto_creado = Agencia.objects.filter(telefono='11036743').exists()
        self.assertFalse(objeto_creado)