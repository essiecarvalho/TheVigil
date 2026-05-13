# 🕯️ The Vigil - Interactive Web Narrative

Um hub interativo e motor de história baseado em texto (Text Adventure), construído com Python e Flask. 

## 📖 Sobre o Projeto
"The Vigil" é uma experiência narrativa interativa onde as escolhas do usuário ditam o rumo da história e o desfecho da cena. Mais do que um jogo de texto, este projeto foi desenvolvido para unir escrita criativa com arquitetura de software, aplicando conceitos práticos de manipulação de estado (*state management*) no back-end e a construção de interfaces de usuário imersivas.

## 🛠️ Tecnologias Utilizadas
* **Back-end:** Python, Flask (Micro-framework Web)
* **Front-end:** HTML5, CSS3
* **Arquitetura de Dados:** Dicionários e estruturas condicionais para mapeamento de rotas e árvores de decisão.

## 🧠 Lógica e Arquitetura
O coração da aplicação é um *Story Engine* (Motor de História) que roda em Python. Ele utiliza o micro-framework Flask com rotas dinâmicas para ler uma base de dados interna de cenas. O motor processa a escolha do usuário e renderiza dinamicamente o *template* HTML correspondente, entregando uma interface fluida com design focado na atmosfera da narrativa (*Dark Academia*).

## 🚀 Como executar o projeto localmente

Para rodar este projeto na sua máquina, siga os passos abaixo:

1. Clone este repositório:
```bash
git clone [https://github.com/essiecarvalho/thevigil.git](https://github.com/essiecarvalho/thevigil.git)
Acesse a pasta do projeto:

Bash
cd thevigil
Instale a dependência do Flask:

Bash
pip install flask
Execute o servidor principal:

Bash
python motor.py
O terminal exibirá um link local (geralmente http://127.0.0.1:5000). Basta segurar Ctrl e clicar no link ou colá-lo no seu navegador para iniciar a experiência.

Desenvolvido por Esther Carvalho.