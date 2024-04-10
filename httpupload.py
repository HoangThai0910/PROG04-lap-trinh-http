import socket

def create_multipart_form_data(file_path, boundary):
    with open(file_path, 'rb') as file:
        form_data = f'--{boundary}\r\n'
        form_data += 'Content-Disposition: form-data; name="image"; filename="' + file_path.split('/')[-1] + '"\r\n'
        form_data += 'Content-Type: image/jpeg\r\n\r\n'
        form_data += file.read().decode('latin1') + '\r\n'
        form_data += f'--{boundary}--\r\n'
    return form_data

def send_post_request(host, port, request_data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(request_data)
    response = b''
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
    s.close()
    return response

def main():
    host = 'thaihv15.000webhostapp.com'
    port = 443  # assuming HTTPS
    boundary = '----WebKitFormBoundary3AzhCaYCFjGxp6xp'
    file_path = '../nerd.jpeg'
    content_length = len(create_multipart_form_data(file_path, boundary))

    request_data = (
        f"POST /student/changeimage.php?id=1 HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "Cookie: PHPSESSID=gsqrbec36qrgnm8jisp4a5dbr7\r\n"
        f"Content-Length: {content_length}\r\n"
        "Cache-Control: max-age=0\r\n"
        'Sec-Ch-Ua: "Chromium";v="119", "Not?A_Brand";v="24"\r\n'
        "Sec-Ch-Ua-Mobile: ?0\r\n"
        'Sec-Ch-Ua-Platform: "Linux"\r\n'
        "Upgrade-Insecure-Requests: 1\r\n"
        "Origin: https://thaihv15.000webhostapp.com\r\n"
        "Content-Type: multipart/form-data; boundary=" + boundary + "\r\n"
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36\r\n"
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n"
        "Sec-Fetch-Site: same-origin\r\n"
        "Sec-Fetch-Mode: navigate\r\n"
        "Sec-Fetch-User: ?1\r\n"
        "Sec-Fetch-Dest: document\r\n"
        "Referer: https://thaihv15.000webhostapp.com/student/changeimage.php?id=1\r\n"
        "Accept-Encoding: gzip, deflate, br\r\n"
        "Accept-Language: en-US,en;q=0.9\r\n"
        "Priority: u=0, i\r\n"
        "\r\n"
        + create_multipart_form_data(file_path, boundary)
    )

    response = send_post_request(host, port, request_data.encode())
    print(response.decode())

if __name__ == "__main__":
    main()
