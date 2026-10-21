<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/hero-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/hero-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-static.svg">
    <img src="assets/hero.svg" alt="Flávio Daniel — Ciência da Computação na UNICAP e técnico em Redes de Computadores. Focos de estudo: redes, sistemas e infraestrutura, hardware, estruturas de dados, depuração de baixo nível e bancos de dados." width="100%">
  </picture>
</p>

> Gosto de investigar o que acontece por baixo da interface: como os sistemas
> se organizam, como os dados percorrem uma rede e como código e hardware se
> encontram.

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

Projeto acadêmico de POO, desenvolvido em equipe de três pessoas, em duas implementações independentes.

- **Terminal:** Java com `CinemaView`, controllers e modelos; `Usuario` delega o cálculo do ingresso a estratégias de preço e os dados são persistidos em arquivos.
- **Web:** páginas React + Vite comunicam via Axios com controllers Spring Boot, repositórios JPA e banco H2.

A versão web teve assistência de IA em parte do código.

[Repositório](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-) ·
[Terminal](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-/tree/main/cinema-console) ·
[Web](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-/tree/main/cinema-system)

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/cinema-flow-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/cinema-flow-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/cinema-flow-static.svg">
    <img src="assets/cinema-flow.svg" alt="Diagrama esquemático do Sistema de Cinema, não uma captura de tela. Terminal Java: CinemaView, CinemaController, Usuario com PrecoComum (preço-base), PrecoCritico (gratuito) e PrecoEstudante (metade), Sessao/Sala/Bilhete e PersistenciaArquivo em filmes.txt e usuarios.txt. Web: páginas React, Axios, SessaoController, SessaoRepository e H2." width="100%">
  </picture>
</p>

### Site ONG Partilhar

Site institucional para uma ONG, com conteúdo sobre acolhimento e bem-estar, quatro categorias de serviços, galeria, depoimentos, voluntariado e doações. Construído com HTML, CSS e JavaScript e publicado na Vercel.

[Código-fonte](https://github.com/Furubioo/SiteOngPartilhar) ·
[Site publicado](https://side-da-ong-partilhar.vercel.app)

<p align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/partilhar-overview-mobile.svg">
    <img src="assets/partilhar-overview.svg" alt="Mapa esquemático do conteúdo do Site ONG Partilhar, não uma captura de tela: apresentação da missão, seções Quem somos/O que fazemos/Por que fazemos, quatro categorias de serviços, galeria, depoimentos, cadastro de voluntariado e doações." width="100%">
  </picture>
</p>

<p align="center"><sub>O mapa representa as seções encontradas no código; não é uma captura da interface publicada.</sub></p>

## Estudos em código

O [repositório acadêmico](https://github.com/Furubioo/registro-academico-ciencia-da-computacao)
organiza estudos por disciplina e tema: exercícios, revisões, notebooks e
projetos didáticos — não uma lista de tecnologias que afirmo dominar.

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/lab-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/lab-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/lab-static.svg">
    <img src="assets/lab.svg" alt="Diagrama esquemático de três estudos. Compilador C simplificado: código-fonte, tokens e árvore sintática. Raspberry Pi: três LEDs ligados a três botões e dois LEDs de feedback do jogo de memória. Peterson: estado possível com T0 na seção crítica e T1 aguardando via sched_yield." width="100%">
  </picture>
</p>

<details>
<summary><b>Ver as 11 áreas do acervo</b></summary>

<br>

| Trilha de estudo | Áreas e exemplos |
| --- | --- |
| **Lógica e fundamentos** | [Python](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-python): 61 exercícios independentes; [C estruturado](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/programacao-estruturada-c): 124 exercícios independentes de fundamentos, vetores, matrizes, strings, ponteiros, structs e arquivos |
| **Estruturas de dados e orientação a objetos** | [Estruturas de dados em C](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/estruturas-dados-c): listas, filas, pilhas, deques e tabela hash; [POO em Java](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/poo-java): projetos didáticos independentes |
| **Compiladores, infraestrutura e hardware** | [Compiladores](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/construcao-compiladores): tokens, lexer, parser e testes; [Concorrência](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/infraestrutura-software): algoritmo de Peterson e threads; [Hardware](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-hardware): jogo de memória com LEDs, botões e GPIO em Raspberry Pi |
| **Matemática computacional** | [Álgebra linear](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/algebra-linear-computacional): matrizes, sistemas lineares, cifra de Hill e transformações 2D/3D; [Cálculo](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/calculo-computacional): limites, derivadas, integrais, curvas e volumes; [Métodos numéricos](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/metodos-numericos): notebooks de modelagem e aproximação |
| **Exploração e análise de dados** | [Projetos exploratórios](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/projetos-exploratorios): notebook de pré-processamento de dados categóricos para estudo de score de crédito |

O acervo também preserva projetos independentes de Java e C. Consulte o
[README acadêmico](https://github.com/Furubioo/registro-academico-ciencia-da-computacao#readme)
para navegar por todas as disciplinas e orientações de execução.

</details>

## Tecnologias

Ferramentas presentes nos projetos e estudos — a lista descreve o contexto do código, não um nível uniforme de domínio:

- **Projetos:** Java, React, Vite, Spring Boot, Maven, H2, HTML, CSS e JavaScript.
- **Estudos:** C, Python, Java e notebooks Jupyter.
- **Ambiente e hardware:** Git, GitHub, Vercel, Raspberry Pi e GPIO.

## Atividade no GitHub

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/github-activity-dark.svg">
    <img src="assets/github-activity.svg" alt="Calendário anual das contribuições públicas de Furubioo no GitHub. Cada célula representa um dia e a intensidade da cor indica o nível de atividade exibido pelo GitHub." width="100%">
  </picture>
</p>

<p align="center">Calendário original armazenado no repositório e atualizado diariamente por workflow; usa somente a página pública de contribuições, sem token pessoal. Se uma atualização falhar, a última imagem válida permanece versionada. O <a href="https://github.com/Furubioo">perfil no GitHub</a> continua sendo a fonte oficial.</p>

## Formação

- Ciência da Computação — 4º período, UNICAP
- Técnico em Redes de Computadores

<p align="center">
  <i>Aprender, testar, depurar e entender o que acontece por dentro.</i>
</p>
