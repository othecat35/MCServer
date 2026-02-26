import logging as log
import json
import urllib.parse
import urllib.request

def request_get(url, params, headers):
  query_string = urllib.parse.urlencode(params)
  log.debug(f"Query string: {query_string}")

  request_url = urllib.request.Request(f"{url}?{query_string}", headers=headers, method="GET")
  with urllib.request.urlopen(request_url) as response:
    return response.read().decode("utf-8")

log.basicConfig(
  level=log.DEBUG,
  format="[%(levelname)s]: %(message)s"
)

response = request_get("https://api.modrinth.com/v2/search", {
  "query": "Lithium",
  "limit": 1
}, {
  "User-Agent": "othecat35/MCServer"
})

log.info(response)
