```
uv run fastapi dev
```
navigate to http://127.0.0.1:8000/notebooks/notebook1

      INFO   Will watch for changes in these directories: ['/home/cmaggio/repos/hello_marimo']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [1345] using WatchFiles
      INFO   Started server process [1347]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
      INFO   127.0.0.1:56416 - "GET /notebooks/notebook1/ HTTP/1.1" 200
      INFO   127.0.0.1:56416 - "GET /notebooks/notebook1/assets/gradient-yHQUC_QB.png HTTP/1.1" 200
      INFO   127.0.0.1:56430 - "GET /notebooks/notebook1/assets/noise-60BoTA8O.png HTTP/1.1" 200
      INFO   127.0.0.1:56446 - "GET /notebooks/notebook1/assets/index-C_IDebto.js HTTP/1.1" 304
      INFO   127.0.0.1:56462 - "GET /notebooks/notebook1/assets/Lora-VariableFont_wght-B2ootaw-.ttf HTTP/1.1" 200
      INFO   127.0.0.1:56484 - "GET /notebooks/notebook1/assets/PTSans-Regular-CxL0S8W7.ttf HTTP/1.1" 304
      INFO   127.0.0.1:56474 - "GET /notebooks/notebook1/assets/FiraMono-Regular-BTCkDNvf.ttf HTTP/1.1" 200
      INFO   127.0.0.1:56446 - "GET /notebooks/notebook1/assets/PTSans-Bold-D9fedIX3.ttf HTTP/1.1" 304
      INFO   127.0.0.1:56484 - "GET /notebooks/notebook1/assets/FiraMono-Medium-DU3aDxX5.ttf HTTP/1.1" 304
      INFO   127.0.0.1:56430 - "GET /notebooks/notebook1/assets/FiraMono-Bold-CLVRCuM9.ttf HTTP/1.1" 304
      INFO   127.0.0.1:56446 - "GET /notebooks/notebook1/assets/index-DfLILvXO.css HTTP/1.1" 304
      INFO   127.0.0.1:56462 - "GET /notebooks/notebook1/assets/useMarimoWebSocket-DnTSKlUU.js HTTP/1.1" 304
      INFO   127.0.0.1:56416 - "GET /notebooks/notebook1/assets/run-page-COthXqUl.js HTTP/1.1" 304
      INFO   127.0.0.1:56430 - "GET /notebooks/notebook1/assets/useMarimoWebSocket-CYiIF7o8.css HTTP/1.1" 200
      INFO   127.0.0.1:56474 - "GET /notebooks/notebook1/assets/createWsUrl-DPustLsY.js HTTP/1.1" 304
      INFO   127.0.0.1:56416 - "GET /notebooks/notebook1/assets/web-vitals-DSwKt_Ty.js HTTP/1.1" 304
      INFO   ('127.0.0.1', 56490) - "WebSocket /notebooks/notebook1/ws?session_id=s_cx7e6k"
      INFO   connection open
      INFO   127.0.0.1:56416 - "POST /notebooks/notebook1/api/kernel/instantiate HTTP/1.1" 200
      INFO   127.0.0.1:56416 - "GET /notebooks/notebook1/public-files-sw.js HTTP/1.1" 200
      INFO   connection closed
      INFO   127.0.0.1:48854 - "GET /notebooks/notebook2/ HTTP/1.1" 200
      INFO   127.0.0.1:48854 - "GET /notebooks/notebook2/assets/gradient-yHQUC_QB.png HTTP/1.1" 200
      INFO   127.0.0.1:48868 - "GET /notebooks/notebook2/assets/index-C_IDebto.js HTTP/1.1" 304
      INFO   127.0.0.1:48890 - "GET /notebooks/notebook2/assets/PTSans-Regular-CxL0S8W7.ttf HTTP/1.1" 304
      INFO   127.0.0.1:48880 - "GET /notebooks/notebook2/assets/Lora-VariableFont_wght-B2ootaw-.ttf HTTP/1.1" 304
      INFO   127.0.0.1:48856 - "GET /notebooks/notebook2/assets/noise-60BoTA8O.png HTTP/1.1" 200
      INFO   127.0.0.1:48904 - "GET /notebooks/notebook2/assets/index-DfLILvXO.css HTTP/1.1" 304
      INFO   127.0.0.1:48890 - "GET /notebooks/notebook2/assets/FiraMono-Medium-DU3aDxX5.ttf HTTP/1.1" 304
      INFO   127.0.0.1:48868 - "GET /notebooks/notebook2/assets/PTSans-Bold-D9fedIX3.ttf HTTP/1.1" 304
      INFO   127.0.0.1:48880 - "GET /notebooks/notebook2/assets/FiraMono-Regular-BTCkDNvf.ttf HTTP/1.1" 304
      INFO   127.0.0.1:48904 - "GET /notebooks/notebook2/assets/FiraMono-Bold-CLVRCuM9.ttf HTTP/1.1" 304
      INFO   127.0.0.1:48890 - "GET /notebooks/notebook2/assets/useMarimoWebSocket-CYiIF7o8.css HTTP/1.1" 304
      INFO   127.0.0.1:48868 - "GET /notebooks/notebook2/assets/createWsUrl-DPustLsY.js HTTP/1.1" 304
      INFO   127.0.0.1:48854 - "GET /notebooks/notebook2/assets/run-page-COthXqUl.js HTTP/1.1" 304
      INFO   127.0.0.1:48856 - "GET /notebooks/notebook2/assets/useMarimoWebSocket-DnTSKlUU.js HTTP/1.1" 304
      INFO   127.0.0.1:48854 - "GET /notebooks/notebook2/assets/web-vitals-DSwKt_Ty.js HTTP/1.1" 304
      INFO   ('127.0.0.1', 48906) - "WebSocket /notebooks/notebook2/ws?session_id=s_gz94v9"
      INFO   connection open
      INFO   127.0.0.1:48854 - "POST /notebooks/notebook2/api/kernel/instantiate HTTP/1.1" 200
      INFO   127.0.0.1:48854 - "GET /notebooks/notebook2/public-files-sw.js HTTP/1.1" 200
