import logging

logging.basicConfig(
    filename='logs/historial.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar_log(mensaje):
    logging.info(mensaje)