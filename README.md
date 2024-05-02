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





