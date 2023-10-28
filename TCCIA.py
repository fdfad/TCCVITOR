import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

tabela = pd.read_csv("Alunos.csv", index_col=0)

tabela.isnull().sum()


tabela["mat"] = pd.to_numeric(tabela["mat"], downcast="float")
tabela["bio"] = pd.to_numeric(tabela["bio"], downcast="float")
tabela["port"] = pd.to_numeric(tabela["port"], downcast="float")
tabela["fisica"] = pd.to_numeric(tabela["fisica"], downcast="float")
tabela["quimica"] = pd.to_numeric(tabela["quimica"], downcast="float")
tabela["filosofia"] = pd.to_numeric(tabela["filosofia"], downcast="float")
tabela["sociologia"] = pd.to_numeric(tabela["sociologia"], downcast="float")
tabela["geo"] = pd.to_numeric(tabela["geo"], downcast="float")
tabela["historia"] = pd.to_numeric(tabela["historia"], downcast="float")
tabela["ingles"] = pd.to_numeric(tabela["ingles"], downcast="float")








plt.show()
print("Analise dos seu desempenho escolar em 6 anos")
time.sleep(1)


############ MATEMATICA #############

print("A sua maior nota em matematica foi " + str(tabela["mat"].dropna().max()))
time.sleep(1)

print("A sua menor nota em matematica foi " + str(tabela["mat"].dropna().min()))
time.sleep(1)

print("A sua nota media em matematica foi " + str(tabela["mat"].dropna().mean()))
time.sleep(1)

############ BIOLOGIA #############

print("A sua maior nota em biologia foi " + str(tabela["bio"].dropna().max()))
time.sleep(1)

print("A sua menor nota em biologia foi " + str(tabela["bio"].dropna().min()))
time.sleep(1)   

print("A sua nota media em biologia foi " + str(tabela["bio"].dropna().mean()))
time.sleep(1)

############ Português #############

print("A sua maior nota em português foi " + str(tabela["port"].dropna().max()))
time.sleep(1)

print("A sua menor nota em português foi " + str(tabela["port"].dropna().min()))
time.sleep(1)

print("A sua nota media em português foi " + str(tabela["port"].dropna().mean()))
time.sleep(1)

############ FÍSICA #############

print("A sua maior nota em física foi " + str(tabela["fisica"].dropna().max()))
time.sleep(1)

print("A sua menor nota em física foi " + str(tabela["fisica"].dropna().min()))
time.sleep(1)

print("A sua nota media em física foi " + str(tabela["fisica"].dropna().mean()))
time.sleep(1)

############ QUIMICA #############

print("A sua maior nota em quimica foi " + str(tabela["quimica"].dropna().max()))
time.sleep(1)

print("A sua menor nota em quimica foi " + str(tabela["quimica"].dropna().min()))
time.sleep(1)

print("A sua nota media em quimica foi " + str(tabela["quimica"].dropna().mean()))
time.sleep(1)

############ FILOSOFIA #############

print("A sua maior nota em filosofia foi " + str(tabela["filosofia"].dropna().max()))
time.sleep(1)

print("A sua menor nota em filosofia foi " + str(tabela["filosofia"].dropna().min()))
time.sleep(1)

print("A sua nota media em filosofia foi " + str(tabela["filosofia"].dropna().mean()))
time.sleep(1)

############ SOCIOLOGIA #############

print("A sua maior nota em sociologia foi " + str(tabela["sociologia"].dropna().max()))
time.sleep(1)

print("A sua menor nota em sociologia foi " + str(tabela["sociologia"].dropna().min()))
time.sleep(1)

print("A sua nota media em sociologia foi " + str(tabela["sociologia"].dropna().mean()))
time.sleep(1)

############ GEOGRAFIA #############

print("A sua maior nota em geografia foi " + str(tabela["geo"].dropna().max()))
time.sleep(1)

print("A sua menor nota em geografia foi " + str(tabela["geo"].dropna().min()))
time.sleep(1)

print("A sua nota media em geografia foi " + str(tabela["geo"].dropna().mean()))
time.sleep(1)

############ INGLES #############

print("A sua maior nota em ingles foi " + str(tabela["ingles"].dropna().max()))
time.sleep(1)

print("A sua menor nota em ingles foi " + str(tabela["ingles"].dropna().min()))
time.sleep(1)

print("A sua nota media em ingles foi " + str(tabela["ingles"].dropna().mean()))
time.sleep(1)

############ HISTORIA #############

print("A sua maior nota em historia foi " + str(tabela["historia"].dropna().max()))
time.sleep(1)

print("A sua menor nota em historia foi " + str(tabela["historia"].dropna().min()))
time.sleep(1)

print("A sua nota media em historia foi " + str(tabela["historia"].dropna().mean()))
time.sleep(1)

print(tabela.describe())

print("Aqui estão alguns graficos para melhor visualização do seu desempenho")
time.sleep(1)


tabela.dropna().hist()
tabela.dropna().plot.area(figsize=(18, 8), subplots=True)

plt.show()

