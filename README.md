# 📊 PROYECTO FINAL: Análisis de Cancelaciones y Retrasos de Aerolíneas

## 📖 Descripción del Proyecto

Este proyecto tiene como objetivo analizar las **cancelaciones y los retrasos en vuelos comerciales**, utilizando datos reales del sector aéreo. A través del estudio de dos bases de datos con información complementaria, se busca comprender el comportamiento operativo de las aerolíneas y los factores que influyen en la puntualidad de los vuelos.

El análisis se centra en identificar patrones temporales, causas principales de retrasos y cancelaciones, así como posibles relaciones entre distintas variables operativas del vuelo.

---

## 🗂️ Bases de Datos Utilizadas

El proyecto se apoya en dos bases de datos principales en formato csv, y extraidas de la web de kaggle.com, que comparten una estructura común y permiten realizar un análisis conjunto:

- **Base de datos de vuelos** (flight_details.csv) 
  Contiene información general de cada vuelo, como la fecha, aerolínea, número de vuelo, aeropuerto de origen y destino, horarios programados y reales, tiempos de taxi, duración del vuelo y distancia recorrida.

- **Base de datos de retrasos y cancelaciones** (flight_delays.csv) 
  Incluye información específica sobre incidencias, como el estado del vuelo (cancelado o no), códigos de cancelación y el desglose de los retrasos según su causa (operativa de la aerolínea, condiciones meteorológicas, sistema nacional del espacio aéreo, seguridad y retrasos por aeronave).

Estas bases de datos permiten analizar no solo si un vuelo se retrasa o se cancela, sino también **el motivo y la magnitud del retraso**.

---

## 🎯 Objetivos del Análisis

Los principales objetivos de este proyecto son:

- Analizar la frecuencia de **cancelaciones y retrasos** en los vuelos.
- Identificar las **principales causas de los retrasos**.
- Estudiar la evolución temporal de las incidencias.
- Comparar el comportamiento entre aerolíneas y rutas concretas.
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

## Variables del dataset:

- **`FL_DATE`**: Fecha del vuelo.
- **`AIRLINE_CODE`**: Código de la aerolínea que opera el vuelo.
- **`DOT_CODE`**: Código identificador de la aerolínea asignado por el Department of Transportation (DOT).
- **`FL_NUMBER`**: Número del vuelo.
- **`ORIGIN`**: Código IATA del aeropuerto de origen.
- **`ORIGIN_CITY`**: Ciudad del aeropuerto de origen.
- **`DEST`**: Código IATA del aeropuerto de destino.
- **`DEST_CITY`**: Ciudad del aeropuerto de destino.
- **`CRS_DEP_TIME`**: Hora de salida programada del vuelo (CRS – Computer Reservation System).
- **`DEP_TIME`**: Hora real de salida del vuelo.
- **`DEP_DELAY`**: Diferencia en minutos entre la hora real y la hora programada de salida (positivo = retraso, negativo = salida anticipada).
- **`TAXI_OUT`**: Minutos desde que el avión abandona la puerta hasta el despegue.
- **`WHEELS_OFF`**: Hora en la que el avión despega.
- **`WHEELS_ON`**: Hora en la que el avión aterriza.
- **`TAXI_IN`**: Minutos desde el aterrizaje hasta la llegada a la puerta.
- **`CRS_ARR_TIME`**: Hora de llegada programada del vuelo.
- **`ARR_TIME`**: Hora real de llegada del vuelo.
- **`ARR_DELAY`**: Diferencia en minutos entre la hora real y la hora programada de llegada (positivo = retraso, negativo = llegada anticipada).
- **`CANCELLED`**: Indicador de vuelo cancelado (`1` = cancelado, `0` = no cancelado).
- **`CANCELLATION_CODE`**: Código del motivo de la cancelación (solo tiene valor cuando `CANCELLED = 1`).
    - **`A` – Carrier**: Cancelación debida a la aerolínea (operaciones, mantenimiento, tripulación, planificación).
    - **`B` – Weather**: Cancelación debida a condiciones meteorológicas adversas.
    - **`C` – NAS**: Cancelación debida a control aéreo / saturación del espacio aéreo (National Airspace System).
    - **`D` – Security**: Cancelación debida a motivos de seguridad.
- **`DIVERTED`**: Indicador de vuelo desviado (`1` = desviado, `0` = no desviado).
- **`CRS_ELAPSED_TIME`**: Duración total programada del vuelo (minutos).
- **`ELAPSED_TIME`**: Duración total real del vuelo (minutos), incluyendo rodaje.
- **`AIR_TIME`**: Tiempo total de vuelo en el aire (minutos).
- **`DISTANCE`**: Distancia del vuelo (millas).
- **`DELAY_DUE_CARRIER`**: Minutos de retraso atribuibles a causas de la aerolínea.
- **`DELAY_DUE_WEATHER`**: Minutos de retraso atribuibles a meteorología.
- **`DELAY_DUE_NAS`**: Minutos de retraso atribuibles al sistema de control aéreo (NAS).
- **`DELAY_DUE_SECURITY`**: Minutos de retraso atribuibles a seguridad.
- **`DELAY_DUE_LATE_AIRCRAFT`**: Minutos de retraso atribuibles a llegada tardía del avión en un vuelo anterior.

