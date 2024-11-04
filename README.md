# Pipeline de DVC para Análisis de Modelos de Machine Learning

Este proyecto implementa un pipeline de Machine Learning utilizando DVC para la gestión de datos y el seguimiento de experimentos. El pipeline permite la carga y preprocesamiento de datos, el entrenamiento de modelos, y la evaluación automática de métricas, además de una búsqueda de hiperparámetros.

## Instrucciones para Reproducir el Proyecto

### Requisitos Previos
- Python 3.8+
- [DVC](https://dvc.org/doc/install)
- Git
- Dependencias adicionales: ver `requirements.txt`

### Instalación

1. Clonar el repositorio:
   ```bash
   git clone <https://github.com/roolzpolo/pipeline_test/>
   cd pipeline_test_1

2. Instalar dependencias
   ```bash
   pip install -r requirements.txt

4. Configurar DVC: Si utilizas almacenamiento remoto para los datos, configurar DVC con:
   ```bash
   dvc remote add -d myremote <URL del almacenamiento remoto>
5. reproducir
   ```bash
   dvc repor

