from PIL import Image
import requests
from io import BytesIO

def display_image(file_path_or_url):
    try:
        # Kiểm tra nếu là URL
        if file_path_or_url.startswith('http'):
            response = requests.get(file_path_or_url)
            img = Image.open(BytesIO(response.content))
        else:
            # Mở ảnh từ đường dẫn file
            img = Image.open(file_path_or_url)

        # Hiển thị ảnh
        img.show()
    except Exception as e:
        print(f"Không thể hiển thị ảnh. Lỗi: {e}")

if __name__ == "__main__":
    # Đường dẫn của file ảnh hoặc URL
    file_path_or_url = "Otto.png"  # hoặc "https://example.com/image.jpg"
    # Hiển thị ảnh từ file hoặc URL
    display_image(file_path_or_url)

