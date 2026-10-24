<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/hero-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/hero-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-static.svg">
    <img src="assets/hero.svg" alt="Flávio Daniel, estudante de Ciência da Computação na UNICAP e técnico em Redes de Computadores. Três eixos de estudo se alternam: Desenvolvimento (a compra de ingresso do Sistema de Cinema, do React ao banco H2), Dados (codificação de variáveis categóricas e divisão treino e teste em um estudo de score de crédito) e IA (comparação entre Random Forest e KNN no mesmo estudo). Uma faixa inferior indica a base técnica: redes, sistemas e hardware." width="100%">
  </picture>
</p>

> Meu interesse está no desenvolvimento de software, em dados e em inteligência
> artificial: construir aplicações e explorar como preparar, organizar e usar
> informações.

Aqui reúno projetos acadêmicos, exercícios e experimentos — cada um no seu
contexto de aprendizado.

<p align="center">
  <a href="#projetos-em-destaque">Projetos em destaque</a> ·
  <a href="#estudos-em-código">Estudos em código</a> ·
  <a href="#tecnologias">Tecnologias</a> ·
  <a href="#atividade-no-github">Atividade no GitHub</a> ·
  <a href="#formação">Formação</a>
</p>

## Projetos em destaque

### Sistema de Cinema

Projeto acadêmico de POO, desenvolvido em equipe de três pessoas, em duas implementações independentes, com fluxos para usuário, crítico e administrador.

- **Terminal:** Java com `CinemaView`, controllers e modelos; `Usuario` delega o cálculo do ingresso a estratégias de preço (comum, crítico gratuito e estudante com metade) e os dados são persistidos em arquivos.
- **Web:** páginas React + Vite comunicam via Axios com controllers Spring Boot, repositórios Spring Data JPA e banco H2; a compra é validada no controller antes de gravar a cadeira.

A versão web teve assistência de IA em parte do código.

[Repositório](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-) ·
[Terminal](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-/tree/main/cinema-console) ·
[Web](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-/tree/main/cinema-system)

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/cinema-flow-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/cinema-flow-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/cinema-flow-static.svg">
    <img src="assets/cinema-flow.svg" alt="Diagrama esquemático do Sistema de Cinema, não uma captura de tela. Terminal em Java: CinemaView, CinemaController, Usuario com PrecoComum (preço-base), PrecoCritico (zero) e PrecoEstudante (metade), Sessao, Sala e Bilhete, e PersistenciaArquivo em filmes.txt e usuarios.txt. Web: ProgramacaoPage, CompraPage, Axios, SessaoController (POST /sessoes/{id}/comprar), SessaoRepository com Spring Data JPA e banco H2. Mostra uma compra aceita e uma recusada por poltrona ocupada." width="100%">
  </picture>
</p>

### Site ONG Partilhar

Site institucional para uma ONG, com conteúdo sobre acolhimento e bem-estar, quatro categorias de serviços, galeria, depoimentos, voluntariado e doações. Construído com HTML, CSS e JavaScript. O site foi retirado do ar; o [código-fonte](https://github.com/Furubioo/SiteOngPartilhar) permanece disponível.

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/partilhar-overview-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/partilhar-overview-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/partilhar-overview-static.svg">
    <img src="assets/partilhar-overview.svg" alt="Mapa esquemático do conteúdo do Site ONG Partilhar, não uma captura de tela: apresentação, três perguntas (quem somos, o que fazemos, por que fazemos), quatro categorias de serviços, galeria com cinco imagens, formulário de voluntariado, depoimentos em carrossel e chamada para doação." width="100%">
  </picture>
</p>

<p align="center"><sub>O mapa representa as seções encontradas no código; não é uma captura da interface.</sub></p>

## Estudos em código

O [repositório acadêmico](https://github.com/Furubioo/registro-academico-ciencia-da-computacao)
organiza estudos por disciplina e tema: exercícios, revisões, notebooks e
projetos didáticos — não uma lista de tecnologias que afirmo dominar.

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/lab-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/lab-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/lab-static.svg">
    <img src="assets/lab.svg" alt="Três estudos do repositório acadêmico. Compilador em C: o lexer transforma y = x + 5; em tokens e o parser os consome, terminando em sucesso ou, sem o ponto e vírgula, em erro. Raspberry Pi: jogo de memória com três LEDs, três botões e LEDs de feedback certo e errado. Peterson: duas threads, wants[], turn e sched_yield, com uma thread por vez na seção crítica." width="100%">
  </picture>
</p>

<details>
<summary><b>Ver as 11 áreas do acervo</b></summary>

<br>

| Trilha de estudo | Áreas e exemplos |
| --- | --- |
| **Lógica e fundamentos** | [Python](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-python): 61 exercícios independentes; [C estruturado](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/programacao-estruturada-c): 124 exercícios independentes de fundamentos, vetores, matrizes, strings, ponteiros, structs e arquivos |
| **Estruturas de dados e orientação a objetos** | [Estruturas de dados em C](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/estruturas-dados-c): listas, filas, pilhas, deques e tabela hash; [POO em Java](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/poo-java): projetos didáticos independentes |
| **Compiladores, infraestrutura e hardware** | [Compiladores](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/construcao-compiladores): tokens, lexer, parser (valida a sintaxe e reporta sucesso ou erro) e testes; [Concorrência](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/infraestrutura-software): algoritmo de Peterson e threads; [Hardware](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-hardware): jogo de memória com LEDs, botões e GPIO em Raspberry Pi |
| **Matemática computacional** | [Álgebra linear](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/algebra-linear-computacional): matrizes, sistemas lineares, cifra de Hill e transformações 2D/3D; [Cálculo](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/calculo-computacional): limites, derivadas, integrais, curvas e volumes; [Métodos numéricos](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/metodos-numericos): notebooks de modelagem e aproximação |
| **Dados e aprendizado de máquina** | [Projetos exploratórios](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/projetos-exploratorios): notebook de score de crédito com codificação de variáveis categóricas, divisão treino/teste e comparação entre Random Forest e KNN (pandas e scikit-learn) |

O acervo também preserva projetos independentes de Java e C. Consulte o
[README acadêmico](https://github.com/Furubioo/registro-academico-ciencia-da-computacao#readme)
para navegar por todas as disciplinas e orientações de execução.

</details>

## Tecnologias

Ferramentas presentes nos projetos e estudos — a lista descreve o contexto do código, não um nível uniforme de domínio:

- **Projetos:** Java, React, Vite, Axios, Spring Boot, Spring Data JPA, Maven, H2, HTML, CSS e JavaScript.
- **Estudos:** C, Python, Java, notebooks Jupyter, pandas e scikit-learn.
- **Ambiente e hardware:** Git, GitHub, Raspberry Pi e GPIO.

## Atividade no GitHub

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/github-activity-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/github-activity-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/github-activity-static.svg">
    <img src="assets/github-activity.svg" alt="Calendário de contribuições públicas de Furubioo no GitHub em 2026: cada célula é um dia e a cor indica a intensidade. Abaixo, o total de contribuições do ano, os dias com atividade e o dia de maior atividade." width="100%">
  </picture>
</p>

<p align="center"><sub>Calendário gerado a partir da página pública de contribuições (sem token pessoal) e atualizado diariamente por workflow; se uma atualização falhar, a última imagem válida permanece. O <a href="https://github.com/Furubioo">perfil no GitHub</a> continua sendo a fonte oficial.</sub></p>

## Formação

- Ciência da Computação — 4º período, UNICAP
- Técnico em Redes de Computadores

<p align="center">
  <i>Aprender, testar, depurar e entender o que acontece por dentro.</i>
</p>
