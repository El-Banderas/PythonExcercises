from carro_camiao import Camiao

# Depois adicionar restrições de peso > 0 e < peso_maximo


camiao1 = Camiao(30, "azul", 100)

print("Peso inicial: ", camiao1.get_peso())
camiao1.acrescenta_peso(30)
print("Acrescenta 30: ", camiao1.get_peso())
camiao1.acrescenta_peso(30)
print("Acrescenta 30: ", camiao1.get_peso())
camiao1.tira_peso(50)
print("Tira 50: ", camiao1.get_peso())