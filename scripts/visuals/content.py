"""Conteúdo editável do perfil. Mude aqui e rode: python3 scripts/visuals/build.py

Regra de ouro: só entra o que dá para provar no código ou em um documento do próprio autor.
Por isso cada tecnologia exige `prova` (onde ela aparece de fato).
"""

IDENTIDADE = {
    'rotulo': 'CIÊNCIA DA COMPUTAÇÃO · UNICAP',
    'nome': 'Flávio Daniel',
    'subtitulo': 'Técnico em Redes de Computadores',
    # Uma linha discreta de status. Use None para ocultar (ex.: depois de efetivado).
    'status': 'aberto a oportunidades de estágio',
}

# (arquivo em assets/icons, rótulo exibido, prova)
TECNOLOGIAS = {
    'LINGUAGENS': [
        ('c', 'C', 'acervo: 124 exercícios, estruturas de dados e compilador'),
        ('python', 'Python', 'acervo: 61 exercícios e notebooks'),
        ('java', 'Java', 'Sistema de Cinema (terminal e back-end) e POO'),
        ('javascript', 'JavaScript', 'Site ONG Partilhar e front-end React'),
        ('html', 'HTML', 'Site ONG Partilhar'),
        ('css', 'CSS', 'Site ONG Partilhar'),
    ],
    'FRAMEWORKS E BIBLIOTECAS': [
        ('react', 'React', 'Sistema de Cinema (cinema-frontend)'),
        ('vite', 'Vite', 'Sistema de Cinema (cinema-frontend)'),
        ('spring', 'Spring Boot', 'Sistema de Cinema (cinema.backend)'),
        ('scikit-learn', 'scikit-learn', 'notebook de score de crédito'),
    ],
    'FERRAMENTAS E PLATAFORMAS': [
        ('maven', 'Maven', 'Sistema de Cinema (mvnw / pom.xml)'),
        ('git', 'Git', 'todos os repositórios'),
        ('github', 'GitHub', 'todos os repositórios'),
        ('raspberrypi', ('Raspberry', 'Pi'), 'acervo: jogo de memória com GPIO'),
    ],
}

# Itens sem ícone no catálogo: aparecem como texto.
TAMBEM = ['Axios', 'Spring Data JPA', 'H2', 'pandas', 'notebooks Jupyter', 'GPIO']
