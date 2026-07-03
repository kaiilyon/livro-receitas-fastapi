from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload

import models
from database import Base, engine, get_session


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def listar(
    request: Request,
    session: Session = Depends(get_session),
):
    receitas = (
        session.query(models.Receita)
        .options(joinedload(models.Receita.categoria))
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="lista.html",
        context={
            "receitas": receitas,
        },
    )


@app.get("/nova")
def nova(
    request: Request,
    session: Session = Depends(get_session),
):
    categorias = session.query(models.Categoria).all()

    return templates.TemplateResponse(
        request=request,
        name="form.html",
        context={
            "categorias": categorias,
        },
    )


@app.post("/salvar")
def salvar(
    id: int = Form(None),
    nome: str = Form(...),
    ingredientes: str = Form(...),
    modo_preparo: str = Form(...),
    categoria_id: int = Form(...),
    session: Session = Depends(get_session),
):
    if id:
        receita = session.get(models.Receita, id)

        receita.nome = nome
        receita.ingredientes = ingredientes
        receita.modo_preparo = modo_preparo
        receita.categoria_id = categoria_id

    else:
        receita = models.Receita(
            nome=nome,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            categoria_id=categoria_id,
        )

        session.add(receita)

    session.commit()

    return RedirectResponse(url="/", status_code=303)


@app.get("/excluir/{receita_id}")
def excluir(
    receita_id: int,
    session: Session = Depends(get_session),
):
    receita = session.get(models.Receita, receita_id)

    if receita:
        session.delete(receita)
        session.commit()

    return RedirectResponse(url="/", status_code=303)


@app.get("/editar/{receita_id}")
def editar(
    receita_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    receita = session.get(models.Receita, receita_id)
    categorias = session.query(models.Categoria).all()

    return templates.TemplateResponse(
        request=request,
        name="form.html",
        context={
            "receita": receita,
            "categorias": categorias,
        },
    )

@app.get("/exibir/{receita_id}")
def exibir(
    receita_id: int,
    request: Request,
    session: Session = Depends(get_session),
):
    receita = (
        session.query(models.Receita)
        .options(joinedload(models.Receita.categoria))
        .filter(models.Receita.id == receita_id)
        .first()
    )

    return templates.TemplateResponse(
        request=request,
        name="exibir.html",
        context={
            "request": request,
            "receita": receita,
        },
    )