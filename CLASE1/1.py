persona1=[]
persona2=[]

persona1.append("Ariana")
persona1.append(21)
persona1.append("Ingeniería")

persona2.append("Alvaro")
persona2.append(20)
persona2.append("Profesor")

suma=persona1[1]+persona2[1]
print(suma)

suma_listas=persona1+persona2
print(suma_listas)

suma_listas.reverse()
print("Mi lista nueva es:{}".format(suma_listas))

suma_listas.pop(1)
suma_listas.pop(3)
print("Mi lista actualizada  es:{}".format(suma_listas))

persona2.clear()
print("Mi lista nueva es:{}".format(persona2))
