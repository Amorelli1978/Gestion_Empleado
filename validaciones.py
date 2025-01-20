

def validar_dni(dni):
    return len(dni)==4 and dni.isdigit()

def validar_nombre_apellido(nombre_apellido):
    return len(nombre_apellido)>0
    

def validar_anio_de_ingreso(año_de_ingreso):
   return año_de_ingreso.isdigit() and 2000<= int(año_de_ingreso)<=2024

def validar_sexo(sexo):
    return sexo in ["M","F"]

def validar_edad(edad):
    return edad.isdigit() and 18 <= int(edad)>90

def validar_salario(salario):
    return salario.replace(",","",1).isdigit and float (salario)>0 