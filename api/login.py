from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            username = data.get('username', '')
            password = data.get('password', '')
            
            # Validasi hardcoded
            if username == 'amettha' and password == 'mart123':
                response = {'message': 'Login berhasil!'}
                self.send_response(200)
            else:
                response = {'error': 'Username atau password salah'}
                self.send_response(401)
                
        except json.JSONDecodeError:
            response = {'error': 'Format data tidak valid'}
            self.send_response(400)
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
