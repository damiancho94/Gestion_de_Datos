# Gestion_de_Datos
En este repositorio se entregaran los avances correspondientes al trabajo final de la materia GESTION DE DATOS

INTEGRANTES:
Damián Felipe Castillo González, Edwin Leonardo Silva Piracoca b & Daniel Alejandro Córdoba Pulido 

2. Alcance y características generales del proyecto.

Con este proyecto se busca mediante el consumo de una base de datos de spotify y un tratamiento de datos adecuado a esta , generar una recomendacion de 5 canciones a un usuario que asi lo desee, esto con pasos previos de limpiesa y tratamiento de datos para evitar errores en las consultas y tener la mejor calidad de datos posibles.

La limpieza y preprocesamiento de los datos son esenciales para garantizar que los resultados sean precisos y confiables. Es importante verificar la calidad y coherencia de los datos antes de utilizarlos en un análisis.

La elección adecuada de las herramientas y técnicas de análisis de datos es fundamental para obtener información valiosa. Dependiendo de los objetivos del análisis, se pueden utilizar diferentes métodos estadísticos, de visualización, de aprendizaje automático, entre otros.

Los resultados del análisis deben ser presentados de manera clara y accesible para que los usuarios puedan comprender fácilmente la información y tomar decisiones informadas en base a ella.

El análisis de datos puede ser útil para identificar patrones y tendencias, así como para descubrir nuevas oportunidades o problemas en un conjunto de datos. Sin embargo, también tiene limitaciones y es importante tener en cuenta el contexto en el que se recopilaron los datos y las limitaciones del análisis en sí mismo.

Ahora por último al realizar un agrupamiento de la popularidad de canciones, se pueden extraer valores como las canciones que menos suenan  y por otro las más exitosas, gracias a la función describe() nos permite observar la media , desviación estándar, los valores mínimos,  maximos, quartiles y conteos de cada canción tanto en exitosos como en no exitosas. 

3. Organización del repositorio.

 Pasos para ejecutar y/o desplegar cada uno de los componentes
implementados.

Para desplegar los resultados del modelo, se crea una tabla en bigquery que tiene dichos resultados para todas las canciones de la muestra, el despliegue por detrás es una consulta a esta tabla teniendo en cuenta que este proceso se le conoce como tipo  BATCH.

Dado que el objetivo es que un usuario pueda usar estos resultados desde cualquier lugar, se hace el montaje de dicha consulta en un servicio de Google cloud llamado App Engine.


Al realizar dicho proceso ,este servicio nos va a generar una URL. 

URL : https://proyecto-gestion-datos.uc.r.appspot.com/docs#/default/query_query_post

Sin embargo, el front para poder hacer uso de dichos resultados es una propiedad que se invoca con el siguiente comando en la URL (/docs)

Para que el usuario pueda dar uso, debe darle click en el botón TRY OUT: 


Y escribir el nombre de la canción en la caja de texto input_text 

Aqui un posible listado para utilizar el programa:


Lahaina Luna,	
One More Try
Juice
Monoi Mas Meiname
Ring
Yeke Yeke
Verliefd

Una vez el usuario coloca el nombre de la canción  se recibirá la recomendación en la caja llamada Response body. 






