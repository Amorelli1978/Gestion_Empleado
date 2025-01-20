class Trabajador:
    def __init__(self,dni,nombre_apellido,anio_de_ingreso,sexo,edad,salario):
        self.dni=dni
        self.nombre_apellido= nombre_apellido
        self.anio_de_ingreso=anio_de_ingreso
        self.sexo=sexo
        self.edad=edad
        self.salario=salario
        
    def __str__(self):
        return (f"DNI: {self.dni},"
                f"NOMBRE Y APELLIDO: {self.nombre_apellido},"
                f"AÑO DE INGRESO: {self.anio_de_ingreso},"
                f"SEXO: (F/M): {self.sexo},"
                f"EDAD: {self.edad},"
                f"SALARIO: {self.salario}"
                )
        
class GestionTrabajadores:
    def __init__(self):
       self.trabajadores=[]
        
    def registrar_trabajador(self,dni,nombre_apellido,anio_de_ingreso,sexo,edad,salario):
        trabajador= Trabajador(dni,nombre_apellido,anio_de_ingreso,sexo,edad,salario)
        self.trabajadores.append(trabajador)
    
    
    def buscar_trabajador(self,dni):
        for trabajador in self.trabajadores:
            if trabajador.dni ==dni:
                return trabajador
            return None
        
    def eliminar_trabajadores(self,dni):
        trabajador= self.buscar_trabajador(dni)
        if trabajador:
            self.trabajadores.remove(trabajador)
            return True
        return False
    
    def listar_trabajadores(self):
        return self.trabajadores      
    