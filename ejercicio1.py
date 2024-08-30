# numero x mayor que 5
# x=3
# if x >5:
#     print("x es mayor que 5")
# elif x== 5:
#     print("x es igual a 5")
# else:
#     print("x es menor que 5")





# numero x entre 5 y 10
# x=3
# if x>= 5 and x<=10:
#     print("x esta entre 5 y 10")
# else:
#     print("el numero no esta entre 5 y 10")

# # otra solución de numero entre 5 y 10
# if x in [5,6,7,8,9,10]:
#         print("x esta entre 5 y 10")
# else:
#     print("el numero no esta entre 5 y 10")


#si acaso puede manejar
#45   17    10
edad=int(input("ingrese la edad: "))
if edad >=18:
    print(f"si puede manejar, ya que tiene {edad} años")
elif edad ==17:
    alguien=input("manejas acompañado de alguien con licencia: ")
    if alguien == "si":
        print("si puede manejar")
    else:
        print(f"no puede manejar, tienes {edad} años y quieres manejas solo")
else:
    print(f"no puede manejar, tienes {edad} años")