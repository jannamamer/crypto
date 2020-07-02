import unittest
import os
import sys
import inspect

current_dir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from caesar_cipher import CaesarCipher


class EncryptTestCase(unittest.TestCase):
    """Test encrypt for caesar_cipher.py"""

    def setUp(self):
        """Setup input text"""
        self.text = "Happy Pride"

    def test_encrypt_shift_1(self):
        """Test encrypt shift 1"""
        cc = CaesarCipher(1, self.text)
        self.assertEqual(cc.encrypt(), 'Ibqqz Qsjef')

    def test_encrypt_shift_2(self):
        """Test encrypt shift 2"""
        cc = CaesarCipher(2, self.text)
        self.assertEqual(cc.encrypt(), 'Jcrra Rtkfg')

    def test_encrypt_shift_15(self):
        """Test encrypt shift 15"""
        cc = CaesarCipher(15, self.text)
        self.assertEqual(cc.encrypt(), 'Wpeen Egxst')

    def test_encrypt_shift_37(self):
        """Test encrypt shift 37"""
        cc = CaesarCipher(37, self.text)
        self.assertEqual(cc.encrypt(), 'Slaaj Actop')

    def test_encrypt_shift_100(self):
        """Test encrypt shift 100"""
        cc = CaesarCipher(100, self.text)
        self.assertEqual(cc.encrypt(), 'Dwllu Lneza')

    def test_decrypt_shift_1(self):
        """Test decrypt shift 1"""
        cc = CaesarCipher(1, 'Ibqqz Qsjef')
        self.assertEqual(cc.decrypt(), self.text)

    def test_decrypt_shift_2(self):
        """Test decrypt shift 2"""
        cc = CaesarCipher(2, 'Jcrra Rtkfg')
        self.assertEqual(cc.decrypt(), self.text)

    def test_decrypt_shift_15(self):
        """Test decrypt shift 15"""
        cc = CaesarCipher(15, 'Wpeen Egxst')
        self.assertEqual(cc.decrypt(), self.text)

    def test_edecrypt_shift_37(self):
        """Test decrypt shift 37"""
        cc = CaesarCipher(37, 'Slaaj Actop')
        self.assertEqual(cc.decrypt(), self.text)

    def test_decrypt_shift_100(self):
        """Test decrypt shift 100"""
        cc = CaesarCipher(100, 'Dwllu Lneza')
        self.assertEqual(cc.decrypt(), self.text)


if __name__ == '__main__':
    unittest.main()
