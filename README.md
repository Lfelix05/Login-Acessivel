# Firebase User Registration

Este projeto é uma aplicação de registro e login de usuários utilizando apenas HTML, CSS, JavaScript e Firebase (Auth e Firestore). O objetivo é permitir o cadastro de usuários com recursos de acessibilidade, sem necessidade de back-end em Python ou Flask.

## Estrutura do Projeto

```
Login-Acessivel
├── firebase-user-registration
│   ├── firebase.js           # Configuração e funções do Firebase
├── register.html             # Página de registro de usuário
├── login.html                # Página de login de usuário
├── home.html                 # Página inicial após login (exemplo)
└── README.md                 # Documentação do projeto
```

## Instalação e Uso

1. **Clone o repositório:**
   ```
   git clone <URL_DO_REPOSITORIO>
   cd Login-Acessivel
   ```

2. **Configure o Firebase:**
   - No arquivo `firebase-user-registration/firebase.js`, insira as credenciais do seu projeto Firebase no objeto `firebaseConfig`.
   - Certifique-se de que a autenticação por Email/Senha está habilitada no console do Firebase.

3. **Abra o projeto:**
   - Basta abrir o arquivo `register.html` ou `login.html` no seu navegador.
   - Não é necessário rodar servidor Python ou instalar dependências.

## Recursos

- Registro de usuário com email, senha, confirmação de senha e seleção de recursos de acessibilidade.
- Login de usuário com autenticação Firebase.
- Dados de acessibilidade e favoritos salvos no Firestore.
- Totalmente front-end, sem necessidade de back-end.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.