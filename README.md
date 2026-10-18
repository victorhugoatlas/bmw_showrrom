# 🚗 BMW Virtual Showroom & Line-Up

Um catálogo virtual full-stack inspirado na interface do site oficial da BMW, desenvolvido em **Django** e **Tailwind CSS**. 

O projeto foi construído para organizar a minha ideia de Line Up ideal para a BMW do Brasil, permitindo que os entusiastas visualizem fotos de alta resolução, filtrem os modelos por categorias e tenham acesso direto aos relatórios e fichas técnicas em **PDF** gerados pelo configurador alemão (`bmw.de`).

---

## 🌟 Funcionalidades

- **Design Premium Inspirado na BMW:** Interface minimalista e moderna com tipografia limpa, ícones e insígnias.
- **Catálogo Organizado:** Ordenação automática rigorosa das séries de veículos (**X7 a X1, 7 a 1**).
- **Ordenação Personalizada Interna:** Campo de ordenação manual (`order`) para organizar versões dentro da mesma família de forma exata.
- **Filtros Dinâmicos Combinados (Sem Reload):**
  - **Séries / Famílias:** Filtre instantaneamente por séries (X7, X5, 3, 5, Z, etc.).
  - **Motorização:** Filtro rápido por tipo de combustível (*Gasolina, Flex, Híbrido Plug-In, Elétrico, Diesel*).
  - **Linha M / M Performance:** Filtro dedicado para exibir apenas modelos da divisão desportiva.
- **Visualizador de Fichas e PDFs:** Acesso ao arquivo PDF de configuração oficial do veículo.
- **Painel de Gestão Integrado (CRUD):** Interface gráfica e formulários amigáveis no próprio site para cadastrar, editar ou remover modelos sem precisar acessar a área administrativa padrão do Django.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.x, Django 5.x
- **Frontend:** HTML5, Tailwind CSS (CDN), JavaScript (Vanilla ES6)
- **Manipulação de Imagens:** Pillow
- **Banco de Dados:** SQLite (Desenvolvimento / Local)

---

## 📁 Estrutura do Projeto

```text
bmw_showroom/
├── catalog/                # Aplicação principal do catálogo
│   ├── fixtures/           # Dados pré-cadastrados (initial_data.json)
│   ├── templates/          # Templates HTML estilizados
│   ├── admin.py            # Configuração do Django Admin
│   ├── forms.py            # Formulários de cadastro/edição
│   ├── models.py           # Modelagem de dados dos veículos
│   ├── urls.py             # Rotas de navegação e ações
│   └── views.py            # Lógica das views e ordenação
├── core/                   # Configurações centrais do Django (settings, urls, wsgi)
├── media/                  # Imagens e PDFs dos veículos
├── .gitignore              # Proteção de arquivos locais e banco de dados
├── manage.py               # Executável de comandos Django
└── README.md               # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para clonar o repositório, instalar as dependências e carregar o catálogo pré-configurado.

### 1. Pré-requisitos
- **Python 3.10+** instalado no seu computador.
- **Git** instalado.

---

### 2. Clonar o Repositório

```bash
git clone https://github.com/victorhugoatlas/bmw_showrrom
cd bmw_showroom
```

---

### 3. Criar e Ativar o Ambiente Virtual

# No Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

# No Linux / macOS:
```bash
python -m venv venv
source venv/bin/activate
```

---

### 4. Instalar as Dependências

```bash
pip install django pillow
```

---

### 5. Configurar o Banco de Dados e Carregar os Dados Iniciais

Execute os comandos abaixo para criar a estrutura das tabelas no banco de dados SQLite local e carregar os veículos e arquivos pré-cadastrados:

```bash
# Criar as tabelas no banco
python manage.py migrate

# Carregar o catálogo completo com todos os modelos e dados
python manage.py loaddata initial_data.json
```

---

### 6. Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

Abra o seu navegador e acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📝 Licença

Este projeto foi desenvolvido com fins educacionais e demonstrativos para portfólio full-stack. As marcas, logos e referências da BMW pertencem ao grupo BMW.