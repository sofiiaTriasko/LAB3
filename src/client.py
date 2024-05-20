import socket
import json

def send_request(request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.send(json.dumps(request).encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

if __name__ == "__main__":
    # Приклад запитів до сервера
    response = send_request({'action': 'add_category', 'name': 'Beverages'})
    print('Response:', response)

    response = send_request({'action': 'add_product', 'name': 'Coke', 'category_id': 1, 'price': 1.5, 'quantity': 50})
    print('Response:', response)

    response = send_request({'action': 'find_products', 'name': 'Coke'})
    print('Response:', response)

    response = send_request({'action': 'update_product', 'product_id': 1, 'price': 1.75})
    print('Response:', response)

    response = send_request({'action': 'delete_product', 'product_id': 1})
    print('Response:', response)

    response = send_request({'action': 'delete_category', 'category_id': 1})
    print('Response:', response)
