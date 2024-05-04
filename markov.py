# Creacción de una cadena de Markov

def matriz_transicion(series):
  mt =  defaultdict(lambda: defaultdict(int))
  # SACAMOS LOS CONTEOS
  for serie in series:
    for e in range(1,len(serie)):
      estado_actual = asignar_estados(serie[e-1])
      estado_siguiente = asignar_estados(serie[e])
      mt[estado_actual][estado_siguiente] += 1
  # SACAMOS LAS PROBABILIDADES
  for e ,t in mt.items():
    tot_trans = sum(t.values())
    for ne in t:
      mt[e][ne] /= tot_trans
  return mt

# Predicción de cadenas de markov

def prediccion_estado(serie,matriz_transicion):
  predicciones = []
  ult_estado = asignar_estados(serie[-1])
  valor_max = max(matriz_transicion[ult_estado].values())

  prediccion_esperada = 0
  for i in matriz_transicion[ult_estado]:
    prediccion_esperada += (matriz_transicion[ult_estado][i] * serie[-1])

  predicciones.append(prediccion_esperada)
  return predicciones
