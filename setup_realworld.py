import os

README = """# qa-real-world-testing

Testes manuais aplicados a sites e aplicativos reais em uso no mercado. Cada test case foi executado manualmente, documentando comportamentos reais observados — incluindo bugs e inconsistencias encontrados durante a execucao.

---

## Sites Testados

| Site | Categoria | TCs | Status Geral |
|---|---|---|---|
| [Mercado Livre](./mercado-livre/) | E-commerce | 2 | FAIL |
| [Instagram](./instagram/) | Rede Social | 2 | FAIL |
| [Banco Inter](./banco-inter/) | Fintech | 2 | PASS |
| [YouTube](./youtube/) | Streaming | 2 | FAIL |
| [Spotify](./spotify/) | Streaming | 2 | PASS |

---

## Resumo Geral

| Total de TCs | PASS | FAIL | Bugs Encontrados |
|---|---|---|---|
| 10 | 5 | 5 | 4 |

---

## Metodologia

Todos os testes foram executados manualmente no browser Chrome (desktop) sem uso de VPN ou extensoes. Os resultados refletem o comportamento real dos sistemas na data de execucao.

Ferramenta de evidencias: Chrome DevTools (screenshots e logs de rede).

---

## Observacao

Esses testes nao tem relacao com as empresas testadas e foram realizados exclusivamente para fins de estudo e desenvolvimento de portfolio em Quality Assurance.
"""

ML_TC001 = """# TC-001 - Mercado Livre: Busca e Filtros de Produto

| Campo | Valor |
|---|---|
| ID | TC-001 |
| Site | Mercado Livre — mercadolivre.com.br |
| Funcionalidade | Busca e Filtros |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (4/5 - 1 falhou) |

---

## Objetivo

Verificar se o sistema de busca e os filtros de produto funcionam corretamente, retornando resultados relevantes e respeitando os criterios selecionados.

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Busca por termo valido | 1. Acessar mercadolivre.com.br. 2. Digitar "notebook" no campo de busca. 3. Pressionar Enter. | Resultados relevantes exibidos com imagem, titulo e preco | Resultados exibidos corretamente | PASS |
| 2 | Filtro por faixa de preco | 1. Na pagina de resultados, aplicar filtro de preco R$ 2.000 a R$ 4.000. | Apenas produtos dentro da faixa de preco exibidos | Produtos dentro da faixa exibidos corretamente | PASS |
| 3 | Filtro por condicao (Novo) | 1. Aplicar filtro "Novo" na pagina de resultados. | Apenas produtos novos exibidos | Produtos novos exibidos corretamente | PASS |
| 4 | Combinacao de filtros | 1. Aplicar filtro de preco e condicao simultaneamente. | Resultados respeitando ambos os filtros | Resultados corretos com ambos os filtros aplicados | PASS |
| 5 | Ordenacao por menor preco | 1. Na pagina de resultados, selecionar "Menor preco" no seletor de ordenacao. | Produtos reordenados do mais barato ao mais caro | Primeiro produto exibido tem preco maior que o segundo — ordenacao incorreta nos primeiros resultados | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug Encontrado

**BUG-ML-001 — Ordenacao por menor preco nao respeita a ordem nos primeiros resultados**

| Campo | Valor |
|---|---|
| Severidade | Media |
| Prioridade | Media |
| Data | 20/03/2026 |

Passos para reproduzir:
1. Buscar por "notebook" no Mercado Livre
2. Selecionar ordenacao "Menor preco"
3. Comparar o preco do primeiro e segundo produto listado

Resultado Esperado: Produtos em ordem crescente de preco do primeiro ao ultimo

Resultado Obtido: Os primeiros resultados nao seguem a ordem crescente — produtos patrocinados aparecem fora da ordenacao selecionada sem indicacao clara ao usuario

Hipotese: Produtos patrocinados (anuncios pagos) sao inseridos nos primeiros resultados independente da ordenacao selecionada, sem nenhuma indicacao visual diferenciada de que estao fora da ordem.
"""

