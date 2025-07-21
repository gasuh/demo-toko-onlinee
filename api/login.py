from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()
            
            # Strict validation (case-sensitive, no whitespace)
            if username == 'amettha' and password == 'mart123':
                response = {
                    "success": True,
                    "message": "Login berhasil! Mengarahkan ke dashboard..."
                }
                self.send_response(200)
            else:
                response = {
                    "success": False,
                    "error": "Username atau password salah!"
                }
                self.send_response(401)
                
        except json.JSONDecodeError:
            response = {
                "success": False,
                "error": "Format data tidak valid!"
            }
            self.send_response(400)
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
