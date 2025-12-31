Adivina Numero
==============

Descripción
-----------
Juego simple de consola para adivinar un número aleatorio entre 1 y 100.

Requisitos
---------
- Python 3.10+ (probado con Python 3.12)

Instalación
-----------
1. Crear y activar un entorno virtual (recomendado):

```bash
python -m venv env
source env/bin/activate
```

2. Instalar dependencias (si las hay):

```bash
pip install -r requirements.txt
```

Uso
---
Ejecutar el comando para jugar (se usará Click para la interfaz CLI):

```bash
python main.py jugar
```

Te pedirá seleccionar una dificultad (1: Easy, 2: Medium, 3: Hard) y luego tendrás un número limitado de intentos para adivinar el número.

Notas
-----
- Se recomienda excluir el entorno virtual (`env/`) del control de versiones. Ya existe una entrada en `.gitignore` para ello.
- Actualmente no hay pruebas automatizadas incluidas.

Contribuciones
--------------
Pull requests bienvenidos. Por favor, abre un *issue* antes de implementar cambios importantes.
