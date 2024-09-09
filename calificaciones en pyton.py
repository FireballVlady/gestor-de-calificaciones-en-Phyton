print ("gestor de calificaciones")
print("ingresa las calificaiones de 6 materias")
español = float(input("ingresa la calificacion de español"))
matematicas = float(input("ingresa la calificacion de matematicas "))
fisica = float(input("ingresa la calificacion de fisica "))
ingles = float(input("ingresa la calificacion de ingles "))
historia = float(input("ingresa la calificacion de historia "))
geografia = float(input("ingresa la calificaion de geografia"))

promedio = 0

promedio = español + matematicas + fisica + ingles + historia + geografia

promedio = promedio / 6

if promedio <= 5:
    print("estas reprobado, promedio de  ", promedio)
elif promedio >= 6:
    print("estas aprobado, `promedio ", promedio)
else:
    print("error al registrar las calificaciones, ingresalas de nuevo")