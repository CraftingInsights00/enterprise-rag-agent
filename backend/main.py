import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Importações do Agno Framework
from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb
from agno.models.openai import OpenAIChat
from agno.knowledge.embedder.openai import OpenAIEmbedder

load_dotenv()

app = FastAPI(title="Agente RAG Corporativo - API")

STORAGE_DIR = "documentos"
DB_URI = os.path.join(STORAGE_DIR, "lancedb_data")
os.makedirs(STORAGE_DIR, exist_ok=True)

embedder = OpenAIEmbedder()

vector_db = LanceDb(
    table_name="rag_documents",
    uri=DB_URI,
    use_tantivy=True,
    embedder=embedder
)

knowledge_base = Knowledge(vector_db=vector_db)

agent = Agent(
    name="Assistente RAG Corporativo",
    model=OpenAIChat(id="gpt-4o-mini"), 
    description="Você é um assistente virtual especialista em análise de documentos locais.",
    knowledge=knowledge_base,
    search_knowledge=True,
    markdown=True,
    instructions=[
        "Sempre que o usuário fizer uma pergunta sobre documentos, experiências, currículos ou dados corporativos, busque na sua base de conhecimento.",
        "Se a base de dados não contiver a resposta, diga de forma clara e amigável: 'Ainda não tenho acesso a esse documento. Por favor, faça o upload dele na barra lateral para que eu possa analisar!'",
        "Seja direto, claro e formate suas respostas de maneira profissional usando markdown."
    ]
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "Backend do Agente RAG rodando perfeitamente."}

@app.post("/upload", description="Rota para subir arquivos para a base de conhecimento do RAG")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Por favor, envie um arquivo no formato PDF.")
    
    file_path = os.path.join(STORAGE_DIR, file.filename)
    
    try:
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        knowledge_base.insert(path=file_path, metadata={"source": file.filename})
        return {"message": f"Arquivo '{file.filename}' processado e vetorizado com sucesso no LanceDB!"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo: {str(e)}")

@app.post("/chat", response_model=ChatResponse, description="Rota para conversar com o Agente RAG")
def chat_with_agent(request: ChatRequest):
    try:
        agent_response = agent.run(request.message)
        return ChatResponse(response=agent_response.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na execução do agente: {str(e)}")