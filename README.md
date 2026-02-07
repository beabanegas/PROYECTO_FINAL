# 📊 PROYECTO FINAL  
## Análisis de Cancelaciones y Retrasos en Vuelos Comerciales

---

## 📖 Descripción del Proyecto

Este proyecto tiene como objetivo analizar las **cancelaciones y los retrasos en vuelos comerciales**, utilizando datos reales del sector aéreo. A través del estudio de dos bases de datos con información complementaria, se busca comprender el comportamiento operativo de las aerolíneas y los factores que influyen en la puntualidad de los vuelos.

El análisis se centra en la identificación de patrones temporales, las principales causas de retrasos y cancelaciones, así como las relaciones existentes entre distintas variables operativas del vuelo.

---

## 🗂️ Bases de Datos Utilizadas

El proyecto se apoya en dos bases de datos principales en formato CSV, extraídas de la plataforma Kaggle, que comparten una estructura común y permiten realizar un análisis conjunto:

- **Base de datos de vuelos** (`flight_details.csv`)  
  Contiene información general de cada vuelo, como la fecha, aerolínea, número de vuelo, aeropuerto de origen y destino, horarios programados y reales, tiempos de taxi, duración del vuelo y distancia recorrida.

- **Base de datos de retrasos y cancelaciones** (`flight_delays.csv`)  
  Incluye información específica sobre incidencias, como el estado del vuelo (cancelado o no), códigos de cancelación y el desglose de los retrasos según su causa (operativa de la aerolínea, condiciones meteorológicas, sistema nacional del espacio aéreo, seguridad y retrasos por aeronave).

Estas bases de datos permiten analizar no solo si un vuelo se retrasa o se cancela, sino también **el motivo y la magnitud del retraso**.

---

## 🎯 Objetivos del Análisis

Los principales objetivos de este proyecto son:

- Analizar la frecuencia de **cancelaciones y retrasos** en los vuelos.
- Identificar las **principales causas de los retrasos**.
- Estudiar la evolución temporal de las incidencias.
- Comparar el comportamiento operativo entre aerolíneas.
- Extraer conclusiones que ayuden a comprender los factores que afectan a la puntualidad aérea.

---

## 🛠️ Herramientas y Tecnologías Empleadas

Para el desarrollo del proyecto se han utilizado las siguientes herramientas:

- **Python** como lenguaje principal de análisis.
- **Pandas y NumPy** para la limpieza, transformación y análisis de datos.
- **Matplotlib y Seaborn** para la creación de visualizaciones gráficas.
- **Jupyter Notebook** como entorno de trabajo y documentación del análisis.
- **Git y GitHub** para el control de versiones y la gestión del proyecto.

En algunos casos, cuando no se tenía claro cómo abordar determinados ejercicios, se contó con el apoyo de personas del entorno y el uso de **ChatGPT** como herramienta de consulta, especialmente en la fase de exploración de datos y creación de gráficos.

---

## 📊 Variables del Dataset

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
- **DEP_DELAY**: Diferencia en minutos entre la hora real y la programada de salida.  
- **TAXI_OUT**: Minutos desde que el avión abandona la puerta hasta el despegue.  
- **WHEELS_OFF**: Hora de despegue del avión.  
- **WHEELS_ON**: Hora de aterrizaje del avión.  
- **TAXI_IN**: Minutos desde el aterrizaje hasta la llegada a la puerta.  
- **CRS_ARR_TIME**: Hora de llegada programada del vuelo.  
- **ARR_TIME**: Hora real de llegada del vuelo.  
- **ARR_DELAY**: Diferencia en minutos entre la hora real y la programada de llegada.  
- **CANCELLED**: Indicador de vuelo cancelado (1 = cancelado, 0 = no cancelado).  
- **CANCELLATION_CODE**: Código del motivo de la cancelación.  
- **DIVERTED**: Indicador de vuelo desviado (1 = desviado, 0 = no desviado).  
- **CRS_ELAPSED_TIME**: Duración programada del vuelo (minutos).  
- **ELAPSED_TIME**: Duración real del vuelo (minutos).  
- **AIR_TIME**: Tiempo total de vuelo en el aire (minutos).  
- **DISTANCE**: Distancia del vuelo (millas).  
- **DELAY_DUE_CARRIER**: Retraso atribuible a la aerolínea.  
- **DELAY_DUE_WEATHER**: Retraso atribuible a meteorología.  
- **DELAY_DUE_NAS**: Retraso atribuible al sistema de control aéreo.  
- **DELAY_DUE_SECURITY**: Retraso atribuible a seguridad.  
- **DELAY_DUE_LATE_AIRCRAFT**: Retraso atribuible a llegada tardía de la aeronave.

