import streamlit as st
import math

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Hidrodinámica - Modo Exposición", layout="wide")

# ---------------- PORTADA ----------------
st.title("💧 HIDRODINÁMICA EN SISTEMAS DE TUBERÍAS")
st.subheader("SIMULACIÓN DE FLUJO DE LIQUIDOS - FISICA I")

st.write("""
**Tema:** Aplicación de la ecuación de continuidad y Bernoulli  
**Casos:** Casa, Tanque de almacenamiento, Medidor Venturi  
""")

st.divider()



rho = 1000
g = 9.81

st.markdown("""
### Ecuaciones utilizadas

**Continuidad**

A₁V₁ = A₂V₂

**Bernoulli**

P₁ + ½ρV₁² + ρgh₁ = P₂ + ½ρV₂² + ρgh₂
""")

# ======================================================
# 🏠 CASO CASA
# ======================================================
st.header(" 1. Presión de agua en el hogar (Ejemplo 14.7) ")

st.image("casa.jpg", caption="Ejemplo Serway")

with st.expander("IDENTIFICAR"):
    st.write("""
    Se analiza el flujo de agua en un sistema de tuberías doméstico.
    El fluido es incompresible y en régimen estacionario.
    Se aplican:
    - Ecuación de continuidad
    - Ecuación de Bernoulli
    """)

with st.expander("PLANTEAR"):
    st.write("""
    Se consideran dos puntos:
    - Punto 1: entrada de la tubería (p1, v1, A1)
    - Punto 2: segundo piso (p2, v2, A2)

    Se asume:
    y1 = 0
    y2 = h
    """)

d1 = st.number_input("Diámetro entrada d1 (cm)", value=2.0)
d2 = st.number_input("Diámetro salida d2 (cm)", value=1.0)
v1 = st.number_input("Rapidez de entrada v1 (m/s)", value=1.5)
p1 = st.number_input("Presión inicial p1 (Pa)", value=4e5)
h = st.number_input("Altura h (m)", value=5.0)

d1 = d1 / 100
d2 = d2 / 100

A1 = math.pi * (d1 / 2) ** 2
A2 = math.pi * (d2 / 2) ** 2

# continuidad
v2 = (A1 / A2) * v1
Q = A1 * v1

# bernoulli
p2 = p1 + 0.5*rho*(v1**2 - v2**2) - rho*g*h

with st.expander(" EJECUTAR CÁLCULOS"):
    st.write("Aplicando ecuación de continuidad:")
    st.latex(r"A_1 v_1 = A_2 v_2")

    st.write("Aplicando Bernoulli:")
    st.latex(r"Presion₁ + \frac{1}{2}\rho v_1^2 + \rho g y_1 = Presion₂ + \frac{1}{2}\rho v_2^2 + \rho g y_2")

st.subheader(" RESULTADOS")

col1, col2, col3 = st.columns(3)

col1.metric("Rapidez v2", f"{v2:.2f} m/s")
col2.metric("Presión p2", f"{p2:.0f} Pa")
col3.metric("Caudal Q", f"{Q:.5f} m³/s")

st.divider()

with st.expander(" EVALUACIÓN FÍSICA"):
    st.write("""
    ✔ Al disminuir el diámetro, la rapidez aumenta (continuidad).  
    ✔ Al aumentar la altura, la presión disminuye (energía potencial).  
    ✔ El caudal se mantiene constante en el sistema.
    """)

with st.expander(" VARIABLES USADAS"):
    st.write(f"""
    d1 = {d1} m  
    d2 = {d2} m  
    v1 = {v1} m/s  
    v2 = {v2:.2f} m/s  
    p1 = {p1} Pa  
    p2 = {p2:.0f} Pa  
    h = {h} m  
    """)

st.success("✔ Modelo basado en ecuaciones de Bernoulli y continuidad (Serway)")
# ======================================================
# ⛽ TANQUE
# ======================================================
st.header(" 2. Rapidez de salida (Ejemplo 14.8) ")

st.image("tanque.jpg", caption="Ejemplo Serway")

with st.expander("IDENTIFICAR"):
    st.write("""
    Se analiza el flujo de salida de un tanque abierto o presurizado.
    El fluido es incompresible y se aplica Bernoulli.
    """)