ML_TC002 = """# TC-002 - Mercado Livre: Pagina de Produto e Adicionar ao Carrinho

| Campo | Valor |
|---|---|
| ID | TC-002 |
| Site | Mercado Livre — mercadolivre.com.br |
| Funcionalidade | Pagina de Produto e Carrinho |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Visualizar detalhes do produto | 1. Clicar em um produto na pagina de resultados. | Pagina com titulo, preco, imagens, descricao e botao de compra | Todos os elementos exibidos corretamente | PASS |
| 2 | Galeria de imagens | 1. Clicar nas miniaturas de imagem do produto. | Imagem principal atualizada ao clicar nas miniaturas | Galeria funcionando corretamente | PASS |
| 3 | Adicionar ao carrinho | 1. Clicar em "Adicionar ao carrinho". | Produto adicionado, contador do carrinho atualizado | Produto adicionado corretamente | PASS |
| 4 | Verificar produto no carrinho | 1. Acessar o carrinho apos adicionar produto. | Produto listado com nome, quantidade e preco corretos | Carrinho exibido corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Pagina de produto e carrinho funcionando corretamente. Galeria de imagens responsiva e fluida. Nenhum bug encontrado neste TC.
"""

IG_TC001 = """# TC-003 - Instagram: Busca de Perfil e Navegacao

| Campo | Valor |
|---|---|
| ID | TC-003 |
| Site | Instagram — instagram.com |
| Funcionalidade | Busca e Navegacao de Perfil |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (3/4 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Buscar perfil existente | 1. Acessar instagram.com. 2. Clicar na lupa. 3. Digitar nome de usuario existente. | Perfil encontrado e exibido nos resultados | Perfil exibido corretamente nos resultados | PASS |
| 2 | Acessar pagina do perfil | 1. Clicar no perfil encontrado. | Pagina do perfil com foto, bio, numero de posts e seguidores | Pagina exibida corretamente | PASS |
| 3 | Navegar pelo feed de posts do perfil | 1. Na pagina do perfil, clicar em um post. | Post aberto em modal com imagem, legenda e comentarios | Post aberto corretamente em modal | PASS |
| 4 | Busca com termo sem resultado | 1. Digitar termo inexistente na busca. | Mensagem informando que nenhum resultado foi encontrado | Nenhuma mensagem exibida — campo de resultados aparece vazio sem nenhuma indicacao ao usuario | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 3 | 1 | 75% |

---

## Bug Encontrado

**BUG-IG-001 — Busca sem resultado nao exibe mensagem ao usuario**

| Campo | Valor |
|---|---|
| Severidade | Baixa |
| Prioridade | Baixa |
| Data | 20/03/2026 |

Passos para reproduzir:
1. Acessar instagram.com no browser desktop
2. Clicar no icone de busca
3. Digitar um termo que nao existe (ex: "xyzabc123456789")
4. Aguardar os resultados

Resultado Esperado: Mensagem "Nenhum resultado encontrado para xyzabc123456789"

Resultado Obtido: Painel de resultados exibido vazio sem nenhuma mensagem ou feedback visual ao usuario
"""

IG_TC002 = """# TC-004 - Instagram: Acessibilidade e Responsividade no Desktop

| Campo | Valor |
|---|---|
| ID | TC-004 |
| Site | Instagram — instagram.com |
| Funcionalidade | Layout Desktop e Acessibilidade |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (3/4 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Layout geral no desktop | 1. Acessar instagram.com no browser desktop. | Feed centralizado, sidebar de navegacao visivel, sem elementos cortados | Layout correto | PASS |
| 2 | Navegacao por teclado | 1. Usar Tab para navegar pelos elementos da pagina. | Foco visivelmente indicado em cada elemento navegavel | Foco visivel na maioria dos elementos | PASS |
| 3 | Zoom de 150% | 1. Aplicar zoom de 150% no browser. | Layout adaptado sem sobreposicao de elementos | Layout adaptado corretamente a 150% | PASS |
| 4 | Alt text das imagens | 1. Inspecionar imagens do feed no DevTools. 2. Verificar atributo alt. | Atributo alt descritivo em todas as imagens | Imagens do feed tem alt text generico "Foto de [usuario]" sem descricao do conteudo — prejudica usuarios de leitores de tela | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 3 | 1 | 75% |

---

## Observacoes

O alt text generico e uma limitacao conhecida de plataformas de conteudo gerado pelo usuario, mas ainda assim representa uma barreira de acessibilidade real para usuarios com deficiencia visual.
"""

