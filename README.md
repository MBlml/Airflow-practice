# Airflow-practice
#### BARAJAS GOMEZ JUAN MANUEL | 216557005 | COMPUTACION TOLERANTE A FALLAS | 12/03/2023

### OBJETIVO:
Creando un ejemplo basico en Python con Airflow

### DESARROLLO:
Apache Airflow es una plataforma de orquestación de flujos de trabajo de código abierto que permite 
a los desarrolladores y científicos de datos programar y automatizar flujos de trabajo complejos. 
Airflow se implementa con Python y se utiliza principalmente para automatizar procesos ETL (extracción, 
transformación y carga) y análisis de datos.

### EJEMPLO EN PRACTICA:
El código fuente es un programa básico en Apache Airflow que define un DAG (Direct Acyclic Graph) con dos tareas. 
En general, los DAG se utilizan para definir flujos de trabajo complejos que incluyen múltiples tareas y dependencias entre ellas. 
Cada tarea es una unidad de trabajo que puede ser ejecutada por Airflow, como por ejemplo ejecutar un script, enviar un correo electrónico 
o mover archivos.

En este caso, el programa define dos tareas:

La primera tarea, "print_date", utiliza el operador "BashOperator" para ejecutar el comando "date" en la consola del sistema. Esto imprimirá la fecha y hora actual en la consola.
La segunda tarea, "sleep", también utiliza el operador "BashOperator" para ejecutar el comando "sleep 5". Esto hace que la tarea se detenga durante 5 segundos antes de completarse.

La última línea del código (t1 >> t2) indica que la segunda tarea depende de la primera. Esto significa que la segunda tarea no se ejecutará hasta que la primera tarea se haya completado correctamente.

##### _(El codigo se puede descargar en el archivo de la parte superior)_

```python
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'hello_airflow',
    default_args=default_args,
    description='Un DAG simple que imprime "Hola, Airflow!"',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print_hello',
    bash_command='echo "Hola, Airflow!"',
    dag=dag,
)
```

### CONCLUSIÓN:
En conclusión, Apache Airflow es una plataforma de orquestación de flujos de trabajo de código abierto 
que permite a los desarrolladores y científicos de datos programar y automatizar flujos de trabajo complejos. 
Airflow se implementa con Python y se utiliza principalmente para automatizar procesos ETL (extracción, transformación 
y carga) y análisis de datos.

### REFERENCIAS:
_O. (2022, 29 diciembre). ¿Qué es Apache Airflow? Introducción. Aprender BIG DATA. https://aprenderbigdata.com/apache-airflow/_
