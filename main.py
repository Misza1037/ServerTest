# import server
#
#
# HOST = ''
# PORT = 65065
#
#
# if __name__ == '__main__':
#     server.connection(HOST, PORT)
#
import os

import aiohttp
from aiohttp import web


async def handler(request: web.Request) -> None:
    return web.json_response({'data': '1037'})


app = web.Application()
app.add_routes([
    web.get('/', handler=handler)
])
print('Starting API Application')
assert 'PORT' in os.environ.keys()
web.run_app(app=app, host='0.0.0.0', port=int(os.environ['PORT']))
