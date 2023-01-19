from store import *
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/') # --> Este es un decorador que esa un metodo de app donde se espesifica la ruta como endpoint
def get_list():
    return [1, 2, 3]


@app.get('/contacto')
def get_contact():
    return {"name": 'Platzi', "numero": 123456}


@app.get('/contacto-html', response_class=HTMLResponse)
def get_contact_html():
    return """
        <html>
            <head>
                <title>html response</title>
            </head>
            <body>
                <h1>Soy un HTML !!!</h1>
                <p> Por lo tanto soy una pagina </p>
            </body>
        </html>
        """





def run():
    get_categories()



if __name__ == '__main__':
    run()