# logistics-performance-etl-bi
Este projeto consiste no desenvolvimento de uma solução de inteligência de dados de ponta a ponta (End-to-End) voltada para o setor de logística e gestão de performance de equipes (People Analytics).   A solução engloba desde a extração e tratamento automatizado de dados operacionais brutos utilizando **Python e Pandas**
Em operações logísticas de grande volume, os relatórios gerados por sistemas integrados frequentemente apresentam inconsistências como registros duplicados, valores nulos, dados corrompidos e falta de padronização textual. 

Este projeto resolve essa dor ao criar um pipeline controlado que garante a qualidade do dado (*Data Quality*) antes que ele alimente a camada de visualização executiva, otimizando o tempo de tomada de decisão da liderança.

### 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python 3.x** (Linguagem base)
* **Pandas** (Engenharia e manipulação de dados)
* **VS Code** (Ambiente de desenvolvimento)
* **Looker Studio** (Visualização de dados e Business Intelligence)

---

## ⚙️ Arquitetura do Pipeline (ETL)

O script desenvolvido em Python realiza o processo completo de **ETL (Extract, Transform, Load)** baseado em regras de negócio específicas da operação:

1. **Extração (Extract):** Leitura automática dos relatórios brutos em formato `.csv` gerados pelo sistema da operação.
2. **Transformação (Transform):**
   * Remoção de registros com IDs duplicados para evitar inflação de volumes.
   * Tratamento de valores vazios (`NaN`) e correção de anomalias numéricas (ex: valores negativos de produção convertidos para zero).
   * Padronização de strings (nomes de colaboradores e setores) limpando espaços em branco e aplicando *Title Case* (`.str.strip().str.title()`).
   * **Injeção de Regras de Negócio:** Criação de colunas calculadas de Eficiência Percentual baseada no atingimento de metas operacionais individuais.
3. **Carga (Load):** Exportação dos dados tratados para um novo arquivo otimizado (`movimentacao_final_looker.csv`), blindando o arquivo original de qualquer corrupção.

---

## 📊 O Dashboard (Looker Studio)

O arquivo tratado foi conectado à nuvem do Looker Studio para a estruturação de um painel de alta legibilidade, dividido estrategicamente em camadas:

* **Camada Macro (Scorecards):** Indicadores consolidados de **Volume Total Processado** (Soma) e **Média Geral de Eficiência** do time.
* **Camada de Comparação (Gráfico de Combinação):** Cruzamento visual dinâmico entre o **Volume Real Processado vs. Meta Esperada** por colaborador, permitindo identificar instantaneamente desvios de performance.
* **Camada Micro (Tabela Detalhada):** Visão analítica aberta por colaborador para auditoria fina dos supervisores da área.
* **Camada de Proporção (Gráfico de Rosca):** Distribuição percentual do status de atingimento de metas da equipe (*Bateu Meta* vs. *Abaixo da Meta*).

---

## 📁 Estrutura do Repositório

```text
├── data/
│   ├── dados_brutos.csv                  # Relatório original extraído do sistema
│   └── movimentacao_final_looker.csv     # Base de dados limpa e calculada pelo Python
├── src/
│   └── pipeline_etl.py                   # Script Python com a lógica de tratamento (Pandas)
└── README.md                             # Documentação do projeto
