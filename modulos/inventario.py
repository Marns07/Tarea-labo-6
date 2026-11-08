import streamlit as st

def mostrar_inventario():
    st.header("Control de Inventario")
    st.write("Bienvenido al módulo de inventario.")
    st.info("Aquí podrás visualizar las existencias actuales.")
    
    # Tabla de demostración de inventario
    datos_inventario = {
        "Producto": ["Laptop HP", "Mouse Inalámbrico", "Teclado Mecánico", "Monitor 24'"],
        "Stock": [15, 42, 28, 10],
        "Estado": ["Normal", "Alto", "Normal", "Bajo"]
    }
    st.table(datos_inventario)
