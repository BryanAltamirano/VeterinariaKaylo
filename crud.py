from database import Session
from models import Cliente, Mascota, Consulta
from logger_config import registrar_log
from validations import *

session = Session()

# =========================================
# CRUD CLIENTES
# =========================================

def agregar_cliente():

    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")

    if not validar_texto(nombre):
        print("Nombre invalido")
        return

    if not validar_telefono(telefono):
        print("Telefono invalido")
        return

    if not validar_texto(direccion):
        print("Direccion invalida")
        return

    nuevo_cliente = Cliente(
        nombre=nombre,
        telefono=telefono,
        direccion=direccion
    )

    session.add(nuevo_cliente)
    session.commit()

    registrar_log(f"Cliente agregado: {nombre}")

    print("\nCliente registrado correctamente\n")


def mostrar_clientes():

    clientes = session.query(Cliente).all()

    if not clientes:
        print("\nNo hay clientes registrados\n")
        return

    print("\n===== CLIENTES =====\n")

    for cliente in clientes:

        print(f"""
ID: {cliente.id_cliente}
Nombre: {cliente.nombre}
Telefono: {cliente.telefono}
Direccion: {cliente.direccion}
        """)


def eliminar_cliente():

    id_cliente = input("ID del cliente a eliminar: ")

    cliente = session.query(Cliente).filter_by(
        id_cliente=id_cliente
    ).first()

    if not cliente:
        print("Cliente no encontrado")
        return

    session.delete(cliente)
    session.commit()

    registrar_log(f"Cliente eliminado: {cliente.nombre}")

    print("Cliente eliminado correctamente")


# =========================================
# CRUD MASCOTAS
# =========================================

def agregar_mascota():

    nombre = input("Nombre mascota: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    id_cliente = input("ID del cliente: ")

    if not validar_texto(nombre):
        print("Nombre invalido")
        return

    if not validar_texto(especie):
        print("Especie invalida")
        return

    if not validar_texto(raza):
        print("Raza invalida")
        return

    if not validar_edad(edad):
        print("Edad invalida")
        return

    cliente = session.query(Cliente).filter_by(
        id_cliente=id_cliente
    ).first()

    if not cliente:
        print("Cliente no encontrado")
        return

    nueva_mascota = Mascota(
        nombre=nombre,
        especie=especie,
        raza=raza,
        edad=int(edad),
        id_cliente=id_cliente
    )

    session.add(nueva_mascota)
    session.commit()

    registrar_log(f"Mascota registrada: {nombre}")

    print("\nMascota registrada correctamente\n")


def mostrar_mascotas():

    mascotas = session.query(Mascota).all()

    if not mascotas:
        print("\nNo hay mascotas registradas\n")
        return

    print("\n===== MASCOTAS =====\n")

    for mascota in mascotas:

        cliente = session.query(Cliente).filter_by(
            id_cliente=mascota.id_cliente
        ).first()

        print(f"""
ID Mascota: {mascota.id_mascota}
Nombre: {mascota.nombre}
Especie: {mascota.especie}
Raza: {mascota.raza}
Edad: {mascota.edad}
Dueño: {cliente.nombre}
        """)


def eliminar_mascota():

    id_mascota = input("ID mascota a eliminar: ")

    mascota = session.query(Mascota).filter_by(
        id_mascota=id_mascota
    ).first()

    if not mascota:
        print("Mascota no encontrada")
        return

    session.delete(mascota)
    session.commit()

    registrar_log(f"Mascota eliminada: {mascota.nombre}")

    print("Mascota eliminada correctamente")


# =========================================
# CRUD CONSULTAS
# =========================================

def registrar_consulta():

    id_mascota = input("ID mascota: ")
    fecha = input("Fecha: ")
    diagnostico = input("Diagnostico: ")
    tratamiento = input("Tratamiento: ")
    costo = input("Costo: ")

    mascota = session.query(Mascota).filter_by(
        id_mascota=id_mascota
    ).first()

    if not mascota:
        print("Mascota no encontrada")
        return

    if not validar_costo(costo):
        print("Costo invalido")
        return

    nueva_consulta = Consulta(
        fecha=fecha,
        diagnostico=diagnostico,
        tratamiento=tratamiento,
        costo=float(costo),
        id_mascota=id_mascota
    )

    session.add(nueva_consulta)
    session.commit()

    registrar_log(
        f"Consulta registrada para mascota: {mascota.nombre}"
    )

    print("\nConsulta registrada correctamente\n")


def mostrar_consultas():

    consultas = session.query(Consulta).all()

    if not consultas:
        print("\nNo hay consultas registradas\n")
        return

    print("\n===== CONSULTAS =====\n")

    for consulta in consultas:

        mascota = session.query(Mascota).filter_by(
            id_mascota=consulta.id_mascota
        ).first()

        print(f"""
ID Consulta: {consulta.id_consulta}
Mascota: {mascota.nombre}
Fecha: {consulta.fecha}
Diagnostico: {consulta.diagnostico}
Tratamiento: {consulta.tratamiento}
Costo: ${consulta.costo}
        """)


# =========================================
# TRUNCAR TABLAS
# =========================================

def truncar_tablas():

    confirmacion = input(
        "¿Seguro que deseas borrar todos los registros? (s/n): "
    )

    if confirmacion.lower() != "s":
        print("Operacion cancelada")
        return

    session.query(Consulta).delete()
    session.query(Mascota).delete()
    session.query(Cliente).delete()

    session.commit()

    registrar_log("Tablas truncadas")

    print("\nTablas vaciadas correctamente\n")


# =========================================
# VER HISTORIAL
# =========================================

def ver_historial():

    try:

        with open(
            "logs/historial.log",
            "r",
            encoding="utf-8"
        ) as archivo:

            contenido = archivo.read()

            print("\n===== HISTORIAL =====\n")
            print(contenido)

    except:
        print("No existe historial")