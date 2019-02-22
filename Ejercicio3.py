print("Programa para saber si un año es bisiesto")
anio=int(input("Introduce el año que desees: "))
residuo=anio%4
if residuo==0:
  print("...")
  residuo2=anio%100
  if residuo2!=0:
    print("el año es bisiesto")
  else:
    print("...")
    residuo3=anio%400
    if residuo3==0:
      print("el año es bisiesto")
    else:
      print("el año no es bisiesto")
else:
  print("El año no es bisiesto")
  
print("fin")  