with st.expander("PLANTEAR"):
    st.write("""
    Punto 1: superficie del líquido (p0, v1 ≈ 0, y1 = h)  
    Punto 2: salida del tubo (patm, v2, y2 = 0)  
    """)

p0 = st.number_input("Presión en superficie p0 (Pa)", value=101325)
patm = st.number_input("Presión atmosférica patm (Pa)", value=101325)
h = st.number_input("Altura del líquido h (m)", value=3.0)
A2 = st.number_input("Área de salida A2 (m²)", value=0.01)

rho = 1000
g = 9.81

v2 = math.sqrt(2*g*h + (2*(p0 - patm)/rho))
Q = A2 * v2

with st.expander("EJECUTAR CÁLCULOS"):
    st.latex(r"v_2 = \sqrt{2gh + \frac{2(P_0 - Presionₐₜₘ)}{\rho}}")
    st.latex(r"\frac{dV}{dt} = A_2 v_2")

st.subheader("RESULTADOS")

col1, col2 = st.columns(2)

col1.metric("Rapidez de salida v2", f"{v2:.2f} m/s")
col2.metric("Caudal Q", f"{Q:.5f} m³/s")

st.divider()

with st.expander("EVALUACIÓN FÍSICA"):
    st.write("""
    ✔ Si el tanque está abierto (p0 = patm), se reduce a Torricelli: v = √(2gh).  
    ✔ Mayor altura → mayor velocidad de salida.  
    ✔ El caudal depende del área de salida.
    """)

with st.expander("VARIABLES USADAS"):
    st.write(f"""
    p0 = {p0} Pa  
    patm = {patm} Pa  
    h = {h} m  
    A2 = {A2} m²  
    v2 = {v2:.2f} m/s  
    Q = {Q:.5f} m³/s  
    """)

st.success("✔ Modelo basado en Bernoulli + Torricelli (Serway)")

# ======================================================
# 📏 VENTURI
# ======================================================
st.header(" 3. El medidor Venturi (Ejemplo 14.9) ")

st.image("venturi.jpg", caption="Ejemplo Serway")

with st.expander("IDENTIFICAR"):
    st.write("""
    Se analiza el flujo en un tubo con sección variable.
    Se usa continuidad y Bernoulli para determinar velocidades.
    """)

with st.expander("PLANTEAR"):
    st.write("""
    Punto 1: tubo ancho (A1, v1, p1)  
    Punto 2: garganta (A2, v2, p2)  
    Diferencia de presión relacionada con h.
    """)

A1 = st.number_input("Área A1 (tubo ancho) (m²)", value=0.02)
A2 = st.number_input("Área A2 (garganta) (m²)", value=0.01)
h = st.number_input("Diferencia de altura h (m)", value=0.2)

rho = 1000
g = 9.81

v1 = math.sqrt((2*g*h) / ((A1/A2)**2 - 1))
v2 = (A1/A2) * v1
Q = A1 * v1

with st.expander("EJECUTAR CÁLCULOS"):
    st.latex(r"A_1 v_1 = A_2 v_2")
    st.latex(r"Presion₁ - Presion₂ = \rho g h")
    st.latex(r"v_1 = \sqrt{\frac{2gh}{(A_1/A_2)^2 - 1}}")

st.subheader("RESULTADOS")

col1, col2 = st.columns(2)

col1.metric("v1 (tubo ancho)", f"{v1:.2f} m/s")
col2.metric("v2 (garganta)", f"{v2:.2f} m/s")

st.metric("Caudal Q", f"{Q:.5f} m³/s")

st.divider()

with st.expander("EVALUACIÓN FÍSICA"):
    st.write("""
    ✔ La velocidad aumenta en la garganta (A2 menor).  
    ✔ La presión disminuye en la zona estrecha.  
    ✔ Se conserva el caudal en todo el sistema.
    """)

with st.expander("VARIABLES USADAS"):
    st.write(f"""
    A1 = {A1} m²  
    A2 = {A2} m²  
    h = {h} m  
    v1 = {v1:.2f} m/s  
    v2 = {v2:.2f} m/s  
    Q = {Q:.5f} m³/s  
    """)

st.success("✔ Modelo basado en Bernoulli + Continuidad (Serway)")
