# PROYECTO_FINAL_VUELOS

## Variables del dataset

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
