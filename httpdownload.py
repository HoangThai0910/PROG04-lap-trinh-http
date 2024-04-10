import socket
import ssl

# Tạo một socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến máy chủ trên cổng 443 (HTTPS)
ssl_context = ssl.create_default_context()
s = ssl_context.wrap_socket(s, server_hostname="thaihv15.000webhostapp.com")
s.connect(("thaihv15.000webhostapp.com", 443))

# Gửi yêu cầu GET để tải ảnh
request = """\
GET /images/f4a2802b076fc64464338f6bd4df48031712765235jpeg HTTP/2\r\n\
Host: thaihv15.000webhostapp.com\r\n\
Cookie: PHPSESSID=gsqrbec36qrgnm8jisp4a5dbr7\r\n\
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\r\n\
Sec-Fetch-Site: none\r\n\
Sec-Fetch-Mode: navigate\r\n\
Sec-Fetch-Dest: empty\r\n\
Referer: https://thaihv15.000webhostapp.com/student/profile.php\r\n\
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36\r\n\
Accept-Encoding: gzip, deflate, br\r\n\
Accept-Language: en-US,en;q=0.9\r\n\
Priority: u=4, i\r\n\r\n"""

s.sendall(request.encode())

# Nhận phản hồi từ máy chủ
response = b""
while True:
    data = s.recv(4096)
    if not data:
        break
    response += data
# Tách phần thân của phản hồi (nội dung của ảnh)
image_data = response.split(b"\r\n\r\n")[1]

# In ra kích thước của ảnh vừa tải
print("Kích thước của ảnh vừa tải là:", len(image_data), "bytes")

s.close()

