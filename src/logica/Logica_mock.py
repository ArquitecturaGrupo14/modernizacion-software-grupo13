'''
Esta clase es tan sólo un mock con datos para probar la interfaz
'''
from itertools import count
from src.modelo.Carrera import Carrera
from src.modelo.Competidor import Competidor
from src.modelo.Apuesta import Apuesta
from src.modelo.Apostador import Apostador
from src.modelo.declarative_base import engine, Base, session, Session
class Logica_mock():

    def __init__(self):
        Base.metadata.create_all(engine)

        #Este constructor contiene los datos falsos para probar la interfaz

        self.session = Session()

        '''Nota:: Instruccion para limpiar la BD'''
        busqueda = self.session.query(Carrera).all()
        for carrera in busqueda:
            self.session.delete(carrera)
                        
        busqueda = self.session.query(Competidor).all()
        for competidor in busqueda:
            self.session.delete(competidor)
                
        busqueda = self.session.query(Apuesta).all()
        for apuesta in busqueda:
            self.session.delete(apuesta)

        busqueda = self.session.query(Apostador).all()
        for apostador in busqueda:
            self.session.delete(apostador)
                        
        self.session.commit()
     
        '''Nota:: Instruccion para poblar la BD'''
        '''Crea los objetos'''
        self.carrera1 = Carrera(nombre = 'Carrera1', abierta = True)
        self.carrera2 = Carrera(nombre = 'Carrera2', abierta = True)
        self.carrera3 = Carrera(nombre = 'Escondite Teams', abierta = True)
        self.carrera4 = Carrera(nombre = 'Lleva Teams', abierta = True)

        '''Adiciona los objetos a la sesión'''
        self.session.add(self.carrera1)
        self.session.add(self.carrera2)
        self.session.add(self.carrera3)
        self.session.add(self.carrera4)

        '''Persiste los objetos y cierra la sesión'''
        self.session.commit()

        '''Crea los objetos'''
        self.competidor1 = Competidor(nombre = 'competidor1Carrera1',probabilidad=0.5,cuota=10,ganador=False,id_carrera=1 )
        self.competidor2 = Competidor(nombre = 'competidor2Carrera1',probabilidad=0.5,cuota=20,ganador=False,id_carrera=1 )
        self.competidor3 = Competidor(nombre = 'competidor3Carrera2',probabilidad=0.3,cuota=15,ganador=False,id_carrera=2 )
        self.competidor4 = Competidor(nombre = 'competidor4Carrera2',probabilidad=0.7,cuota=25,ganador=False,id_carrera=2 )

        '''Adiciona los objetos a la sesión'''
        self.session.add(self.competidor1)
        self.session.add(self.competidor2)
        self.session.add(self.competidor3)
        self.session.add(self.competidor4)

        '''Persiste los objetos y cierra la sesión'''
        self.session.commit()


        '''Crea los objetos'''
        self.apostador1 = Apostador(nombre = 'apostador1')
        self.apostador2 = Apostador(nombre = 'apostador2')
        self.apostador3 = Apostador(nombre = 'apostador3')
        self.apostador4 = Apostador(nombre = 'apostador4')

        '''Adiciona los objetos a la sesión'''
        self.session.add(self.apostador1)
        self.session.add(self.apostador2)
        self.session.add(self.apostador3)
        self.session.add(self.apostador4)

        '''Persiste los objetos y cierra la sesión'''
        self.session.commit()



        '''Crea los objetos'''
        self.apostador1 = Apuesta(valor = 50,id_carrera=1,id_competidor=1,id_apostador=1)
        self.apostador2 = Apuesta(valor = 100,id_carrera=1,id_competidor=2,id_apostador=2)
        self.apostador3 = Apuesta(valor = 30,id_carrera=2,id_competidor=3,id_apostador=3)
        self.apostador4 = Apuesta(valor = 70,id_carrera=2,id_competidor=4,id_apostador=4)

        '''Adiciona los objetos a la sesión'''
        self.session.add(self.apostador1)
        self.session.add(self.apostador2)
        self.session.add(self.apostador3)
        self.session.add(self.apostador4)

        '''Persiste los objetos y cierra la sesión'''
        self.session.commit()


        self.session.close()

    

        self.apostadores = [{'Nombre':'Apostador1'},{'Nombre':"Ana Andrade"},{'Nombre':"Aymara Castillo"}]
        self.apuestas = [{'Apostador':'Pepe Pérez', 'Carrera':'Carrera 1', 'Valor':10, 'Competidor':'Juan Pablo Montoya'},\
                        {'Apostador':'Ana Andrade', 'Carrera':'Carrera 1', 'Valor':25, 'Competidor':'Michael Schumacher'},\
                        {'Apostador':'Aymara Castillo', 'Carrera':'Carrera 1', 'Valor':14, 'Competidor':'Juan Pablo Montoya'},\
                        {'Apostador':'Aymara Castillo', 'Carrera':'Carrera 2', 'Valor':45, 'Competidor':'Usain Bolt'}]

        


    def dar_carreras(self):
        carreras = [elem.__dict__ for elem in session.query(Carrera).all()]
        return carreras

       
    def dar_carrera(self, id_carrera):

        dic_carrera=[]
        busqueda = [elem.__dict__ for elem in session.query(Carrera).filter(Carrera.id == id_carrera).all()]
        
        if(len(busqueda)>0):
            dic_carrera = busqueda[0]
        return dic_carrera
        
        # PAso desde interfazeporra
    def dar_id_carrera(self, nombre_carrera):

        busqueda = session.query(Carrera).filter(Carrera.nombre == nombre_carrera).first()
        

        #print("El registro carrera es: "+str(busqueda.id))
        return busqueda.id


            
    def crear_carrera(self, nombre):
        busqueda = session.query(Carrera).filter(Carrera.nombre == nombre).all()
        if len(busqueda) == 0:
            carrera1 = Carrera(nombre=nombre,abierta=True)
            session.add(carrera1)
            session.commit()
            return True
        else:
            return False


    def editar_carrera(self, id, nombre):
        self.carreras[id]['Nombre'] = nombre

    def terminar_carrera(self, id):
        #Paso2: Busco la carrera por I para cambiar el estado de la carrera
        busqueda = session.query(Carrera).filter(Carrera.id == id).first()
        carrera = session.query(Carrera).get(busqueda.id)
        carrera.abierta = False
        session.add(carrera)
        session.commit()       

        #return False

    def eliminar_carrera(self, id):

        busqueda_apuesta = session.query(Apuesta,Carrera).join(Apuesta.carrera).filter(Apuesta.id_carrera == id['id']).all()

        if(len(busqueda_apuesta)==0):
            carrera = session.query(Carrera).get(id['id'])
            session.delete(carrera)
            session.commit()


    def dar_apostadores(self):
        apostadores = [elem.__dict__ for elem in session.query(Apostador).all()]
        return apostadores

    def aniadir_apostador(self, nombre):
        busqueda = session.query(Apostador).filter(Apostador.nombre == nombre).all()
        if len(busqueda) == 0:
            apostador1 = Apostador(nombre=nombre)
            session.add(apostador1)
            session.commit()
            return True
        else:
            return False
    
    def editar_apostador(self, id, nombre):
        self.apostadores[id]['Nombre'] = nombre
    
    def eliminar_apostador(self, id):
        del self.apostadores[id]

    def dar_competidores_carrera(self, id):

        competidores = session.query(Competidor).filter(Competidor.id_carrera == id).all()

        list_competidores=[]

        if (len(competidores)>0):
            for dic_competidores in competidores:
                list_competidores.append({'Nombre':dic_competidores.nombre})
                
       
        return list_competidores

    def dar_competidor(self, id_carrera, id_competidor):
        return self.carreras[id_carrera]['Competidores'][id_competidor].copy()

    
    def aniadir_competidor(self, id, nombre, probabilidad, nombre_carrera):
        
        id_carrera = session.query(Carrera).filter(Carrera.nombre == nombre_carrera).first()
               
        busqueda = session.query(Competidor).filter(Competidor.nombre == nombre).all()
        if len(busqueda) == 0:
           
            competidor1 = Competidor(nombre=nombre,probabilidad=probabilidad,id_carrera=id_carrera.id,cuota=probabilidad/(1-probabilidad),ganador=False)
            session.add(competidor1)
            session.commit()
            return True
        else:
            return False



    def editar_competidor(self, id_carrera, id_competidor, nombre, probabilidad):
        self.carreras[id_carrera]['Competidores'][id_competidor]['Nombre']=nombre
        self.carreras[id_carrera]['Competidores'][id_competidor]['Probabilidad']=probabilidad
    
    def eliminar_competidor(self, id_carrera, id_competidor):
        del self.carreras[id_carrera]['Competidores'][id_competidor]


    def dar_apuestas_carrera(self, id_carrera):

        self.apuestas = session.query(Apuesta,Carrera, Competidor, Apostador).join(Apuesta.carrera,Apuesta.competidor,Apuesta.apostador).filter(Apuesta.id_carrera == id_carrera).all()

        list_apuesta=[]
        nombre_carrera=""
        if (len(self.apuestas)>0):
            for dic_aptas in self.apuestas:
                list_apuesta.append({'Carrera':str(dic_aptas.Carrera.nombre),'Apostador':str(dic_aptas.Apostador.nombre),'Valor':dic_aptas.Apuesta.valor,'Competidor':str(dic_aptas.Competidor.nombre)})
                
            nombre_carrera = list_apuesta[0]['Carrera']
        
        return list(filter(lambda x: x['Carrera']==nombre_carrera, list_apuesta))


    def dar_apuesta(self, id_carrera, id_apuesta):
        return self.dar_apuestas_carrera(id_carrera)[id_apuesta].copy()

    def crear_apuesta(self, apostador, id_carrera, valor, competidor):
        datos_apostador = session.query(Apostador).filter(Apostador.nombre == apostador).first()
        datos_competidor = session.query(Competidor).filter(Competidor.nombre == competidor).first()
        apuesta = Apuesta(id_apostador=datos_apostador.id, valor=valor, id_carrera=id_carrera, id_competidor=datos_competidor.id)
        session.add(apuesta)
        session.commit()
        return True
        
    def editar_apuesta(self,apostador_actual,competidor_actual,valor_nuevo,apostador_nuevo,competidor_nuevo,id_carrera):

        
        ''' Busqueda de ID para valores actuales'''
        #reg_carrera = session.query(Carrera).filter(Carrera.nombre == nombre_carrera).first()
        reg_apostador = session.query(Apostador).filter(Apostador.nombre == apostador_actual).first()
        reg_competidor = session.query(Competidor).filter(Competidor.nombre == competidor_actual).first()

        ''' Busqueda de ID para valores nuevos'''
        reg_apostador_nuevo = session.query(Apostador).filter(Apostador.nombre == apostador_nuevo).first()
        reg_competidor_nuevo = session.query(Competidor).filter(Competidor.nombre == competidor_nuevo).first()
        
        id_apuesta_ = session.query(Apuesta).filter(Apuesta.id_carrera == id_carrera,Apuesta.id_apostador==reg_apostador.id,Apuesta.id_competidor==reg_competidor.id).first()
        
        #Paso2: Busco la apuesta por I para cambiar el estado de la carrera
        busqueda_apuesta = session.query(Apuesta).filter(Apuesta.id == id_apuesta_.id).first()
        #print("La apuesta es: "+ str(busqueda_apuesta))
        apuesta = session.query(Apuesta).get(busqueda_apuesta.id)
        apuesta.id_apostador=reg_apostador_nuevo.id
        apuesta.id_competidor=reg_competidor_nuevo.id
        apuesta.valor=valor_nuevo
        # # carrera.abierta = False
        session.add(apuesta)
        session.commit()   




    def eliminar_apuesta(self, id_carrera, id_apuesta):
        nombre_carrera =self.carreras[id_carrera]['Nombre']
        i = 0
        id = 0
        while i < len(self.apuestas):
            if self.apuestas[i]['Carrera'] == nombre_carrera:
                if id == id_apuesta:
                    self.apuestas.pop(i)
                    return True
                else:
                    id+=1
            i+=1
        
        return False
                

        del self.apuesta[id_apuesta]

    def dar_reporte_ganancias(self, id_carrera, id_competidor):

        self.terminar_carrera(id_carrera)


        nombre_competidor = session.query(Competidor).filter(Competidor.nombre == id_competidor).first()
        competidor = session.query(Competidor).get(nombre_competidor.id)
        competidor.ganador = True
        session.add(competidor)
        session.commit()    
        
     
        resultado_apuestas = self.dar_apuestas_carrera(id_carrera)

  
        list_ganancias=[]
        total_ganacia = 0
        total_apuesta = 0
        for i in range(len(resultado_apuestas)):
            ganancia = 0
            total_apuesta+=resultado_apuestas[i]['Valor']
            if resultado_apuestas[i]['Competidor']==nombre_competidor.nombre:
                ganancia = resultado_apuestas[i]['Valor']+(resultado_apuestas[i]['Valor']/competidor.cuota)
                total_ganacia+=ganancia
                
                
            list_ganancias.append((resultado_apuestas[i]['Apostador'],ganancia))


        ganancia_casa = total_apuesta - total_ganacia
      
        return list_ganancias, ganancia_casa
    