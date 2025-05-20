# Firebase User Registration

Este projeto é uma aplicação de registro de usuários que utiliza o Firebase como banco de dados. A aplicação é construída com Flask e permite que os usuários se registrem fornecendo seu email e senha.

## Estrutura do Projeto

```
firebase-user-registration
├── src
│   ├── app.py               # Ponto de entrada da aplicação Flask
│   ├── firebase_service.py   # Lógica para interagir com o Firebase
│   ├── models
│   │   └── user.py          # Definição da classe User
│   └── types
│       └── index.py         # Tipos e interfaces utilizados no projeto
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd firebase-user-registration
   ```

2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Configure as credenciais do Firebase no arquivo `firebase_service.py`.
2. Execute a aplicação:
   ```
   python src/app.py
   ```

3. Acesse a aplicação em seu navegador em `http://localhost:5000`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.