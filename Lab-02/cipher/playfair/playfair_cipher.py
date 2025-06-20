class PlayfairCipher:
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        
        # Loại bỏ ký tự trùng lặp trong key
        seen = set()
        key_unique = ""
        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                key_unique += char
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Không có J
        remaining_letters = [
            letter for letter in alphabet if letter not in seen
        ]
        
        # Tạo matrix 5x5
        matrix_string = key_unique + ''.join(remaining_letters)
        matrix = [list(matrix_string[i:i+5]) for i in range(0, 25, 5)]
        
        return matrix
    
    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None, None
    
    def prepare_text(self, text):
        # Chuyển "J" thành "I" và loại bỏ ký tự không phải chữ cái
        text = text.replace("J", "I").upper()
        text = ''.join([char for char in text if char.isalpha()])
        
        # Thêm X giữa các ký tự giống nhau và cuối text nếu cần
        prepared = ""
        i = 0
        while i < len(text):
            prepared += text[i]
            if i + 1 < len(text):
                if text[i] == text[i + 1]:
                    prepared += "X"
                else:
                    prepared += text[i + 1]
                    i += 1
            else:
                prepared += "X"  # Thêm X nếu độ dài lẻ
            i += 1
        
        return prepared
    
    def playfair_encrypt(self, plain_text, matrix):
        prepared_text = self.prepare_text(plain_text)
        encrypted_text = ""
        
        for i in range(0, len(prepared_text), 2):
            char1 = prepared_text[i]
            char2 = prepared_text[i + 1] if i + 1 < len(prepared_text) else 'X'
            
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)
            
            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:  # Hình chữ nhật
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            char1 = cipher_text[i]
            char2 = cipher_text[i + 1] if i + 1 < len(cipher_text) else 'X'
            
            row1, col1 = self.find_letter_coords(matrix, char1)
            row2, col2 = self.find_letter_coords(matrix, char2)
            
            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:  # Hình chữ nhật
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]
        
        # Loại bỏ X thừa ở cuối
        if decrypted_text.endswith('X'):
            decrypted_text = decrypted_text[:-1]
        
        return decrypted_text 