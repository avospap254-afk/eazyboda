from flask import os
import Flask, request

app = Flask(__name__)

# Prices in KSH - Eldoret real prices
PRICES = {
    ("Town", "Annex"): 100,
    ("Town", "Kapsoya"): 150,
    ("Town", "Kimumu"): 150,
    ("Town", "Elgon View"): 200,
    ("Town", "Langas"): 100,
    ("Town", "Munyaka"): 200,
    ("Town", "West Indies"): 100,
    ("Town", "Kipkaren"): 300,
    ("Town", "Ainabkoi"): 250,
    ("Annex", "Kapsoya"): 100,
    ("Annex", "Kimumu"): 150,
}

PLACES = ["Town", "Annex", "Kapsoya", "Kimumu", "Elgon View", "Langas", "Munyaka", "West Indies", "Kipkaren", "Ainabkoi"]

def get_price(frm, to):
    if frm == to:
        return 50
    if (frm, to) in PRICES:
        return PRICES[(frm, to)]
    if (to, frm) in PRICES:
        return PRICES[(to, frm)]
    return 150 # default price

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        frm = request.form.get("from")
        to = request.form.get("to")
        price = get_price(frm, to)
        result = f"<div style='background:#00e676;color:black;padding:20px;border-radius:15px;margin-top:20px'><h2>🛵 {frm} → {to}</h2><h1>KSH {price}</h1><p>Don't let them overcharge you!</p><a href='https://wa.me/254107790016?text=I need a boda from {frm} to {to}' style='background:black;color:white;padding:10px 20px;border-radius:10px;text-decoration:none'>Order on WhatsApp</a></div>"

    options = "".join([f"<option>{p}</option>" for p in PLACES])
    
    return f"""
    <html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>body{{font-family:Arial;background:#111;color:white;text-align:center;padding:20px}} select,button{{padding:15px;width:100%;margin:10px 0;border-radius:10px;font-size:18px}} button{{background:#ffcc00;font-weight:bold}}</style></head>
    <body>
    <h1>🛵 EazyBoDa</h1>
    <p>Know the REAL price before you ride</p>
    <form method='POST'>
    <label>From:</label><select name='from'>{options}</select>
    <label>To:</label><select name='to'>{options}</select>
    <button>CHECK PRICE →</button>
    </form>
    {result}
    <p style='margin-top:30px;color:#888'>Made by EazyBoDa - Eldoret</p>
    </body></html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
