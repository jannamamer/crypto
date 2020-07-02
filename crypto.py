import sys

from caesar_cipher import CaesarCipher


class Crypto:
    """A class to manage all cryptography"""

    def __init__(self, args):
        self.args = args

    def start(self):
        if len(self.args) <= 1:
            self._exit()

        try:
            text = self.args[2]
        except IndexError:
            self._exit()

        for shift in range(1, 27):
            cc = CaesarCipher(shift, text)

            if '-d' in self.args:
                text_result = cc.decrypt()
            elif '-e' in self.args:
                text_result = cc.encrypt()

            if '-f' in self.args:
                text_file = self.args[4]
                self._find_text(text_file, text_result)
            else:
                print(text_result)

    def _exit(self):
        sys.exit(f"Usage: {self.args[0]} [options]\n"
                 "Example: {self.args[0]} -d 'Drkxu iye!'")

    def _find_text(self, text_file, text_result):
        with open(text_file) as file_object:
            for line in file_object:
                if line.strip() in text_result:
                    print(text_result)


if __name__ == '__main__':
    crypto = Crypto(sys.argv)
    crypto.start()
