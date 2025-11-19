class AdministrativoRepo:
    def __init__(self):
        self.admins = {}

    def guardar(self, admin):
        self.admins[admin.administrativoId] = admin

    def buscar(self, admin_id):
        return self.admins.get(admin_id)

    def eliminar(self, admin_id):
        if admin_id in self.admins:
            del self.admins[admin_id]

    def listar(self):
        return list(self.admins.values())
