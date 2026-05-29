import json

from database import Session
from models import Cliente, Mascota, Consulta
from logger_config import registrar_log

session = Session()


def generar_backup():

    # =========================
    # CLIENTES
    # =========================

    clientes = session.query(Cliente).all()

    datos_clientes = []

    for cliente in clientes:

        datos_clientes.append({
            "id_cliente": cliente.id_cliente,
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
            "direccion": cliente.direccion
        })

    with open(
        "backups/clientes.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos_clientes,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    # =========================
    # MASCOTAS
    # =========================

    mascotas = session.query(Mascota).all()

    datos_mascotas = []

    for mascota in mascotas:

        datos_mascotas.append({
            "id_mascota": mascota.id_mascota,
            "nombre": mascota.nombre,
            "especie": mascota.especie,
            "raza": mascota.raza,
            "edad": mascota.edad,
            "id_cliente": mascota.id_cliente
        })

    with open(
        "backups/mascotas.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos_mascotas,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    # =========================
    # CONSULTAS
    # =========================

    consultas = session.query(Consulta).all()

    datos_consultas = []

    for consulta in consultas:

        datos_consultas.append({
            "id_consulta": consulta.id_consulta,
            "fecha": consulta.fecha,
            "diagnostico": consulta.diagnostico,
            "tratamiento": consulta.tratamiento,
            "costo": consulta.costo,
            "id_mascota": consulta.id_mascota
        })

    with open(
        "backups/consultas.json",
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos_consultas,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    registrar_log("Backup generado")

    print("\nBackup generado correctamente\n")