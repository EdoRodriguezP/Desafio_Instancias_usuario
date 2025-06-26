class Usuario():
    # Método constructor: inicializa los atributos de la instancia
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre                
        self.apellidos = apellido           
        self.email = email                  
        self.genero = genero               

    # Representación en texto de la instancia (para imprimir)
    def __repr__(self):
        return f"{self.nombre}"