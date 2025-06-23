#Se crea la "Agenda" y se cargan los contactos
agenda = [
    {"nombre": "Ana", "telefono": "338", "email": "ana@email.com"},
    {"nombre": "Diego", "telefono": "419", "email": "diego@correo.com"},
    {"nombre": "Valentina", "telefono": "775", "email": "valentina@example.com"},
    {"nombre": "Javier", "telefono": "279", "email": "javier@correo.com"},
    {"nombre": "Agustina", "telefono": "395", "email": "agustina@mail.com"},
    {"nombre": "Carlos", "telefono": "111", "email": "carlos@correo.com"},
    {"nombre": "Julia", "telefono": "899", "email": "julia@example.com"},
    {"nombre": "Martina", "telefono": "771", "email": "martina@correo.com"},
    {"nombre": "Agustina", "telefono": "810", "email": "agustina@example.com"},
    {"nombre": "Camila", "telefono": "204", "email": "camila@example.com"},
    {"nombre": "Bruno", "telefono": "916", "email": "bruno@mail.com"},
    {"nombre": "Camila", "telefono": "845", "email": "camila@email.com"},
    {"nombre": "Florencia", "telefono": "143", "email": "florencia@email.com"},
    {"nombre": "Florencia", "telefono": "714", "email": "florencia@correo.com"},
    {"nombre": "Santiago", "telefono": "624", "email": "santiago@email.com"},
    {"nombre": "Carlos", "telefono": "145", "email": "carlos@correo.com"},
    {"nombre": "Luis", "telefono": "468", "email": "luis@mail.com"},
    {"nombre": "Tomás", "telefono": "768", "email": "tomás@email.com"},
    {"nombre": "Sofía", "telefono": "264", "email": "sofía@mail.com"},
    {"nombre": "Lucas", "telefono": "529", "email": "lucas@correo.com"},
    {"nombre": "Valentina", "telefono": "496", "email": "valentina@mail.com"},
    {"nombre": "Luis", "telefono": "752", "email": "luis@email.com"},
    {"nombre": "Sofía", "telefono": "340", "email": "sofía@mail.com"},
    {"nombre": "Mateo", "telefono": "224", "email": "mateo@correo.com"},
    {"nombre": "Diego", "telefono": "491", "email": "diego@example.com"},
    {"nombre": "Paula", "telefono": "909", "email": "paula@example.com"},
    {"nombre": "Elena", "telefono": "156", "email": "elena@example.com"},
    {"nombre": "Pedro", "telefono": "350", "email": "pedro@mail.com"},
    {"nombre": "Martina", "telefono": "110", "email": "martina@email.com"},
    {"nombre": "Tomás", "telefono": "318", "email": "tomás@correo.com"},
    {"nombre": "Javier", "telefono": "568", "email": "javier@mail.com"},
    {"nombre": "Sofía", "telefono": "213", "email": "sofía@mail.com"},
    {"nombre": "Martina", "telefono": "965", "email": "martina@email.com"},
    {"nombre": "Agustina", "telefono": "602", "email": "agustina@example.com"},
    {"nombre": "Ana", "telefono": "575", "email": "ana@correo.com"},
    {"nombre": "Diego", "telefono": "468", "email": "diego@example.com"},
    {"nombre": "Julia", "telefono": "722", "email": "julia@email.com"},
    {"nombre": "Ana", "telefono": "771", "email": "ana@correo.com"},
    {"nombre": "Javier", "telefono": "993", "email": "javier@correo.com"},
    {"nombre": "Agustina", "telefono": "664", "email": "agustina@example.com"},
    {"nombre": "Martina", "telefono": "758", "email": "martina@email.com"},
    {"nombre": "Florencia", "telefono": "784", "email": "florencia@correo.com"},
    {"nombre": "Javier", "telefono": "610", "email": "javier@example.com"},
    {"nombre": "Paula", "telefono": "537", "email": "paula@example.com"},
    {"nombre": "Diego", "telefono": "766", "email": "diego@mail.com"},
    {"nombre": "Paula", "telefono": "139", "email": "paula@email.com"},
    {"nombre": "Javier", "telefono": "970", "email": "javier@mail.com"},
    {"nombre": "Camila", "telefono": "863", "email": "camila@correo.com"},
    {"nombre": "Mateo", "telefono": "976", "email": "mateo@correo.com"},
    {"nombre": "Sofía", "telefono": "631", "email": "sofía@mail.com"},
    {"nombre": "Elena", "telefono": "652", "email": "elena@mail.com"},
    {"nombre": "Agustina", "telefono": "561", "email": "agustina@example.com"},
    {"nombre": "Lucas", "telefono": "971", "email": "lucas@correo.com"},
    {"nombre": "Elena", "telefono": "559", "email": "elena@mail.com"},
    {"nombre": "Bruno", "telefono": "564", "email": "bruno@example.com"},
    {"nombre": "Julia", "telefono": "220", "email": "julia@example.com"},
    {"nombre": "Valentina", "telefono": "602", "email": "valentina@correo.com"},
    {"nombre": "Julia", "telefono": "271", "email": "julia@correo.com"},
    {"nombre": "Florencia", "telefono": "387", "email": "florencia@example.com"},
    {"nombre": "Luis", "telefono": "586", "email": "luis@example.com"},
    {"nombre": "Tomás", "telefono": "726", "email": "tomás@email.com"},
    {"nombre": "Valentina", "telefono": "453", "email": "valentina@example.com"},
    {"nombre": "Paula", "telefono": "125", "email": "paula@example.com"},
    {"nombre": "Agustina", "telefono": "422", "email": "agustina@correo.com"},
    {"nombre": "Paula", "telefono": "457", "email": "paula@example.com"},
    {"nombre": "Lucas", "telefono": "979", "email": "lucas@example.com"},
    {"nombre": "Martina", "telefono": "518", "email": "martina@mail.com"},
    {"nombre": "Tomás", "telefono": "438", "email": "tomás@mail.com"},
    {"nombre": "Luis", "telefono": "474", "email": "luis@example.com"},
    {"nombre": "Valentina", "telefono": "283", "email": "valentina@email.com"},
    {"nombre": "Ana", "telefono": "552", "email": "ana@mail.com"},
    {"nombre": "Bruno", "telefono": "599", "email": "bruno@mail.com"},
    {"nombre": "Elena", "telefono": "545", "email": "elena@email.com"},
    {"nombre": "Florencia", "telefono": "842", "email": "florencia@email.com"},
    {"nombre": "Elena", "telefono": "977", "email": "elena@email.com"},
    {"nombre": "Ana", "telefono": "242", "email": "ana@email.com"},
    {"nombre": "Ana", "telefono": "961", "email": "ana@mail.com"},
    {"nombre": "Camila", "telefono": "912", "email": "camila@correo.com"},
    {"nombre": "Pedro", "telefono": "657", "email": "pedro@correo.com"},
    {"nombre": "Diego", "telefono": "580", "email": "diego@example.com"},
    {"nombre": "Pedro", "telefono": "873", "email": "pedro@correo.com"},
    {"nombre": "Javier", "telefono": "727", "email": "javier@example.com"},
    {"nombre": "Santiago", "telefono": "845", "email": "santiago@mail.com"},
    {"nombre": "Florencia", "telefono": "179", "email": "florencia@mail.com"},
    {"nombre": "Javier", "telefono": "152", "email": "javier@email.com"},
    {"nombre": "Valentina", "telefono": "704", "email": "valentina@example.com"},
    {"nombre": "Carlos", "telefono": "914", "email": "carlos@example.com"},
    {"nombre": "Camila", "telefono": "290", "email": "camila@mail.com"},
    {"nombre": "Javier", "telefono": "626", "email": "javier@mail.com"},
    {"nombre": "Tomás", "telefono": "467", "email": "tomás@example.com"},
    {"nombre": "Ana", "telefono": "876", "email": "ana@correo.com"},
    {"nombre": "Martina", "telefono": "794", "email": "martina@mail.com"},
    {"nombre": "Carlos", "telefono": "132", "email": "carlos@mail.com"},
    {"nombre": "Javier", "telefono": "275", "email": "javier@mail.com"},
    {"nombre": "Paula", "telefono": "195", "email": "paula@email.com"},
    {"nombre": "Valentina", "telefono": "932", "email": "valentina@example.com"},
    {"nombre": "Lucas", "telefono": "806", "email": "lucas@example.com"},
    {"nombre": "Camila", "telefono": "524", "email": "camila@mail.com"},
    {"nombre": "Elena", "telefono": "510", "email": "elena@mail.com"},
    {"nombre": "Luis", "telefono": "976", "email": "luis@correo.com"},
]

