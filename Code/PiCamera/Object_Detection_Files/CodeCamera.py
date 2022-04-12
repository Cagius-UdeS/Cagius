#Importation des librairies
import FonctionsCam as funcam

funcam.InitGPIO()
P,N = funcam.Scan()
print(P)
print(N)
  