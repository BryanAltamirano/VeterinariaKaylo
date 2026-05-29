from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(15), nullable=False)
    direccion = Column(String(150), nullable=False)


class Mascota(Base):
    __tablename__ = "mascotas"

    id_mascota = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(50), nullable=False)
    raza = Column(String(50), nullable=False)
    edad = Column(Integer, nullable=False)

    id_cliente = Column(
        Integer,
        ForeignKey("clientes.id_cliente"),
        nullable=False
    )


class Consulta(Base):
    __tablename__ = "consultas"

    id_consulta = Column(Integer, primary_key=True)

    fecha = Column(String(30), nullable=False)

    diagnostico = Column(String(300), nullable=False)

    tratamiento = Column(String(300), nullable=False)

    costo = Column(Float, nullable=False)

    id_mascota = Column(
        Integer,
        ForeignKey("mascotas.id_mascota"),
        nullable=False
    )