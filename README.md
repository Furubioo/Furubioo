<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/hero-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/hero-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-static.svg">
    <img src="assets/hero.svg" alt="Flávio Daniel, estudante de Ciência da Computação na UNICAP e técnico em Redes de Computadores. Desenvolvimento e dados aparecem como focos com projetos; IA aparece separada, apenas como interesse, sem projeto de modelagem ou treinamento." width="100%">
  </picture>
</p>

> Meus focos de estudo são desenvolvimento de software e dados. Também tenho
> interesse em IA, ainda sem projetos de modelagem ou treinamento para apresentar.

Aqui reúno projetos acadêmicos, exercícios e experimentos — cada um no seu
contexto de aprendizado.

<p align="center">
  <a href="#sobre">Sobre</a> ·
  <a href="#projetos-em-destaque">Projetos em destaque</a> ·
  <a href="#acervo-de-estudos">Acervo de estudos</a> ·
  <a href="#tecnologias">Tecnologias</a> ·
  <a href="#atividade-no-github">Atividade no GitHub</a> ·
  <a href="#formação">Formação</a>
</p>

## Sobre

Flávio Daniel é estudante de Ciência da Computação na UNICAP e técnico em Redes de Computadores. O foco principal de estudo está em desenvolvimento de software, dados e exploração de conceitos de IA como interesse acadêmico e experimental, sem projetos de modelagem ou treinamento para apresentar.

## Projetos em destaque

### Sistema de Cinema

Projeto acadêmico de POO, desenvolvido em equipe de três pessoas, em duas implementações independentes.

- **Terminal:** Java com `CinemaView`, `CinemaController` e `Usuario`; `EstrategiaPreco` oferece `PrecoComum` (preço-base), `PrecoCritico` (R$ 0) e `PrecoEstudante` (metade). Os dados são persistidos em `filmes.txt` e `usuarios.txt`.
- **Web:** páginas React + Vite usam Axios em `localhost:8080`; `POST /sessoes/{id}/comprar` chega a `SessaoController` e `SessaoRepository` (Spring Data JPA), com persistência em H2.

A versão web teve assistência de IA em parte do código.

