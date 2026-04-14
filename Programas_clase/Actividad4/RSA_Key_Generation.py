import math

# 1: Generar dos números primos distintos p y q
# Simplificación k=6 dígitos totales, por lo tanto p y q de son de 3 dígitos
p = 499 
q = 503 

# 2: Calcular el módulo n
# n = p * q
n = p * q

# 3: Calcular la función phi de Euler
# phi(n) = (p - 1)(q - 1)
phi = (p - 1) * (q - 1)

# 4: Elegir un entero e
# Debe cumplir 1 < e < phi y gcd(e, phi) = 1
e = 65537  # Comúnmente usado por ser un primo de Fermat y eficiente para la encriptación
if math.gcd(e, phi) != 1:
    # Si 65537 no funciona con estos primos, usamos uno más pequeño
    e = 17 

# 5: Calcular el inverso multiplicativo modular d
# d = e^(-1) mod phi(n)
d = pow(e, -1, phi)

# PASO 6: Retornar Llave Pública (n, e) yPrivada (n, d)
print(f"Llave Pública (n, e): ({n}, {e})")
print(f"Llave Privada (n, d): ({n}, {d})")