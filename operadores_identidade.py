# operadores de identidade analisam o endereço, enquanto operadores de igualdade analisam o valor
cidade_p1 = "sao paulo"
cidade_p2 = "sao paulo"
cidade_p3 = "rio de janeiro"
print(id(cidade_p1))
print(id(cidade_p2))
print(id(cidade_p3))
print(cidade_p1 is cidade_p2)
