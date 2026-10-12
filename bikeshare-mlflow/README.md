# Experimentos de demanda de bicicletas con MLflow

Proyecto generado con Cookiecutter para llevar el modelo de SeoulBikeData del
notebook exploratorio a ejecuciones CLI reproducibles. Conserva la regresión
lineal original como referencia y registra Random Forest parametrizados en un
experimento MLflow independiente.

## Organización del código

- `run_experiment.py`: punto de entrada CLI y presentación del resultado.
- `bikeshare/data_loading.py`: lectura del CSV y validación de columnas.
- `bikeshare/cleaning.py`: conversiones, eliminación de duplicados y filas inválidas.
- `bikeshare/preprocessing.py`: variables de calendario, split cronológico e imputación/codificación.
- `bikeshare/modeling.py`: ajuste del Random Forest y la regresión lineal de referencia.
- `bikeshare/evaluation.py`: métricas y artefactos gráficos/JSON.
- `bikeshare/tracking.py`: experimento, parámetros, métricas, artefactos y modelo MLflow.
- `bikeshare/pipeline.py`: coordina las etapas sin concentrar su lógica.
- `bikeshare/settings.py` y `bikeshare/cli.py`: configuración común y argumentos CLI.

## Requisitos y datos

- Python 3.14.7 (versión usada para estas corridas).
- `pip install -r requirements.txt`.
- El CSV `data/SeoulBikeData.csv`, leído con codificación `cp1252`.

## Una corrida

Desde esta carpeta, sin argumentos:

```powershell
python run_experiment.py
```

Los valores por defecto son 120 árboles, profundidad 12, hoja mínima 1,
`max_features=1.0`, semilla 42 y prueba cronológica de 20%. Cambia los
hiperparámetros directamente desde la CLI, sin editar el script:

```powershell
python run_experiment.py --n-estimators 160 --max-depth 8 --min-samples-leaf 2 --max-features 0.8 --random-state 42
```

`--data` permite indicar otro CSV y `--experiment-name` cambia el experimento.
La partición reserva siempre el tramo final ordenado por fecha y hora; las
imputaciones/codificación se ajustan solo con entrenamiento. Los predictores
numéricos se imputan con mediana y las categorías se codifican con One-Hot.

## Cinco corridas de comparación

Con el entorno virtual activo, ejecutar desde esta carpeta:

```powershell
python run_five.py
```

El script fija cuatro hiperparámetros y compara cinco profundidades del árbol;
cada corrida se añade al experimento `SeoulBikeData - experimentacion Random Forest`.
Para comprobar reproducibilidad, repetir uno de los comandos con los mismos
argumentos y contrastar métricas y parámetros.


## Declaración de uso de Copilot

Se utilizó Copilot únicamente como apoyo para revisar la redacción y la
ortografía de este README.
