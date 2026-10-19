# 💧 **Controle de Níveis de Água | Python.**

## 🔧 **Sobre o Projeto:**

Este projeto foi desenvolvido como uma atividade de programação em Python com o objetivo de simular o monitoramento do nível de água de um reservatório.

O programa executa no terminal e exibe uma mensagem correspondente ao nível atual do reservatório, utilizando cores diferentes para representar cada situação.

### 🌈 **Níveis do reservatório:**

| Nível | Situação | Cor |
|:---:|---|---|
| 1 | Muito Baixo (Crítico!) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito Alto (Alerta!) | Azul |

## ⚙️ **Funcionamento:**

O programa utiliza uma lista para armazenar as situações do reservatório e uma função para definir a cor correspondente ao nível informado. O nível atual é definido diretamente no código, simulando uma situação real de monitoramento.

### Exemplo:

nivel_atual = 2

Nesse caso, o programa identifica o nível como Baixo e exibe a mensagem na cor amarela.

## 🤖 **Tecnologias e ferramentas presentes no projeto:**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-0.4.x-green)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-blue?logo=visualstudiocode&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github&logoColor=white)

## 💻 **Como utilizar o programa:**

**1. Clone o repositório;**

No terminal, execute:
```
git clone https://github.com/juliafunes/controle-niveis-de-agua
```

Depois, acesse a pasta do projeto:

```
cd controle-niveis-agua
```

**2. Instale a biblioteca Colorama;**

O projeto utiliza a biblioteca Colorama para exibir as mensagens com cores diferentes no terminal.

Instale a biblioteca com:
```
pip install colorama
```

**3. Execute o programa;**

Execute o arquivo Python pelo terminal:
```
python app.py
```

**4. Altere o nível do reservatório.**

O nível atual pode ser definido diretamente no código por meio da variável:
```
nivel_atual = 2
```
## 🎯 **Aprendizados:**

Durante o desenvolvimento deste projeto, foram praticados os seguintes conceitos:

- Criação e utilização de listas em Python;
- Criação e utilização de funções;
- Uso de parâmetros em funções;
- Utilização de estruturas condicionais (if, elif e else);
- Uso de variáveis para armazenar informações;
- Acesso a elementos de uma lista utilizando índices;
- Importação e utilização de bibliotecas externas;
- Utilização da biblioteca Colorama para alterar as cores no terminal;
- Uso do return para retornar valores de uma função;
- Organização e estruturação de um programa em Python;
- Execução e testes do programa pelo terminal;
- Prática de programação estruturada;
- Versionamento e compartilhamento do projeto utilizando o GitHub.

### Projeto desenvolvido por **Júlia Funes** como atividade prática de programação.