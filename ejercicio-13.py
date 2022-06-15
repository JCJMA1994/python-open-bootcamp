paises = input("Ingrese paises separados con coma: ")

set_paises = [pais for pais in paises.split(",")]
print(",".join(sorted(list(set(set_paises)))))