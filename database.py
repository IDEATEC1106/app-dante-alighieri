import pymssql

def obtener_conexion():
    """Establece la conexión oficial a la base de datos de la plataforma."""
    return pymssql.connect(
        server='38.224.68.171',
        port=1433,
        user='colegio',
        password='da2380',
        database='PLATAFORMA',
        timeout=8
    )

def ejecutar_login(user):
    """Ejecuta el SP de login y retorna el primer registro encontrado."""
    conn = None
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('sp_Personal_LoginApp', [user])
        return cursor.fetchone()
    except pymssql.Error as ex:
        print(f"Error en sp_Personal_LoginApp: {ex}")
        return None
    finally:
        if conn:
            conn.close()

def obtener_info_alumno(id_alumno):
    """Ejecuta el SP para obtener los datos académicos del estudiante."""
    conn = None
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('sp_Alumno_GetInfoAluApp', [id_alumno])
        return cursor.fetchone()
    except pymssql.Error as ex:
        print(f"Error en sp_Alumno_GetInfoAluApp: {ex}")
        return None
    finally:
        if conn:
            conn.close()

def obtener_cuotas_pendientes(id_alumno):
    """Trae la lista de deudas vigentes desde el procedimiento almacenado."""
    conn = None
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('sp_Alumno_GetAluCuoPenApp', [id_alumno])
        return cursor.fetchall()
    except pymssql.Error as ex:
        print(f"Error en sp_Alumno_GetAluCuoPenApp: {ex}")
        return []
    finally:
        if conn:
            conn.close()

def obtener_cuotas_pagadas(id_alumno):
    """Trae el historial de pagos realizados desde el nuevo procedimiento."""
    conn = None
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(as_dict=True)
        # --- CAMBIADO AL NOMBRE CORRECTO DE TU SP ---
        cursor.callproc('sp_Alumno_GetAluPagosApp', [id_alumno])
        return cursor.fetchall()
    except pymssql.Error as ex:
        print(f"Error en sp_Alumno_GetAluPagosApp: {ex}")
        return []
    finally:
        if conn:
            conn.close()
            
def obtener_comunicados_no_leidos(id_alumno):
    """Trae los comunicados NO leídos ('E') asignados al estudiante."""
    conn = None
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('sp_Comunicados_GetComuExAluApp', [id_alumno])
        return cursor.fetchall()
    except pymssql.Error as ex:
        print(f"Error en sp_Comunicados_GetComuExAluApp: {ex}")
        return []
    finally:
        if conn:
            conn.close()
            
def actualizar_estado_comunicado(id_comunica):
    """Cambia el estado del comunicado de 'E' a 'L' en la base de datos."""
    conn = None
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        # Ejecutamos el SP pasando el parámetro requerido
        cursor.callproc('sp_Comunicados_UpdEsta', [id_comunica])
        conn.commit()  # Confirmamos el cambio en SQL Server
        return True
    except pymssql.Error as ex:
        print(f"Error en sp_Comunicados_UpdEsta: {ex}")
        return False
    finally:
        if conn:
            conn.close()
            
def obtener_comunicados_leidos(id_alumno):
    """Trae los comunicados YA leídos ('L') desde su propio SP."""
    conn = None
    try:
        conn = obtener_conexion()
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('sp_Comunicados_GetComuLxAluApp', [id_alumno])
        return cursor.fetchall()
    except pymssql.Error as ex:
        print(f"Error en sp_Comunicados_GetComuLxAluApp: {ex}")
        return []
    finally:
        if conn:
            conn.close()