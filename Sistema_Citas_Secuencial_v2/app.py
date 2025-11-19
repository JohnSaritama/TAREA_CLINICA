import csv
from modelos.administrativo import Administrativo
from repos.repo_administrativo import AdministrativoRepo
from servicios.administrativo_servicio import AdministrativoServicio

from datetime import date, time

from modelos.paciente import Paciente
from modelos.doctor import Doctor

from repos.repo_paciente import PacienteRepo
from repos.repo_doctor import DoctorRepo
from repos.repo_cita import CitaRepo

from servicios.notificacion import EmailNotificacion
from servicios.cita_servicio import CitaServicio

pacientes = PacienteRepo()
doctores = DoctorRepo()
citas = CitaRepo()
notificador = EmailNotificacion()

service = CitaServicio(pacientes, doctores, citas, notificador)


print("\nCargando datos desde datos.csv...")

with open("datos.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Cargar pacientes
        if row["tipo"] == "paciente" and row["id"].strip() != "":
            pacientes.guardar(
                Paciente(
                    int(row["id"]),
                    row["nombre"],
                    int(row["edad"]),
                    row["correo"]
                )
            )

        # Cargar doctores
        if row["tipo"] == "doctor" and row["doctorId"].strip() != "":
            doctores.guardar(
                Doctor(
                    int(row["doctorId"]),
                    row["nombre"],
                    row["especialidad"]
                )
            )



print("\nDOCTORES :")
for d in doctores.doctores.values():
    print(" ", d)



print("\n=== AGENDAR CITA MÉDICA ===\n")

pid = int(input("ID del paciente: "))
did = int(input("ID del doctor: "))

fecha_txt = input("Fecha (AAAA-MM-DD): ")
hora_txt = input("Hora (HH:MM): ")


anio, mes, dia = map(int, fecha_txt.split("-"))
h, m = map(int, hora_txt.split(":"))

fecha = date(anio, mes, dia)
hora = time(h, m)

try:
    cita = service.agendar_cita(pid, did, fecha, hora)
    print("\nCita creada con éxito:\n", cita)
except Exception as e:
    print("\n Error:", e)
