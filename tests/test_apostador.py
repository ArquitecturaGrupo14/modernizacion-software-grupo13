import unittest
import random

from src.modelo.Apostador import Apostador
from src.logica.Logica_mock import Logica_mock
from src.modelo.declarative_base import Session
from faker import Faker

class ApostadorTestCase(unittest.TestCase):
    
        
        def setUp(self):

                self.logica = Logica_mock()
                self.session = Session()
                self.data_factory = Faker()
                Faker.seed(1000)
                
                self.data = []
                self.apostadores = []   
                
                for i in range(0,10):
                        self.data.append((self.data_factory.unique.name()))
                        self.apostadores.append(Apostador(nombre = self.data[-1]))
                        self.session.add(self.apostadores[-1])
                                       
                self.session.commit()
		
        def test_constructor(self):
                for apostadores, dato in zip(self.apostadores, self.data):
                        self.assertEqual(apostadores.nombre, dato)
        
        def tearDown(self):
                self.session = Session()
                busqueda = self.session.query(Apostador).all()
                for apostador in busqueda:
                        self.session.delete(apostador)
                self.session.commit()
                self.session.close()
                
        def test_aniadir_apostador(self):
                self.data.append((self.data_factory.unique.name()))
                self.assertEqual(self.logica.aniadir_apostador(self.data[-1]),True)
                
        def test_aniadir_apostador_repetida(self):
                self.data.append((self.data_factory.unique.name()))
                self.logica.aniadir_apostador(self.data[-1])
                resultado=self.logica.aniadir_apostador(self.data[-1])
                self.assertNotEqual(resultado, True)
                
        def test_verificar_almacenamiento_aniadir_apostador(self):
                self.data.append((self.data_factory.unique.name()))
                self.logica.aniadir_apostador(self.data[-1][0])
                self.session = Session()
                apostador = self.session.query(Apostador).filter(Apostador.nombre == self.data[-1][0]).first()
                self.assertEqual(apostador.nombre, self.data[-1][0])
                
        def test_dar_apostadores(self):
                consulta1 = self.logica.dar_apostadores()
                self.data.append((self.data_factory.unique.name()))
                self.logica.aniadir_apostador(nombre = self.data[-1][0])
                consulta2 = self.logica.dar_apostadores()
                self.assertGreater(len(consulta2), len(consulta1))