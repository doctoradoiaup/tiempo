# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:46:06 2024

@author: jperezr
"""

import streamlit as st
from datetime import datetime
import time

# Configurar la fecha del sorteo
fecha_sorteo = datetime(2025, 2, 27)

# Título de la aplicación
st.title("¡Sorteo en camino!")

# Espacio para mostrar el contador
contador = st.empty()

while True:
    # Obtener la fecha y hora actuales
    fecha_actual = datetime.now()

    # Calcular la diferencia
    diferencia = fecha_sorteo - fecha_actual

    # Comprobar si la fecha ha pasado
    if diferencia.total_seconds() <= 0:
        contador.markdown("¡El sorteo ha comenzado!")
        break

    # Calcular días, horas, minutos y segundos restantes
    dias_restantes = diferencia.days
    horas_restantes = diferencia.seconds // 3600
    minutos_restantes = (diferencia.seconds % 3600) // 60
    segundos_restantes = diferencia.seconds % 60

    # Actualizar el contador en la aplicación
    contador.markdown(f"**Faltan:**")
    contador.markdown(f"{dias_restantes} días, {horas_restantes} horas, {minutos_restantes} minutos y {segundos_restantes} segundos para la realización del sorteo.")

    # Esperar 1 segundo antes de actualizar
    time.sleep(1)