import unittest
from unittest.mock import patch
import questionnaire


def conversion_nombre():
    num_str=input("Rentrez un nombre")
    return int(num_str)
class Testunitaire(unittest.TestCase):


    def test_conversion_nombre_validée(self):
        with patch("builtins.input",return_value="10"):
            self.assertEqual(conversion_nombre(),10)
        with patch("builtins.input",return_value="100"):
            self.assertEqual(conversion_nombre(),100)


    def test_conversion_nombre_invalidée(self):
        with patch("builtins.input",return_value="abcd"):
            self.assertRaises(ValueError,conversion_nombre)

class TestsQuestion(unittest.TestCase):
    def test_question_bonne_mauvaise_reponse(self):
        choix=("choix1","choix2","choix3")
       
        q = questionnaire.Question("titre_question", choix, "choix2")
        with patch("builtins.input", return_value="1"):
            self.assertFalse(q.poser(1, 1))
        with patch("builtins.input", return_value="2"):
            self.assertTrue(q.poser(1, 1))
        with patch("builtins.input", return_value="3"):
            self.assertFalse(q.poser(1, 1))
        
unittest.main()