## Variables del dataset (añadidas durante el análisis para la creación de KPIs):

- **YEAR**: Año extraído de `FL_DATE`. Útil para filtros y agregaciones anuales.
- **QUARTER**: Trimestre (1–4) extraído de `FL_DATE`. Útil para análisis trimestral.
- **MONTH**: Mes (1–12) extraído de `FL_DATE`. Útil para series temporales mensuales.
- **WEEKDAY**: Día de la semana extraído de `FL_DATE` (Monday, Tuesday, etc.). Útil para analizar patrones por día.
- **IS_CANCELLED**: Indicador booleano (True/False) derivado de `CANCELLED` (1/0). Se usa para excluir cancelaciones en KPIs de puntualidad y retrasos.
- **IS_DIVERTED**: Indicador booleano (True/False) derivado de `DIVERTED` (1/0). Se usa para KPIs de vuelos desviados y filtros operativos.
- **IS_ON_TIME_ARR**: Indicador booleano (True/False) que marca si el vuelo llegó en hora:
  - `ARR_DELAY <= 15` y `IS_CANCELLED = False`.
- **IS_DELAYED_ARR**: Indicador booleano (True/False) que marca si el vuelo llegó con retraso:
  - `ARR_DELAY > 15` y `IS_CANCELLED = False`.
- **DELAY_BUCKET**: Segmentación del retraso en llegada (`ARR_DELAY`) en tramos (solo para vuelos no cancelados):
  - `Early (<0)`: llegada adelantada
  - `0-15`: llegada en hora
  - `16-30`: retraso moderado
  - `31-60`: retraso alto
  - `>60`: retraso severo  
  Se usa para gráficos de distribución de retrasos (p. ej. apilado 100%).
- **SCHED_DIFF_MIN**: Diferencia en minutos entre duración real y duración programada:
  - `SCHED_DIFF_MIN = ELAPSED_TIME - CRS_ELAPSED_TIME`  
  Valores positivos indican que el vuelo tardó más de lo previsto; valores negativos, menos de lo previsto.
- **CRS_DEP_HOUR**: Hora (0–23) extraída de `CRS_DEP_TIME` (formato "HH:MM"). Útil para análisis por hora de salida.
- **TIME_BLOCK**: Franja horaria basada en `CRS_DEP_HOUR`:
  - `Noche` (00:00–05:59)
  - `Mañana` (06:00–11:59)
  - `Mediodía` (12:00–17:59)
  - `Tarde` (18:00–23:59)  
  Útil para comparar volumen y puntualidad por franja horaria.

---

## Resumen del trabajo realizado

### 1. Preparación y unificación de los datos
- Carga de las bases de datos de vuelos en Jupyter Notebook (.ipynb).
- Unión de las distintas bases de datos en un único dataset final (`df_final`).
- Verificación inicial de estructura, tipos de datos, valores nulos y duplicados.
- Tomamos la decisión de analizar sólo los vuelos con ORIGIN de ATL (Aeropuerto de Altanta) al comprobar que las bases de datos son poco manejables debido a su tamaño.

### 2. Limpieza de columnas
- Eliminación de columnas no relevantes o redundantes para el análisis y los KPIs:
  - `Unnamed: 0` (índice antiguo sin valor analítico)
  - `AIRLINE_DOT` (información redundante con `AIRLINE`)
  - `DOT_CODE` (identificador técnico no necesario para el dashboard)
  - `ORIGIN_CITY` (redundante al analizar un único aeropuerto)
- Reordenación de columnas para mejorar la legibilidad del dataset (ORIGIN como columna principal).

### 3. Normalización de tipos de datos
Se crearon dos funciones reutilizables para aplicar la limpieza de tipos de datos:
- `eda_preliminar`
- `clean_flights_df(df)`


### 4. Creación de columnas derivadas para KPIs
Se añadieron nuevas variables necesarias para el análisis y el dashboard:
- Variables temporales: `YEAR`, `QUARTER`, `MONTH`, `WEEKDAY`
- Flags operativos: `IS_CANCELLED`, `IS_DIVERTED`
- Puntualidad:
  - `IS_ON_TIME_ARR` (ARR_DELAY ≤ 15, no cancelado)
  - `IS_DELAYED_ARR` (ARR_DELAY > 15, no cancelado)
