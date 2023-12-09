import streamlit as st
from streamlit_option_menu import option_menu
from data_processor import read_data, get_sessions_by_id
from validate import validate_date, validate_user_id, validate_mac_ap

def main():
    st.title("Sistema de Reportes de Sesiones de Usuarios")
    st.write("Bienvenido al sistema de reportes de sesiones de usuarios")

    file_path = 'Usuarios WiFi.txt'  # Ruta al archivo de datos

    data = read_data(file_path)  # Lee los datos del archivo al iniciar la aplicación

    # Opciones del menú
    with st.sidebar:
        options = ["Inicio", "Listar todas las sesiones mediante un ID", "Otra opción", "Otra opción más"]
        selected_option = option_menu("Seleccione una opción", options, default_index=0)

    # Opción 1: Inicio
    if selected_option == "Inicio":
        st.table(data.head(10))  # Muestra las primeras 10 filas del DataFrame

    # Opción 2: Listar todas las sesiones mediante un ID
    if selected_option == "Listar todas las sesiones mediante un ID":
        with st.form(key="form1"):
            user_id = st.text_input("Ingrese el ID de usuario:")
            submit_button = st.form_submit_button(label='Mostrar sesiones')
            if submit_button:
                if not validate_user_id(user_id):
                    st.error("ID de usuario inválido. Por favor, ingrese un ID válido.")
                    
        if user_id:
            user_sessions = get_sessions_by_id(user_id, data)
            st.table(user_sessions)
            st.success(f"Se encontraron {len(user_sessions)} sesiones para el ID de usuario {user_id}")
    
    # Opción 3: Otra opción
    if selected_option == "Otra opción":
        st.write("Esta es otra opción")

if __name__ == "__main__":
    main()