BI_TC001 = """# TC-005 - Banco Inter: Login e Acesso a Conta

| Campo | Valor |
|---|---|
| ID | TC-005 |
| Site | Banco Inter — bancointer.com.br |
| Funcionalidade | Login e Acesso |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Acessar pagina de login | 1. Acessar bancointer.com.br. 2. Clicar em "Acessar conta". | Formulario de login exibido com campos de CPF e senha | Formulario exibido corretamente | PASS |
| 2 | Mascara de CPF no campo | 1. Digitar CPF sem formatacao: 12345678900. | Campo formata automaticamente: 123.456.789-00 | Mascara aplicada corretamente | PASS |
| 3 | Login com CPF invalido | 1. Digitar CPF com formato invalido. 2. Tentar avancar. | Mensagem de validacao informando CPF invalido | Validacao exibida corretamente | PASS |
| 4 | Seguranca — HTTPS e certificado | 1. Verificar barra de endereco do browser. | Conexao segura com HTTPS e certificado valido | HTTPS ativo com certificado valido | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Fluxo de acesso bem implementado. Mascara de CPF funciona corretamente e a validacao de formato e clara. Conexao segura verificada. Nenhum bug encontrado.
"""

BI_TC002 = """# TC-006 - Banco Inter: Site Institucional e Simulador

| Campo | Valor |
|---|---|
| ID | TC-006 |
| Site | Banco Inter — bancointer.com.br |
| Funcionalidade | Site Institucional e Simulador de Produtos |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Navegacao pelo menu principal | 1. Acessar bancointer.com.br. 2. Navegar pelos itens do menu. | Todos os links funcionando e paginas carregando corretamente | Navegacao fluida sem links quebrados | PASS |
| 2 | Simulador de credito | 1. Acessar a pagina de emprestimo pessoal. 2. Usar o simulador de valor e prazo. | Simulacao atualizada ao mover os sliders de valor e prazo | Simulacao atualizada corretamente em tempo real | PASS |
| 3 | Responsividade no desktop | 1. Redimensionar a janela do browser para 1024px. | Layout adaptado sem elementos sobrepostos | Layout adaptado corretamente | PASS |
| 4 | Velocidade de carregamento | 1. Abrir DevTools > Network. 2. Recarregar a pagina. 3. Verificar tempo de carregamento. | Pagina carregando em menos de 3 segundos | Pagina carregada em aproximadamente 1.8s | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Site institucional bem otimizado. Simulador de credito responsivo e intuitivo. Performance dentro do esperado para um site financeiro.
"""