# Se crea una función extraer el nombre de cada contacto
# Se usa para ordenar la agenda por nombre alfabeticamente
def obtener_nombre(contacto):
    return contacto["nombre"]

# Búsqueda lineal
def busqueda_lineal(agenda, nombre):
    #Recorre con ciclo for. 
    #Por cada contacto en la agenda, si coincide con el nombre pasado por parametro retorna el contacto
    for contacto in agenda:
        #Para simplicar la prueba utilizamos lower para que no distinga entre mayusculas o minusculas
        if contacto["nombre"].lower() == nombre.lower(): 
            return contacto
    return None

# Ordena la lista por nombre usando "sort" y la funcion obtener_nombre
agenda.sort(key=obtener_nombre)

#Imprimo la agenda completa ordenada alfabeticamente
print("Agenda ordenada:\n")
for contacto in agenda:
    print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

# Búsqueda binaria con lista ya ordenada
def buscar_binaria(agenda, nombre):

    #Declaro "Las puntas del indice como izquierda y derecha"
    izquierda = 0
    derecha = len(agenda) - 1
    
    #Mientras izquierda sea menor que derecha
    while izquierda <= derecha:
        #calcula el medio y guarda en variale medio
        medio = (izquierda + derecha) // 2
        #variable nombre_medio es igual a la agenda [con el medio calculado arriba] y el nombre que este en ese indice
        nombre_medio = agenda[medio]["nombre"]

        #Si el nombre en ese indice medio es igual al nombre traido como parametro devuelve el mismo valor.
        if nombre_medio.lower() == nombre.lower():
            return agenda[medio]
        #Si el nombre como parametro es menor al nombre medio. Derecha va a ser igual a medio - 1
        elif nombre.lower() < nombre_medio.lower():
            derecha = medio - 1
            #Sino izquierda va a ser igual a medio + 1
        else:
            izquierda = medio + 1

            #En resumen divide la lista en 2 y busca en cada mitad por separado comparando con un elemento central.
            #Si en menor se descarta la mitad izquierda y si es mayor la mitad derecha.

    return None

#Medicion tiempo busqueda lineal
import time
inicio_lineal = time.time()
resultado_lineal = busqueda_lineal(agenda,"Carlos")
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal

#Medicion tiempo busqueda binaria
inicio_binaria = time.time()
resultado_binaria = buscar_binaria(agenda,"Carlos")
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria

# Prueba búsqueda lineal y resultado por pantalla
resultado_lineal = busqueda_lineal(agenda, "Carlos")
print("Resultado búsqueda lineal:")
print(f"Nombre: {resultado_lineal['nombre']}, Teléfono: {resultado_lineal['telefono']}, Email: {resultado_lineal['email']}")
print(f"Tiempo de busqueda: {tiempo_lineal:.6f} segundos")

print("")
# Prueba búsqueda binaria y resultado por pantalla
resultado_binaria = buscar_binaria(agenda, "Carlos")
print("Resultado búsqueda binaria:")
print(f"Nombre: {resultado_binaria['nombre']}, Teléfono: {resultado_binaria['telefono']}, Email: {resultado_binaria['email']}")
print(f"Tiempo de busqueda: {tiempo_binaria:.6f} segundos")