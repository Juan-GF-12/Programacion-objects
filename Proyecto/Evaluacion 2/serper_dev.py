import http.client
import json
busqueda=input("¿Que deseas buscar hoy?: ")
conn = http.client.HTTPSConnection("google.serper.dev")
info_busqueda = json.dumps({
  "q": busqueda
})
headers = {
  'X-API-KEY': '4f044cd471e12a1204ee4d3e06e7b6f12bf57d40',
  'Content-Type': 'application/json'
}
conn.request("POST", "/search", info_busqueda, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
