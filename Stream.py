import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(page_title="Buscador de palabras FRM", page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS14bSWA3akUYXe-VV04Nw2K0QnQCwCV9SG8g&s")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS14bSWA3akUYXe-VV04Nw2K0QnQCwCV9SG8g&s", width=250)
st.title("Buscador de palabras FRM")

def buscar_palabras_clave(pdf_file, palabras_clave):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    resultados = {palabra: [] for palabra in palabras_clave}
    
    for num_pagina in range(len(doc)):
        pagina = doc[num_pagina]
        texto = pagina.get_text("text")
        
        for palabra in palabras_clave:
            if palabra.lower() in texto.lower():
                resultados[palabra].append(num_pagina + 1)
    
    return resultados

pdf_file = st.file_uploader("Sube un archivo PDF", type=["pdf"])
palabra_input = st.text_input("Ingresa una o más palabras clave (separadas por comas)")

if pdf_file and palabra_input:
    palabras_clave = [p.strip() for p in palabra_input.split(",")]
    resultados = buscar_palabras_clave(pdf_file, palabras_clave)
    
    st.subheader("Resultados de la búsqueda:")
    for palabra, paginas in resultados.items():
        if paginas:
            st.write(f'**{palabra}** se encontró en las páginas: {paginas}')
        else:
            st.write(f'**{palabra}** no se encontró en el documento.')

st.markdown("---")
st.markdown("### Financial Risk Management - Franco Olivares")