- Segmentación de retrasos:
  - `DELAY_BUCKET` (Early, 0–15, 16–30, 31–60, >60)
- Cumplimiento de planificación:
  - `SCHED_DIFF_MIN` = ELAPSED_TIME − CRS_ELAPSED_TIME
- Análisis por hora:
  - `CRS_DEP_HOUR`
  - `TIME_BLOCK` (Noche, Mañana, Mediodía, Tarde)

### 5. Estructura del proyecto y control de versiones
- Organización del proyecto con entorno virtual (`proyecto_final.venv`) y carpeta `src` para código reutilizable.
- Uso de Git para control de versiones:
- Preparación del proyecto para continuar con la fase de análisis de KPIs y posterior creación del dashboard en Excel.

En este punto, el dataset final está limpio, tipado correctamente y enriquecido con todas las columnas necesarias para calcular los KPIs definidos y construir el dashboard operativo.

---

## Resumen del análisis realizado

El proyecto se ha desarrollado siguiendo un enfoque de análisis de datos progresivo, combinando análisis exploratorio, visualización y estadística inferencial.

En primer lugar, se analizó el **volumen de vuelos por aerolínea y año**, lo que permitió identificar el impacto de 2020 en la operativa aérea y la posterior recuperación parcial en los años siguientes. A partir de este análisis se seleccionaron las **10 aerolíneas con mayor volumen**, agrupando el resto bajo la categoría *Other* para mejorar la legibilidad de los resultados.

Posteriormente, se estudió la **puntualidad de llegada por aerolínea**, así como la evolución del **retraso medio de llegada por año**, identificando diferencias claras entre compañías y una tendencia general al aumento de los retrasos en los últimos años del periodo analizado.

El análisis por **franja horaria** mostró patrones consistentes en todas las aerolíneas, destacando la mañana como la franja más puntual y la tarde como la más problemática. Estos resultados fueron validados mediante un **contraste de hipótesis (ANOVA)**, confirmando que las diferencias observadas entre franjas horarias son estadísticamente significativas.

A continuación, se realizó un **desglose de los retrasos por causa**, evidenciando que los factores operativos imputables a la aerolínea y el efecto arrastre de aeronaves retrasadas concentran la mayor parte de los minutos de retraso. En paralelo, se analizó la **tasa y los motivos de cancelación**, concluyendo que las cancelaciones son poco frecuentes y están principalmente asociadas a decisiones operativas y a condiciones meteorológicas.

Finalmente, se incorporó un análisis estadístico avanzado mediante **medidas de dispersión** y **correlaciones**, demostrando que la variabilidad y los retrasos extremos son tan relevantes como el retraso medio, y que el retraso de llegada está fuertemente condicionado por el retraso en la salida, mientras que la distancia del vuelo tiene un impacto prácticamente nulo.

---

  ## Conclusiones finales

El análisis realizado sobre la operativa de vuelos permite extraer las siguientes conclusiones principales:

- El volumen de vuelos experimenta una caída generalizada en 2020, seguida de una recuperación progresiva en los años posteriores. No obstante, en 2023 varias aerolíneas aún no alcanzan los niveles previos a 2019.
- Existen diferencias claras en la puntualidad de llegada entre aerolíneas. Algunas compañías regionales presentan un comportamiento más estable y puntual, mientras que aerolíneas con mayor volumen muestran una mayor variabilidad en los retrasos.
- El análisis por franja horaria evidencia un patrón consistente: los vuelos programados por la mañana son los más puntuales, mientras que la franja de tarde concentra los mayores retrasos medios.
- Un contraste de hipótesis (ANOVA) confirma que las diferencias en el retraso medio entre franjas horarias son estadísticamente significativas, por lo que la franja horaria es un factor determinante en la puntualidad de llegada.
- El estudio de las causas de los retrasos muestra que los factores operativos imputables a la aerolínea y el efecto arrastre de aeronaves retrasadas son las principales fuentes de minutos de retraso, por encima de causas meteorológicas o de seguridad.
- Las cancelaciones son poco frecuentes en comparación con los retrasos. Cuando ocurren, están principalmente asociadas a decisiones de la aerolínea y a condiciones meteorológicas adversas.
- El análisis de dispersión revela que no solo importa el retraso medio, sino también la estabilidad operativa. Algunas aerolíneas presentan una alta variabilidad y una mayor probabilidad de retrasos extremos, lo que impacta negativamente en la experiencia del pasajero.
- El análisis de correlaciones confirma que el retraso de llegada está fuertemente condicionado por el retraso en la salida, mientras que variables como la distancia del vuelo tienen un impacto prácticamente nulo.

En conjunto, los resultados indican que los problemas de puntualidad están principalmente ligados a factores operativos y de gestión, y que la recuperación del tráfico aéreo tras 2020 ha venido acompañada de un incremento en la complejidad operativa y en los retrasos.


