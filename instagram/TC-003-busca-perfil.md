# TC-003 - Instagram: Busca de Perfil e Navegacao

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