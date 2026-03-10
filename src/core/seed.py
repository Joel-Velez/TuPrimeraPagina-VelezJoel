from faker import Faker

from core.models import Cargo, Empleado, Tarea

fake = Faker()

def run_seed():
    seed_cargos()
    seed_empleados()
    seed_tareas()

def seed_cargos():
    for _ in range(10):
        Cargo.objects.create(cargo=fake.job(), salario=fake.random_int(min=100, max=1000), descripcion=fake.text())
        
def seed_empleados():
    for _ in range(100):
        Empleado.objects.create(
            nombre=fake.first_name(),
            apellido=fake.last_name(),
            email=fake.email(),
            fecha_nacimiento=fake.date(),
            fecha_de_ingreso=fake.date(),
            cargo=Cargo.objects.order_by('?').first()
        )
        
def seed_tareas():
    for _ in range(300):
        Tarea.objects.create(
            nombre=fake.job(),
            descripcion=fake.text(),
            empleado=Empleado.objects.order_by('?').first()
        )