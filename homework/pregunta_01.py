# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import pandas as pd
import zipfile


def pregunta_01():
    #
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    ruta_zip, dir_salida_zip = "files/input.zip", "files/"
    ruta_dir_output = "files/output"

    # Descomprimir el archivo zip
    with zipfile.ZipFile(ruta_zip, "r") as zip_ref:
        zip_ref.extractall(dir_salida_zip)

    # Definir los directorios de entrada y salida
    dir_entrada = os.path.join(dir_salida_zip, "input")
    dir_train = os.path.join(dir_entrada, "train")
    dir_test = os.path.join(dir_entrada, "test")

    # Función para generar el CSV
    def generar_csv(dir_entrada, archivo_salida):
        datos = []
        for sentimiento in ["negative", "positive", "neutral"]:
            dir_sentimiento = os.path.join(dir_entrada, sentimiento)
            for nombre_archivo in os.listdir(dir_sentimiento):
                if nombre_archivo.endswith(".txt"):
                    ruta_archivo = os.path.join(dir_sentimiento, nombre_archivo)
                    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                        frase = archivo.read().strip()
                        datos.append(
                            {
                                "phrase": frase,
                                "target": sentimiento,
                            }
                        )

        df = pd.DataFrame(datos)
        df.to_csv(archivo_salida, index=False)

    # Crear la carpeta de salida si no existe
    os.makedirs(ruta_dir_output, exist_ok=True)

    # Generar los archivos CSV
    generar_csv(dir_train, os.path.join(ruta_dir_output, "train_dataset.csv"))
    generar_csv(dir_test, os.path.join(ruta_dir_output, "test_dataset.csv"))


if __name__ == "__main__":
    pregunta_01()
