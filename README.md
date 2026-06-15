\# Enterprise RAG Agent 🤖📊


Este repositório contém uma aplicação completa de \*\*RAG (Retrieval-Augmented Generation)\*\* corporativo desenhada sob uma arquitetura de microsserviços totalmente desacoplada (Backend API e Frontend UI). 



O sistema foi desenvolvido com foco em cenários de \*\*Análise de Dados e Inteligência Artificial\*\*, permitindo a ingestão dinâmica de relatórios corporativos densos em PDF, vetorização em memória de alta performance e consultas semânticas avançadas com engenharia de prompts refinada.



\---



\## 📺 Demonstração em Vídeo (Showcase)



Abaixo você pode conferir o agente de IA em ação, realizando o upload e interpretando cenários complexos do relatório de \*\*Desempenho Financeiro da Petrobras no 4º Trimestre de 2025 (4T25)\*\*.





https://github.com/user-attachments/assets/405cec0d-f4ef-4140-b9d4-43b52c2f9148







> 💡 \*Nota: Caso o vídeo acima não carregue diretamente no markdown do GitHub, você pode localizá-lo diretamente dentro da pasta `/assets` deste repositório.\*



\---



\## 🧪 Casos de Teste e Capacidade Analítica (Exemplo Petrobras 4T25)



Para testar o limite de interpretação de dados, contextualização e síntese do agente, foram realizadas três consultas analíticas de negócios baseadas no documento extraído da Petrobras. O comportamento esperado e validado no vídeo foi:



| # | Pergunta do Usuário | Capacidade Avaliada na IA | Comportamento do Agente |

|---|---------------------|---------------------------|------------------------|

| \*\*1\*\* | \*Qual foi o lucro líquido da Petrobras no 4º trimestre de 2025 e como ele se compara ao trimestre anterior?\* | \*\*Recuperação Numérica e Comparação\*\* | O agente localizou os valores exatos de lucro no balanço patrimonial e calculou a variação percentual/nominal em relação ao 3T25. |

| \*\*2\*\* | \*Mesmo com uma produção robusta, o que justificou a queda no lucro e no EBITDA em 2025 de acordo com o documento?\* | \*\*Análise de Causa-Raiz e Correlação\*\* | A IA cruzou os dados operacionais com os fatores de mercado (ex: variação do preço do barril de Brent ou despesas operacionais), isolando a justificativa corporativa do texto. |

| \*\*3\*\* | \*Faça um resumo executivo em 3 pontos sobre a saúde financeira e operacional da Petrobras no final de 2025.\* | \*\*Sumarização Executiva e Síntese\*\* | O agente transformou páginas de tabelas e relatórios em 3 tópicos acionáveis (\*bullet points\*), mantendo o tom estritamente profissional exigido pelo sistema. |



\---



\## 📐 Arquitetura do Repositório



A estrutura foi projetada para simular um ambiente de produção real, separando a lógica de negócio da interface com o usuário:



\* `backend/`: API assíncrona robusta utilizando \*\*FastAPI\*\*. Gerencia os endpoints de upload (`/upload`) e a interface do agente (`/chat`). Utiliza o `OpenAIEmbedder` para converter o texto em vetores de alta dimensionalidade (`text-embedding-3-small`).

\* `frontend/`: Interface Web desenvolvida em \*\*Streamlit\*\*. Gerencia a sessão de histórico de conversa (`st.session\_state`), arquivos carregados pelo usuário e simula um efeito visual de digitação contínua (\*Streaming UI\*) para otimizar a experiência do usuário (UX).

\* `assets/`: Armazena os arquivos de mídia e demonstração do portfólio.

\* `LanceDB`: Banco de dados vetorial serverless embarcado. Utiliza indexação híbrida associada ao ecossistema do \*\*Agno Framework\*\* para buscas por similaridade de cosseno com altíssima velocidade e baixo consumo de infraestrutura.



\---



\## 🛠️ Instalação e Execução Local



\### Pré-requisitos

\* Python 3.10 ou superior instalado.

\* Chave de API da OpenAI (`OPENAI\_API\_KEY`).



\### 1. Preparação do Ambiente

```bash

\# Clonar o projeto

git clone \[https://github.com/CraftingInsights00/enterprise-rag-agent.git](https://github.com/CraftingInsights00/enterprise-rag-agent.git)

cd enterprise-rag-agent



\# Criar e ativar o ambiente virtual

python -m venv venv

\# No Windows: venv\\Scripts\\activate | No Linux/Mac: source venv/bin/activate



\# Instalar dependências unificadas

pip install -r requirements.txt

