# Hand Detector Framework

Este é um framework simples em Django para detecção de landmarks em imagens de mãos usando o padrão de projeto Strategy. O framework suporta as estratégias MediaPipeHandDetector e OpenPoseHandDetector.

## Estrutura de Diretórios

- **hand_detector_project/**: O diretório principal do projeto Django.
- **hand_detector/**: O aplicativo Django que contém a lógica do framework.
  - **migrations/**: Migrations do Django para o banco de dados.
  - **tests/**: Testes para o aplicativo.
- **manage.py**: Script de gerenciamento do Django.
- **README.md**: Este arquivo de documentação.

## Configuração e Execução

1. Clone este repositório.
2. Crie e ative um ambiente virtual (recomendado).
3. Instale as dependências: `pip install -r requirements.txt`.
4. Execute as migrações: `python manage.py migrate`.
5. Inicie o servidor de desenvolvimento: `python manage.py runserver`.
6. Acesse o aplicativo em http://127.0.0.1:8000/.

