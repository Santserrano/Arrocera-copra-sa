# Arrocera Copra S.A
![head](header.png)
### Instalación desde CMD o Powershell

```bash
git clone https://github.com/Santserrano/Arrocera-copra-sa.git

```
### Contruir el Sistema 
Ejecute el archivo `db_ordenes.py` para construir la base de datos de Usuarios y Ordenes.
Una vez ejecutado el archivo anterior, puedo correr `login.py` para comenzar a utilizar el sistema.

![head](interfaces.png)

Los roles y cuentas de acceso en la base de datos se encuentran definidas de la siguiente manera.
```bash
def db_usuarios():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    usuario TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    rol TEXT NOT NULL)''')

    usuarios = [
        ('gerente_general', '1234', 'Gerente_general'),
        ('gerente_transporte', '1234', 'Gerente_transporte'),
        ('gerente_produccion', '1234', 'Gerente_producción')
    ]

    c.executemany('INSERT OR IGNORE INTO usuarios (usuario, password, rol) VALUES (?, ?, ?)', usuarios)

    conn.commit()
    conn.close()
```
### Entendiendo el funcionamiento
Dentro de la carpeta `components` se encuentran los archivos correspondientes a cada interfaz, así también como la base de datos.
- `login.py` Interfaz de inicio de sesión
- `db_ordenes.py` Base de datos
- `ID_log.py` Interfaz gerente general
- `ID_log2.py` Interfaz gerente de transporte
- `mapa_transporte.py` Mapa de los recorridos
- `nueva_orden.py` Formulario nuevas ordenes
- `config_acc.py` Configuración de cuenta
- `ops_transporte.py` Listado operaciones de transporte
### Configurar git 

Clone el repositorio como se menciona en el inicio de la documentación.
Luego, utilizando CMD o Windows Powershell posicionado en la carpeta del proyecto, realice los cambios pertinentes y haga uso de los siguientes comandos para generar el commit y que se vea reflejada la actualización.

En "Descripción breve de los cambios realizados" puede reemplazar con un comentario acerca de los cambios que realizó.

```bash
git add .
git commit -m "Descripción breve de los cambios realizados"
git push origin master
```

También puede utilizar el siguiente comando para verificar el estado de los cambios que aún no han sido guardados:
```bash
git status
```

Para actualizar el repositorio local con el repositorio actualizado en github, utilice el siguiente comando:
```bash
git pull
```
