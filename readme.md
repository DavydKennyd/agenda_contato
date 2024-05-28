# Agenda de Contatos

Este é um projeto simples de uma agenda de contatos em Python, que permite adicionar, remover, listar e salvar contatos em um arquivo JSON.

## Estrutura do Projeto

```bash
meu_projeto/
│
├── contato.py
├── agenda.py
├── main.py
└── agenda.json (será criado automaticamente ao salvar contatos)
```


### Arquivo `contato.py`

Este arquivo define a classe `Contato`, que representa um contato na agenda.

### Arquivo `agenda.py`

Este arquivo define a classe `Agenda`, que gerencia uma lista de contatos. A classe inclui métodos para adicionar, remover, listar e salvar contatos em um arquivo JSON.

### Arquivo `main.py`

Este arquivo contém a função principal que interage com o usuário através do terminal, permitindo a gestão dos contatos na agenda.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone o repositório ou baixe os arquivos do projeto.
3. Navegue até o diretório do projeto no terminal.
4. Execute o arquivo `main.py` com o comando:

```sh
python main.py
```
# Funcionalidade

1. **Adicionar Contato**  
   Permite ao usuário adicionar um novo contato, solicitando o nome, telefone e email.

2. **Remover Contato**  
   Permite ao usuário remover um contato existente pelo nome.

3. **Listar Contatos**  
   Exibe todos os contatos atualmente salvos na agenda.

4. **Sair**  
   Encerra o programa.

# Dependências

Este projeto não possui dependências externas além do Python padrão.

# Autor

Feito por Davyd Kennyd. Sinta-se à vontade para contribuir, relatar problemas ou fazer perguntas.
