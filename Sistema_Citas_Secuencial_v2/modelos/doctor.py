class Doctor:
    def __init__(self, doctorId, nombre, especialidad):
        self.doctorId = doctorId
        self.nombre = nombre
        self.especialidad = especialidad

    def __repr__(self):
        return f"Doctor(doctorId={self.doctorId}, nombre='{self.nombre}', esp='{self.especialidad}')"
