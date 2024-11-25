from fastapi import FastAPI
from fastapi.responses import Response
import httpx

app = FastAPI()

# @app.get("/")
# def welcome():
#     return {"message": "Welcome"}

APP_PORTS = {
    'app_1': '3000',
    'app_2': '3001'
}

def trimAppPrefix(path: str):
    path_vars = path.split('/')
    return [path_vars[0], '/'.join(path_vars[1:])]

@app.get("/{path:path}")
async def proxy(path: str):
    #client targets 3000 we find respective app target it's port
    async with httpx.AsyncClient() as client:
        res = trimAppPrefix(path)
        app_code = res[0]
        trimmed_path = res[1]
        port = APP_PORTS[app_code]
        print(app_code, trimmed_path, port)
        url  = "http://localhost:" + port + "/" + trimmed_path
        print(url)
        response = await client.request(
            method= "GET",
            url= url,
            headers=None,
            content=None
        )
        if response.headers.get("content-type") == "text/html; charset=utf-8":
            content = response.text.replace('src="/static/', 'src="'+ app_code +'/static/')
            content = content.replace('/favicon.ico', app_code + '/favicon.ico')
            content = content.replace('/manifest.json', app_code + '/manifest.json')
            return Response(
                content=content,
                status_code=response.status_code,
            )
        return Response(
            content=response.content,
            status_code=response.status_code,
        )
