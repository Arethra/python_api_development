```text
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Scripts\uvicorn.exe\__main__.py", line 7, in <module>
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\click\core.py", line 1157, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\click\core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\click\core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\click\core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\uvicorn\main.py", line 412, in main
    run(
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\uvicorn\main.py", line 579, in run
    server.run()
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\uvicorn\server.py", line 65, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\asyncio\runners.py", line 194, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\asyncio\base_events.py", line 687, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\uvicorn\server.py", line 69, in serve
    await self._serve(sockets)
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\uvicorn\server.py", line 76, in _serve
    config.load()
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\uvicorn\config.py", line 434, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\ADEWUYI\Documents\fastapi\venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\ADEWUYI\Documents\fastapi\main.py", line 5, in <module>
    @app.get("/")
     ^^^^^^^^^^^^
TypeError: FastAPI.get() missing 1 required positional argument: 'path'
```


CODE:
```python
from fastapi import FastAPI

app = FastAPI

@app.get("/")
def root():
    return {"message": "Hello World"}
```

SOLUTION:

```python
app = FastAPI()
```
