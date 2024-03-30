import json
from django.core.management.base import BaseCommand
from reservas.models.ruta import Ruta

class Command(BaseCommand):
    help = 'Inserta las provincias de Cuba en la base de datos'

    def handle(self, *args, **options):
        with open('reservas/management/commands/provincias.json', 'r') as f:
            provincias_data = json.load(f)["Provincias"]

        for provincia_data in provincias_data:
            self.stdout.write(self.style.SUCCESS(f'Insertando {provincia_data["nombre"]}'))
            Ruta.objects.create(lugar=provincia_data['nombre'])
            for municipio in provincia_data.get('municipios', []):
                self.stdout.write(self.style.SUCCESS(f'Insertando {municipio}'))
                Ruta.objects.create(lugar=municipio)
                

        self.stdout.write(self.style.SUCCESS('Provincias insertadas exitosamente'))