[Repositório](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-) ·
[Terminal](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-/tree/main/cinema-console) ·
[Web](https://github.com/Furubioo/Sistema-de-Cinema-JAVA-/tree/main/cinema-system)

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/cinema-flow-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/cinema-flow-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/cinema-flow-static.svg">
    <img src="assets/cinema-flow.svg" alt="Diagrama esquemático das duas implementações do Sistema de Cinema. No terminal, a compra percorre CinemaView, CinemaController, Usuario, as estratégias alternativas PrecoComum (preço-base), PrecoCritico (R$ 0) e PrecoEstudante (metade), Sessao, Sala, Bilhete e PersistenciaArquivo. Na Web, uma requisição POST /sessoes/{id}/comprar segue de ProgramacaoPage/CompraPage por Axios em localhost:8080, SessaoController, SessaoRepository e H2; a resposta volta em trilha tracejada." width="100%">
  </picture>
</p>

### Site ONG Partilhar

Site institucional para uma ONG, com conteúdo sobre acolhimento e bem-estar, quatro categorias de serviços, galeria, depoimentos, voluntariado e doações. Construído com HTML, CSS e JavaScript e publicado na Vercel.

[Código-fonte](https://github.com/Furubioo/SiteOngPartilhar) ·
[Site publicado](https://side-da-ong-partilhar.vercel.app)

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/partilhar-overview-mobile.svg">
    <source media="(max-width: 600px)" srcset="assets/partilhar-overview-mobile-animated.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/partilhar-overview.svg">
    <img src="assets/partilhar-overview-animated.svg" alt="Mapa esquemático, não uma captura de tela, na ordem real do HTML do Site ONG Partilhar: Início, Sobre, Serviços, Galeria com cinco imagens, formulário de voluntariado, três depoimentos em carrossel JavaScript e Doações." width="100%">
  </picture>
</p>

<p align="center"><sub>O mapa segue a ordem do HTML — inclusive o formulário antes do carrossel e as doações depois — e não é uma captura da interface publicada.</sub></p>

## Acervo de estudos

O [repositório acadêmico](https://github.com/Furubioo/registro-academico-ciencia-da-computacao) reúne exercícios, revisões, notebooks, projetos didáticos e experimentos em múltiplas áreas. A seguir, as 11 áreas estão visíveis diretamente no perfil, sem menus ocultos.

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/lab-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/lab-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/lab-static.svg">
    <img src="assets/lab.svg" alt="Painel esquemático com cenas de três estudos. Compilador C: expressão e árvore sintática. Raspberry Pi: LEDs GPIO 18, 23 e 24; botões 27, 17 e 22; feedback certo no GPIO 15 ou errado no GPIO 14. Peterson: wants[0] e wants[1], turn, uma thread por vez na seção crítica e a outra aguardando com sched_yield()." width="100%">
  </picture>
</p>

### Fundamentos e programação

- [Python](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-python) — 61 exercícios independentes de fundamentos e lógica.
- [C estruturado](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/programacao-estruturada-c) — 124 exercícios sobre fundamentos, vetores, matrizes, strings, ponteiros, structs e arquivos.

### Estruturas e arquitetura de software

- [Estruturas de dados em C](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/estruturas-dados-c) — listas, filas, pilhas, deques e tabela hash.
- [POO em Java](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/poo-java) — projetos didáticos independentes de orientação a objetos.
- [Construção de compiladores](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/construcao-compiladores) — tokens, lexer, parser e testes.
- [Infraestrutura de software e concorrência](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/infraestrutura-software) — algoritmo de Peterson e estudos de threads.

### Hardware e matemática computacional

- [Fundamentos de hardware](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-hardware) — Raspberry Pi, GPIO, LEDs, botões e lógica de controle.
- [Álgebra linear computacional](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/algebra-linear-computacional) — matrizes, sistemas lineares, cifra de Hill e transformações 2D/3D.
- [Cálculo computacional](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/calculo-computacional) — limites, derivadas, integrais, curvas e volumes.
- [Métodos numéricos](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/metodos-numericos) — notebooks de modelagem e aproximação.

### Dados

- [Projetos exploratórios](https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/projetos-exploratorios) — notebooks e experimentos de análise e pré-processamento de dados.

O acervo também preserva projetos independentes de Java e C. Consulte o [README acadêmico](https://github.com/Furubioo/registro-academico-ciencia-da-computacao#readme) para aprofundamento e execução das disciplinas.

## Tecnologias

Ferramentas presentes nos projetos e estudos — a lista descreve o contexto do código, não um nível uniforme de domínio:

- **Projetos:** Java, React, Vite, Spring Boot, Maven, H2, HTML, CSS e JavaScript.
- **Estudos:** C, Python, Java e notebooks Jupyter.
- **Ambiente e hardware:** Git, GitHub, Vercel, Raspberry Pi e GPIO.

## Atividade no GitHub

<p align="center">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/project-timeline-mobile.svg">
    <img src="assets/project-timeline.svg" alt="Linha do tempo dos três repositórios em destaque: primeiro e último commit do Site ONG Partilhar, Sistema de Cinema e acervo acadêmico, consultados na API pública do GitHub." width="100%">
  </picture>
</p>

<p align="center">Datas do primeiro e do último commit (data do committer), consultadas na API REST pública do GitHub e atualizadas diariamente por workflow, sem token pessoal. <a href="https://github.com/Furubioo/Sistema-de-Cinema-JAVA-">Sistema de Cinema</a> · <a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao">Acervo acadêmico</a> · <a href="https://github.com/Furubioo/SiteOngPartilhar">Site ONG Partilhar</a>. O <a href="https://github.com/Furubioo">perfil no GitHub</a> continua sendo a fonte oficial das contribuições.</p>

## Formação

- Ciência da Computação — 4º período, UNICAP
- Técnico em Redes de Computadores

<p align="center">
  <i>Aprender, testar, depurar e entender o que acontece por dentro.</i>
</p>
