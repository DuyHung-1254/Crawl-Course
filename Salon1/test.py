from PIL import Image
import matplotlib.pyplot as plt

# Đường dẫn đến file ảnh của bạn
# image_path = './data/Introduction/data/Introduction/logo-OYJ34ERC.png'
image_path = './data/Introduction/logo-OYJ34ERC.png'

# Mở và đọc ảnh
img = Image.open(image_path)

# Hiển thị ảnh
plt.imshow(img)
plt.axis('off')  # Ẩn trục
plt.show()
