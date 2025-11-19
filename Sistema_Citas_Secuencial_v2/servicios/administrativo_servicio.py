class AdministrativoServicio:
    def __init__(self, repo_paciente, repo_doctor, repo_cita):
        self.repo_paciente = repo_paciente
        self.repo_doctor = repo_doctor
        self.repo_cita = repo_cita

    # Gestión de pacientes
    def crear_paciente(self, paciente):
        self.repo_paciente.guardar(paciente)

    def editar_paciente(self, paciente):
        self.repo_paciente.guardar(paciente)

    def eliminar_paciente(self, paciente_id):
        self.repo_paciente.eliminar(paciente_id)

    # Gestión de doctores
    def crear_doctor(self, doctor):
        self.repo_doctor.guardar(doctor)

    def editar_doctor(self, doctor):
        self.repo_doctor.guardar(doctor)

    def eliminar_doctor(self, doctor_id):
        self.repo_doctor.eliminar(doctor_id)

    # Gestión de citas
    def cancelar_cita(self, cita_id):
        cita = self.repo_cita.buscar(cita_id)
        if cita:
            cita.estado = "CANCELADA"
