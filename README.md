# PROYECTO CRUD CON FLASK Y MONGODB EN BASE DE DATOS TIPO RÉPLICA


###### Presentado por:
- Alejandro Ramirez 
- Alicia Valencia Acevedo
- Julian Esteban Daza
- Jaime Andrés Mejia Osorio
------------



## Introduccion
En un mundo cada vez más globalizado y digitalizado, donde las aplicaciones y páginas web son herramientas cotidianas,
las empresas buscan proteger y garantizar la disponibilidad de su información las 24 horas del día, los 7 días de la semana.
Sin embargo, ¿cómo logran hacerlo cuando se trata de bases de datos que pueden fallar en cualquier momento? Aquí es donde entra
en juego la replicación de datos, un proceso fundamental que implica copiar y almacenar datos empresariales en múltiples ubicaciones.
Este proceso puede ser único o continuo, dependiendo de las necesidades de la organización. En el último caso, el objetivo es asegurar
que los datos replicados se actualicen periódicamente y sean consistentes con la fuente original. El propósito principal de la replicación
de datos es mejorar la disponibilidad y accesibilidad de los datos y la solidez y consistencia del sistema.

![Captura de pantalla 2024-05-02 103359](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/545a0f82-cb05-4f1d-b4dc-ef3535eff3fc)


La replicación de datos opera mediante la transferencia de información de un lugar a otro, ya sea entre dos servidores locales en la misma área o en diferentes ubicaciones geográficas, lo cual depende del objetivo de la replicación, si es para asegurar la disponibilidad constante del servicio o un respaldo de la misma. los datos se pueden duplicar a través de varios procedimientos de duplicación; Los tipos de replicación son:



### Replicación completa

Implica copiar datos completos desde el origen al sistema de destino, incluida la información nueva, modificada y actual. Sin embargo, esta técnica de replicación de datos requiere más potencia de procesamiento y aumenta la carga en la red. Además, el costo generalmente aumenta a medida que mantener la coherencia se vuelve difícil al copiar grandes volúmenes de datos.


### Replicación parcial

Solo una parte de los datos se replica en esta técnica de replicación de datos, como los datos actualizados. Por lo tanto, es más rápido que la replicación de tablas completas porque trata con un volumen comparativamente más pequeño, lo que reduce la carga de la red y los problemas de consistencia.

### Replicación basada en registros

Esta técnica sólo es viable para bases de datos replicación, ya que se realiza utilizando archivos de registro binarios presentes en la base de datos. Lee datos directamente de los archivos de registro, lo que reduce la carga en el sistema de producción. Esta técnica se acerca más a la replicación de datos en tiempo real.


### Replicación incremental basada en claves

El incremento basado en claves es un proceso de replicación de la base de datos que actualiza o cambia los datos que se han modificado desde la última actualización a través de las claves de replicación. Dado que se copia una menor cantidad de datos con este proceso, resulta mucho más rápido y eficiente que la replicación completa. Sin embargo, la desventaja de hacer esto es que falla al replicar los datos ya eliminados.


## Desventajas de la replicación de datos

Surgen principalmente debido a la complejidad de mantener la coherencia de los datos en ubicaciones diversas. Algunos de los desafíos más comunes incluyen:

- Mayores costos: Al mantener copias duplicadas de los mismos datos en múltiples ubicaciones y sistemas de bases de datos, los costos generales de almacenamiento y procesamiento tienden a aumentar.
Limitaciones de tiempo: La ejecución y gestión del proceso de duplicación requiere una inversión significativa de tiempo por parte de un equipo interno para garantizar que los datos copiados estén alineados con los datos de origen.

- Ancho de banda: Mantener la coherencia entre las réplicas de datos puede generar un aumento en el tráfico de la red.
  
- Datos inconsistentes: Sincronizar las actualizaciones entre entornos distribuidos es complicado, ya que la copia de datos desde múltiples fuentes en diferentes momentos puede resultar en conjuntos de datos que no están sincronizados entre sí. Esta falta de sincronización puede ser temporal o incluso permanente si no se aborda adecuadamente.

------------

# NUESTRO PROYECTO

El presente proyecto aborda la implementación de un sistema CRUD (Crear, Leer, Actualizar, Eliminar) el cual se basa en un sistema de tareas utilizando Flask como framework web y MongoDB como base de datos, aprovechando las capacidades de replicación de MongoDB la cual se usa para mejorar la disponibilidad y la tolerancia a fallos del sistema. 

### CONCEPTOS NECESARIOS

