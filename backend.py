import sqlite3  # Importa el módulo sqlite3 para manejar la base de datos SQLite

# Función para conectar a la base de datos y crear la tabla si no existe
def connect():
    """
    Conecta a la base de datos 'books.db' y crea la tabla 'book' si no existe.
    La tabla tiene las siguientes columnas:
    - id: Identificador único (clave primaria)
    - title: Título del libro (texto)
    - author: Autor del libro (texto)
    - year: Año de publicación (entero)
    - isbn: Número ISBN del libro (entero)
    """
    conn = sqlite3.connect("books.db")  # Conecta a la base de datos (o la crea si no existe)
    cur = conn.cursor()  # Crea un cursor para ejecutar comandos SQL
    # Crea la tabla 'book' si no existe
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()  # Confirma los cambios
    conn.close()  # Cierra la conexión

# Función para insertar un nuevo registro en la tabla
def insert(title, author, year, isbn):
    """
    Inserta un nuevo registro en la tabla 'book'.
    Parámetros:
    - title: Título del libro
    - author: Autor del libro
    - year: Año de publicación
    - isbn: Número ISBN del libro
    """
    conn = sqlite3.connect("books.db")  # Conecta a la base de datos
    cur = conn.cursor()  # Crea un cursor
    # Inserta un nuevo registro en la tabla
    cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)", (title, author, year, isbn))
    conn.commit()  # Confirma los cambios
    conn.close()  # Cierra la conexión

# Función para obtener todos los registros de la tabla
def view():
    """
    Recupera todos los registros de la tabla 'book'.
    Retorna:
    - Una lista de tuplas, donde cada tupla representa un registro.
    """
    conn = sqlite3.connect("books.db")  # Conecta a la base de datos
    cur = conn.cursor()  # Crea un cursor
    cur.execute("SELECT * FROM book")  # Ejecuta la consulta para obtener todos los registros
    rows = cur.fetchall()  # Recupera todos los resultados
    conn.close()  # Cierra la conexión
    return rows  # Retorna los registros

# Función para buscar registros en la tabla
def search(title="", author="", year="", isbn=""):
    """
    Busca registros en la tabla 'book' que coincidan con los parámetros proporcionados.
    Parámetros:
    - title: Título del libro (opcional)
    - author: Autor del libro (opcional)
    - year: Año de publicación (opcional)
    - isbn: Número ISBN del libro (opcional)
    Retorna:
    - Una lista de tuplas con los registros que coinciden.
    """
    conn = sqlite3.connect("books.db")  # Conecta a la base de datos
    cur = conn.cursor()  # Crea un cursor
    # Ejecuta la consulta con los parámetros proporcionados
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()  # Recupera los resultados
    conn.close()  # Cierra la conexión
    return rows  # Retorna los registros que coinciden

# Función para eliminar un registro de la tabla
def delete(id):
    """
    Elimina un registro de la tabla 'book' basado en su ID.
    Parámetros:
    - id: Identificador único del registro a eliminar.
    """
    conn = sqlite3.connect("books.db")  # Conecta a la base de datos
    cur = conn.cursor()  # Crea un cursor
    # Ejecuta la consulta para eliminar el registro con el ID especificado
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()  # Confirma los cambios
    conn.close()  # Cierra la conexión

# Función para actualizar un registro en la tabla
def update(id, title, author, year, isbn):
    """
    Actualiza un registro en la tabla 'book' basado en su ID.
    Parámetros:
    - id: Identificador único del registro a actualizar.
    - title: Nuevo título del libro.
    - author: Nuevo autor del libro.
    - year: Nuevo año de publicación.
    - isbn: Nuevo número ISBN del libro.
    """
    conn = sqlite3.connect("books.db")  # Conecta a la base de datos
    cur = conn.cursor()  # Crea un cursor
    # Ejecuta la consulta para actualizar el registro con el ID especificado
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()  # Confirma los cambios
    conn.close()  # Cierra la conexión

# Llama a la función connect para asegurarse de que la tabla exista al iniciar el programa
connect()

# Ejemplos de uso (comentados para evitar ejecución accidental)
# insert("The sea", "John tablet", 1918, 913123132)  # Inserta un nuevo registro
# delete(3)  # Elimina el registro con ID 3
update(4, "The moon", "John Smooth", 1917, 99999)  # Actualiza el registro con ID 4
print(view())  # Muestra todos los registros
print(search(author="John Smith"))  # Busca registros con el autor "John Smith"
