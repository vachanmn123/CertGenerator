from PIL import Image, ImageDraw, ImageFont
from pymongo import MongoClient
from flask import g
import dotenv
import certifi

ca = certifi.where()


def write_name(name: str, branch: str) -> str:
    img = None
    if branch == "CSBS":
        img = Image.open("csbscert.png")
    elif branch == "BT":
        img = Image.open("btcert.png")
    else:
        img = Image.open("isecert.png")
    d = ImageDraw.Draw(img)
    location = (705, 685)
    text_color = (255, 255, 255)
    font = ImageFont.truetype("Courgette-Regular.ttf", 75)
    d.text(location, name, fill=text_color, font=font)
    img.save("certificates/" + name + ".png")
    return "certificates/" + name + ".png"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        client = MongoClient(
            dotenv.get_key(dotenv.find_dotenv(), "MONGODB_URI", None), tlsCAFile=ca
        )
        db = g._database = client["feedback"]
    return db


write_name("Vachan MN", "CSBS")
