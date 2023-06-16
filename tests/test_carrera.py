import unittest

from src.modelo.Carrera import Carrera
from src.modelo.Apuesta import Apuesta
from src.modelo.Apostador import Apostador
from src.modelo.Competidor import Competidor
from src.logica.Logica_mock import Logica_mock
from src.modelo.declarative_base import Session

from faker import Faker
import random


class CarreraTestCase(unittest.TestCase):

        def setUp(self):

                self.logica = Logica_mock()
                self.session = Session()
		

                '''Crea una instancia de Faker'''
                self.data_factory = Faker()

                '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
                Faker.seed(1000)

                '''Genera 10 datos en data y creamos las  Carreras'''
                self.data = []
                self.dataComp = []
                self.carreras = []  
                self.competidores = []       

                for _ in range(0,100):
                        self.data.append((self.data_factory.job(),True))
                        self.carreras.append(Carrera(nombre = self.data[-1][0],abierta = self.data[-1][1]))
                        self.session.add(self.carreras[-1])
                        
                        self.dataComp.append((self.data_factory.unique.name(),self.data_factory.pyfloat(0,1,positive=True),self.data_factory.random_int(1,10)))
                        self.competidores.append(Competidor(nombre = self.dataComp[-1][0],probabilidad=self.dataComp[-1][1],cuota=self.dataComp[-1][1]/(1-self.dataComp[-1][1]),ganador=False,id_carrera=self.dataComp[-1][2]))
                        self.session.add(self.competidores[-1])

                '''Persiste los objetos
                En este setUp no se cierra la sesión para usar las carreras en las pruebas'''
                self.session.commit()

                '''Crea una logica para hacer las pruebas'''
                self.logica2 = Logica_mock()

                '''Abre la sesión'''
                self.session = Session()

                '''Crea los objetos'''
                self.carrera1 = Carrera(nombre = 'Sapo League', abierta = True)
                self.carrera2 = Carrera(nombre = 'Rayuela League', abierta = True)
                self.carrera3 = Carrera(nombre = 'Escondite Teams', abierta = True)
                self.carrera4 = Carrera(nombre = 'Lleva Teams', abierta = True)

                '''Adiciona los objetos a la sesión'''
                self.session.add(self.carrera1)
                self.session.add(self.carrera2)
                self.session.add(self.carrera3)
                self.session.add(self.carrera4)

                '''Persiste los objetos y cierra la sesión'''
                self.session.commit()
                self.session.close()
                

        # def test_constructor(self):
        #         for carrera, dato in zip(self.carreras, self.data):
        #                 self.assertEqual(carrera.nombre, dato[0])
        
        def tearDown(self):
                self.session = Session()
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
                self.session.close()

       
        def test_crear_carrera(self):
                
                '''Test crear Carrera'''
                self.data.append((self.data_factory.job(), True))
                #self.assertEqual(self.logica.crear_carrera("Natacion"),True)

                resultado = self.logica.crear_carrera(nombre = self.data[-1][0])
                self.assertEqual(resultado, True)

        def test_eliminar_carrera(self):
                
                '''Test eliminar Carrera'''
                reg_carrera = self.data_factory.random_int(1,10)
                consulta_carrera = self.logica.dar_carrera(reg_carrera)
                self.logica.eliminar_carrera(consulta_carrera)
                consulta_carrera2 = self.logica.dar_carrera(reg_carrera)
                self.assertEqual(len(consulta_carrera2), 0)



        def test_crear_carrera_repetida(self):
                '''Test crear carrera repetida'''
                resultado = self.logica.crear_carrera(nombre = self.data[-1][0])
                self.assertEqual(resultado, True)

               
        def test_verificar_almacenamiento_crear_carrera(self):
                '''Test verificar almacenamiento Carrera'''
                self.data.append((self.data_factory.job(),True))
                self.logica.crear_carrera(nombre = self.data[-1][0])
                carrera = self.session.query(Carrera).filter(Carrera.nombre == self.data[-1][0]).first()
                self.assertEqual(carrera.nombre, self.data[-1][0])               


        def test_dar_carreras(self):
                consulta1 = self.logica.dar_carreras()
                self.data.append((self.data_factory.unique.name()))
                self.logica.crear_carrera(nombre = self.data[-1][0])
                consulta2 = self.logica.dar_carreras()
                self.assertGreater(len(consulta2), len(consulta1))
                
              
        def test_dar_reporte_ganancias(self):
                self.dataComp.append((self.data_factory.unique.name(),self.data_factory.pyfloat(0,1,positive=True),self.data_factory.random_int(1,10)))
                carrera = self.session.query(Carrera).filter(Carrera.id == self.dataComp[-1][2]).first()
                self.logica.aniadir_competidor(self.dataComp[-1][2],self.dataComp[-1][0],self.dataComp[-1][1],carrera.nombre)
                self.session = Session()
                self.logica.dar_reporte_ganancias(self.dataComp[-1][2], self.dataComp[-1][0])
                competidor1 = self.session.query(Competidor).filter(Competidor.nombre == self.dataComp[-1][0]).first()
                self.assertEqual(competidor1.ganador,True)
                
        # def test_dar_reporte_ganadores(self):
        #         self.dataComp.append((self.data_factory.unique.name(),self.data_factory.pyfloat(0,1,positive=True),self.data_factory.random_int(1,10)))
        #         competidor = self.session.query(Competidor).filter(Competidor.id == self.dataComp[-1][2]).first()
        #         ganadores=self.logica.dar_reporte_ganancias(competidor.id_carrera, competidor.nombre)
        #         self.assertIsNotNone(ganadores)  

        def test_terminar_carrera(self):
                id_aleatorio=self.data_factory.random_int(1,10)
                self.logica.terminar_carrera(id_aleatorio)
                carrera1 = self.session.query(Carrera).filter(Carrera.id == id_aleatorio).first()
                self.assertEqual(carrera1.abierta,False)                     
