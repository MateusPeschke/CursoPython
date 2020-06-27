import matplotlib.pyplot as plt


x = [i for i in range(1,7)]
y = [i for i in range(11,17)]

meses = ['Janeiro','Fevereiero','Março','Abril','Maio','Junho']
valores = [105235,107697,110256,109236,108859,109986]


plt.plot(meses,valores, color =  "yellow") # grafico de linha 

plt.bar(meses,valores, color = "green") # grafico de barra

plt.scatter(meses,valores, color = "blue") # grafico de ponto

plt.title("Faturamento no primeiro semestre de 2017")


plt.xlabel("Meses")
plt.ylabel("Valores")
plt.xlim("Janeiro","Junho") # limite do grafico
plt.ylim(100000,130000) # limite do grafico


plt.show()