from http.server import HTTPServer, BaseHTTPRequestHandler
import json


guests_file = "guests.json"


class Server(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/guests":

            with open(guests_file, "r") as file:
                guests = json.load(file)


            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps(guests).encode()
            )


    def do_POST(self):

        if self.path == "/invite":


            length = int(self.headers["Content-Length"])


            data = self.rfile.read(length)


            guest = json.loads(data)


            with open(guests_file,"r") as file:
                guests = json.load(file)



            guests.append(guest)



            with open(guests_file,"w") as file:
                json.dump(guests,file,indent=4)



            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()


            self.wfile.write(
                b'{"message":"Invite ajoute"}'
            )



server = HTTPServer(
    ("localhost",3000),
    Server
)


print("Serveur lance sur http://localhost:3000")


server.serve_forever()