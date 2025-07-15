# Book Inventory Desktop Application

## Descripción del Proyecto

Esta es una aplicación de escritorio para gestionar un inventario de libros. Permite a los usuarios realizar operaciones básicas como:

- Ver todos los registros de libros.
- Buscar libros por título, autor, año o ISBN.
- Agregar nuevos libros al inventario.
- Actualizar la información de libros existentes.
- Eliminar libros del inventario.
- Cerrar la aplicación.

La aplicación está construida utilizando `tkinter` para la interfaz gráfica y `sqlite3` para la gestión de la base de datos.

![Interface](/utils/interface.jpeg)

---

## Características

1. **Interfaz gráfica amigable**:
   - Diseñada con `tkinter`, permite a los usuarios interactuar fácilmente con el inventario de libros.

2. **Gestión de base de datos**:
   - Utiliza SQLite para almacenar y gestionar los datos de los libros.

3. **Operaciones CRUD**:
   - Crear, Leer, Actualizar y Eliminar registros de libros.

4. **Portabilidad**:
   - La aplicación puede ser empaquetada como un ejecutable para facilitar su distribución.

---

## Dependencias

Para ejecutar este proyecto, necesitas las siguientes dependencias:

- **Python 3.12 o superior**: Asegúrate de tener Python instalado en tu sistema.
- **tkinter**: Incluido por defecto en la mayoría de las instalaciones de Python.
- **sqlite3**: Incluido por defecto en Python.

Si deseas empaquetar la aplicación como un ejecutable, también necesitas:

- **PyInstaller**: Para instalarlo, ejecuta:
  ```bash
  pip install pyinstaller
  ```

---

## Estructura del Proyecto

El proyecto consta de dos scripts principales:

### 1. `frontend.py`

Este script contiene la lógica de la interfaz gráfica de usuario (GUI). Aquí se definen los elementos visuales y las interacciones del usuario con la aplicación.

#### Funciones principales:

- **`get_selected_row(event)`**:
  - Detecta la fila seleccionada en el `Listbox` y llena los campos de entrada con los datos de esa fila.
  - Permite realizar operaciones como actualizar o eliminar el registro seleccionado.

- **`view_command()`**:
  - Muestra todos los registros de libros en el `Listbox`.

- **`search_command()`**:
  - Busca libros en la base de datos según los criterios ingresados en los campos de entrada.

- **`add_command()`**:
  - Agrega un nuevo libro al inventario utilizando los datos ingresados en los campos de entrada.

- **`delete_command()`**:
  - Elimina el libro seleccionado del inventario.

- **`update_command()`**:
  - Actualiza la información del libro seleccionado con los datos ingresados en los campos de entrada.

#### Elementos visuales:

- **Etiquetas (`Label`)**: Para los campos de título, autor, año e ISBN.
- **Entradas (`Entry`)**: Para que el usuario ingrese datos.
- **Lista (`Listbox`)**: Para mostrar los registros de libros.
- **Botones (`Button`)**: Para realizar operaciones como ver, buscar, agregar, actualizar, eliminar y cerrar la aplicación.
- **Barra de desplazamiento (`Scrollbar`)**: Para navegar por la lista de registros.

---

### 2. `backend.py`

Este script contiene la lógica para interactuar con la base de datos SQLite. Aquí se definen las funciones para realizar operaciones CRUD en la base de datos.

#### Funciones principales:

- **`connect()`**:
  - Conecta a la base de datos `books.db` y crea la tabla `book` si no existe.

- **`insert(title, author, year, isbn)`**:
  - Inserta un nuevo registro en la tabla `book`.

- **`view()`**:
  - Recupera todos los registros de la tabla `book`.

- **`search(title="", author="", year="", isbn="")`**:
  - Busca registros en la tabla `book` que coincidan con los parámetros proporcionados.

- **`delete(id)`**:
  - Elimina un registro de la tabla `book` basado en su ID.

- **`update(id, title, author, year, isbn)`**:
  - Actualiza un registro en la tabla `book` basado en su ID.

#### Base de datos:

- La base de datos `books.db` contiene una tabla llamada `book` con las siguientes columnas:
  - `id`: Identificador único (clave primaria).
  - `title`: Título del libro.
  - `author`: Autor del libro.
  - `year`: Año de publicación.
  - `isbn`: Número ISBN del libro.

---

## Cómo Ejecutar el Proyecto

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Book_Inventory_Desktop_Database
   ```

2. **Ejecuta la aplicación**:
   - En un entorno con Python instalado, ejecuta:
     ```bash
     python frontend.py
     ```

3. **Empaqueta la aplicación (opcional)**:
   - Si deseas crear un ejecutable, utiliza `PyInstaller`:
     ```bash
     pyinstaller frontend.py --onedir --windowed
     ```
   - El ejecutable estará disponible en la carpeta `dist`.

---

## Notas Importantes

- **Compatibilidad con macOS**:
  - Si estás empaquetando la aplicación en macOS, utiliza el modo `--onedir` en lugar de `--onefile` para evitar problemas de compatibilidad.

- **Restricciones de seguridad en macOS**:
  - Si macOS bloquea la ejecución de la aplicación, utiliza el siguiente comando para permitir su ejecución:
    ```bash
    xattr -d com.apple.quarantine /path/to/frontend.app
    ```

---

## Ejemplo de Uso

1. Abre la aplicación.
2. Agrega un nuevo libro ingresando los datos en los campos de entrada y presionando "Add entry".
3. Busca un libro ingresando criterios en los campos de entrada y presionando "Search entry".
4. Selecciona un libro de la lista para actualizar o eliminarlo.
5. Presiona "Update selected" para modificar los datos del libro seleccionado.
6. Presiona "Delete selected" para eliminar el libro seleccionado.