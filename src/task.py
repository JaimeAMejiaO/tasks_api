# Este archivo contiene la clase Task que representa una tarea en la aplicación
# Se crea con la finalidad de poner tener una estructura de los datos que guardaremos en la BD
class Task:

    # Constructor de la clase
    def __init__(self, title, description, done) -> None:
        self.title = title
        self.description = description
        self.done = done
    
    # Método para convertir la tarea en un diccionario
    def toCollection(self):
        return {
            'title': self.title,
            'description': self.description,
            'done': self.done
        }
