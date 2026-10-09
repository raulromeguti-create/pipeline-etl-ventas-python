# En este script debemos limpiar los datos sucios, calcular totales
# y agrupar por categoria

import csv
import json
from datetime import datetime
from collections import defaultdict

# 1. comenzaremos leyendos los datos del CSV
def extraer_ventas(datos):
    with open("data/ventas_dia.csv", "r", encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


# 3. Voy a crear una función para comprobar si todos los campos son validos
def campos_validos(col):
    campos_requeridos = ["fecha", "producto", "categoria", "cliente"]

    res = True

    for campo in campos_requeridos:
        if campo not in col or not str(col[campo]).strip():
            res = False

    return res
                


# 2. Comenzaremos limpiando los datos sucios
def transformar_ventas(datos):
    nueva_lista=[]
    lista_errores = []

    for fila,reg in enumerate(datos):

        try:
            valor_cantidad = 0
            dinero_total = 0

            if not campos_validos(reg):
                print (f"      Ha habido un erro en la fila {fila}")
                lista_errores.append({
                    "fila" : fila,
                    "columna" : reg
                })
                continue
                
            

            if not reg["cantidad"].strip():
                valor_cantidad = 1
            else:
                valor_cantidad = float(reg["cantidad"])

            valor = float(reg["precio_unitario"])

            dinero_total += valor_cantidad * valor

            nueva_lista.append({
                "fecha" : reg["fecha"],
                "producto" : reg["producto"],
                "categoria" : reg["categoria"],
                "cantidad" : valor_cantidad,
                "precio_unitario" : reg["precio_unitario"],
                "total" : round(dinero_total,2),
                "cliente" : reg["cliente"]
            })

        except ValueError:
            print("      Error en el campo del dinero_unitario")
            lista_errores.append({
                                "fila" : fila,
                                "columna" : reg
                            })


    return nueva_lista, lista_errores

# 4. Ahora vamos a generar unas muestras
def generar_resumen(ventas_limpias):

    if not ventas_limpias:
        return {"error:": "No hay datos validos"}

    total_facturado = sum(v["total"] for v in ventas_limpias)
    num_transacciones = len(ventas_limpias)
    ticket_medio = total_facturado / num_transacciones

    por_categoria = defaultdict(lambda: {"total": 0, "transacciones": 0})
    for v in ventas_limpias:
        cat = v["categoria"]
        por_categoria[cat]["total"] += v["total"]
        por_categoria[cat]["transacciones"] += 1

    productos_total = defaultdict(float)
    for v in ventas_limpias:
        productos_total[v["producto"]] += v["total"]

    top_productos = sorted(productos_total.items(), key = lambda x : x[1], reverse=True)[:3]

    # Clientes únicos
    clientes = set(v["cliente"] for v in ventas_limpias)
    
    return {
        "fecha_reporte": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total_facturado": round(total_facturado, 2),
        "num_transacciones": num_transacciones,
        "ticket_medio": round(ticket_medio, 2),
        "clientes_unicos": len(clientes),
        "por_categoria": dict(por_categoria),
        "top_3_productos": [
            {"producto": p, "total": round(t, 2)} for p, t in top_productos
        ],
    }

# 5. Vamos a mostrar la salida en un json
def guardar_resultado(resumen, errores, ruta_salida, ruta_errores):
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=2, ensure_ascii=False)

    if errores:
        with open(ruta_errores, "w", encoding = "utf-8") as f:
            json.dump(errores,f,indent = 2, ensure_ascii= False)