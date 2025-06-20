import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size

    binary_message = ""
    message = ""
    delimiter = '11111111'  # Delimiter để đánh dấu kết thúc tin nhắn

    # Đọc từng pixel cho đến khi tìm thấy delimiter
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]
                
                # Kiểm tra mỗi 8 bit xem có phải delimiter không
                if len(binary_message) >= 8:
                    byte = binary_message[-8:]
                    if byte == delimiter:
                        # Xử lý phần tin nhắn trước delimiter
                        for i in range(0, len(binary_message)-8, 8):
                            message += chr(int(binary_message[i:i+8], 2))
                        return message

    # Nếu không tìm thấy delimiter, xử lý toàn bộ tin nhắn
    for i in range(0, len(binary_message), 8):
        if i + 8 <= len(binary_message):
            message += chr(int(binary_message[i:i+8], 2))

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    try:
        encoded_image_path = sys.argv[1]
        decoded_message = decode_image(encoded_image_path)
        print("Decoded message:", decoded_message)
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()