from model.model import Model

model = Model()

model.read_year()
model.read_shape(1999)

model.crea_grafo(1999,'triangle')
model.vicini()

model.ricerca()