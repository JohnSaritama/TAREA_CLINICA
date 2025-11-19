class PacienteRepo:
    def __init__(self):
        self.pacientes = {}

    def guardar(self, paciente):
        self.pacientes[paciente.id] = paciente

    def buscar_por_id(self, id):
        return self.pacientes.get(id)
