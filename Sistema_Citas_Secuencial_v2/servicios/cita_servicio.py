from modelos.cita import Cita
from modelos.estado_cita import EstadoCita

class CitaServicio:
    def __init__(self, paciente_repo, doctor_repo, cita_repo, notificador):
        self.paciente_repo = paciente_repo
        self.doctor_repo = doctor_repo
        self.cita_repo = cita_repo
        self.notificador = notificador

    def agendar_cita(self, paciente_id, doctorId, fecha, hora):
        paciente = self.paciente_repo.buscar_por_id(paciente_id)
        doctor = self.doctor_repo.buscar_por_id(doctorId)

        if not paciente:
            raise Exception("Paciente no encontrado")
        if not doctor:
            raise Exception("Doctor no encontrado")

        citas = self.cita_repo.listar_por_doctor_y_fecha(doctorId, fecha)
        for c in citas:
            if c.hora == hora and c.estado != EstadoCita.CANCELADA:
                raise Exception("El doctor no está disponible en esa hora")

        cita = Cita(fecha, hora, paciente, doctor)
        self.cita_repo.guardar(cita)

        mensaje = f"Hola {paciente.nombre}, su cita con {doctor.nombre} fue creada."
        self.notificador.enviar(paciente.correo, "Cita agendada", mensaje)

        return cita
