from crud import *
from backup import generar_backup
from restore import restaurar_backup
from database import Session
from models import Cliente, Mascota, Consulta

session = Session()


def mostrar_estadisticas():

    total_clientes = session.query(Cliente).count()
    total_mascotas = session.query(Mascota).count()
    total_consultas = session.query(Consulta).count()

    print(f"""
====================================
          ESTADISTICAS
====================================

Clientes registrados : {total_clientes}
Mascotas registradas : {total_mascotas}
Consultas registradas: {total_consultas}

====================================
    """)


def menu():

    while True:

        print("""
╔══════════════════════════════════╗
║        VETERINARIA KAYLO        ║
╠══════════════════════════════════╣
║                                  ║
║  1. Registrar cliente            ║
║  2. Mostrar clientes             ║
║  3. Eliminar cliente             ║
║                                  ║
║  4. Registrar mascota            ║
║  5. Mostrar mascotas             ║
║  6. Eliminar mascota             ║
║                                  ║
║  7. Registrar consulta           ║
║  8. Mostrar consultas            ║
║                                  ║
║  9. Generar backup JSON          ║
║ 10. Restaurar backup             ║
║                                  ║
║ 11. Ver historial LOG            ║
║ 12. Truncar tablas               ║
║ 13. Ver estadisticas             ║
║                                  ║
║ 14. Salir                        ║
║                                  ║
╚══════════════════════════════════╝
        """)

        opcion = input("Seleccione una opcion: ")

        # CLIENTES
        if opcion == "1":
            agregar_cliente()

        elif opcion == "2":
            mostrar_clientes()

        elif opcion == "3":
            eliminar_cliente()

        # MASCOTAS
        elif opcion == "4":
            agregar_mascota()

        elif opcion == "5":
            mostrar_mascotas()

        elif opcion == "6":
            eliminar_mascota()

        # CONSULTAS
        elif opcion == "7":
            registrar_consulta()

        elif opcion == "8":
            mostrar_consultas()

        # BACKUPS
        elif opcion == "9":
            generar_backup()

        elif opcion == "10":
            restaurar_backup()

        # SISTEMA
        elif opcion == "11":
            ver_historial()

        elif opcion == "12":
            truncar_tablas()

        elif opcion == "13":
            mostrar_estadisticas()

        elif opcion == "14":
            print("\nSaliendo del sistema...")
            break

        else:
            print("\nOpcion invalida\n")