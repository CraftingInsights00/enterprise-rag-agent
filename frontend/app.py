import streamlit as st
import httpx
import time

st.set_page_config(
    page_title="Agente RAG - Chatbot",
    page_icon="🤖",
    layout="centered"
)

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.title("Assistente de IA com RAG")
st.subheader("Converse com seus documentos locais")

with st.sidebar:
    st.header("📂 Documentação")
    st.write("Suba arquivos (.pdf) para alimentar a base de conhecimento do agente.")
    
    uploaded_file = st.file_uploader(
        "Escolha um arquivo", 
        type=["pdf"], 
        help="Apenas arquivos PDF são suportados pelo agente atualmente."
    )
    
    if uploaded_file is not None:
        if st.button("Processar Documento", use_container_width=True):
            with st.spinner("Vetorizando arquivo no LanceDB... Aguarde."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = httpx.post(f"{BACKEND_URL}/upload", files=files, timeout=60.0)
                    
                    if response.status_code == 200:
                        st.success(response.json().get("message"))
                    else:
                        st.error(f"Erro no servidor: {response.json().get('detail')}")
                        
                except Exception as e:
                    st.error(f"Não foi possível conectar ao backend: {str(e)}")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Suba um documento PDF na barra lateral e me faça perguntas sobre ele."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Digite sua pergunta aqui..."):
    
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("assistant"):
        try:
            payload = {"message": user_input}
            
            # Requisição POST convencional para o backend
            response = httpx.post(f"{BACKEND_URL}/chat", json=payload, timeout=60.0)
            
            if response.status_code == 200:
                full_response = response.json().get("response")
                
                # Simulação do efeito de digitação (Streaming visual no Frontend)
                def text_generator():
                    for word in full_response.split(" "):
                        yield word + " "
                        time.sleep(0.04)
                
                output_text = st.write_stream(text_generator())
                st.session_state.messages.append({"role": "assistant", "content": output_text})
            else:
                st.error(f"⚠️ Erro no servidor: Código {response.status_code}")
                
        except Exception as e:
            st.error(f"Erro de comunicação com o backend: {str(e)}")