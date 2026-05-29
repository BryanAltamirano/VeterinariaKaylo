from database import engine
from models import Base
from menu import menu

def iniciar_sistema():

    Base.metadata.create_all(engine)

    print("""
==================================
   SISTEMA VETERINARIA KAYLO
==================================
    """)

    menu()


if __name__ == "__main__":
    iniciar_sistema()