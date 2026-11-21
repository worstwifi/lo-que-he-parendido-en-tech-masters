import streamlit as st

# ------------------------------------------------------------
# TECH MASTER
# Landing page estudiantil desarrollada con Python + Streamlit.
# El contenido representa los temas trabajados en el taller.
# ------------------------------------------------------------

st.set_page_config(
    page_title="Tech Master | Lo que aprendimos",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Estilos ----------
st.markdown(
    """
    <style>
    :root {
        --cyan: #06b6d4;
        --cyan-dark: #0891b2;
        --ink: #17212b;
        --muted: #64748b;
        --line: #e7edf2;
        --soft: #f5f9fb;
    }

    .stApp {
        background: #ffffff;
        color: var(--ink);
    }

    .block-container {
        max-width: 1220px;
        padding-top: 2.2rem;
        padding-bottom: 3.5rem;
    }

    [data-testid="stSidebar"] {
        background: #fbfdfe;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #64748b;
    }

    h1, h2, h3 {
        color: var(--ink);
        letter-spacing: -0.035em;
    }

    h1 { font-weight: 800; }
    h2, h3 { font-weight: 750; }

    p, li {
        color: #526273;
        line-height: 1.7;
    }

    .eyebrow {
        color: var(--cyan-dark);
        font-size: .76rem;
        font-weight: 800;
        letter-spacing: .16em;
        text-transform: uppercase;
        margin-bottom: .8rem;
    }

    .hero {
        position: relative;
        overflow: hidden;
        border: 1px solid #dceef2;
        border-radius: 28px;
        padding: clamp(1.5rem, 4vw, 3.2rem);
        background:
            radial-gradient(circle at 83% 18%, rgba(6,182,212,.13), transparent 24%),
            radial-gradient(circle at 92% 85%, rgba(8,145,178,.10), transparent 25%),
            linear-gradient(135deg, #ffffff 0%, #f5fbfd 62%, #effbfe 100%);
        min-height: 350px;
    }

    .hero h1 {
        max-width: 760px;
        font-size: clamp(2.35rem, 5.5vw, 4.5rem);
        line-height: 1.02;
        margin: .35rem 0 1rem 0;
        color: #12212c;
    }

    .hero-copy {
        max-width: 680px;
        font-size: 1.08rem;
        color: #5b6b78;
    }

    .hero-art {
        position: absolute;
        width: min(34%, 340px);
        right: 4%;
        top: 50%;
        transform: translateY(-50%);
        opacity: .95;
        pointer-events: none;
    }

    .pill {
        display: inline-block;
        border: 1px solid #c9edf4;
        background: #e9faff;
        color: #087e9d;
        border-radius: 999px;
        padding: .38rem .75rem;
        margin: .2rem .28rem .15rem 0;
        font-size: .78rem;
        font-weight: 700;
    }

    .section-kicker {
        color: var(--cyan-dark);
        text-transform: uppercase;
        letter-spacing: .13em;
        font-size: .72rem;
        font-weight: 800;
        margin-bottom: .35rem;
    }

    .topic-card {
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1.15rem 1.2rem;
        background: #fff;
        min-height: 158px;
        transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
        animation: rise .55s ease both;
    }

    .topic-card:hover {
        transform: translateY(-5px);
        border-color: #9eddea;
        box-shadow: 0 14px 32px rgba(8, 145, 178, .10);
    }

    .topic-icon {
        width: 42px;
        height: 42px;
        border-radius: 13px;
        display: grid;
        place-items: center;
        color: #0786a3;
        background: #e8faff;
        font-size: 1.35rem;
        margin-bottom: .8rem;
    }

    .topic-card h3 {
        font-size: 1.08rem;
        margin: 0 0 .35rem 0;
    }

    .topic-card p {
        font-size: .91rem;
        margin: 0;
    }

    .info-panel {
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1.25rem;
        background: #fbfdfe;
    }

    .soft-note {
        background: #effbfe;
        border-left: 4px solid var(--cyan);
        padding: .9rem 1rem;
        border-radius: 0 12px 12px 0;
        color: #45616b;
        margin: .8rem 0;
    }

    .footer {
        border-top: 1px solid var(--line);
        padding-top: 1.4rem;
        margin-top: 3rem;
        color: #82909c;
        font-size: .82rem;
    }

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #06a9c7;
        background: #06b6d4;
        color: white;
        font-weight: 700;
        padding: .58rem 1rem;
        transition: all .2s ease;
    }

    .stButton > button:hover {
        background: #0891b2;
        border-color: #0891b2;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(6, 182, 212, .18);
    }

    div[data-testid="stMetric"] {
        background: #f7fbfc;
        border: 1px solid var(--line);
        border-radius: 15px;
        padding: 1rem;
    }

    div[data-testid="stExpander"] {
        border: 1px solid var(--line);
        border-radius: 14px;
    }

    .stProgress > div > div > div > div {
        background-color: var(--cyan);
    }

    @keyframes rise {
        from { opacity: 0; transform: translateY(9px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 800px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1.2rem;
        }
        .hero {
            min-height: auto;
            padding: 1.5rem;
        }
        .hero-art {
            position: relative;
            display: block;
            width: 72%;
            max-width: 260px;
            right: auto;
            top: auto;
            transform: none;
            margin: 1rem auto 0 auto;
        }
        .hero h1 {
            font-size: clamp(2.1rem, 10vw, 3.2rem);
        }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: .01ms !important;
            transition-duration: .01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Navegación ----------
PAGES = [
    "Inicio",
    "¿Qué es SVG?",
    "Cambiar colores",
    "Animaciones y transiciones",
    "HTML básico",
    "Electrónica básica",
    "Zona interactiva",
    "Compartir con QR",
]

st.sidebar.markdown(
    """
    <div style="padding: .2rem 0 1rem 0;">
      <div style="font-size:1.5rem;font-weight:850;letter-spacing:-.05em;color:#17212b;">
        TECH <span style="color:#06b6d4;">MASTER.</span>
      </div>
      <div style="font-size:.68rem;letter-spacing:.15em;font-weight:800;color:#81909c;">
        LO QUE APRENDIMOS EN EL TALLER
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
page = st.sidebar.radio("EXPLORAR CONTENIDO", PAGES, label_visibility="visible")
st.sidebar.divider()
st.sidebar.caption("Una recopilación estudiantil de los temas que trabajamos en Tech Master.")
st.sidebar.markdown(
    """
    <div style="border:1px solid #dceef2;background:#f0fbfd;border-radius:13px;padding:12px;color:#52707b;font-size:.82rem;">
      <strong style="color:#087e9d;">TECH MASTER</strong><br>
      Tecnología, creatividad y aprendizaje.
    </div>
    """,
    unsafe_allow_html=True,
)

progress_map = {
    "Inicio": 0.0,
    "¿Qué es SVG?": 0.17,
    "Cambiar colores": 0.34,
    "Animaciones y transiciones": 0.51,
    "HTML básico": 0.68,
    "Electrónica básica": 0.85,
    "Zona interactiva": 0.88,
    "Compartir con QR": 1.0,
}
st.markdown(
    f"""
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:-.4rem;">
      <span style="font-size:.72rem;font-weight:800;letter-spacing:.12em;color:#82909c;">RECORRIDO TECH MASTER</span>
      <span style="font-size:.72rem;color:#82909c;">{int(progress_map[page] * 100)}%</span>
    </div>
    """,
    unsafe_allow_html=True,
)
st.progress(progress_map[page])

# ---------- Utilidades de presentación ----------
def heading(kicker, title, description=None):
    st.markdown(f'<div class="section-kicker">{kicker}</div>', unsafe_allow_html=True)
    st.title(title)
    if description:
        st.write(description)


def topic_card(icon, title, description):
    st.markdown(
        f"""
        <div class="topic-card">
          <div class="topic-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def photo(url, caption, width="100%"):
    st.image(url, caption=caption, use_container_width=(width == "100%"))


# ---------- Inicio ----------
if page == "Inicio":
    st.markdown(
        """
        <div class="hero">
          <div class="eyebrow">TECH MASTER · TECNOLOGÍA Y CREATIVIDAD</div>
          <h1>Esto fue lo que aprendimos en el taller Tech Master.</h1>
          <p class="hero-copy">
            En esta página reunimos algunos de los temas que trabajamos durante el taller:
            gráficos SVG, cambios de color, animaciones y transiciones, HTML básico y electrónica.
          </p>
          <div style="margin-top:1.2rem;">
            <span class="pill">SVG</span>
            <span class="pill">Colores</span>
            <span class="pill">Animaciones</span>
            <span class="pill">HTML básico</span>
            <span class="pill">Electrónica</span>
          </div>
          <svg class="hero-art" viewBox="0 0 330 280" xmlns="http://www.w3.org/2000/svg" aria-label="Formas geométricas abstractas">
            <defs>
              <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0" stop-color="#67e8f9"/>
                <stop offset="1" stop-color="#0891b2"/>
              </linearGradient>
              <linearGradient id="g2" x1="0" y1="0" x2="1" y2="1">
                <stop offset="0" stop-color="#cffafe"/>
                <stop offset="1" stop-color="#67e8f9"/>
              </linearGradient>
            </defs>
            <circle cx="178" cy="137" r="102" fill="#e6faff"/>
            <rect x="88" y="42" width="132" height="132" rx="30" fill="url(#g1)" transform="rotate(15 154 108)"/>
            <circle cx="210" cy="174" r="54" fill="url(#g2)" stroke="#0891b2" stroke-width="3"/>
            <path d="M42 206 L101 101 L160 206 Z" fill="#ffffff" stroke="#06b6d4" stroke-width="7" stroke-linejoin="round"/>
            <circle cx="249" cy="55" r="12" fill="#06b6d4"/>
            <circle cx="65" cy="66" r="8" fill="#67e8f9"/>
            <path d="M238 222 l22 13 -22 13 -22 -13z" fill="#0891b2"/>
          </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    heading("CONTENIDO DEL TALLER", "Los temas que trabajamos", "Explora cada sección para recordar qué es y qué aprendimos sobre cada tema.")

    c1, c2, c3 = st.columns(3)
    with c1:
        topic_card("◈", "SVG", "Conocimos los gráficos vectoriales y algunos de sus elementos.")
    with c2:
        topic_card("◉", "Cambios de color", "Probamos cómo modificar el relleno y el contorno de las formas.")
    with c3:
        topic_card("↗", "Animaciones", "Realizamos movimientos y transiciones con la herramienta usada para SVG.")

    c4, c5, c6 = st.columns(3)
    with c4:
        topic_card("</>", "HTML básico", "Reconocimos etiquetas y funciones fundamentales para organizar una página.")
    with c5:
        topic_card("⌘", "Electrónica", "Conocimos componentes electrónicos y placas de desarrollo.")
    with c6:
        topic_card("✦", "Zona interactiva", "Pon a prueba lo aprendido con actividades sencillas.")

    st.write("")
    st.markdown(
        """
        <div class="soft-note">
          <strong>¿Cómo usar esta página?</strong><br>
          Explora los temas desde el menú lateral. Al final encontrarás actividades para experimentar
          con colores, responder preguntas y realizar cálculos básicos de electrónica.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("También conocimos estas placas")
    left, right = st.columns(2)
    with left:
        photo(
            "https://images.unsplash.com/photo-1553406830-ef2513450d76?auto=format&fit=crop&w=1000&q=85",
            "Placas y componentes electrónicos",
        )
        st.markdown("**Arduino UNO**")
        st.write("Una placa utilizada en proyectos educativos para trabajar con entradas, salidas y componentes.")
    with right:
        photo(
            "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1000&q=85",
            "Detalle de una placa electrónica",
        )
        st.markdown("**ESP32**")
        st.write("Una familia de microcontroladores que, en muchos modelos, incluye conectividad inalámbrica.")

# ---------- SVG ----------
elif page == "¿Qué es SVG?":
    heading("01 · GRÁFICOS VECTORIALES", "¿Qué es SVG?", "SVG significa Scalable Vector Graphics, es decir, gráficos vectoriales escalables.")
    st.write(
        "Es un formato de imagen que describe gráficos mediante elementos como formas, líneas y trazos. "
        "A diferencia de una imagen formada por píxeles, un SVG puede ampliarse sin perder definición."
    )
    m1, m2, m3 = st.columns(3)
    m1.metric("Escalable", "Sin pixelarse")
    m2.metric("Editable", "Colores y formas")
    m3.metric("Formato", "Vectorial")

    st.subheader("Algunos elementos de SVG")
    elements = [
        ("<svg>", "Es el contenedor principal del gráfico."),
        ("<circle>", "Dibuja un círculo."),
        ("<rect>", "Dibuja un rectángulo."),
        ("<line>", "Dibuja una línea."),
        ("<path>", "Permite definir formas mediante comandos y coordenadas."),
        ("<polygon>", "Crea una forma cerrada a partir de varios puntos."),
    ]
    cols = st.columns(3)
    for i, (tag, desc) in enumerate(elements):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**`{tag}`**")
                st.caption(desc)

    st.subheader("Ejemplo visual")
    st.markdown(
        """
        <div class="info-panel">
          <svg viewBox="0 0 600 220" width="100%" xmlns="http://www.w3.org/2000/svg">
            <rect x="10" y="10" width="580" height="200" rx="22" fill="#f0fbfd"/>
            <circle cx="160" cy="110" r="62" fill="#06b6d4"/>
            <rect x="265" y="48" width="125" height="125" rx="16" fill="#a5f3fc" stroke="#0891b2" stroke-width="5"/>
            <path d="M445 165 L500 55 L555 165 Z" fill="#0891b2"/>
          </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.code(
        '<svg viewBox="0 0 600 220">\n'
        '  <circle cx="160" cy="110" r="62" fill="#06b6d4" />\n'
        '  <rect x="265" y="48" width="125" height="125" rx="16" />\n'
        '</svg>',
        language="xml",
    )
    st.caption("El ejemplo muestra un círculo, un rectángulo y un triángulo creados con elementos SVG.")

# ---------- Colores ----------
elif page == "Cambiar colores":
    heading("02 · PERSONALIZACIÓN", "Cambiar los colores de un SVG", "Los atributos de color permiten modificar la apariencia de las formas.")
    st.markdown(
        """
        - **`fill`:** cambia el color interior de una forma.
        - **`stroke`:** cambia el color del contorno.
        - **`stroke-width`:** controla el grosor del contorno.
        """
    )
    left, right = st.columns([.85, 1.4], gap="large")
    with left:
        fill = st.color_picker("Color de relleno", "#06B6D4")
        stroke = st.color_picker("Color del contorno", "#164E63")
        stroke_width = st.slider("Grosor del contorno", 1, 14, 4)
    with right:
        st.markdown("**Vista previa en vivo**")
        svg_preview = f"""
        <div class="info-panel">
          <svg viewBox="0 0 500 260" width="100%" xmlns="http://www.w3.org/2000/svg">
            <rect x="8" y="8" width="484" height="244" rx="22" fill="#f0fbfd"/>
            <circle cx="250" cy="130" r="82" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>
            <circle cx="220" cy="98" r="13" fill="#ffffff" opacity=".72"/>
          </svg>
        </div>
        """
        st.markdown(svg_preview, unsafe_allow_html=True)
    st.subheader("Así se vería el código")
    st.code(
        f'<circle cx="250" cy="130" r="82" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{stroke_width}" />',
        language="xml",
    )
    st.info("Prueba distintas combinaciones para observar cómo cambian el relleno y el borde.")

# ---------- Animaciones ----------
elif page == "Animaciones y transiciones":
    heading(
        "03 · MOVIMIENTO",
        "Animaciones y transiciones",
        "También realizamos animaciones utilizando la misma herramienta con la que trabajamos los SVG.",
    )
    st.write(
        "Con estas funciones pudimos dar movimiento a los elementos y crear transiciones entre diferentes estados. "
        "Por ejemplo, una forma puede cambiar de posición, tamaño o apariencia."
    )
    a, b, c = st.columns(3)
    with a:
        topic_card("↔", "Movimiento", "Un elemento puede desplazarse de un lugar a otro.")
    with b:
        topic_card("◉", "Cambio visual", "Una forma puede cambiar de color o tamaño.")
    with c:
        topic_card("≈", "Transición", "El cambio puede verse progresivo y fluido.")

    st.subheader("Ejemplo visual")
    st.markdown(
        """
        <div class="info-panel">
          <svg viewBox="0 0 620 170" width="100%" xmlns="http://www.w3.org/2000/svg">
            <style>
              .moving-dot {
                animation: travel 3s ease-in-out infinite alternate,
                           tint 3s ease-in-out infinite alternate;
              }
              @keyframes travel {
                from { transform: translateX(0); }
                to { transform: translateX(390px); }
              }
              @keyframes tint {
                from { fill: #06b6d4; }
                to { fill: #0e7490; }
              }
            </style>
            <path d="M40 85 H580" stroke="#cbd5e1" stroke-width="5" stroke-linecap="round"/>
            <circle class="moving-dot" cx="55" cy="85" r="24" fill="#06b6d4"/>
          </svg>
          <p style="text-align:center;margin:0;color:#64748b;font-size:.9rem;">
            El círculo se desplaza y cambia gradualmente de color.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="soft-note">
          <strong>Importante:</strong> este ejemplo sirve para mostrar el resultado de una animación.
          En el taller trabajamos estos efectos desde la misma herramienta utilizada para editar los SVG;
          no estamos presentándolos como otro lenguaje que hayamos aprendido.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- HTML ----------
elif page == "HTML básico":
    heading("04 · PÁGINAS WEB", "Lo básico de HTML", "HTML permite organizar el contenido de una página web mediante etiquetas.")
    st.write(
        "En el taller conocimos algunas funciones y etiquetas básicas. Esta sección resume la estructura "
        "general de un documento HTML y algunos elementos que se utilizan para mostrar contenido."
    )
    st.subheader("Estructura básica de un documento")
    st.code(
        '<!DOCTYPE html>\n'
        '<html lang="es">\n'
        '<head>\n'
        '  <meta charset="UTF-8">\n'
        '  <title>Mi primera página</title>\n'
        '</head>\n'
        '<body>\n'
        '  <h1>Hola, mundo</h1>\n'
        '  <p>Estoy aprendiendo HTML.</p>\n'
        '</body>\n'
        '</html>',
        language="html",
    )
    st.subheader("Etiquetas frecuentes")
    st.table(
        {
            "Etiqueta": ["<h1> a <h6>", "<p>", "<a>", "<img>", "<ul> y <li>", "<div>", "<button>"],
            "Función": [
                "Crear títulos",
                "Escribir párrafos",
                "Agregar enlaces",
                "Mostrar imágenes",
                "Organizar listas",
                "Agrupar contenido",
                "Crear botones",
            ],
        }
    )
    st.markdown(
        """
        <div class="soft-note">
          En esta sección nos enfocamos únicamente en las funciones y etiquetas básicas de HTML
          que conocimos en el taller.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- Electrónica ----------
elif page == "Electrónica básica":
    heading("05 · ELECTRÓNICA", "Introducción a la electrónica", "Conocimos componentes y placas que permiten construir circuitos y proyectos electrónicos.")
    st.write(
        "La electrónica trabaja con la electricidad y con componentes que permiten controlar señales "
        "o realizar distintas funciones."
    )

    st.subheader("Tres magnitudes importantes")
    c1, c2, c3 = st.columns(3)
    with c1:
        topic_card("V", "Voltaje", "Diferencia de potencial eléctrico. Se mide en voltios (V).")
    with c2:
        topic_card("I", "Corriente", "Flujo de carga eléctrica. Se mide en amperios (A).")
    with c3:
        topic_card("Ω", "Resistencia", "Oposición al paso de corriente. Se mide en ohmios (Ω).")

    st.subheader("Componentes electrónicos")
    components = {
        "Resistencia": "Limita la corriente y ayuda a proteger otros componentes.",
        "LED": "Diodo que emite luz cuando está conectado con la polaridad adecuada.",
        "Protoboard": "Permite montar circuitos de prueba sin necesidad de soldar.",
        "Potenciómetro": "Es una resistencia variable que permite ajustar una señal.",
        "Condensador": "Almacena temporalmente energía eléctrica.",
        "Diodo": "Permite principalmente el paso de corriente en un sentido.",
        "Transistor": "Puede funcionar como interruptor electrónico o amplificador.",
    }
    col1, col2 = st.columns(2)
    for i, (name, description) in enumerate(components.items()):
        with (col1 if i % 2 == 0 else col2):
            with st.expander(name):
                st.write(description)

    st.subheader("Placas de desarrollo")
    arduino, esp = st.columns(2, gap="large")
    with arduino:
        photo(
            "https://images.unsplash.com/photo-1553406830-ef2513450d76?auto=format&fit=crop&w=1000&q=85",
            "Ejemplo de placa y componentes electrónicos",
        )
        st.markdown("### Arduino UNO")
        st.write("Placa utilizada en proyectos educativos para trabajar con entradas, salidas y componentes.")
        st.caption("Ejemplos de uso: LEDs, botones, sensores y proyectos sencillos.")
    with esp:
        photo(
            "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1000&q=85",
            "Detalle de una placa electrónica",
        )
        st.markdown("### ESP32")
        st.write("Familia de microcontroladores que incluye conectividad inalámbrica en muchos de sus modelos.")
        st.caption("Ejemplos de uso: sensores conectados, automatización y proyectos IoT.")

    st.subheader("Sensores y actuadores")
    s1, s2 = st.columns(2)
    with s1:
        topic_card("⌁", "Sensores", "Captan información del entorno, como distancia, luz o temperatura.")
    with s2:
        topic_card("⚙", "Actuadores", "Realizan acciones, como emitir luz o producir movimiento.")

    st.warning(
        "Para realizar prácticas, utiliza circuitos de baja tensión. No trabajes con tensión de red "
        "ni conectes motores directamente a los pines de una placa. Sigue las indicaciones del docente."
    )

# ---------- Zona interactiva ----------
elif page == "Zona interactiva":
    heading("06 · PON A PRUEBA LO APRENDIDO", "Zona interactiva", "Experimenta con algunos de los conceptos que aparecen en esta página.")
    tab1, tab2, tab3 = st.tabs(["🎨 Personalizador SVG", "🧠 Quiz del taller", "⚡ Calculadora de Ohm"])

    with tab1:
        st.subheader("Crea tu combinación de colores")
        left, right = st.columns([.8, 1.4], gap="large")
        with left:
            color1 = st.color_picker("Color principal", "#06B6D4", key="svg_main")
            color2 = st.color_picker("Color secundario", "#A5F3FC", key="svg_second")
            shape = st.selectbox("Forma principal", ["Círculo", "Rectángulo", "Triángulo"])
        with right:
            if shape == "Círculo":
                main_shape = f'<circle cx="245" cy="110" r="66" fill="{color1}"/>'
            elif shape == "Rectángulo":
                main_shape = f'<rect x="180" y="45" width="130" height="130" rx="18" fill="{color1}"/>'
            else:
                main_shape = f'<path d="M245 38 L320 170 L170 170 Z" fill="{color1}"/>'
            st.markdown(
                f"""
                <div class="info-panel">
                  <svg viewBox="0 0 500 220" width="100%" xmlns="http://www.w3.org/2000/svg">
                    <rect x="8" y="8" width="484" height="204" rx="20" fill="#f0fbfd"/>
                    {main_shape}
                    <circle cx="365" cy="110" r="36" fill="{color2}"/>
                    <path d="M60 160 L95 65 L130 160 Z" fill="{color2}"/>
                  </svg>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.caption("Los colores seleccionados se aplican a las formas del gráfico SVG.")

    with tab2:
        st.subheader("¿Qué tanto recuerdas?")
        quiz = [
            ("¿Qué significa SVG?", ["Scalable Vector Graphics", "Simple Visual Graphic", "System Vector Grid"], 0,
             "SVG significa Scalable Vector Graphics."),
            ("¿Qué atributo cambia el relleno de una forma SVG?", ["stroke", "fill", "href"], 1,
             "fill cambia el relleno; stroke cambia el contorno."),
            ("¿Qué lenguaje organiza la estructura de una página web?", ["HTML", "CSS", "Python"], 0,
             "HTML organiza el contenido de una página web."),
            ("¿Qué magnitud se mide en ohmios?", ["Voltaje", "Corriente", "Resistencia"], 2,
             "La resistencia se mide en ohmios (Ω)."),
            ("¿Qué placa incluye conectividad inalámbrica en muchos modelos?", ["Arduino UNO clásico", "ESP32", "Protoboard"], 1,
             "Muchos modelos ESP32 incorporan Wi-Fi y Bluetooth."),
        ]
        with st.form("quiz_form"):
            answers = []
            for i, (question, options, correct, explanation) in enumerate(quiz):
                answers.append(st.radio(question, options, key=f"quiz_{i}"))
            submitted = st.form_submit_button("Comprobar respuestas", use_container_width=True)

        if submitted:
            score = sum(
                answers[i] == quiz[i][1][quiz[i][2]]
                for i in range(len(quiz))
            )
            st.session_state["quiz_score"] = score
            st.session_state["quiz_answers"] = answers

        if "quiz_score" in st.session_state:
            score = st.session_state["quiz_score"]
            saved_answers = st.session_state["quiz_answers"]
            st.markdown("---")
            st.metric("Tu resultado", f"{score}/{len(quiz)}")
            st.progress(score / len(quiz))
            for i, answer in enumerate(saved_answers):
                correct_answer = quiz[i][1][quiz[i][2]]
                if answer == correct_answer:
                    st.success(f"Pregunta {i + 1}: ¡Correcto!")
                else:
                    st.error(f"Pregunta {i + 1}: la respuesta correcta era **{correct_answer}**. {quiz[i][3]}")
            if st.button("Volver a intentar"):
                del st.session_state["quiz_score"]
                del st.session_state["quiz_answers"]
                st.rerun()

    with tab3:
        st.subheader("Calculadora de Ley de Ohm")
        mode = st.radio(
            "¿Qué deseas calcular?",
            ["Corriente", "Voltaje", "Resistencia"],
            horizontal=True,
        )
        if mode == "Corriente":
            v = st.number_input("Voltaje (V)", min_value=0.0, value=5.0, step=0.5)
            r = st.number_input("Resistencia (Ω)", min_value=0.1, value=220.0, step=10.0)
            current_ma = (v / r) * 1000
            st.metric("Corriente", f"{current_ma:.2f} mA")
            st.latex(r"I = \frac{V}{R}")
        elif mode == "Voltaje":
            i_ma = st.number_input("Corriente (mA)", min_value=0.0, value=20.0, step=1.0)
            r = st.number_input("Resistencia (Ω)", min_value=0.1, value=220.0, step=10.0)
            voltage = (i_ma / 1000) * r
            st.metric("Voltaje", f"{voltage:.2f} V")
            st.latex(r"V = I \times R")
        else:
            v = st.number_input("Voltaje (V)", min_value=0.0, value=5.0, step=0.5)
            i_ma = st.number_input("Corriente (mA)", min_value=0.1, value=20.0, step=1.0)
            resistance = v / (i_ma / 1000)
            st.metric("Resistencia", f"{resistance:.2f} Ω")
            st.latex(r"R = \frac{V}{I}")
        st.caption("Es un modelo ideal para circuitos resistivos. Comprueba siempre los límites de tus componentes.")


# ---------- Compartir con QR ----------
elif page == "Compartir con QR":
    heading(
        "07 · COMPARTE EL PROYECTO",
        "Entra desde cualquier dispositivo",
        "Genera un código QR para que otras personas puedan abrir el landing page desde su celular o tablet.",
    )

    st.markdown(
        """
        <div class="soft-note">
          <strong>Antes de generar el QR:</strong> el landing page debe estar publicado en Internet.
          Un enlace como <code>localhost:8501</code> solo funciona en tu propia computadora y no sirve
          para que otras personas entren desde fuera.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("1. Pega el enlace público de tu página")
    public_url = st.text_input(
        "URL del landing page",
        placeholder="https://tu-proyecto.streamlit.app",
        help="Pega aquí el enlace que te proporciona Streamlit Community Cloud u otro servicio de alojamiento.",
        key="public_landing_url",
    ).strip()

    if public_url:
        if not (public_url.startswith("https://") or public_url.startswith("http://")):
            st.error("El enlace debe comenzar con https:// o http://.")
        else:
            try:
                import qrcode
                from io import BytesIO

                qr = qrcode.QRCode(
                    version=None,
                    error_correction=qrcode.constants.ERROR_CORRECT_M,
                    box_size=10,
                    border=4,
                )
                qr.add_data(public_url)
                qr.make(fit=True)
                qr_image = qr.make_image(fill_color="#17212b", back_color="white").convert("RGB")

                image_buffer = BytesIO()
                qr_image.save(image_buffer, format="PNG")
                image_bytes = image_buffer.getvalue()

                left, right = st.columns([1, 1.25], gap="large")
                with left:
                    st.markdown("**2. Escanea este código QR**")
                    st.image(image_bytes, caption="Código QR de Tech Master", width=280)
                with right:
                    st.markdown("**3. Comparte el acceso**")
                    st.write("Cualquier persona que escanee el código podrá abrir el enlace desde su dispositivo, siempre que tenga conexión a Internet.")
                    st.code(public_url, language=None)
                    st.download_button(
                        "Descargar código QR (PNG)",
                        data=image_bytes,
                        file_name="tech-master-qr.png",
                        mime="image/png",
                        use_container_width=True,
                    )
                    st.success("El código QR está listo. Pruébalo con la cámara de otro celular antes de compartirlo.")
            except ImportError:
                st.error(
                    "Falta instalar la librería para crear el QR. Ejecuta en la terminal: "
                    "py -m pip install -r requirements.txt"
                )
    else:
        st.info("Cuando tengas publicado el landing page, pega aquí su enlace para crear el QR.")

    with st.expander("¿Cómo publico la página para que otros puedan entrar?"):
        st.markdown(
            """
            Una opción sencilla es **Streamlit Community Cloud**:

            1. Sube los archivos `app.py` y `requirements.txt` a un repositorio de GitHub.
            2. Entra a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con GitHub.
            3. Selecciona el repositorio y el archivo principal `app.py`.
            4. Pulsa **Deploy** y espera a que termine la publicación.
            5. Copia el enlace público que te genere Streamlit.
            6. Vuelve a esta sección, pega el enlace y descarga el QR.

            La dirección pública suele tener este formato: `https://nombre-del-proyecto.streamlit.app`.
            """
        )

    st.caption(
        "Nota: el QR contiene el enlace de acceso; no guarda ni publica el proyecto por sí mismo."
    )

# ---------- Pie de página ----------
st.markdown(
    """
    <div class="footer">
      <strong style="color:#087e9d;">TECH MASTER</strong> · Lo que aprendimos en el taller<br>
      Trabajo realizado como recopilación estudiantil de los temas vistos.
    </div>
    """,
    unsafe_allow_html=True,
)
