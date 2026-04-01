# TC-002 - Mercado Livre: Pagina de Produto e Adicionar ao Carrinho

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