<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/hero-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/hero-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-static.svg">
    <img src="assets/hero.svg" alt="Flávio Daniel, estudante de Ciência da Computação na UNICAP e técnico em Redes de Computadores, aberto a oportunidades de estágio. Três eixos de estudo se alternam: Desenvolvimento (a compra de ingresso do Sistema de Cinema, do React ao banco H2), Dados (codificação de variáveis categóricas e divisão treino e teste em um estudo de score de crédito) e IA (comparação entre Random Forest e KNN no mesmo estudo). Uma faixa inferior indica a base técnica: redes, sistemas e hardware." width="100%">
  </picture>
</p>

> Meu interesse está no desenvolvimento de software, em dados e em inteligência
> artificial: construir aplicações e explorar como preparar, organizar e usar
> informações.

Projetos, estudos e experimentos — cada um com o contexto em que foi feito.

## Tecnologias

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/tech-stack-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/tech-stack-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/tech-stack-static.svg">
    <img src="assets/tech-stack.svg" alt="Tecnologias presentes nos projetos e estudos. Linguagens: C, Python, Java, JavaScript, HTML e CSS. Frameworks e bibliotecas: React, Vite, Spring Boot e scikit-learn. Ferramentas e plataformas: Maven, Git, GitHub e Raspberry Pi. Também aparecem: Axios, Spring Data JPA, H2, pandas, notebooks Jupyter e GPIO." width="100%">
  </picture>
</p>

## Projetos

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

Site institucional para uma ONG, com conteúdo sobre acolhimento e bem-estar, serviços, galeria, depoimentos, voluntariado e doações. Construído com HTML, CSS e JavaScript. O site foi retirado do ar; o [código-fonte](https://github.com/Furubioo/SiteOngPartilhar) permanece disponível.

<details>
<summary>Ver a estrutura da página</summary>

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/partilhar-overview-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/partilhar-overview-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/partilhar-overview-static.svg">
    <img src="assets/partilhar-overview.svg" alt="Mapa esquemático do conteúdo do Site ONG Partilhar, não uma captura de tela: apresentação, três perguntas (quem somos, o que fazemos, por que fazemos), quatro categorias de serviços, galeria com cinco imagens, formulário de voluntariado, depoimentos em carrossel e chamada para doação." width="100%">
  </picture>
</p>

<p align="center"><sub>Esquema do conteúdo encontrado no código; não é uma captura da interface.</sub></p>

</details>

## Estudos em código

O [repositório acadêmico](https://github.com/Furubioo/registro-academico-ciencia-da-computacao) reúne 11 áreas de estudo em 5 trilhas — exercícios, revisões, notebooks e projetos didáticos, não uma lista de tecnologias que afirmo dominar.

<table>
  <tr>
    <td width="132" align="center"><img src="assets/icons/python.svg" width="34" height="34" alt="Python"> <img src="assets/icons/c.svg" width="34" height="34" alt="C"></td>
    <td><b>Lógica e fundamentos</b><br><a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-python">Python</a>: 61 exercícios · <a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/programacao-estruturada-c">C estruturado</a>: 124 exercícios<br><sub>lógica, vetores, matrizes, strings, ponteiros, structs e arquivos</sub></td>
  </tr>
  <tr>
    <td width="132" align="center"><img src="assets/icons/c.svg" width="34" height="34" alt="C"> <img src="assets/icons/java.svg" width="34" height="34" alt="Java"></td>
    <td><b>Estruturas de dados e orientação a objetos</b><br><a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/estruturas-dados-c">Estruturas de dados em C</a> · <a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/poo-java">POO em Java</a><br><sub>listas, filas, pilhas, deques, tabela hash · projetos didáticos independentes</sub></td>
  </tr>
  <tr>
    <td width="132" align="center"><img src="assets/icons/c.svg" width="34" height="34" alt="C"> <img src="assets/icons/python.svg" width="34" height="34" alt="Python"> <img src="assets/icons/raspberrypi.svg" width="34" height="34" alt="Raspberry Pi"></td>
    <td><b>Compiladores, concorrência e hardware</b><br><a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/construcao-compiladores">Compiladores</a> · <a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/infraestrutura-software">Concorrência</a> · <a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/fundamentos-hardware">Hardware</a><br><sub>lexer, parser e testes · algoritmo de Peterson e threads · jogo de memória com GPIO</sub></td>
  </tr>
  <tr>
    <td width="132" align="center"><img src="assets/icons/python.svg" width="34" height="34" alt="Python"></td>
    <td><b>Matemática computacional</b><br><a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/algebra-linear-computacional">Álgebra linear</a> · <a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/calculo-computacional">Cálculo</a> · <a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/metodos-numericos">Métodos numéricos</a><br><sub>notebooks: matrizes, cifra de Hill, transformações 2D/3D, limites, derivadas, integrais e modelagem</sub></td>
  </tr>
  <tr>
    <td width="132" align="center"><img src="assets/icons/python.svg" width="34" height="34" alt="Python"> <img src="assets/icons/scikit-learn.svg" width="34" height="34" alt="scikit-learn"></td>
    <td><b>Dados e aprendizado de máquina</b><br><a href="https://github.com/Furubioo/registro-academico-ciencia-da-computacao/tree/main/projetos-exploratorios">Projetos exploratórios</a><br><sub>score de crédito: variáveis categóricas, treino e teste, Random Forest e KNN</sub></td>
  </tr>
</table>

<p align="center"><sub>Três deles em movimento:</sub></p>

<p align="center">
  <picture>
    <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="assets/lab-mobile-static.svg">
    <source media="(max-width: 600px)" srcset="assets/lab-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/lab-static.svg">
    <img src="assets/lab.svg" alt="Três estudos do repositório acadêmico. Compilador em C: o lexer transforma y = x + 5; em tokens e o parser os consome, terminando em sucesso ou, sem o ponto e vírgula, em erro. Raspberry Pi: jogo de memória com três LEDs, três botões e LEDs de feedback certo e errado. Peterson: duas threads, wants[], turn e sched_yield, com uma thread por vez na seção crítica." width="100%">
  </picture>
</p>

## Formação

- **Ciência da Computação** — UNICAP · desde 2025, conclusão prevista em 2028
- **Técnico em Redes de Computadores** — ETE Pastor Isaac Martins Rodrigues · 2020–2022
