from tarea12 import app
from tarea12.controladores import controlador

app.secret_key = 'mantener en secreto'

if __name__=="__main__":
    app.run(debug=True)  