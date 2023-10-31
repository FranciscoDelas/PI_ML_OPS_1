# Proyecto Machine Learning Operations (MLOps)


## El proyecto se centra en la creación de un MVP de un sistema de recomendación de videojuegos para usuarios en la plataforma Steam. Como Data Scientist en Steam, el objetivo es abordar los desafíos de un conjunto de datos poco maduro y realizar tareas de Data Engineering para preparar los datos, diseñar y entrenar un modelo de Machine Learning que brinde recomendaciones de juegos personalizadas a los usuarios. El enfoque es desarrollar un Minimum Viable Product (MVP) de manera rápida para cumplir con los objetivos del proyecto.
________________________________________________________________________________________________________________________
QUE ENCONTRAMOS EN EL REPOSITORIO?
## Notebooks
- **01-Analisis_Sentimiento.ipynb:** Resolución de la consigna de Feature Engineering para análisis de sentimiento.
- **02-Funcion01.ipynb:** Resolución FUNCION 1 para la API
- **03-Funcion02.ipynb:** Resolución FUNCION 2 para la API
- **04-EDA.ipynb:** Resolución de la consigna de Análisis Exploratorio de Datos.
- **05-Funcion_Sistema_Recomendacion.ipynb:** Resolución de la consigna para el modelo de recomendación.

## Archivos de Datos
- **df_Anlaisis_Sentimiento** Archivo CSV para el analisis de sentimiento.
- **df_Funcion01** Archivo CSV para FUNCION 1
- **df_Funcion02** Archivo CSV para FUNCION 2
- **df_eda.csv:** Archivo CSV utilizado en el análisis exploratorio de datos (EDA).
- **df_SistemaRecomendacion2.csv:** Archivo CSV utilizado en el modelo de sistema de recomendación.

## Requisitos
Asegúrate de tener instaladas las siguientes bibliotecas y dependencias para ejecutar el proyecto:
- Python 3.x
- FastAPI
- (Lista de otras bibliotecas y dependencias---> **requirements.txt**)
________________________________________________________________________________________________________________________

### Paso a Paso para Navegar en el Repositorio

#### 1. Notebooks

Esta sección contiene una serie de notebooks que representan diferentes etapas del proyecto. Sigue el orden de los notebooks para comprender mejor el flujo del proyecto.

////////////////////////////////////////////////////////////////////////////////////////////////////////////
### Notebook 01 - Analisis_Sentimiento.ipynb

El Notebook 01 Se centra en la resolución de la consigna de análisis de sentimiento para el proyecto. Aquí está la descripción general de lo que se hace en este notebook:

- En primer lugar, se importan las bibliotecas necesarias, como Pandas y TextBlob, y se crea un DataFrame llamado `dfreviews` a partir del archivo JSON 'user_reviews.json'. El objetivo es convertir las líneas del archivo JSON en un DataFrame de Pandas.

- Se realiza una limpieza inicial de los datos eliminando filas con valores nulos en el DataFrame `dfreviews`.

- A continuación, se desanida la columna 'reviews' del DataFrame y se toman subcolumnas como nuevas columnas. Se crean las columnas 'item_id' y 'review', y se eliminan filas con valores nulos en la columna 'review'.

- Luego, se procede a realizar el análisis de sentimiento sobre la columna 'review' utilizando la biblioteca TextBlob. Se define una función `sentiment_analysis` que calcula la polaridad del sentimiento y asigna un valor numérico (0, 1 o 2) para representar si el sentimiento es negativo, neutral o positivo, respectivamente.

- La función `sentiment_analysis` se aplica a la columna 'review', y se crea una nueva columna llamada 'sentiment_analysis' en el DataFrame `dfreviews` para almacenar los resultados del análisis de sentimiento.

En resumen, este notebook se encarga de la preparación de los datos, la limpieza y el análisis de sentimiento de las reseñas de usuarios en Steam, y crea una nueva columna 'sentiment_analysis' que representa la polaridad del sentimiento. Estos pasos son esenciales para el desarrollo posterior del sistema de recomendación basado en el análisis de sentimiento de las reseñas de juegos.

////////////////////////////////////////////////////////////////////////////////////////////////////////////
#### Notebook 02 - Funcion 1
Este notebook realiza varias operaciones en un conjunto de datos de juegos de Steam, con el objetivo de analizar la cantidad de juegos y el porcentaje de contenido gratuito por año, para un desarrollador específico. A continuación, te explico paso a paso lo que hace:

