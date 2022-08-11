# Data Sources

En nuestro flujo de trabajo ideal tenemos que conectarnos a muchas fuentes de datos.

En la clase de hoy vamos a utilizar pandas para leer varios archivos de datos.

Sabemos que el gerente quiere saber que datasets hubo. De que se tratan, cuales son las caracteristicas. Además pidio la data historica de ypf desde '2012-01-01' hasta'2022-05-02' . Sería bueno saber el precio máximo y el mínimo de cierre y la fecha. Para esto vamos a utilizar la librería `pandas`.

## Datasets de Jorge:
* ventas_comercial
* para_borrar.tsv
* tarea_del_nene.csv
* alllines.txt
EXTRA:
* 💡 **Tip**  https://pypi.org/project/yfinance/





### Repo vs Estructura de Trabajo

La estructura del repositorio simplemente es el orden de las carpetas de un proyecto. Cada team puede tener su convención y su orden. Cuestión que luego puede devenir en problemas de **reproducibilidad** del proyecto respecto a otros equipos.

```
proyecto_ejemplo/
├── data/ 
│   └── 01_raw              Data inmutable, en lo posible raw de una fuente de datos
│   └── 02_intermediate     Data con transformaciones
│   └── 03_primary          Esta definición se adapta a cada proyecto. Es data que sirve ya para exploraciones.
│   └── 04_feature          Pueden ser variables establecidas
|   └── 05_model_input      Train,test,validation.
│   └── 06_models           El modelo ya eentrenado (es una estructura de datos y no una fuente)
│   └── 07_model_output     predict
│   └── 07_reporting        Pueden ser reportes para presentar.
│ 
├── laboratory/             notebooks en una instancia de laboratorio, en nuestro caso con titulo del tema
│   └── eda                 Exploración de la data
│   └── preprocessing       Preprocesamiento de la data, posiblemente para creación de features
│   └── model_training      Implementaciones de algoritmos
│   └── evaluation          Testeo y evaluación
|
├── figures/                Imagenes guardadas de plots o resultados
├── output/                 outputs, pesos de modelos, prediccion o hiperparámetros óptimos 
├── source/                 modulos creados por nosotros
│   └── __init__.py      Make the folder a package.
    └── process.py       Example module.
├── environment.yml      Virtual environment definition.
├── README.md            README with info of the project.
└── requirements.txt     Install requeriments.
```


Hay dos grandes tipos de repositorios para nuestra profesión, los que están en modo laboratorio (cómo el nuestro) y los que están en modo producción en los cuales desarrollan un "pipeline" 

Los equipos tienden a comenzar con un flujo de trabajo manual, donde no existe una infraestructura real. La recopilación de datos, la limpieza de datos, el entrenamiento de modelos y la evaluación probablemente se escriban en un solo cuaderno. El cuaderno se ejecuta localmente para producir un modelo, que se entrega a un ingeniero encargado de convertirlo en un punto final de API. Esencialmente, en este flujo de trabajo, el modelo es el producto.
