#!/usr/bin/env python3
"""
Generador de index.html para Aero Vapes.

Como esto es un sitio 100% estatico (sin backend/base de datos), el stock
vive en el array PRODUCTS de este archivo. Para actualizar cantidades:

  1. Edita el numero "stock" del sabor que corresponda mas abajo.
  2. Corre:  python3 build.py
  3. Commiteá y pusheá index.html a GitHub (o volvé a publicar el Artifact).

Un sabor con stock 0 se muestra automaticamente como "Agotado" en la tienda,
y si TODOS los sabores de un modelo quedan en 0, esa tarjeta se ordena al
final de la grilla.
"""
import base64
import json
import os

IMG_DIR = os.path.join(os.path.dirname(__file__), "aero-images")


def data_uri(fname):
    path = os.path.join(IMG_DIR, fname)
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return "data:image/jpeg;base64," + b64


PRODUCTS = [
    {"id": "ignite-v400-vmix", "name": "IGNITE V400 V-MIX 40k", "price": 29990, "flavors": [
        {"name": "Pineapple Ice + Passion Fruit Sour Kiwi", "stock": 2, "img": data_uri("IGNITE_V400_V_MIX_40k_Pineapple_Ice_Passion_Fruit_Sour_Kiwi_.jpg")},
        {"name": "Grape Pop + Peach Ice", "stock": 2, "img": data_uri("IGNITE_V400_V_MIX_40k_Grape_Pop_Peach_Ice_.jpg")},
        {"name": "Menthol + Mighty Melon", "stock": 1, "img": data_uri("IGNITE_V400_V_MIX_40k_Menthol_Mighty_Melon_.jpg")},
    ]},
    {"id": "ignite-v80", "name": "IGNITE V80 8k", "price": 19900, "flavors": [
        {"name": "Black Green Apple", "stock": 2, "img": data_uri("IGNITE_V80_8k_Black_Green_Apple_.jpg")},
    ]},
    {"id": "ice-king-40k", "name": "Ice King 40k", "price": 27500, "flavors": [
        {"name": "Blueberry Ice", "stock": 2, "img": data_uri("Ice_King_40k_Blueberry_Ice_.jpg")},
        {"name": "Green Apple Ice", "stock": 1, "img": data_uri("Ice_King_40k_Green_Apple_Ice_.jpg")},
        {"name": "Strawberry Ice", "stock": 1, "img": data_uri("Ice_King_40k_Strawberry_Ice_.jpg")},
        {"name": "Watermelon Ice", "stock": 2, "img": data_uri("Ice_King_40k_Watermelon_Ice_.jpg")},
    ]},
    {"id": "trio-40k", "name": "Trio 40k", "price": 26500, "flavors": [
        {"name": "Raspberry Watermelon", "stock": 2, "img": data_uri("Trio_40k_Raspberry_Watermelon_.jpg")},
        {"name": "Blueberry Pom Slushy", "stock": 2, "img": data_uri("Trio_40k_Blueberry_Pom_Slushy_.jpg")},
        {"name": "Sour Strawberry Dragonfruit", "stock": 0, "img": data_uri("Trio_40k_Sour_Strawberry_Dragonfruit_.jpg")},
    ]},
    {"id": "gh-23k", "name": "GH 23k", "price": 25900, "flavors": [
        {"name": "Ice Mint", "stock": 2, "img": data_uri("GH_23k_Ice_Mint_.jpg")},
        {"name": "Spring Mint", "stock": 1, "img": data_uri("GH_23k_Spring_Mint_.jpg")},
    ]},
    {"id": "te-30k", "name": "TE 30K", "price": 25900, "flavors": [
        {"name": "Blueberry Ice", "stock": 2, "img": data_uri("TE_30K_Blueberry_ice_.jpg")},
        {"name": "Strawberry Watermelon Ice", "stock": 2, "img": data_uri("TE_30K_Strawberry_Watermelon_Ice_.jpg")},
        {"name": "Green Apple Ice", "stock": 2, "img": data_uri("TE_30K_Green_Apple_Ice_.jpg")},
    ]},
    {"id": "bc-5k", "name": "BC 5K", "price": 8900, "flavors": [
        {"name": "Blackberry Cherry", "stock": 1, "img": data_uri("BC_5K_Blackberry_Cherry_.jpg")},
        {"name": "Cherry Dragon Fruit", "stock": 1, "img": data_uri("BC_5K_Cherry_Dragon_Fruit_.jpg")},
        {"name": "Orange Pear Nectar", "stock": 2, "img": data_uri("BC_5K_Orange_Pear_Nectar_.jpg")},
    ]},
    {"id": "eb-bc-pro-40k", "name": "EB BC PRO 40k", "price": 23900, "flavors": [
        {"name": "Strawberry Raspberry Frost", "stock": 1, "img": data_uri("EB_BC_PRO_40k_Strawberry_Raspberry_Frost_.jpg")},
        {"name": "Golden Berry", "stock": 1, "img": data_uri("EB_BC_PRO_40k_Golden_Berry_.jpg")},
        {"name": "Watermelon Ice", "stock": 2, "img": data_uri("EB_BC_PRO_40k_Watermelon_Ice_.jpg")},
        {"name": "Winter Mint", "stock": 2, "img": data_uri("EB_BC_PRO_40k_Winter_Mint_.jpg")},
    ]},
]


def data_uri_abs(path):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return "data:image/png;base64," + b64


def main():
    base_dir = os.path.dirname(__file__)
    products_json = json.dumps(PRODUCTS, ensure_ascii=False)

    with open(os.path.join(base_dir, "template.html"), encoding="utf-8") as f:
        html = f.read()

    html = html.replace("__PRODUCTS_JSON__", products_json)
    html = html.replace("__WORDMARK_HERO__", data_uri_abs(os.path.join(base_dir, "brand", "wordmark-hero.png")))
    html = html.replace("__WORDMARK_NAV__", data_uri_abs(os.path.join(base_dir, "brand", "wordmark-nav.png")))

    out_path = os.path.join(base_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("OK ->", out_path, os.path.getsize(out_path), "bytes")


if __name__ == "__main__":
    main()
