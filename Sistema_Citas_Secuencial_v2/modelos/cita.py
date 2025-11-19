from modelos.estado_cita import EstadoCita

class Cita:
    _ids = 1

    def __init__(self, fecha, hora, paciente, doctor):
        self.id = Cita._ids
        Cita._ids += 1
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.doctor = doctor
        self.estado = EstadoCita.PENDIENTE

    def __repr__(self):
        return (f"Cita(id={self.id}, fecha={self.fecha}, hora={self.hora}, "
                f"estado={self.estado.value}, paciente={self.paciente.nombre}, "
                f"doctor={self.doctor.nombre})")