#### CRUD
Es un acrónimo que significa Crear, Leer, Actualizar y Eliminar (en inglés: Create, Read, Update, Delete). Estas cuatro operaciones son las funciones básicas que se emplean para interactuar con bases de datos y sistemas de gestión de datos.

- Create (Crear registros): Se trata de introducir información.
- Read (Leer registros): Consultar la información de un registro o de un conjunto de ellos.
- Update (Actualizar registros): Modificar cualquiera de las columnas de la base de datos.
- Delete (Eliminar registros): Borrar datos del sistema de almacenamiento.
  
#### FLASK
Es un “micro” Framework para desarrollar una aplicación web básica o que se quiera desarrollar de una forma ágil y rápida. Flask puede ser muy conveniente, para determinadas aplicaciones no se necesitan muchas extensiones.

#### MONGODB

Es un sistema de gestión de bases de datos no relacional de código abierto que utiliza documentos flexibles en lugar de tablas y filas para procesar y almacenar diversas formas de datos.

Como solución de base de datos NoSQL, MongoDB no requiere un sistema de gestión de bases de datos relacionales, por lo que proporciona un modelo de almacenamiento de datos flexible que permite a los usuarios almacenar y consultar tipos de datos multivariados con facilidad. Esto no únicamente simplifica la gestión de bases de datos para los desarrolladores, sino que también crea un entorno altamente escalable para aplicaciones y servicios multiplataforma.

#### METODOS DE PETICION HTTP
HTTP define un conjunto de métodos de petición para indicar la acción que se desea realizar para un recurso determinado. Los más usados son: 

- POST:  Se usa el método de petición HTTP POST cuando se necesitan enviar datos al servidor.
- GET: Una petición GET solicita al servidor una información o recurso concreto.
- PUT: Se usa el metodo de HTTP PUT se utiliza para la actualizacion de informacion existente.
- DELETE: Se usa el metodo de HTTP DELETE para eliminar los datos a través de un servicio web REST.

### CREAR RÉPLICAS EN MONGODB

En el plan gratuito de MongoDB, no se permite la administración completa de réplicas debido a las limitaciones impuestas por este tipo de plan. MongoDB ofrece un clúster M0 gratuito con tres nodos de réplica preestablecidos, pero no es posible agregar, eliminar o modificar los nodos existentes. Aún así, se proporcionan comandos básicos para iniciar y verificar el conjunto de réplicas:

![Captura de pantalla 2024-05-02 105841](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/eb32552e-0988-44b6-ac68-86a638dd7e67)


------------

### LIBRERÍAS USADAS PARA EL DESARROLLO


- Librería PyMongo: Es una librería oficial de Python la cual se usa para manejar datos BSON (Binary JSON) que es el formato de serialización utilizado por MongoDB el cual se usa para generar y manipular identificadores únicos en documentos MongoDB.

- Librería Flask: Se usa para crear aplicaciones web, servicios RESTful y otros servicios web. Proporciona los módulos esenciales para el desarrollo web, como el renderizado de plantillas HTML, el manejo de solicitudes HTTP, el enrutamiento, las redirecciones y la gestión de cookies y sesiones. 

- Librería bson: Permite codificar y decodificar documentos en el formato BSON (Binary JSON) utilizado por MongoDB. BSON es una representación binaria de JSON diseñada para una transmisión y almacenamiento más eficientes. Esta librería facilita la serialización y deserialización de datos entre Python y MongoDB.

------------

### ¿CÓMO IMPLEMENTAR UN CRUD CON FLASK Y MONGODB?

A continuación se explicarán las líneas de código y su función dentro del mismo.

El primer paso es importar un constructor de flask para hacer levantamiento del servidor web usando flask, al mismo tiempo que se importa la configuración para la base de datos mongo, y inicializando el archivo app.py como el inicio de nuestra aplicación

![Captura de pantalla 2024-05-02 110204](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/6b26ee68-0830-438f-a7f4-055ed3b3c3ec)


@app.route(‘/’) define una ruta para la página principal, task_list = tasks.find() se encarga de realizar una consulta a la base de datos para obtener todas las tareas y las almacena en la variable task_list y return render_template('index.html', tasks=tasks_list) se encarga de renderizar la la plantilla ´index.html´ y pasa la lista de tareas tasks_list para que se muestre en la misma

![Captura de pantalla 2024-05-02 110312](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/de824831-061f-43a2-84c3-9337f9653fa9)

@app.route(‘/add’) crea una ruta para la página de agregar tareas, def view_add_task() se encarga de crear la vista para el método de agregar tareas, def add_task() se encarga de obtener los campos del formulario y crear una nueva tarea con una respuesta JSON que contiene un mensaje de éxito y los detalles de la tarea añadida


