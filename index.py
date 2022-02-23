
def menu():
    print("INGRESE OPCION QUE DESEA EJECUTAR\n 1. crear ticket\n 2. consultar ticket\n 3. eliminar ticket\n 4. editar ticket \n 5.enlistar tickets \n")
    redireccion=None
    opcion=int(input("DIGITE OPCION"))
    if opcion==1:
        redireccion='/creacionTicket.html'
    if opcion ==2:
        redireccion='/consultaTicket.html'
    if opcion ==3:
        redireccion='/eliminarTicket.html'
    if opcion ==4:
        redireccion='/editarTicket.html'
    if opcion ==5:
        redireccion='/recuperaTickets.html'
    return(redireccion)
