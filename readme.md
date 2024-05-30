# Monitoramento de eventos de entretenimento Sympla 

Este script Python acessa o site da sympla, coleta os dados dos eventos de entretenimento mais vistos nas últimas 24 horas e exporta os dados para uma planilha chamado eventos.csv. Os campos incluídos no arquivo são: `Nome do evento`, `Data do evento`, `Local do evento`, `Descricao do evento`, `Sobre o produtor`.


## Execução do Script

1. **Execute o script Python**
- O script acessará o site da sympla.
- Serão coletadas as informações dos eventos de entretenimento mais vistos nas últimas 24 horas.
- Os dados coletados vão ser exportados para uma planilha.

## Pré-requisitos

- Python 3.x
- Virtualenv (opcional, mas recomendado)

## Instalação

1. **Clone o repositório:**

```bash```
- git clone https://github.com/leonardotideveloper/monitoramento-sympla.git
- cd seu-projeto

2. **Crie e ative um ambiente virtual(opcional):**
- python -m venv venv
- source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'

3. **Instale as dependências:**
```bash```
- pip install -r requirements.txt

4. **Utilização:**
- python schedule.py
