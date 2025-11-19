class INotificacion:
    def enviar(self, correo, asunto, mensaje):
        raise NotImplementedError

class EmailNotificacion(INotificacion):
    def enviar(self, correo, asunto, mensaje):
        print(f"\nEnviando correo a {correo}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}\n")
