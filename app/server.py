import aiohttp
import asyncio
import uvicorn
from fastai.vision.all import *
import torchvision.transforms as T
import PIL 
from io import BytesIO
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles




# direct link generated for our model
#export_file_url = 'https://drive.google.com/uc?export=download&id=1-7lp7rG9SVIxThWeH2xRspGzZD8p8y7E'
#export_file_name = 'export.pkl'

classes = ['tshirt','pantalon','pull','short']
path = Path(__file__).parent

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))


async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f:
                f.write(data)


async def setup_learner():
    #await download_file(export_file_url, path / export_file_name)
    try:
        learn = load_learner('app/models/export.pkl')
        return learn
    except :
        print('An exception occured')
        raise


loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_learner())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()


@app.route('/')
async def homepage(request):
    html_file = path / 'view' / 'index.html'
    return HTMLResponse(html_file.open().read())


@app.route('/analyze', methods=['POST'])
async def analyze(request):
    img_data = await request.form()
    img_bytes = await (img_data['file'].read())
    img_pil = PIL.Image.open(BytesIO(img_bytes))
    img_tensor = T.ToTensor()(img_pil)
    img_fastai = Image(img_tensor)
    pred = learn.predict(img_fastai)
    prediction = pred[0]
    return JSONResponse({'result': str(prediction)})


if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run(app=app, host='0.0.0.0', port=5000, log_level="info")