![Captura de pantalla 2024-05-02 110434](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/f4a73efc-51cd-45b5-a9ef-519bc474ae94)


@app.route(‘/<id>’) se encarga de crear la ruta para eliminar una tarea, tomando en cuenta el id de la misma, @app.route(‘/update/<id>’) es la encargada de actualizar las tareas mediante el método POST


![Captura de pantalla 2024-05-02 110513](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/000c4399-b80e-4eee-ab61-64bb21168e10)


![Captura de pantalla 2024-05-02 110605](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/de466f61-a198-4ca0-b657-5baed5dfbce5)


@app.errorhandler(404)se encarga de manejar el error 404 que ocurra y el if__name__ == ‘__main__’ se asegura que la aplicación esté siendo ejecutada como el programa principal, si esto es verdadero ejecuta en debug en el puerto 5000




![Captura de pantalla 2024-05-02 110654](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/7ce288a0-07b7-43a4-98e8-7a00cfb09d40)


Crea la clase tarea, donde se define un método constructor  dandole los campo, y se crea el método toCollection(self) el cual se encarga de de convertir la tarea en un diccionario

![Captura de pantalla 2024-05-02 110814](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/fa972851-340a-4659-9b44-f77e7ce66981)

se encarga de conectar con la base de datos

![Captura de pantalla 2024-05-02 110905](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/838de6d5-a8be-42c9-bdd0-65660a164eed)


Son las diferentes vistas creadas para los métodos del proyecto

![Captura de pantalla 2024-05-02 110951](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/8c939507-9d31-4528-b250-96c5262158ae)

------------

### ¿CÓMO SE SUBIÓ A GOOGLE CLOUD?

El proceso de subir la aplicación al servidor se llevó a cabo usando Docker e implementando este contenedor en la instancia de un servicio en Cloud Run, que es un servicio de computación serverless totalmente gestionado que forma parte de la plataforma Google Cloud.

------------

#### DOCKER

![Captura de pantalla 2024-05-02 111139](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/ee3c1869-f1de-45b2-82b7-4bcd3d6b5bb5)

Lo que tenemos en nuestro Dockerfile básicamente es que a partir de la imagen base para python 3.12 comenzamos estableciendo el directorio de trabajo en la ruta “/app”, para luego continuar instalando las librerías que usaremos, las cuales tenemos definidas en nuestro archivo “requirements.txt”. Debemos copiar todo el contenido de nuestra carpeta “src” que es donde tenemos todo el código fuente de nuestra aplicación, y así, exponiendo el puerto 5000 (donde usualmente se ejecuta Flask) y ejecutando nuestro archivo “app.py” podremos continuar para hacer el build de nuestra imagen.
Cabe recalcar que la variable de entorno MONGO_URI para la conexión a nuestra base de datos no la escribimos en el Dockerfile para evitar que queden expuestas las credenciales, esta la configuramos cuando vayamos a implementar el contenedor de nuestra imagen.

------------

#### GOOGLE CLOUD

En cuanto al servidor para implementar nuestro contenedor de Docker hemos elegido usar Google Cloud, ya que gracias a su servicio de Cloud Run nos facilita bastante la implementación	de nuestro contenedor.
Lo primero es que en nuestro proyecto en Google Cloud debemos habilitar el servicio de Cloud Run, una vez habilitado, lo que hacemos es que nuestra  imagen de Docker debemos subirla al repositorio de imágenes de nuestro proyecto, lo cual se hace a través del Artifact Registry que es un servicio de alojamiento de imágenes brindado por Google Cloud, a partir de aquí, solo hace falta crear nuestro servicio en Cloud Run usando como base la imágen que hemos cargado previamente, ya una vez configurados todos los parámetros de nuestro contenedor a ejecutar (como por ejemplo la variable de entorno MONGO_URI, la cantidad de memoria y de VCPUs) ya quedaría nuestra aplicación disponible en la web.

![Captura de pantalla 2024-05-02 111331](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/a7a94c2d-17fd-4974-9637-9d2bca3a76ee)


### REPOSITORIO

El proyecto lo trabajamos con github, el repositorio se encuentra en el siguiente enlace:

https://github.com/JaimeAMejiaO/tasks_api

### Aplicacion
Aplicacion desplegada:

https://app-distribuidos-yhkxjw6uxq-uc.a.run.app


### REFERENCIAS

- https://flask.palletsprojects.com/en/3.0.x/

- https://pypi.org/project/pymongo/

- https://www.mongodb.com/docs/atlas/sample-data/

- https://www.mongodb.com/docs/atlas/getting-started/

- https://www.mongodb.com/docs/atlas/create-connect-deployments/





