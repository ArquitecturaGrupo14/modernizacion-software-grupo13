import unittest
from src.modelo.Apostador import Apostador

from src.modelo.Apuesta import Apuesta
from src.modelo.Carrera import Carrera
from src.modelo.Competidor import Competidor
from src.logica.Logica_mock import Logica_mock
from src.modelo.declarative_base import Session

from faker import Faker
import random

class ApuestaTestCase(unittest.TestCase):

        def setUp(self):
                self.logica = Logica_mock()
                self.session = Session()
		

                '''Crea una instancia de Faker'''
                self.data_factory = Faker()

                '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
                Faker.seed(1000)

                '''Genera 10 datos en data y creamos las  apuestas'''
                self.dataApuesta = []
                self.dataCarrera = []
                self.dataApostador = []
                self.dataCompetidor = []


                self.apuestas = [] 
                self.carreras = []  
                self.apostador = [] 
                self.competidor = []      

                for _ in range(0,10):
                                              
                        # Aleatorios para Carrera
                        self.dataCarrera.append((self.data_factory.unique.job(),1))
                        self.carreras.append(Carrera(nombre = self.dataCarrera[-1][0],abierta = self.dataCarrera[-1][1]))
                        self.session.add(self.carreras[-1])

                        # Aleatorio para Apostador
                        self.nom_apostador=self.data_factory.unique.name()
                        self.dataApostador.append(self.nom_apostador)
                        self.apostador.append(Apostador(nombre = self.dataApostador[-1]))
                        self.session.add(self.apostador[-1])

                        # Aleatorio para competidor
                        self.nom_competidor=self.data_factory.unique.last_name()
                        self.dataCompetidor.append((self.nom_competidor,self.data_factory.random_int(0,1),float(self.data_factory.random_int(1,10)),0,self.data_factory.random_int(1,10)))
                        self.competidor.append(Competidor(nombre = self.dataCompetidor[-1][0],probabilidad=self.dataCompetidor[-1][1],cuota=self.dataCompetidor[-1][2],ganador=self.dataCompetidor[-1][3],id_carrera=self.dataCompetidor[-1][4]))
                        self.session.add(self.competidor[-1])

                        # Aleatorio para Apuesta
                        self.dataApuesta.append((float(self.data_factory.random_int(100,999)),self.data_factory.random_int(1,10),self.data_factory.random_int(1,10),self.data_factory.random_int(1,10)))
                        self.apuestas.append(Apuesta(valor = self.dataApuesta[-1][0],id_carrera = self.dataApuesta[-1][1],id_competidor = self.dataApuesta[-1][2],id_apostador = self.dataApuesta[-1][3]))
                        self.session.add(self.apuestas[-1])


                '''Persiste los objetos
                En este setUp no se cierra la sesión para usar las apuestas en las pruebas'''
                self.session.commit()


        def tearDown(self):

                self.session = Session()

                # Eliminar Datos
                busqueda = self.session.query(Apuesta).all()
                for apuesta in busqueda:
                        self.session.delete(apuesta)
                
                busqueda = self.session.query(Carrera).all()
                for carrera in busqueda:
                        self.session.delete(carrera)

                busqueda = self.session.query(Apostador).all()
                for apostador in busqueda:
                        self.session.delete(apostador)

                busqueda = self.session.query(Competidor).all()
                for competidor in busqueda:
                        self.session.delete(competidor)
                
                self.session.commit()
                self.session.close()


        
        def test_crear_apuesta(self):
                self.dataApuesta.append((float(self.data_factory.random_int(100,999)),self.data_factory.random_int(1,10),self.data_factory.random_int(1,10),self.data_factory.random_int(1,10)))
                competidor = self.session.query(Competidor).filter(Competidor.id_carrera == self.dataApuesta[-1][1]).first()
                apostador= self.session.query(Apostador).filter(Apostador.id == self.dataApuesta[-1][3]).first()
                self.assertEqual(self.logica.crear_apuesta(apostador.nombre,self.dataApuesta[-1][1],self.dataApuesta[-1][0],competidor.nombre),True)
                
                        
        def test_verificar_almacenamiento_crear_apuesta(self):
                self.dataApuesta.append((float(self.data_factory.random_int(100,999)),self.data_factory.random_int(1,10),self.data_factory.random_int(1,10),self.data_factory.random_int(1,10)))
                competidor = self.session.query(Competidor).filter(Competidor.id_carrera == self.dataApuesta[-1][1]).first()
                resul_apostador= self.session.query(Apostador).filter(Apostador.id == self.dataApuesta[-1][3]).first()
                self.assertEqual(self.logica.crear_apuesta(resul_apostador.nombre,self.dataApuesta[-1][1],self.dataApuesta[-1][0],competidor.nombre),True)
                self.session = Session()
                resul_apuesta= self.session.query(Apuesta).filter(Apuesta.id_apostador == self.dataApuesta[-1][3] and Apuesta.id_competidor==self.dataApuesta[-1][1] and Apuesta.valor==self.dataApuesta[-1][0]).first()
                self.assertEqual(resul_apuesta.id_apostador,self.dataApuesta[-1][3])
                



        def test_editar_apuesta(self):
                '''Test editar Apuestas'''
                apuesta=self.session.query(Apuesta,Carrera, Competidor, Apostador).join(Apuesta.carrera,Apuesta.competidor,Apuesta.apostador).filter(Apuesta.id == 1).all()
                dic_aptas =apuesta[0]
                test = self.logica.editar_apuesta(dic_aptas.Apostador.nombre,dic_aptas.Competidor.nombre,float(self.data_factory.random_int(100,999)),self.nom_apostador,self.nom_competidor,dic_aptas.Apuesta.id)
                self.assertEqual(test,None)



# Con Datos Aleatorios

        def test_dar_apuestas_carrera(self):

                '''Test dar Apuestas'''

                consulta1 = self.logica.dar_apuestas_carrera(self.dataApuesta[-1][1])
                self.dataApuesta.append((
                        #self.data_factory.first_name(),
                        "Apostador1",
                        self.data_factory.random_int(1,2),
                        self.data_factory.random_int(10000,99999),
                        #self.data_factory.last_name()))
                        "Competidor1"))
                # self.logica.crear_apuesta(
                #         #id_apostador = self.data[-1][0],
                #         apostador = self.dataApuesta[-1][0],
                #         id_carrera = self.dataApuesta[-1][1],
                #         valor = self.dataApuesta[-1][2],
                #         competidor = self.dataApuesta[-1][3])
              
                # consulta2 = self.logica.dar_apuestas_carrera(self.dataApuesta[-1][1])
                #self.assertGreater(len(consulta2), len(consulta1))
                self.assertGreater(len(consulta1), 0)
