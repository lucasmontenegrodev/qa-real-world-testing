# TC-001 - Mercado Livre: Busca e Filtros de Produto

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