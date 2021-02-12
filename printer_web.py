from flask import Flask, request
from flask_cors import CORS
from ticket import Ticket
from flask_restful import Resource, Api
from escpos.printer import Usb

app = Flask(__name__)
CORS(app)
api = Api(app)
printer = None

class PrintConfigure(Resource):
   def get(self,proveedor,modelo):
     self.proveedor = proveedor
     self.modelo = modelo
     global printer
     printer = Usb(0x04b8, 0x0e15)
     return {'result':'success'}

     
class PrintTicket(Resource):

   def post(self):
     print ("LLegando peticion")
     ticket_data = request.get_json()
     print ("1..")
     print (ticket_data)
     def_page = {
      "ancho_ticket": 46,
      "ancho_precio":5,
      "ancho_total":6,
      "ancho_cantidad": 4,
      "lineas_x_descripcion": 3,
      "decimales":1
     }
     global printer
     if printer == None:
       printer = Usb(0x04b8, 0x0e15)
     ticket = Ticket(printer, def_page)
     ticket.print_ticket(ticket_data)

     return {"saludo":"Hello, World!"}

api.add_resource(PrintConfigure,'/configure/<string:proveedor>/<string:modelo>')
api.add_resource(PrintTicket,'/print_ticket/')


if __name__ == '__main__':
    app.run()