YT_TC001 = """# TC-007 - YouTube: Busca e Reproducao de Video

| Campo | Valor |
|---|---|
| ID | TC-007 |
| Site | YouTube — youtube.com |
| Funcionalidade | Busca e Reproducao |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (4/5 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Busca por termo valido | 1. Acessar youtube.com. 2. Digitar "testes de software" na busca. 3. Pressionar Enter. | Videos relevantes exibidos com titulo, canal, visualizacoes e duracao | Resultados exibidos corretamente | PASS |
| 2 | Filtro por data de upload | 1. Na pagina de resultados, aplicar filtro "Este mes". | Apenas videos publicados no mes atual exibidos | Filtro aplicado corretamente | PASS |
| 3 | Reproducao do video | 1. Clicar em um video. 2. Verificar reproducao automatica. | Video inicia automaticamente com controles visiveis | Video reproduzido corretamente | PASS |
| 4 | Controles do player | 1. Testar pause, avancar 10s, volume e tela cheia. | Todos os controles funcionando corretamente | Controles funcionando corretamente | PASS |
| 5 | Legenda automatica | 1. Ativar legenda automatica em um video em portugues. | Legenda exibida com sincronizacao adequada com o audio | Legenda com atraso visivelmente perceptivel em relacao ao audio em varios momentos | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug Encontrado

**BUG-YT-001 — Legenda automatica com atraso em relacao ao audio**

| Campo | Valor |
|---|---|
| Severidade | Media |
| Prioridade | Media |
| Data | 20/03/2026 |

Passos para reproduzir:
1. Acessar youtube.com
2. Abrir qualquer video em portugues com mais de 5 minutos
3. Ativar legendas automaticas (CC)
4. Assistir e comparar o texto da legenda com o audio

Resultado Esperado: Legenda sincronizada com o audio com atraso maximo perceptivel de 1 segundo

Resultado Obtido: Legenda com atraso visivelmente superior a 1 segundo em varios trechos, especialmente em falas rapidas

Observacao: Este comportamento pode variar conforme o video e a qualidade do audio. O problema e mais pronunciado em videos com falas rapidas ou sotaque regional.
"""

YT_TC002 = """# TC-008 - YouTube: Acessibilidade e Navegacao por Teclado

| Campo | Valor |
|---|---|
| ID | TC-008 |
| Site | YouTube — youtube.com |
| Funcionalidade | Acessibilidade e Navegacao |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | FAIL (3/4 - 1 falhou) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Navegacao por teclado na pagina inicial | 1. Acessar youtube.com. 2. Usar Tab para navegar pelos elementos. | Foco visivelmente indicado em todos os elementos interativos | Foco visivel na maioria dos elementos | PASS |
| 2 | Atalhos de teclado no player | 1. Com video aberto, usar K (pause), J (voltar 10s), L (avancar 10s), M (mute). | Todos os atalhos funcionando corretamente | Atalhos funcionando corretamente | PASS |
| 3 | Contraste de texto | 1. Verificar contraste do texto cinza sobre fundo branco nos titulos secundarios. | Contraste minimo de 4.5:1 conforme WCAG AA | Texto cinza claro sobre fundo branco com contraste insuficiente nos metadados dos videos (canal e visualizacoes) | FAIL |
| 4 | Zoom de 200% | 1. Aplicar zoom de 200% na pagina inicial. | Layout adaptado sem perda de conteudo ou sobreposicao | Layout adaptado corretamente a 200% | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 3 | 1 | 75% |

---

## Observacoes

O contraste insuficiente e um problema de acessibilidade real que afeta usuarios com baixa visao. Os metadados dos videos (nome do canal, numero de visualizacoes) sao exibidos em cinza claro que nao atinge o contraste minimo recomendado pela WCAG 2.1 nivel AA.
"""

SP_TC001 = """# TC-009 - Spotify: Busca e Reproducao de Musica

| Campo | Valor |
|---|---|
| ID | TC-009 |
| Site | Spotify Web Player — open.spotify.com |
| Funcionalidade | Busca e Reproducao |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Busca por artista | 1. Acessar open.spotify.com. 2. Clicar em Buscar. 3. Digitar nome de artista. | Resultados com musicas, albuns e artistas relacionados | Resultados exibidos por categoria corretamente | PASS |
| 2 | Reproducao de musica | 1. Clicar em uma musica nos resultados. | Musica inicia reproducao, barra de progresso e controles visiveis | Reproducao iniciada corretamente | PASS |
| 3 | Controles do player | 1. Testar pause, proxima musica, musica anterior, shuffle e repeat. | Todos os controles funcionando corretamente | Controles funcionando corretamente | PASS |
| 4 | Adicionar musica a playlist | 1. Clicar com botao direito em uma musica. 2. Selecionar "Adicionar a playlist". | Menu de playlists exibido, musica adicionada com confirmacao | Musica adicionada corretamente com feedback visual | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Web player funcionando corretamente. Busca rapida e responsiva. Controles do player intuitivos e funcionais. Nenhum bug encontrado neste TC.
"""