1. Importa las bibliotecas necesarias, incluyendo pandas para el manejo de datos, json para la lectura de archivos JSON, ast para manipular estructuras de datos de Python y tabulate para presentar los resultados de manera tabular.

2. Lee un archivo JSON llamado 'steam_games.json' y lo convierte en un DataFrame llamado 'dfgame'.

3. Realiza varias operaciones de limpieza de datos en el DataFrame 'dfgame', incluyendo la eliminación de filas con valores faltantes, la selección de columnas relevantes y el formateo de fechas.

4. Define una función llamada 'developer' que toma un argumento de 'desarrollador' y filtra el DataFrame 'dfgame' para obtener datos específicos del desarrollador.

5. Utiliza la función 'groupby' de pandas para agrupar los datos por año y calcular la cantidad de juegos y el porcentaje de contenido gratuito para ese desarrollador en cada año.

6. Imprime los resultados en formato tabular utilizando la función 'print' y 'tabulate'.

7. Finalmente, guarda los resultados en un archivo CSV llamado 'df_Funcion1.csv'.

El ejemplo específico en el notebook está utilizando el desarrollador 'Ankama Studio', mostrando la cantidad de juegos y el porcentaje de contenido gratuito por año para este desarrollador en particular.
////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////
#### Notebook 03 - Funcion 2
Este segundo notebook realiza una serie de operaciones complejas para analizar el gasto de un usuario en juegos de Steam, el porcentaje de recomendación basado en las reseñas y la cantidad de juegos jugados. A continuación, se describen los pasos detallados que se llevan a cabo:

1. Importa las bibliotecas necesarias, incluyendo pandas para el manejo de datos, json para la lectura de archivos JSON, ast para manipular estructuras de datos de Python y tabulate para presentar los resultados de manera tabular.

2. Lee tres archivos JSON y los convierte en DataFrames llamados 'dfreviews', 'dfgame' y 'dfitem'.

3. Realiza una serie de operaciones de limpieza de datos en cada uno de los DataFrames, incluyendo la eliminación de filas con valores nulos y conversiones de tipo de datos.

4. Fusiona los DataFrames 'dfreviews', 'dfgame' y 'dfitem' en un solo DataFrame llamado 'df_merged', eliminando las columnas que no son necesarias.

5. Calcula el gasto total, el número total de elementos jugados y el porcentaje de recomendaciones para cada usuario.

6. Guarda los resultados en un archivo CSV llamado 'df_Funcion2.csv'.

7. Define una función llamada 'userdata' que toma un argumento 'user_id', lee el archivo CSV 'df_Funcion2.csv' y busca el usuario correspondiente en el DataFrame. Si encuentra al usuario, la función devuelve un diccionario con el gasto total, el porcentaje de recomendación y la cantidad de elementos jugados para ese usuario. Si no encuentra al usuario, la función devuelve un mensaje que indica que el usuario no está en la base de datos.

8. Se proporciona un ejemplo de llamada a la función 'userdata' con el ID de usuario "76561197970982479", y se muestra un diccionario con los detalles de gasto, porcentaje de recomendación y cantidad de elementos jugados para ese usuario específico.

////////////////////////////////////////////////////////////////////////////////////////////////////////////
#### Notebook 04 - EDA.ipynb
El análisis exploratorio de datos (EDA) realizado en el Notebook 03 se enfoca en comprender y explorar los datos relacionados con las reseñas de usuarios de juegos de Steam, y se realiza una investigación de las opiniones de los usuarios y su relación con las recomendaciones de juegos. A continuación, se enumera una descripción de las principales tareas realizadas y los hallazgos clave:

1. **Creación del DataFrame Fusionado**: Se crea un DataFrame fusionando los datos de dos fuentes: "steam_games.json" y "user_reviews.json". El primero contiene información sobre los juegos, mientras que el segundo contiene reseñas de usuarios.

2. **Filtrado y Limpieza de Datos**: Se realizan operaciones de limpieza de datos, incluyendo la eliminación de filas nulas y columnas no necesarias.

3. **Análisis de Distribuciones**: Se visualiza la distribución de datos mediante histogramas y gráficos de barras. Se analiza la distribución de las puntuaciones de análisis de sentimientos y de la columna 'recommend' (recomendación).

4. **Resumen de Sentimientos**: Se calcula la media y la desviación estándar de las puntuaciones de análisis de sentimientos. Se encuentra que, en promedio, las opiniones tienden a ser más positivas que negativas.

