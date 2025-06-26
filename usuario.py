class Usuario():
    # Método constructor: inicializa los atributos de la instancia
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre                # Nombre del usuario
        self.apellidos = apellido           # Apellido del usuario
        self.email = email                  # Email del usuario
        self.genero = genero                # Género del usuario

    # Representación en texto de la instancia (para imprimir)
    def __repr__(self):
        return f"{self.nombre}"