```
uv run litestar run
```
navigate to http://127.0.0.1:8000/notebooks/notebook1

     ┌──────────────────────────────┬──────────────────────┐
     │ Litestar version             │ 2.14.0               │
     │ Debug mode                   │ Disabled             │
     │ Python Debugger on exception │ Disabled             │
     │ CORS                         │ Disabled             │
     │ CSRF                         │ Disabled             │
     │ OpenAPI                      │ Enabled path=/schema │
     │ Compression                  │ Disabled             │
     └──────────────────────────────┴──────────────────────┘
     INFO:     Started server process [1394]
     INFO:     Waiting for application startup.
     INFO:     Application startup complete.
     INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
     INFO:     127.0.0.1:56740 - "GET / HTTP/1.1" 200 OK
     INFO:     127.0.0.1:56740 - "GET /favicon.ico HTTP/1.1" 404 Not Found
     INFO:     127.0.0.1:56750 - "GET /notebook1/ HTTP/1.1" 200 OK
     INFO:     ('127.0.0.1', 35512) - "WebSocket /notebook1/ws/?session_id=s_u9diol" 403
     INFO:     connection rejected (403 Forbidden)
     INFO:     connection closed
     INFO:     127.0.0.1:56750 - "GET /notebook1/public-files-sw.js/ HTTP/1.1" 404 Not Found
     INFO:     ('127.0.0.1', 35518) - "WebSocket /notebook1/ws/?session_id=s_u9diol" 403
     INFO:     connection rejected (403 Forbidden)
     INFO:     connection closed
     INFO:     ('127.0.0.1', 35520) - "WebSocket /notebook1/ws/?session_id=s_u9diol" 403
     INFO:     connection rejected (403 Forbidden)
     INFO:     connection closed
     INFO:     ('127.0.0.1', 35530) - "WebSocket /notebook1/ws/?session_id=s_u9diol" 403
     INFO:     connection rejected (403 Forbidden)
     INFO:     connection closed
     INFO:     ('127.0.0.1', 35538) - "WebSocket /notebook1/ws/?session_id=s_u9diol" 403
     INFO:     connection rejected (403 Forbidden)
     INFO:     connection closed
     INFO:     127.0.0.1:56750 - "GET /notebook2/ HTTP/1.1" 200 OK
     INFO:     ('127.0.0.1', 35544) - "WebSocket /notebook2/ws/?session_id=s_ujsdgw" 403
     INFO:     connection rejected (403 Forbidden)
     INFO:     connection closed
     INFO:     127.0.0.1:56750 - "GET /notebook2/public-files-sw.js/ HTTP/1.1" 404 Not Found
     INFO:     ('127.0.0.1', 44400) - "WebSocket /notebook2/ws/?session_id=s_ujsdgw" 403
     INFO:     connection rejected (403 Forbidden)
     INFO:     connection closed
