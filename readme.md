# 🚌 Achados e Perdidos Unimar

Aplicação web responsiva desenvolvida em **Python/Streamlit** para o gerenciamento de pertences esquecidos ou perdidos em ônibus, com uma interface para a equipe da empresa e outra para os passageiros.

---

## 📑 Sumário

1. [Objetivo Principal](#1-objetivo-principal)
2. [Módulos da Interface Administrativa](#2-módulos-da-interface-administrativa)
3. [Interface do Passageiro](#3-interface-do-passageiro)
4. [Design e Identidade Visual](#4-design-e-identidade-visual)
5. [Tecnologias Utilizadas](#5-tecnologias-utilizadas)
6. [Como Executar](#6-como-executar)

---

## 1. Objetivo Principal

Desenvolvimento de uma aplicação web responsiva em **Python/Streamlit** composta por duas interfaces integradas:

- **Painel Administrativo**: para a equipe da empresa.
- **Portal do Passageiro**: acessível via **QR Code** / dispositivo móvel.

---

## 2. Módulos da Interface Administrativa

### 📦 1. Itens Cadastrados
Separação clara entre os pertences:
- **Aguardando Retirada**
- **Itens Devolvidos** (com histórico detalhado de entregas)

### ➕ 2. Cadastrar Novo Item
Formulário de registro com:
- Seleção do **local de guarda**: *Vila das Contratadas / Vale* ou *Garagem Unimar*.
- **Geração automática** do código/matrícula do item.
- Acionamento da **câmera** com fluxo de **Permissão**, **Salvar** e **Limpar/Refazer**.

### 📋 3. Análise de Devoluções e Recebedores
- Visualização da **galeria de comprovantes/documentos**.
- **Baixa final das entregas**, com captura de foto do recebedor e registro do documento no momento da entrega.

---

## 3. Interface do Passageiro

| Recurso | Descrição |
|---|---|
| 🔎 **Busca em Tempo Real** | Filtro por palavra-chave, linha/rota do ônibus e código do pertence. |
| 📩 **Agendamento de Retirada** | Formulário direto no item para solicitar o resgate do pertence. |
| 📢 **Alerta de Perda** | Formulário para registrar perdas recentes, com detalhes da rota e data do ocorrido. |

---

## 4. Design e Identidade Visual

### Imagem de Fundo
Integração direta da foto oficial da frota Unimar (`1001217215.jpg`), convertida em **Base64** para carregamento automático em qualquer dispositivo, sem depender de links externos.

### Tipografia
- **Cabeçalhos**: fonte **Poppins** (tamanho grande).
- **Corpo de texto**: pilha de fontes modernas — *SF Pro / Helvetica / Arial / Segoe UI*.

### Esquema de Cores
- Cabeçalhos e rótulos em **Azul Unimar** (`#1D61B0`).
- Caixas de texto com **fundo claro** e texto em **preto**, para máxima legibilidade.
- Suporte nativo ao idioma português (`lang="pt-BR"`).

### Rodapé Interativo
Dois botões em formato de **ícones redondos**, com borda azul e fundo branco (usando **Font Awesome**), direcionando para:
- 🌐 **Site Oficial da Unimar**
- 📍 **Rota no Google Maps**

---

## 5. Tecnologias Utilizadas

- **Python**
- **Streamlit**
- **HTML/CSS** (customização da interface)
- **Google Fonts** (Poppins)
- **Font Awesome** (ícones do rodapé)

---

## 6. Como Executar

```bash
# 1. Instale as dependências
pip install streamlit

# 2. Execute a aplicação (ajuste o nome do arquivo principal, se necessário)
streamlit run app.py
```

> 💡 Mantenha o arquivo `1001217215.jpg` na mesma pasta da aplicação para que a imagem de fundo seja convertida em Base64 corretamente.