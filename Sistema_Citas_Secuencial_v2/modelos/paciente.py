class Paciente:
    def __init__(self, id, nombre, edad, correo):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def __repr__(self):
        return f"Paciente(id={self.id}, nombre='{self.nombre}')"
