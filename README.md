# PROYECTO FINAL: Análisis de Cancelaciones y Retrasos en Vuelos Comerciales

---

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar las **cancelaciones y los retrasos en vuelos comerciales**, utilizando datos reales del sector aéreo. A partir del estudio de dos bases de datos complementarias, se busca comprender el comportamiento operativo de las aerolíneas y los factores que influyen en la puntualidad de los vuelos.

El análisis se centra en la identificación de patrones temporales, el estudio de las principales causas de retrasos y cancelaciones, y la relación entre distintas variables operativas del vuelo. El proyecto combina análisis exploratorio en Python con una capa final de análisis visual mediante un dashboard interactivo.

---

## Bases de Datos Utilizadas

El proyecto se apoya en dos bases de datos principales en formato CSV, extraídas de la plataforma Kaggle, que comparten una estructura común y permiten realizar un análisis conjunto:

- **Base de datos de vuelos** (`flight_details.csv`)  
  Contiene información general de cada vuelo: fecha, aerolínea, número de vuelo, aeropuerto de origen y destino, horarios programados y reales, tiempos de taxi, duración del vuelo y distancia recorrida.

- **Base de datos de retrasos y cancelaciones** (`flight_delays.csv`)  
  Incluye información específica sobre incidencias operativas: estado del vuelo (cancelado o no), códigos de cancelación y desglose de los retrasos según su causa (operativa de la aerolínea, meteorología, sistema nacional del espacio aéreo, seguridad y llegada tardía de la aeronave).

Estas bases permiten analizar no solo si un vuelo se retrasa o se cancela, sino también **el motivo y la magnitud del retraso**.

---

## Objetivos del Análisis

Los principales objetivos de este proyecto son:

- Analizar la frecuencia de **cancelaciones y retrasos**.
- Identificar las **principales causas de los retrasos**.
- Estudiar la evolución temporal de las incidencias.
- Comparar el comportamiento operativo entre aerolíneas.
- Construir métricas que permitan evaluar la puntualidad y el cumplimiento del horario.
- Facilitar un análisis flexible mediante visualización interactiva.

---

## Herramientas y Tecnologías Empleadas

Para el desarrollo del proyecto se han utilizado las siguientes herramientas:

- **Python** como lenguaje principal de análisis.
- **Pandas y NumPy** para la limpieza, transformación y análisis de datos.
- **Matplotlib y Seaborn** para la creación de visualizaciones.
- **Jupyter Notebook** como entorno de trabajo y documentación del análisis.
- **Microsoft Excel** para la construcción del dashboard interactivo y el análisis visual final.
- **Git y GitHub** para el control de versiones y la gestión del proyecto.

En algunos casos, cuando no se tenía claro cómo abordar determinados ejercicios, se contó con el apoyo del entorno y con el uso de **ChatGPT** como herramienta de consulta, especialmente durante la fase de exploración de datos y creación de gráficos.

---

## Estructura del Proyecto y Documentos Generados

El proyecto se organiza en distintos notebooks y archivos que reflejan las fases del análisis y permiten seguir de forma clara la evolución del trabajo:

- **1.0_Detalles_Vuelos.ipynb**  
  Exploración inicial del dataset de vuelos.

- **1.1_Detalles_Vuelos_Limpieza.ipynb**  
  Limpieza y normalización de la base de datos de vuelos.

- **1.2_Detalles_Vuelos_Limpieza_ATL.ipynb**  
  Filtrado del dataset para vuelos con origen ATL.

- **2.0_Incidencias_Vuelos.ipynb**  
  Exploración inicial del dataset de retrasos y cancelaciones.

- **2.1_Incidencias_Vuelos_Limpieza.ipynb**  
  Limpieza y tipado del dataset de incidencias.

- **2.2_Incidencias_Vuelos_Limpieza_ATL.ipynb**  
  Filtrado de incidencias para vuelos con origen ATL.

- **3.0_Vuelos_Union.ipynb**  
  Unión de ambas bases de datos.

- **3.1_Vuelos_Union_Análisis.ipynb**  
  Análisis exploratorio, creación de KPIs, visualizaciones y análisis estadístico.

### Archivos de datos

- **flight_details.csv / flight_delays.csv**  
  Bases de datos originales.

- **flight_details_atl.csv / flight_delays_atl.csv**  
  Subconjuntos filtrados por origen ATL.

- **flights_final_atl.csv**  
  Dataset final limpio y enriquecido, utilizado tanto para el análisis como para el dashboard.

### Otros archivos

- **dictionary.html**  
  Diccionario de datos original.

