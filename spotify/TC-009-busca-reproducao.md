# TC-009 - Spotify: Busca e Reproducao de Musica

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