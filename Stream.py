import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(page_title="Radar Regulatorio FRM", page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS14bSWA3akUYXe-VV04Nw2K0QnQCwCV9SG8g&s")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS14bSWA3akUYXe-VV04Nw2K0QnQCwCV9SG8g&s", width=250)
st.title("Buscador de palabras FRM")

def buscar_palabras_clave(pdf_file, palabras_clave):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    resultados = {palabra: [] for palabra in palabras_clave}
    contexto = {palabra: [] for palabra in palabras_clave}
    
    for num_pagina in range(len(doc)):
        pagina = doc[num_pagina]
        texto = pagina.get_text("text")
        lineas = texto.split("\n")
        
        for palabra in palabras_clave:
            for linea in lineas:
                if palabra.lower() in linea.lower():
                    resultados[palabra].append(num_pagina + 1)
                    contexto[palabra].append(f'Página {num_pagina + 1}: "{linea.strip()}"')
    
    return resultados, contexto

pdf_file = st.file_uploader("Sube un archivo PDF", type=["pdf"])
palabra_input = st.text_input("Ingresa una o más palabras clave (separadas por comas)")

if pdf_file and palabra_input:
    palabras_clave = [p.strip() for p in palabra_input.split(",")]
    resultados, contexto = buscar_palabras_clave(pdf_file, palabras_clave)
    
    st.subheader("Resultados de la búsqueda:")
    for palabra, paginas in resultados.items():
        if paginas:
            st.write(f'**{palabra}** se encontró en las páginas: {paginas}')
        else:
            st.write(f'**{palabra}** no se encontró en el documento.')
    
    st.subheader("Contexto de las palabras encontradas:")
    for palabra, frases in contexto.items():
        if frases:
            for frase in frases:
                st.write(f'🔹 {frase}')
        else:
            st.write(f'No se encontró contexto para **{palabra}**.')

st.markdown("---")
st.markdown("Financial Risk Management - Franco Olivares")

