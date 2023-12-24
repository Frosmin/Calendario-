

# hayEN = "en hola"
# print(hayEN[1])


# #imprimor todas las letras de la palabra hayEN
# for i in hayEN:
#     if i == 'h' :
#         print(True)
#     else:
#         print(False)    
# print("--------------------------------------------")
# def hay (palabra, letra):
#    for i in palabra:
#        if  i == letra:
#            print(True)
#     #    else:
#     #           print(False) 

# hay("hola mundo", 'o')


 
def hayRecursivo (palabra, letra):
    if len(palabra) == 0:
        print(False)
    else:
        if palabra[0] == letra:
            print(True)
        else:
            hayRecursivo(palabra[1:], letra)

hayRecursivo("hola mundo", 's')