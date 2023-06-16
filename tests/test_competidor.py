import unittest
import random

from src.modelo.Competidor import Competidor
from src.modelo.Carrera import Carrera
from src.logica.Logica_mock import Logica_mock
from src.modelo.declarative_base import Session
from faker import Faker


class CompetidorTestCase(unittest.TestCase):

        
        def setUp(self):

                self.logica = Logica_mock()
                self.session = Session()
                self.data_factory = Faker()
                Faker.seed(1000)
                
                self.data = []
                self.datacar = []
                self.competidores = []   
                self.carreras = []       

                for j in range(0,4):
                        self.datacar.append((self.data_factory.name(),True))
                        self.carreras.append(Carrera(nombre = self.datacar[-1][0],abierta =True))
                        self.session.add(self.carreras[-1])
                self.session.add(self.carreras[-1])
                
                for i in range(0,10):
                        self.data.append((self.data_factory.unique.name(),
                        self.data_factory.pyfloat(0,1,positive=True),
                        self.data_factory.random_int(1,3)))
                        self.competidores.append(
                                Competidor(
                                        nombre = self.data[-1][0],probabilidad=self.data[-1][1],cuota=self.data[-1][1]/(1-self.data[-1][1]),ganador=False,id_carrera=self.data[-1][2]))
                        self.session.add(self.competidores[-1])
                                       
                self.session.commit()
		
        def test_constructor(self):
                for competidores, dato in zip(self.competidores, self.data):
                        self.assertEqual(competidores.nombre, dato[0])
                        self.assertEqual(competidores.probabilidad, dato[1])
                        self.assertEqual(competidores.id_carrera, dato[2])
        
        def tearDown(self):
                self.session = Session()
                busqueda = self.session.query(Competidor).all()
                busquedaCar = self.session.query(Carrera).all()
                for competidor in busqueda:
                        self.session.delete(competidor)
                for carrera in busquedaCar:
                        self.session.delete(carrera)
                self.session.commit()
                self.session.close()
                
        def test_aniadir_competidor(self):
                self.data.append((self.data_factory.unique.name(), self.data_factory.pyfloat(0,1,positive=True), self.data_factory.random_int(1,3)))
                carrera = self.session.query(Carrera).filter(Carrera.id == self.data[-1][2]).first()
                self.assertEqual(self.logica.aniadir_competidor(self.data[-1][2],self.data[-1][0],self.data[-1][1],carrera.nombre),True)
                
        def test_aniadir_competidor_repetida(self):
                self.data.append((self.data_factory.unique.name(), self.data_factory.pyfloat(0,1,positive=True), self.data_factory.random_int(1,3)))
                carrera = self.session.query(Carrera).filter(Carrera.id == self.data[-1][2]).first()
                self.logica.aniadir_competidor(self.data[-1][2],self.data[-1][0],self.data[-1][1],carrera.nombre)
                resultado=self.logica.aniadir_competidor(self.data[-1][2],self.data[-1][0],self.data[-1][1],carrera.nombre)
                self.assertNotEqual(resultado, True)
                
        def test_verificar_almacenamiento_aniadir_competidor(self):
                self.data.append((self.data_factory.unique.name(), self.data_factory.pyfloat(0,1,positive=True), self.data_factory.random_int(1,3)))
                carrera = self.session.query(Carrera).filter(Carrera.id == self.data[-1][2]).first()
                self.logica.aniadir_competidor(self.data[-1][2],self.data[-1][0],self.data[-1][1],carrera.nombre)
                self.session = Session()
                competidor = self.session.query(Competidor).filter(Competidor.nombre == self.data[-1][0]).first()
                self.assertEqual(competidor.nombre, self.data[-1][0])
                self.assertEqual(competidor.probabilidad, self.data[-1][1])