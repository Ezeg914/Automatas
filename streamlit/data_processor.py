# data_processor.py
import pandas as pd


def read_data(file_path):
    # Leer el archivo 'Usuarios WiFi.txt' usando Pandas
    df = pd.read_csv(file_path, sep=';')  # Asegúrate de ajustar los separadores según la estructura real del archivo
    return df

def get_sessions_by_id(user_id, data_frame):
    # Filtrar el DataFrame por ID de usuario y devolver las sesiones
    user_sessions = data_frame[data_frame['ID Conexion unico'] == user_id]
    return user_sessions

# Más funciones para manejar otras consultas de datos según las necesidades de la aplicación