5. **Comparación de Sentimientos y Recomendaciones**: Se compara la media de las puntuaciones de análisis de sentimientos entre juegos recomendados y no recomendados. Se encuentra una diferencia significativa, con juegos recomendados teniendo puntuaciones de sentimientos más positivas.

6. **Implicaciones para la Recomendación**: Se discuten las implicaciones de los hallazgos en la función de recomendación de juegos, sugiriendo que las opiniones positivas influyen en las recomendaciones.

7. **Almacenamiento de Resultados**: Finalmente, se guarda el DataFrame resultante en un archivo CSV llamado 'eda.csv' para futuros análisis.

Los hallazgos clave se pueden leer en el notebook.

////////////////////////////////////////////////////////////////////////////////////////////////////////////
#### Notebook 05 - Funcion_Sistema_Recomendacion.ipynb
El Notebook 04 se centra en la creación de un modelo de recomendación basado en la similitud del coseno. A continuación, se describen los pasos clave para crear el modelo y su objetivo:

**Creación de DataFrames de Juegos y Reseñas:**

1. Se crean dos DataFrames: `dfgames` y `dfreviews`, a partir de los archivos "steam_games.json" y "user_reviews.json", respectivamente. Estos DataFrames contienen información sobre los juegos y las reseñas de los usuarios.

**Limpieza y Preparación de Datos:**

2. Se realiza una limpieza de los DataFrames para eliminar filas y columnas no necesarias, así como la manipulación de los datos para fusionar la información relevante.

3. Se aplican técnicas de análisis de sentimientos a las reseñas de los usuarios para asignar puntuaciones de análisis de sentimientos a las reseñas, indicando si son negativas, neutrales o positivas.

**Representación de Datos y Creación de DataFrame para Similitud:**

4. Se crea un DataFrame `df_SimilitudCoseno` que servirá como base para el modelo de recomendación. Se incluyen las puntuaciones de análisis de sentimientos y se convierten los géneros de los juegos en una representación one-hot.

**Cálculo de Similitud del Coseno:**

5. Se utiliza la similitud del coseno para calcular la similitud entre los juegos en función de sus características, que incluyen recomendaciones, análisis de sentimientos y géneros.

**Función de Recomendación de Juegos:**

6. Se crea una función llamada `recomendacion_juego(id_producto)` que toma como entrada el ID de un juego y devuelve una lista de juegos recomendados en función de la similitud del coseno. La función utiliza el DataFrame `df_SimilitudCoseno` y el cálculo de similitud previamente realizado.

7. La función encuentra juegos similares al juego de entrada y devuelve una lista de juegos recomendados, excluyendo el propio juego.

**Objetivo del Modelo:**

El objetivo del modelo de recomendación basado en similitud del coseno es proporcionar recomendaciones de juegos a los usuarios en función de las características de los juegos, como las reseñas de los usuarios, las recomendaciones y los géneros. El modelo busca identificar juegos similares al juego seleccionado por el usuario y recomendarlos, lo que puede ayudar a los usuarios a descubrir nuevos juegos que puedan interesarles en función de sus preferencias y experiencias pasadas.

**El modelo considera características específicas de los juegos:**

1. Reseñas de Usuarios: En el código del notebook, se utiliza la columna "review" del DataFrame para realizar un análisis de sentimiento de las reseñas de usuarios. Esto implica que se están considerando las reseñas de los usuarios como una característica importante para evaluar la similitud entre juegos. Las reseñas se utilizan para calcular la puntuación de sentimiento, que es uno de los factores utilizados en la medida de similitud del coseno.
2. Recomendaciones de Usuarios: El DataFrame también incluye información sobre si un juego fue recomendado por los usuarios. Esta columna, denominada "recommend", se utiliza en el cálculo de la similitud del coseno y se menciona en la función de recomendación de juegos. Las recomendaciones de usuarios son un indicador de la aceptación y el interés en un juego, lo que lo convierte en una característica importante en el modelo.
3. Géneros de Juegos: En el código, se convierten los géneros de juegos en una representación one-hot, lo que significa que se crean columnas binarias para cada género. Esto permite que los géneros se consideren como características en el cálculo de similitud. Los géneros de juegos son una característica fundamental para determinar la similitud entre juegos, ya que los usuarios a menudo tienen preferencias específicas de género.

Este modelo es especialmente útil en plataformas de juegos como Steam, donde hay una gran cantidad de juegos disponibles, y los usuarios pueden beneficiarse de recomendaciones personalizadas para encontrar juegos que se adapten a sus gustos.