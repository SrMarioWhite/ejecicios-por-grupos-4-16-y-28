from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/dias")
async def dias(request: Request):
    lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return templates.TemplateResponse(request=request, name="dias.html", context={"dias_semana": lista_dias})

@app.get("/")
async def pais(request: Request):
    return templates.TemplateResponse(request=request, name="pais.html")

@app.get("/asignatura")
async def asignatura(request: Request):
    data = {
        "Matemáticas": ["Álgebra", "Geometría", "Cálculo"],
        "Ciencias": ["Física", "Química", "Biología"],
        "Historia": ["Historia Antigua", "Historia Media", "Historia Moderna"]
    }
    return templates.TemplateResponse(request=request, name="asignatura.html", context={"asignaturas": data})
