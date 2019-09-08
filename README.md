# proyecto2018-unlp-api-python
Demo de uso de python con frontend Vue

## Iniciar ambiente

### Requisitos

- python3
- virtualenv

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

TODO
----

- [ ] Retornar json para ejemplo de api rest.
- [ ] Mejorar el modulo de configuración. Tal vez sea mejor una clase que una función.
- [ ] Usar una hoja de estilos simple para que quede de ejemplo.
