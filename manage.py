"""Manger script."""
import os
from csv import reader
from lotoes import db, create_app
from initial_data import usuarios, provincias, sorteosLnac
from lotoes.secciones.usuarios.model_usuario import Usuario
from lotoes.secciones.clientes.model_cliente import Provincia, Cliente
from lotoes.secciones.sorteosLnac.model_sorteoLnac import SorteoLnac

env = os.getenv('FLASK_CONFIG')
#if env is None or env not in ["test", "prod"]:
env = "dev"

app = create_app(env)
app.app_context().push()

db.drop_all()

db.create_all()

obj_list = []
for usuario in usuarios:
    data_obj= Usuario(**usuario)
    obj_list.append(data_obj)

for provincia in provincias:
    data_obj= Provincia(**provincia)
    obj_list.append(data_obj)
    
for sorteos in sorteosLnac:
    data_obj= SorteoLnac(**sorteos)
    obj_list.append(data_obj)
    
with open('data/Clientes.csv', 'r') as read_obj:
        csv = reader(read_obj)
        for row in csv:
            if isinstance(row[20], int):
                print(cp)
                cp=int(row[20]) 
            cliente = Cliente(
                          nombre=row[1],
                          tipo_cliente=1,
                          clasificacion_interna=1,
                          persona_contacto=row[25],
                          tipo_documento=1,
                          documento=row[8],
                          telefono=row[14],
                          #movil=int(row[15])
                          email=row[16],
                          direccion=row[17],
                          municipio=row[18],
                          #provincia=row[14],
                          #cp=cp,
                          #notas=row[16] 
                        ) 
            obj_list.append(cliente)


db.session.add_all(obj_list)
db.session.commit()