import streamlit as st
import datetime
import random
import base64

# ---------------------------------------------------------
# 1. FUNÇÃO PARA CARREGAR A IMAGEM DE FUNDO EM BASE64
# ---------------------------------------------------------
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    img_base64 = get_base64_of_bin_file('1001217215.jpg')
    bg_style = f"data:image/jpeg;base64,{img_base64}"
except Exception:
    bg_style = "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?q=80&w=1920&auto=format&fit=crop"

# ---------------------------------------------------------
# 2. CONFIGURAÇÃO DA PÁGINA E ESTILIZAÇÃO CSS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Unimar - Achados e Perdidos",
    page_icon="🚌",
    layout="wide"
)

st.markdown(f"""
    <style>
    /* Importação de Fontes do Google e Ícones do FontAwesome */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

    /* Fundo geral da aplicação */
    .stApp {{
        background: linear-gradient(rgba(15, 23, 42, 0.78), rgba(15, 23, 42, 0.90)), 
                    url('{bg_style}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Configuração padrão do corpo da página */
    html, body, [class*="css"], div, p, span, label {{
        font-family: -apple-system, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, 'Segoe UI', sans-serif !important;
        color: #FFFFFF !important;
    }}

    /* CABEÇALHOS (H1, H2, H3) EM AZUL UNIMAR (#1D61B0) */
    h1, h2, h3, .stApp h1, .stApp h2, .stApp h3 {{
        font-family: 'Poppins', -apple-system, 'SF Pro Display', sans-serif !important;
        color: #1D61B0 !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px;
    }}

    h1 {{ font-size: 2.2rem !important; }}
    h2 {{ font-size: 1.6rem !important; }}
    h3 {{ font-size: 1.3rem !important; }}

    /* ESTILIZAÇÃO DAS CAIXAS DE TEXTO / INPUTS / CAMPOS DE FORMULÁRIO (TEXTO EM PRETO) */
    div[data-baseweb="input"] input, 
    div[data-baseweb="textarea"] textarea, 
    div[data-baseweb="select"] div,
    input, textarea, select {{
        color: #000000 !important;
        background-color: #FFFFFF !important;
        font-weight: 500 !important;
    }}

    /* Cor do texto de instrução (placeholder) dentro das caixas */
    input::placeholder, textarea::placeholder {{
        color: #666666 !important;
    }}

    /* Rótulos/Labels em cima dos campos de texto (cor azul para destacar) */
    .stTextInput > label, .stTextArea > label, .stSelectbox > label, .stDateInput > label {{
        color: #1D61B0 !important;
        font-weight: 600 !important;
    }}

    /* Cartões / Containeres transparentes escuros para contraste */
    div[data-testid="stColumn"] > div, .stCard {{
        background-color: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(29, 97, 176, 0.3);
        border-radius: 14px;
        padding: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.25);
    }}

    /* Ajuste de cor do texto interno dos cards para preto */
    div[data-testid="stColumn"] p, div[data-testid="stColumn"] span, div[data-testid="stColumn"] label {{
        color: #111827 !important;
    }}

    /* Botões estilizados em Azul com Texto Branco */
    .stButton>button {{
        border-radius: 8px;
        font-weight: 600;
        background-color: #1D61B0 !important;
        color: #FFFFFF !important;
        border: none !important;
        font-family: -apple-system, 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif !important;
    }}

    /* Sidebar personalizada */
    section[data-testid="stSidebar"] {{
        background-color: rgba(15, 23, 42, 0.95) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}

    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {{
        color: #FFFFFF !important;
    }}

    /* Rodapé com ícones redondos */
    .footer-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 60px;
        padding: 25px 0 10px 0;
        margin-top: 40px;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .footer-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none !important;
        color: #FFFFFF !important;
        transition: transform 0.2s ease-in-out;
    }}

    .footer-item:hover {{
        transform: translateY(-4px);
    }}

    .icon-circle {{
        width: 65px;
        height: 65px;
        border-radius: 50%;
        background-color: #FFFFFF;
        border: 2px solid #1D61B0;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        margin-bottom: 8px;
    }}

    .icon-circle i {{
        font-size: 30px;
        color: #1D61B0;
    }}

    .footer-title {{
        font-family: -apple-system, 'SF Pro Text', 'Helvetica Neue', Arial, sans-serif;
        font-size: 14px;
        font-weight: 600;
        color: #FFFFFF;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. BASE DE DADOS (SESSION STATE)
# ---------------------------------------------------------
if "banco_objetos" not in st.session_state:
    st.session_state.banco_objetos = [
        {
            "codigo": "UNI-8492",
            "descricao": "Mochila preta Targus com notebook",
            "linha": "Rota Industrial / Vale",
            "localizacao": "Garagem Unimar",
            "data_registro": "01/10/2026",
            "status": "Disponível",
            "dados_entrega": None
        },
        {
            "codigo": "UNI-3310",
            "descricao": "Chaveiro com 3 chaves e controle de alarme",
            "linha": "Circular Unimar",
            "localizacao": "Vila das Contratadas / Vale",
            "data_registro": "02/10/2026",
            "status": "Disponível",
            "dados_entrega": None
        },
        {
            "codigo": "UNI-1204",
            "descricao": "Garrafa térmica azul",
            "linha": "Linha 04 - Executivo",
            "localizacao": "Vila das Contratadas / Vale",
            "data_registro": "28/09/2026",
            "status": "Entregue",
            "dados_entrega": {
                "nome": "Carlos Eduardo",
                "documento": "123.456.789-00",
                "data_hora": "02/10/2026 14:30"
            }
        }
    ]

# ---------------------------------------------------------
# 4. NAVEGAÇÃO LATERAL (MODO PASSAGEIRO OU PAINEL ADMIN)
# ---------------------------------------------------------
st.sidebar.markdown("### 🚌 Unimar Transportes")
perfil_acesso = st.sidebar.radio(
    "Selecione o Modo de Visualização:",
    ["📱 Tela do Passageiro", "⚙️ Painel do Administrador"],
    key="perfil_acesso_radio"
)

st.sidebar.markdown("---")
st.sidebar.caption("📌 **Projeto de Extensão - Achados e Perdidos**")

# =========================================================
# TELA DO PASSAGEIRO
# =========================================================
if perfil_acesso == "📱 Tela do Passageiro":
    st.title("🔍 Achados e Perdidos — Unimar")
    st.write("Esqueceu algum pertence nos veículos da frota? Pesquise abaixo ou cadastre uma solicitação de busca.")
    
    st.markdown("---")
    
    col_busca, col_solicitar = st.columns([2, 1])
    
    # --- COLUNA 1: BUSCA DE PERTENCES ---
    with col_busca:
        st.markdown("### 🔎 Buscar Item Encontrado")
        
        termo_busca = st.text_input(
            "Digite o nome do objeto, linha do ônibus ou palavra-chave:",
            placeholder="Ex: Mochila, Chave, Garrafa, Linha Vale..."
        )
        
        itens_disponiveis = [i for i in st.session_state.banco_objetos if i["status"] in ["Disponível", "Agendado"]]
        
        if termo_busca:
            resultados = [
                i for i in itens_disponiveis 
                if termo_busca.lower() in i["descricao"].lower() 
                or termo_busca.lower() in i.get("linha", "").lower()
                or termo_busca.lower() in i["codigo"].lower()
            ]
        else:
            resultados = itens_disponiveis

        st.markdown(f"**Itens Encontrados e Guardados ({len(resultados)}):**")
        
        if not resultados:
            st.info("Nenhum pertence encontrado com a palavra pesquisada.")
        else:
            for item in resultados:
                with st.expander(f"📌 {item['codigo']} — {item['descricao']}"):
                    st.write(f"🚌 **Linha/Rota:** {item.get('linha', 'Frota Geral')}")
                    st.write(f"📍 **Local de Retirada:** {item['localizacao']}")
                    st.write(f"📅 **Data de Entrada:** {item.get('data_registro', 'Recente')}")
                    
                    st.markdown("---")
                    st.write("**É o seu pertence?** Solicite a retirada preenchendo os dados abaixo:")
                    
                    with st.form(key=f"form_resgate_{item['codigo']}"):
                        nome_p = st.text_input("Seu Nome Completo:")
                        contato_p = st.text_input("Telefone/WhatsApp para contato:")
                        detalhe_p = st.text_area("Descreva detalhes/marcas do item para confirmação:")
                        
                        btn_solicitar = st.form_submit_button("📩 Solicitar Agendamento de Retirada")
                        
                        if btn_solicitar:
                            if not nome_p or not contato_p:
                                st.error("Por favor, preencha seu nome e telefone de contato.")
                            else:
                                item["status"] = "Agendado"
                                st.success(f"Solicitação enviada com sucesso! Código de acompanhamento: **{item['codigo']}**. Nossa equipe entrará em contato via WhatsApp/Telefone.")

    # --- COLUNA 2: REGISTRAR ALERTA DE PERDA ---
    with col_solicitar:
        st.markdown("### 📢 Não encontrou seu pertence?")
        st.caption("Deixe um alerta registrado para que a equipe te avise caso o objeto seja encontrado no ônibus.")
        
        with st.form(key="form_alerta_perda"):
            item_perdido = st.text_input("O que você perdeu?", placeholder="Ex: Óculos de grau com armação preta")
            linha_onibus = st.text_input("Linha ou horário do ônibus (se souber):")
            data_perda = st.date_input("Data do ocorrido:", datetime.date.today())
            nome_contato = st.text_input("Seu Nome:")
            tel_contato = st.text_input("Seu Telefone / WhatsApp:")
            
            sub_alerta = st.form_submit_button("🚀 Cadastrar Alerta de Perda")
            
            if sub_alerta:
                if not item_perdido or not tel_contato:
                    st.error("Preencha ao menos o que foi perdido e o telefone de contato.")
                else:
                    st.success("Alerta registrado! Se os motoristas ou a equipe de limpeza encontrarem seu pertence, entraremos em contato imediatamente.")

# =========================================================
# TELA DO ADMINISTRADOR (EQUIPE UNIMAR)
# =========================================================
else:
    st.title("⚙️ Painel de Gestão - Equipe Unimar")
    st.write("Plataforma administrativa de controle de achados e perdidos.")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    # 1. ITENS CADASTRADOS
    with col1:
        st.markdown("### 📦 1. Itens Cadastrados")
        st.caption("Visualização e gestão dos pertences registrados.")
        
        aba_selecionada = st.radio(
            "Exibir lista de:",
            ["Aguardando Retirada", "Itens Devolvidos"],
            key="radio_admin_itens"
        )
        
        st.markdown("---")
        
        if aba_selecionada == "Aguardando Retirada":
            pendentes = [i for i in st.session_state.banco_objetos if i["status"] in ["Disponível", "Agendado"]]
            st.write(f"**Total pendente:** {len(pendentes)}")
            for item in pendentes:
                tag_status = "🟡 Agendado" if item["status"] == "Agendado" else "🟢 Disponível"
                with st.expander(f"📌 {item['codigo']} - {item['descricao']}"):
                    st.write(f"**Local:** {item['localizacao']}")
                    st.write(f"**Status:** {tag_status}")
                    
        else:
            entregues = [i for i in st.session_state.banco_objetos if i["status"] == "Entregue"]
            st.write(f"**Total entregue:** {len(entregues)}")
            for item in entregues:
                with st.expander(f"✅ {item['codigo']} - {item['descricao']}"):
                    st.write(f"**Local:** {item['localizacao']}")
                    if item["dados_entrega"]:
                        st.write(f"**Recebedor:** {item['dados_entrega']['nome']}")
                        st.write(f"**Data:** {item['dados_entrega']['data_hora']}")

    # 2. CADASTRAR NOVO ITEM
    with col2:
        st.markdown("### ➕ 2. Cadastrar Novo Item")
        st.caption("Registro rápido de pertences encontrados nos ônibus.")
        
        desc_novo = st.text_input("Descrição do Objeto Encontrado:", placeholder="Ex: Carteira de couro preta")
        linha_nova = st.text_input("Linha/Ônibus onde foi encontrado:", placeholder="Ex: Rota Industrial")
        
        local_guarda = st.radio(
            "Local de Guarda:",
            ["Vila das Contratadas / Vale", "Garagem Unimar"],
            key="radio_local_admin"
        )
        
        st.markdown("---")
        
        if "cam_item_ativa" not in st.session_state:
            st.session_state.cam_item_ativa = False
        if "foto_item_temp" not in st.session_state:
            st.session_state.foto_item_temp = None

        if not st.session_state.cam_item_ativa:
            if st.button("📷 Abrir Câmera para Fotografar Item", key="btn_abrir_cam_item"):
                st.session_state.cam_item_ativa = True
                st.rerun()
        else:
            st.warning("⚠️ **Permissão do Dispositivo:** Por favor, permita o acesso à câmera.")
            captura = st.camera_input("Fotografar Item", key="camera_item_input")
            
            if captura:
                st.image(captura, caption="Pré-visualização da Imagem", use_container_width=True)
                col_save, col_clear = st.columns(2)
                
                with col_save:
                    if st.button("💾 Salvar Foto", type="primary", key="save_img_item"):
                        st.session_state.foto_item_temp = captura.getvalue()
                        st.success("Imagem salva!")
                        
                with col_clear:
                    if st.button("🗑️️ Limpar", key="clear_img_item"):
                        st.session_state.foto_item_temp = None
                        st.rerun()

        st.markdown("---")
        
        if st.button("✅ Finalizar Cadastro e Gerar Matrícula", type="primary", use_container_width=True):
            if not desc_novo:
                st.error("Por favor, preencha a descrição do item.")
            else:
                codigo_gerado = f"UNI-{random.randint(1000, 9999)}"
                data_hoje = datetime.datetime.now().strftime("%d/%m/%Y")
                
                novo_registro = {
                    "codigo": codigo_gerado,
                    "descricao": desc_novo,
                    "linha": linha_nova if linha_nova else "Frota Geral",
                    "localizacao": local_guarda,
                    "data_registro": data_hoje,
                    "status": "Disponível",
                    "foto_item": st.session_state.foto_item_temp,
                    "dados_entrega": None
                }
                
                st.session_state.banco_objetos.append(novo_registro)
                st.success(f"Cadastro realizado! Código do Item: **{codigo_gerado}**")
                
                st.session_state.cam_item_ativa = False
                st.session_state.foto_item_temp = None
                st.rerun()

    # 3. ANÁLISE DE DEVOLUÇÕES
    with col3:
        st.markdown("### 📋 3. Análise de Devoluções")
        st.caption("Baixa final e conferência de comprovantes de entrega.")
        
        opcao_devolucao = st.radio(
            "Selecione a Ação:",
            ["Informações do Recebedor", "Fotografar Recebedor/Documento"],
            key="radio_devolucao_admin"
        )
        
        st.markdown("---")
        
        if opcao_devolucao == "Informações do Recebedor":
            st.write("**Galeria de Comprovantes Registrados:**")
            entregues = [i for i in st.session_state.banco_objetos if i["status"] == "Entregue"]
            
            if not entregues:
                st.info("Nenhum histórico de recebedor salvo até o momento.")
            else:
                for item in entregues:
                    dados = item.get("dados_entrega", {})
                    with st.expander(f"👤 {dados.get('nome', 'Sem nome')} ({item['codigo']})"):
                        st.write(f"**Item:** {item['descricao']}")
                        st.write(f"**Documento:** {dados.get('documento', 'N/A')}")
                        st.write(f"**Data/Hora:** {dados.get('data_hora', 'N/A')}")
                        
                        if dados.get("foto_recebedor"):
                            st.image(dados["foto_recebedor"], caption="Comprovante / Rosto do Recebedor", use_container_width=True)
                            
        else:
            st.write("**Dar Baixa / Registrar Entrega:**")
            pendentes = [i for i in st.session_state.banco_objetos if i["status"] in ["Disponível", "Agendado"]]
            
            if not pendentes:
                st.info("Não há itens pendentes para entrega no momento.")
            else:
                item_selecionado = st.selectbox("Selecione o Item para Entrega:", [f"{i['codigo']} - {i['descricao']}" for i in pendentes])
                codigo_item = item_selecionado.split(" - ")[0]
                
                nome_rec = st.text_input("Nome Completo do Passageiro Recebedor:")
                doc_rec = st.text_input("Documento (CPF / RG):")
                
                if "cam_dev_ativa" not in st.session_state:
                    st.session_state.cam_dev_ativa = False
                if "foto_dev_temp" not in st.session_state:
                    st.session_state.foto_dev_temp = None

                if not st.session_state.cam_dev_ativa:
                    if st.button("📷 Fotografar Recebedor / Documento", key="btn_abrir_cam_dev"):
                        st.session_state.cam_dev_ativa = True
                        st.rerun()
                else:
                    st.warning("⚠️ **Permissão do Dispositivo:** Por favor, permita o acesso à câmera.")
                    captura_dev = st.camera_input("Capturar Rosto / Documento", key="camera_dev_input")
                    
                    if captura_dev:
                        st.image(captura_dev, caption="Foto do Recebedor/Documento", use_container_width=True)
                        col_save_dev, col_clear_dev = st.columns(2)
                        
                        with col_save_dev:
                            if st.button("💾 Salvar Foto", key="save_img_dev"):
                                st.session_state.foto_dev_temp = captura_dev.getvalue()
                                st.success("Foto armazenada!")