class Administrativo:
    def __init__(self, administrativoId, nombre, correo, contraseña, rol="ADMIN"):
        self.administrativoId = administrativoId
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol

    def __str__(self):
        return f"Administrativo({self.administrativoId}, {self.nombre}, {self.correo}, rol={self.rol})"
