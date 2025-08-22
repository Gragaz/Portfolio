# Tillåter python läsa json filer
import json

# Laddar in json filen
def load(filename):
    try:
        # Öppnar filen i read(r) läge. with säger att filen stängs automatiskt efteråt
        with open(filename, 'r', encoding="utf-8") as f:
            data = json.load(f)
            data = sorted(data, key=lambda x: x['project_id'])
    except FileNotFoundError:
        data = []
    return data