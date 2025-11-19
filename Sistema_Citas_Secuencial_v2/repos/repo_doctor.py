class DoctorRepo:
    def __init__(self):
        self.doctores = {}

    def guardar(self, doctor):
        self.doctores[doctor.doctorId] = doctor

    def buscar_por_id(self, doctorId):
        return self.doctores.get(doctorId)
