import requests as rq
from sys import argv

request_model = "python3 listdir.py -w [Wordlist path] [Hostname]"
wordlist = argv[2]
host = argv[3]

if argv[1] == "-w":
    if wordlist:
        with open(wordlist, "r") as src:
            try:
                content = src.read().splitlines()
                for i in content:
                    payload = f"{host}" + f"{i}"
                    if payload.startswith("https://") or payload.startswith("http://"):
                        req = rq.get(payload)
                        print(f"==> {i} -------- {req}")
                    else:
                        print("Bad Request, URL must be full!")
                        src.close()
                        break
            except ValueError:
                print("Invalid Value!")
            except Exception:
                print("Error!")
    else:
        print("Wrong path or wordlist does not exist")
else:
    print(request_model)
    
            
        