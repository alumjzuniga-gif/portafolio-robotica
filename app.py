import streamlit as st
import socket
import subprocess
import re
import time

st.set_page_config(
    page_title="Portafolio de Programación y Robótica",
    page_icon="🤖",
    layout="wide"
)

def obtener_url_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return f"http://{ip}:8501"
    except Exception:
        return "http://localhost:8501"

def generar_tunel_publico():
    try:
        proceso = subprocess.Popen(
            ["ssh", "-o", "StrictHostKeyChecking=no", "-R", "80:localhost:8501", "nokey@localhost.run"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        inicio = time.time()
        while time.time() - inicio < 12:
            linea = proceso.stdout.readline()
            if linea:
                coincidencia = re.search(r"https://[a-zA-Z0-9-]+\.lhr\.life", linea)
                if coincidencia:
                    return coincidencia.group(0)
        return None
    except Exception:
        return None

# ==========================================
# ENCABEZADO Y MÉTRICAS (INFORMATIVO)
# ==========================================
st.title("🤖 Portafolio de Ingeniería, Programación y Robótica")
st.subheader("Bitácora técnica de proyectos desarrollados en clase (100% Python / 0% HTML)")
st.write(
    "Este portafolio documenta la transición desde la lógica pura de programación en entornos virtuales "
    "hasta el diseño, fabricación 3D y control de hardware físico."
)

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Módulos Completados", "6 Proyectos", "Software y Hardware")
col_m2.metric("Tecnologías Web", "CodePen & Python", "Zero HTML")
col_m3.metric("Hardware Armado", "Sumo & Brazo 3D", "Sensores y Motores")
col_m4.metric("Manufactura Digital", "Impresión 3D", "Prototipado Rápido")

st.markdown("---")

# ==========================================
# 80% CONTENIDO INFORMATIVO POR PESTAÑAS
# ==========================================
st.header("📚 Documentación Técnica de Clases")

tab_prog, tab_rob, tab_3d = st.tabs([
    "💻 Módulo 1: Programación y Lógica Visual",
    "⚙️ Módulo 2: Robótica Física y Mecánica",
    "🖨️ Módulo 3: Manufactura y Diseño 3D"
])

with tab_prog:
    st.subheader("Desarrollo Web sin HTML y Simulaciones Físicas")
    
    with st.expander("1. Fundamentos de Desarrollo y Arquitectura de Código", expanded=True):
        st.write(
            "Iniciamos comprendiendo la terminología esencial del desarrollo de software: variables, "
            "funciones, ciclos, eventos y manipulación del DOM. El reto principal consistió en construir "
            "interfaces funcionales evitando el uso tradicional de etiquetas HTML."
        )
        st.info("**Conceptos clave:** Sintaxis limpia, renderizado dinámico, gestión de estados y depuración en consola.")

    with st.expander("2. Creación de Robots y Vehículos Virtuales en CodePen", expanded=True):
        st.write(
            "Aplicamos matemáticas y geometría computacional dentro de CodePen para dibujar y animar "
            "carritos y robots desde cero mediante ejes cartesianos (X, Y) y estilos generados dinámicamente."
        )
        st.info("**Conceptos clave:** Coordenadas 2D, jerarquía de componentes visuales y animaciones por fotogramas.")

    with st.expander("3. Simulación de Física: Pelota Multi-Pantalla", expanded=True):
        st.write(
            "Desarrollamos un algoritmo de movimiento continuo donde una esfera rebota dentro de los límites "
            "de la ventana. Al impactar contra bordes específicos, simula atravesar el monitor hacia una segunda pantalla."
        )
        st.info("**Conceptos clave:** Vectores de velocidad, detección de colisiones y ángulos de reflexión.")

with tab_rob:
    st.subheader("Integración de Electrónica, Sensores y Control")

    with st.expander("4. Diseño y Competencia de Carritos de Sumo", expanded=True):
        st.write(
            "Construimos robots autónomos de sumo que detectan al oponente mediante sensores ultrasónicos "
            "o infrarrojos y lo empujan fuera del perímetro sin salirse de la línea blanca."
        )
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown("**Arquitectura de Hardware:**")
            st.write("- Motores DC de alto torque para empuje.")
            st.write("- Sensores de proximidad para rastreo de objetivos.")
            st.write("- Sensores ópticos inferiores para detectar el borde del ring.")
        with col_s2:
            st.markdown("**Estrategia de Ingeniería:**")
            st.write("- Centro de gravedad bajo para evitar volcaduras.")
            st.write("- Distribución de peso sobre las llantas motrices.")
            st.write("- Algoritmo de búsqueda en espiral y ataque frontal.")

    with st.expander("5. Cinemática y Control de Brazo Robótico 3D", expanded=True):
        st.write(
            "Ensamblamos un brazo robótico articulado fabricado pieza por pieza, analizando cómo los grados "
            "de libertad permiten que la pinza alcance cualquier punto en el espacio."
        )
        st.info("**Conceptos clave:** Servomotores PWM, grados de libertad, torque de carga y cinemática directa.")

with tab_3d:
    st.subheader("Del Modelo Digital al Objeto Tangible")

    with st.expander("6. Operación y Calibración de Impresoras 3D", expanded=True):
        st.write(
            "Aprendimos el flujo completo de manufactura aditiva: desde la preparación de archivos STL "
            "en el software laminador hasta la calibración física de la máquina."
        )
        st.write("- **Nivelación de cama caliente:** Fundamental para la adherencia de la primera capa.")
        st.write("- **Control térmico:** Ajuste de temperatura del extrusor (200°C - 215°C para PLA).")
        st.write("- **Relleno (Infill) y soportes:** Balance entre resistencia mecánica y tiempo de impresión.")

st.markdown("---")

# ==========================================
# 20% SECCIÓN INTERACTIVA
# ==========================================
st.header("🎮 Laboratorio Interactivo (20%)")

col_int1, col_int2 = st.columns(2)

with col_int1:

    st.subheader("🦾 Simulador de Ejes del Brazo 3D")
    base = st.slider("Ángulo de Base (Rotación X)", 0, 180, 90)
    codo = st.slider("Ángulo de Codo (Elevación Y)", 0, 180, 45)
    pinza = st.selectbox("Estado de la Pinza", ["Abierta (0°)", "Media (45°)", "Cerrada (90°)"])
    
    import math
    rad_base = math.radians(base)
    rad_codo = math.radians(codo)
    
    x_codo = math.cos(rad_base) * 5
    y_codo = math.sin(rad_base) * 5
    x_pinza = x_codo + math.cos(rad_codo) * 4
    y_pinza = y_codo + math.sin(rad_codo) * 4
    
    st.line_chart(
        {"Altura Y": [0, y_codo, y_pinza]},
        height=200
    )
    
    st.caption(f"Telemetría en vivo -> Base: {base}° | Codo: {codo}° | Pinza: {pinza} | Alcance X: {round(x_pinza, 1)} cm")
    if st.button("Ejecutar secuencia de agarre"):
        st.success(f"¡Posición alcanzada! Base: {base}°, Codo: {codo}°, Pinza: {pinza}")

with col_int2:
    st.subheader("🧠 Reto Rápido de Conocimientos")
    pregunta = st.radio(
        "¿Qué sensor es indispensable en un carrito de sumo para NO salirse solo del ring?",
        [
            "Sensor de temperatura ambiental",
            "Sensor óptico / infrarrojo apuntando al suelo (detecta la línea blanca)",
            "Sensor de humedad"
        ]
    )
    if st.button("Verificar respuesta"):
        if "infrarrojo" in pregunta:
            st.balloons()
            st.success("¡Correcto! El sensor infrarrojo detecta el borde blanco.")
        else:
            st.error("Incorrecto. ¡Inténtalo de nuevo!")

st.markdown("---")

# ==========================================
# ACCESO RÁPIDO DESDE CELULAR (CÓDIGO QR)
# ==========================================
st.header("📱 Acceso Rápido desde Celular")

if "url_activa" not in st.session_state:
    st.session_state.url_activa = "https://portafolio-robotica-sroaoutzezvdytrqgdwtja.streamlit.app/"

col_qr1, col_qr2 = st.columns([1, 2])

with col_qr2:
    st.subheader("Conectar desde cualquier celular")
    st.write("Si el QR abre una página en blanco en tu celular, presiona este botón para activar el enlace público:")
    if st.button("🌐 Activar enlace público para celular"):
        with st.spinner("Creando conexión segura para tu celular..."):
            nuevo_link = generar_tunel_publico()
            if nuevo_link:
                st.session_state.url_activa = nuevo_link
                st.success(f"¡Listo! Escanea el QR actualizado ({nuevo_link})")
            else:
                st.warning("No se pudo crear el túnel automático. Usa tu red Wi-Fi local.")

    url_final = st.text_input("Enlace actual del QR:", value=st.session_state.url_activa)

with col_qr1:
    try:
        import qrcode
        from io import BytesIO
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(url_final)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img_qr.save(buffer, format="PNG")
        st.image(buffer.getvalue(), caption="Escanea con tu cámara", width=220)
    except Exception:
        st.image(f"https://api.qrserver.com/v1/create-qr-code/?size=220x220&data={url_final}", caption="Escanea con tu cámara", width=220)
