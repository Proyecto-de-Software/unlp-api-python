# Proyecto 2018 aplicación de ejemplo

Aplicación de ejemplo para la cátedra de Proyecto de Software de la UNLP.

## Iniciar ambiente

### Requisitos

- python3
- virtualenv

### Ejecución

```bash
$ virtualenv -p python3 venv
# Para iniciar el entorno virtual
$ . venv/bin/activate
# Instalar las dependencias dentro del entorno virtual
$ pip install -u requirements.txt
# En el directorio raiz
$ FLAS_EN=dev python run.py
```

Para salir del entorno virutal, ejecutar:

```bash
$ deactivate
```

## Estructura de carpetas del proyecto

```bash
config            # Módulo de donde se obtienen las variables de configuración
helpers           # Módulo donde se colocan funciones auxiliares para varias partes del código
models            # Módulo con la lógica de negocio de la aplicación y la conexión a la base de datos
resources         # Módulo con los controladores de la aplicación (parte web)
templates         # Módulo con los templates
db.py             # Instancia de base de datos
__init__.py       # Instancia de la aplicación y ruteo
```

## TODO

- [ ] Usar una hoja de estilos simple para que quede de ejemplo.
