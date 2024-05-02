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

![Captura de pantalla 2024-05-02 105841](https://github.com/JaimeAMejiaO/tasks_api/assets/131828918/eb32552e-0988-44b6-ac68-86a638dd7e67)



