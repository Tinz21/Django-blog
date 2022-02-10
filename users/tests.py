from django.test import TestCase

from .api.serializers import UserRegisterSerializer
from .api.serializers import UserSerializer

# Create your tests here.
class TestModelRegisterUser(TestCase):
    def test_validate_a_new_user_data_register_succesfully(self):
        user = UserRegisterSerializer(
            data={'username':'pepe','password':'pass','email':'pepe@mail.com'}
        )
        self.assert_(user.is_valid(), "Bad request, some field is not valid")
        user.save()
        self.assertNotEqual(user.data['password'],'pass', 'Error, password not encrypted')    


class TestUserView(TestCase):
    def test_validate_a_new_user_data_register_succesfully(self):
        user1={'pk':None,'username':'pepe','password':'pass','email':'pepe@mail.com'}
        user2={'username':'sara','password':'pass','email':'sara@mail.com'}
        userupdated = UserSerializer(user1['pk'],user2)
        userupdated.is_valid()
        self.assertNotEqual(user1['username'],userupdated.data['username'],"User not updated")
