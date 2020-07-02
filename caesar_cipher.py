import string


class CaesarCipher:
    """A class to decrypt / encrypt a string using caesar cipher."""

    def __init__(self, shift, text):
        """Initialize class"""
        self.shift = shift % 26
        self.text = text
        self.alpha_lower = string.ascii_lowercase
        self.alpha_upper = string.ascii_uppercase

    def _check_letter_case(self, letter):
        if letter in self.alpha_lower:
            self.alpha = self.alpha_lower
        elif letter in self.alpha_upper:
            self.alpha = self.alpha_upper
        else:
            self.alpha = ""

    def _update_position(self, current_position, action):
        if action == 'd':
            self.new_position = current_position - self.shift
        elif action == 'e':
            self.new_position = current_position + self.shift

        if self.new_position >= 26:
            self.new_position = self.new_position - 26

    def decrypt(self):
        decrypted_text = []
        for letter in self.text:
            self._check_letter_case(letter)

            if self.alpha:
                current_position = self.alpha.index(letter)
                self._update_position(current_position, 'd')
                decrypted_text.append(self.alpha[self.new_position])
            else:
                decrypted_text.append(letter)

        return ''.join(decrypted_text)

    def encrypt(self):
        encrypted_text = []

        for letter in self.text:
            self._check_letter_case(letter)

            if self.alpha:
                current_position = self.alpha.index(letter)
                self._update_position(current_position, 'e')
                encrypted_text.append(self.alpha[self.new_position])
            else:
                encrypted_text.append(letter)

        return ''.join(encrypted_text)
