import pandas as pd

df = pd.read_csv("dados_brutos.csv")

print("--- TABELA BRUTA DO JEITO QUE VEIO DO SISTEMA ---")
print(df)
import pandas as pd


df = pd.read_csv("dados_brutos.csv")

print("--- TABELA BRUTA DO JEITO QUE VEIO DO SISTEMA ---")
print(df)
print("-" * 50)  
df = df.drop_duplicates(subset=["id_registro"], keep="first")
print("--- TABELA APÓS REMOVER DUPLICADOS ---")
print(df)
import pandas as pd

df = pd.read_csv("dados_brutos.csv")

print("--- TABELA BRUTA DO JEITO QUE VEIO DO SISTEMA ---")
print(df)
print("-" * 50)

df = df.drop_duplicates(subset=["id_registro"], keep="first")

df["colaborador"] = df["colaborador"].str.strip().str.title()

print("--- TABELA APÓS PADRONIZAR OS NOMES ---")
print(df)
print("-" * 50)
import pandas as pd


df = pd.read_csv("dados_brutos.csv")

print("--- TABELA BRUTA DO JEITO QUE VEIO DO SISTEMA ---")
print(df)
print("-" * 50)


df = df.drop_duplicates(subset=["id_registro"], keep="first")

df["colaborador"] = df["colaborador"].str.strip().str.title()


df["pecas_processadas"] = df["pecas_processadas"].fillna(0)

print("--- TABELA APÓS TRATAR O VALOR VAZIO (NaN) ---")
print(df)
print("-" * 50)
import pandas as pd

df = pd.read_csv("dados_brutos.csv")

print("--- TABELA BRUTA DO JEITO QUE VEIO DO SISTEMA ---")
print(df)
print("-" * 50)


df = df.drop_duplicates(subset=["id_registro"], keep="first")

df["colaborador"] = df["colaborador"].str.strip().str.title()

df["pecas_processadas"] = df["pecas_processadas"].fillna(0)


df.loc[df["pecas_processadas"] < 0, "pecas_processadas"] = 0

print("--- TABELA APÓS CORRIGIR VALORES NEGATIVOS ---")
print(df)
print("-" * 50)

df.loc[df["pecas_processadas"] < 0, "pecas_processadas"] = 0



df.loc[df["colaborador"] == "Nao Identificado", "colaborador"] = (
    "NÃO IDENTIFICADO (AUDITORIA)"
)


print("--- TABELA COM LIMPEZA FINAL ---")
print(df)
print("-" * 50)
import pandas as pd

# 1. Abre o arquivo CSV real
df = pd.read_csv("dados_brutos.csv")

print("--- TABELA BRUTA DO JEITO QUE VEIO DO SISTEMA ---")
print(df)
print("-" * 50)

# ==========================================
# ETAPA DE LIMPEZA (CONCLUÍDA)
# ==========================================
df = df.drop_duplicates(subset=["id_registro"], keep="first")
df["colaborador"] = df["colaborador"].str.strip().str.title()
df["pecas_processadas"] = df["pecas_processadas"].fillna(0)
df.loc[df["pecas_processadas"] < 0, "pecas_processadas"] = 0
df.loc[df["colaborador"] == "Nao Identificado", "colaborador"] = (
    "NÃO IDENTIFICADO (AUDITORIA)"
)


# ==========================================
# NOVO BLOC0: CRIANDO COLUNAS DE CÁLCULO
# ==========================================

# Coluna Nova 1: Porcentagem de Eficiência
# Dividimos o processado pela meta e multiplicamos por 100. O round(..., 1) deixa só uma casa decimal.
df["eficiencia_porcentagem"] = round(
    (df["pecas_processadas"] / df["meta_setor"]) * 100, 1
)

# Coluna Nova 2: Status da Meta (Bateu ou Não?)
# O .apply(lambda ...) funciona como o "SE" (IF) do Excel linha por linha
df["status_meta"] = df["eficiencia_porcentagem"].apply(
    lambda x: "Bateu Meta" if x >= 100.0 else "Abaixo da Meta"
)


# Mostra o resultado final absoluto na tela do terminal
print("--- RELATÓRIO FINAL PRONTO PARA O LOOKER STUDIO ---")
print(df)
print("-" * 50)

# Salva esse resultado em um arquivo NOVO no seu computador
df.to_csv("movimentacao_final_looker.csv", index=False)
print("💾 Arquivo 'movimentacao_final_looker.csv' salvo com sucesso na pasta!")