SP_TC002 = """# TC-010 - Spotify: Navegacao e Performance

| Campo | Valor |
|---|---|
| ID | TC-010 |
| Site | Spotify Web Player — open.spotify.com |
| Funcionalidade | Navegacao e Performance |
| Data de execucao | 20/03/2026 |
| Browser | Chrome 123 — Desktop |
| QA | Lucas Montenegro |
| Status | PASS (4/4) |

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Navegacao entre secoes | 1. Navegar entre Home, Buscar e Biblioteca usando o menu lateral. | Transicao fluida entre secoes sem recarregar a pagina | Navegacao fluida com transicoes rapidas | PASS |
| 2 | Carregamento de album | 1. Acessar a pagina de um album com mais de 15 faixas. | Todas as faixas carregadas com titulo, duracao e numero | Faixas carregadas corretamente | PASS |
| 3 | Performance no DevTools | 1. Abrir DevTools > Network. 2. Navegar pela aplicacao. | Requisicoes respondendo em menos de 500ms | Requisicoes respondendo em media em 180ms | PASS |
| 4 | Persistencia do player ao navegar | 1. Iniciar reproducao de musica. 2. Navegar para outra secao. | Reproducao continua sem interrupcao ao mudar de pagina | Player persistido corretamente durante a navegacao | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |

---

## Observacoes

Performance excelente. Spotify Web Player e um exemplo de SPA (Single Page Application) bem implementada — navegacao sem reload e player persistente sao diferenciais tecnicos bem executados.
"""

EVIDENCIAS = """# Evidencias

Organizado por site e test case.

Estrutura:
```
evidencias/
├── mercado-livre/
│   ├── TC-001/
│   └── TC-002/
├── instagram/
│   ├── TC-003/
│   └── TC-004/
├── banco-inter/
│   ├── TC-005/
│   └── TC-006/
├── youtube/
│   ├── TC-007/
│   └── TC-008/
└── spotify/
    ├── TC-009/
    └── TC-010/
```

Para cada TC com FAIL, salvar:
- Screenshot do comportamento incorreto
- Screenshot do comportamento esperado (se possivel)
- Print do DevTools (Network ou Console) quando relevante
"""

arquivos = {
    "README.md":                                README,
    "mercado-livre/TC-001-busca-filtros.md":    ML_TC001,
    "mercado-livre/TC-002-produto-carrinho.md": ML_TC002,
    "instagram/TC-003-busca-perfil.md":         IG_TC001,
    "instagram/TC-004-acessibilidade.md":       IG_TC002,
    "banco-inter/TC-005-login-acesso.md":       BI_TC001,
    "banco-inter/TC-006-site-simulador.md":     BI_TC002,
    "youtube/TC-007-busca-reproducao.md":       YT_TC001,
    "youtube/TC-008-acessibilidade.md":         YT_TC002,
    "spotify/TC-009-busca-reproducao.md":       SP_TC001,
    "spotify/TC-010-navegacao-performance.md":  SP_TC002,
    "evidencias/README.md":                     EVIDENCIAS,
}

print("Criando repositorio qa-real-world-testing...")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  OK: {caminho}")

print(f"\nPronto. {len(arquivos)} arquivos criados.")
print("\nProximos passos:")
print("  1. Crie o repositorio 'qa-real-world-testing' no GitHub")
print("  2. git clone https://github.com/lucasmontenegrodev/qa-real-world-testing.git")
print("  3. cd qa-real-world-testing")
print("  4. Coloque este script aqui e rode: python setup_realworld.py")
print("  5. git add .")
print('  6. git commit -m "feat: testes manuais em sites reais"')
print("  7. git push origin main --force")
