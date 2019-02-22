
dinero_sacar=int(input("Inserte el valor a sacar: "))
if (dinero_sacar%5000)==0 and dinero_sacar<=1000000:
  residuo50=dinero_sacar%50000
  billetes50=(dinero_sacar-residuo50)/50000
  
  residuo20=residuo50%20000
  billetes20=(residuo50-residuo20)/20000
  
  residuo10=residuo20%10000
  billetes10=(residuo20-residuo10)/10000
  
  billetes5=residuo10/5000
  print("Billetes de 50000: ",str (billetes50))
  print("Billetes de 20000: ",str (billetes20))
  print("Billetes de 10000: ",str (billetes10))
  print("Billetes de 5000: ",str (billetes5))

else:
  print("el valor no es valido")
  