- **src/**  
  Funciones reutilizables empleadas durante la limpieza y el análisis.

- **proyecto_final.venv**  
  Entorno virtual del proyecto.

- **README.md**  
  Documento descriptivo del proyecto.

---

## Variables del Dataset

### Variables originales

- **FL_DATE**: Fecha del vuelo.  
- **AIRLINE_CODE**: Código de la aerolínea que opera el vuelo.  
- **DOT_CODE**: Código identificador de la aerolínea asignado por el Department of Transportation (DOT).  
- **FL_NUMBER**: Número del vuelo.  
- **ORIGIN**: Código IATA del aeropuerto de origen.  
- **ORIGIN_CITY**: Ciudad del aeropuerto de origen.  
- **DEST**: Código IATA del aeropuerto de destino.  
- **DEST_CITY**: Ciudad del aeropuerto de destino.  
- **CRS_DEP_TIME**: Hora de salida programada del vuelo.  
- **DEP_TIME**: Hora real de salida del vuelo.  
- **DEP_DELAY**: Diferencia en minutos entre la hora real y la hora programada de salida.  
- **TAXI_OUT**: Minutos transcurridos desde que el avión abandona la puerta hasta el despegue.  
- **WHEELS_OFF**: Hora de despegue del avión.  
- **WHEELS_ON**: Hora de aterrizaje del avión.  
- **TAXI_IN**: Minutos transcurridos desde el aterrizaje hasta la llegada a la puerta.  
- **CRS_ARR_TIME**: Hora de llegada programada del vuelo.  
- **ARR_TIME**: Hora real de llegada del vuelo.  
- **ARR_DELAY**: Diferencia en minutos entre la hora real y la hora programada de llegada.  
- **CANCELLED**: Indicador de vuelo cancelado (1 = cancelado, 0 = no cancelado).  
- **CANCELLATION_CODE**: Código del motivo de la cancelación.  
- **DIVERTED**: Indicador de vuelo desviado (1 = desviado, 0 = no desviado).  
- **CRS_ELAPSED_TIME**: Duración programada del vuelo, en minutos.  
- **ELAPSED_TIME**: Duración real del vuelo, en minutos.  
- **AIR_TIME**: Tiempo total de vuelo en el aire, en minutos.  
- **DISTANCE**: Distancia del vuelo en millas.  
- **DELAY_DUE_CARRIER**: Minutos de retraso atribuibles a la operativa de la aerolínea.  
- **DELAY_DUE_WEATHER**: Minutos de retraso atribuibles a condiciones meteorológicas.  
- **DELAY_DUE_NAS**: Minutos de retraso atribuibles al sistema nacional del espacio aéreo (NAS).  
- **DELAY_DUE_SECURITY**: Minutos de retraso atribuibles a controles de seguridad.  
- **DELAY_DUE_LATE_AIRCRAFT**: Minutos de retraso atribuibles a la llegada tardía de la aeronave.

### Variables creadas durante el análisis (KPIs)

- **YEAR, QUARTER, MONTH, WEEKDAY**
- **IS_CANCELLED, IS_DIVERTED**
- **IS_ON_TIME_ARR**
- **IS_DELAYED_ARR**
- **DELAY_BUCKET**
- **SCHED_DIFF_MIN**
- **CRS_DEP_HOUR**
- **TIME_BLOCK**

Estas variables permiten analizar la puntualidad desde una perspectiva temporal y operativa.

---

## Proceso de Trabajo

### 1. Preparación y unificación de los datos
- Carga de datos.
- Unión de datasets.
- Revisión de tipos, nulos y duplicados.
- Filtrado de vuelos con origen **ATL (Aeropuerto de Atlanta)** para mejorar la manejabilidad del análisis.

### 2. Funciones creadas
- **eda_preliminar(df)**: análisis exploratorio inicial.
- **clean_flights_df(df)**: limpieza, normalización y tipado de variables.

### 3. Limpieza y normalización
- Eliminación de columnas redundantes.
- Normalización de variables temporales.
- Reordenación del dataset.

### 4. Creación de variables derivadas
- KPIs de puntualidad y retraso.
- Segmentación por franjas horarias y tramos de retraso.

### 5. Control de versiones
- Uso de entorno virtual.
- Gestión del proyecto con Git y GitHub.

### 6. Creación del dashboard final
- Diseño y construcción de un **dashboard interactivo en Excel** a partir del dataset final limpio y enriquecido.
- Definición de KPIs clave y visualizaciones orientadas al análisis operativo.
- Implementación de filtros dinámicos para el análisis por aerolínea, periodo temporal y franja horaria.
- Integración del dashboard como herramienta final de análisis y apoyo a la toma de decisiones.

---

## Resultados y Análisis

El análisis exploratorio realizado en Python permitió identificar patrones relevantes en los datos, como el impacto del año 2020 en la operativa aérea, diferencias significativas de puntualidad entre aerolíneas y franjas horarias, y la concentración del retraso en causas operativas imputables a la aerolínea y a la llegada tardía de aeronaves.

Estos resultados fueron contrastados mediante análisis estadístico (ANOVA), sirviendo como base conceptual para el diseño del dashboard final.

---

## Dataset y Dashboard de Análisis de Incidencias de Vuelos (ATL)

El proyecto culmina con la construcción de un **dashboard interactivo en Excel**, alimentado por el dataset final limpio y enriquecido.

El objetivo del dashboard **no es extraer conclusiones generales**, sino permitir un análisis flexible y dinámico del comportamiento de cada aerolínea de forma individual, en función de los filtros seleccionados.

---

## Nota metodológica clave

El análisis realizado en **Visual Studio Code (Python)** y el análisis visual del **dashboard en Excel** **no se sustituyen**, sino que **se complementan**:

- El análisis en Python permite comprender el dataset, validar hipótesis y construir métricas.
- El dashboard permite explorar esos resultados de forma interactiva y contextualizada.

Ambas partes forman un único flujo de análisis.

---

## Conclusiones

- La puntualidad aérea está fuertemente condicionada por factores operativos.
- La franja horaria influye de forma significativa en los retrasos de llegada.
- Las cancelaciones son menos frecuentes que los retrasos y responden principalmente a decisiones operativas y condiciones meteorológicas.
- El retraso en la salida es el principal predictor del retraso en la llegada.
- El análisis combinado (Python + dashboard) permite una comprensión más completa del comportamiento operativo.

---

## Próximos Pasos

- Profundizar en el análisis estadístico para el resto de aeropuertos.
- Incorporar análisis comparativos entre aeropuertos.
- Estudiar medidas para disminuir los retrasos por causas internas del propio aeropuerto. 

---

## Autora

- **Beatriz Banegas**  
- Proyecto desarrollado como parte del curso de **Data Analytics**
