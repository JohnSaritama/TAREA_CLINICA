class CitaRepo:
    def __init__(self):
        self.citas = {}

    def guardar(self, cita):
        self.citas[cita.id] = cita

    def listar_por_doctor_y_fecha(self, doctorId, fecha):
        return [c for c in self.citas.values() if c.doctor.doctorId == doctorId and c.fecha == fecha]
