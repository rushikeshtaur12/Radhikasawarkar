from POM.ajio import Ajio1,Ajio2,Ajio3,Ajio4
from Data import reading_object
import pytest
data_obj =reading_object.read_data()

@pytest.mark.parametrize("value1",data_obj)
class Testajio:
    def test_ajio1(self,_driver,value1):
        name = Ajio1(_driver)
        name.test_signin(value1)

    def test_ajio2(self,_driver,value1):
        name = Ajio2(_driver)
        name.test_email(value1)

    def test_ajio3(self, _driver,value1):
        name = Ajio3(_driver)
        name.test_facebook(value1)

    def test_ajio4(self, _driver,value1):
        name = Ajio4(_driver)
        name.test_google(value1)


