import json

from database import Session
from models import Cliente, Mascota, Consulta
from logger_config import registrar_log

session = Session()


def restaurar_backup():

    # =========================
    # CLIENTES
    # =========================

    with open(
        "backups/clientes.json",
        "r",
        encoding="utf-8"
    ) as archivo:

        clientes = json.load(archivo)

    for cliente in clientes:

        existe = session.query(Cliente).filter_by(
            id_cliente=cliente["id_cliente"]
        ).first()

        if not existe:

            nuevo_cliente = Cliente(
                id_cliente=cliente["id_cliente"],
                nombre=cliente["nombre"],
                telefono=cliente["telefono"],
                direccion=cliente["direccion"]
            )

            session.add(nuevo_cliente)

    # =========================
    # MASCOTAS
    # =========================

    with open(
        "backups/mascotas.json",
        "r",
        encoding="utf-8"
    ) as archivo:

        mascotas = json.load(archivo)

    for mascota in mascotas:

        existe = session.query(Mascota).filter_by(
            id_mascota=mascota["id_mascota"]
        ).first()

        if not existe:

            nueva_mascota = Mascota(
                id_mascota=mascota["id_mascota"],
                nombre=mascota["nombre"],
                especie=mascota["especie"],
                raza=mascota["raza"],
                edad=mascota["edad"],
                id_cliente=mascota["id_cliente"]
            )

            session.add(nueva_mascota)

    # =========================
    # CONSULTAS
    # =========================

    with open(
        "backups/consultas.json",
        "r",
        encoding="utf-8"
    ) as archivo:

        consultas = json.load(archivo)

    for consulta in consultas:

        existe = session.query(Consulta).filter_by(
            id_consulta=consulta["id_consulta"]
        ).first()

        if not existe:

            nueva_consulta = Consulta(
                id_consulta=consulta["id_consulta"],
                fecha=consulta["fecha"],
                diagnostico=consulta["diagnostico"],
                tratamiento=consulta["tratamiento"],
                costo=consulta["costo"],
                id_mascota=consulta["id_mascota"]
            )

            session.add(nueva_consulta)

    session.commit()

    registrar_log("Backup restaurado")

    print("\nRestauracion completada\n")