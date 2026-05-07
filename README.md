# Automação de Cadastro de Produtos 🐍📦

Este projeto foi desenvolvido para automatizar o fluxo de entrada de dados em sistemas legados ou web, onde não há uma API disponível. O script utiliza técnicas de **RPA (Robotic Process Automation)** para ler uma base de dados externa e realizar o preenchimento automático de formulários.

##  Tecnologias Utilizadas
- **Python**: Linguagem principal.
- **Pandas**: Para manipulação e leitura da base de dados (CSV).
- **PyAutoGUI**: Para controle de mouse e teclado e automação da interface.
- **Time**: Gerenciamento de intervalos de execução (pausas de segurança).

## Funcionalidades
- Leitura automatizada de arquivos `.csv` contendo listas de produtos.
- Navegação automática entre campos do formulário (Login, Nome, Preço, Categoria).
- Tratamento de fluxo com pausas configuráveis para evitar erros de carregamento de página.
- Feedback visual ao usuário ao finalizar o processo.

##  Como rodar o projeto
1. Instale as dependências:
   ```bash
   pip install pyautogui pandas