### Variables creadas durante el análisis (KPIs)

- **YEAR, QUARTER, MONTH, WEEKDAY**: Variables temporales derivadas de `FL_DATE`.  
- **IS_CANCELLED, IS_DIVERTED**: Indicadores booleanos derivados.  
- **IS_ON_TIME_ARR**: Vuelo llegado en hora (`ARR_DELAY ≤ 15`).  
- **IS_DELAYED_ARR**: Vuelo llegado con retraso (`ARR_DELAY > 15`).  
- **DELAY_BUCKET**: Segmentación del retraso en tramos.  
- **SCHED_DIFF_MIN**: Diferencia entre duración real y programada del vuelo.  
- **CRS_DEP_HOUR**: Hora de salida programada.  
- **TIME_BLOCK**: Franja horaria (Noche, Mañana, Mediodía, Tarde).

---

## 🔄 Proceso de Trabajo

### 1. Preparación y unificación de los datos
- Carga de las bases de datos en Jupyter Notebook.
- Unión de los datasets en un único archivo final.
- Revisión de estructura, tipos de datos, valores nulos y duplicados.
- Selección de vuelos con origen **ATL (Aeropuerto de Atlanta)** para reducir el volumen y mejorar la manejabilidad de los datos.

### 2. Funciones creadas durante el análisis
  - **eda_preliminar(df)**  
  Función de análisis exploratorio inicial que permite obtener una primera visión del dataset.  
  Muestra una muestra aleatoria de registros, las dimensiones del conjunto de datos, la información de tipos de datos, el porcentaje de valores nulos, el número de duplicados y las frecuencias de las variables categóricas.  
  Se utiliza para validar la estructura del dataset antes de iniciar la limpieza y transformación de datos.

  - **clean_flights_df(df)**  
  Función de limpieza y normalización de datos aplicada al dataset de vuelos.  
  Convierte la fecha del vuelo a formato datetime, normaliza los indicadores de cancelación y desvío a valores binarios, transforma las columnas horarias al formato `"HH:MM"` y tipa correctamente las variables de tiempo en minutos.  
  Su objetivo es dejar el dataset en un formato consistente y reutilizable para el análisis posterior y la creación de KPIs.

### 3. Limpieza y normalización
- Eliminación de columnas redundantes o sin valor analítico.
- Reordenación de columnas para mejorar la legibilidad.
- Normalización de tipos de datos mediante funciones reutilizables.

### 4. Creación de variables derivadas
- Generación de KPIs operativos, temporales y de puntualidad.
- Segmentación de retrasos y creación de métricas de cumplimiento operativo.

### 5. Control de versiones
- Uso de entorno virtual y estructura organizada del proyecto.
- Control de versiones mediante Git y GitHub.

---

## 📈 Resultados y Análisis

El análisis permitió identificar el impacto del año 2020 en la operativa aérea, así como la recuperación progresiva en los años posteriores. Se observaron diferencias significativas en la puntualidad entre aerolíneas y franjas horarias, destacando la mañana como la franja más puntual y la tarde como la más problemática.

El desglose de retrasos por causa mostró que los factores operativos imputables a la aerolínea y el efecto arrastre de aeronaves retrasadas concentran la mayor parte de los minutos de retraso. Estos resultados fueron validados mediante contrastes estadísticos (ANOVA).

---

## ✅ Conclusiones

- La puntualidad aérea está fuertemente condicionada por factores operativos.
- La franja horaria es un elemento determinante en el retraso de llegada.
- Las cancelaciones son menos frecuentes que los retrasos y se deben principalmente a decisiones operativas y condiciones meteorológicas.
- El retraso en la salida es el principal predictor del retraso en la llegada.

---

## 🔮 Próximos Pasos

- Mejorar el enfoque del informe final mediante un esquema previo del análisis.
- Profundizar en el análisis estadístico por aerolínea.
- Desarrollar un dashboard más avanzado para el seguimiento de KPIs.

---

## ✒️ Autora

- **Beatriz Banegas**
- Proyecto desarrollado como parte del curso de **Data Analytics**.
