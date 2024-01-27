import psutil

def plist():
    p = psutil.process_iter()
    try:
        return set([i.name() for i in p])-set([""])
    except:
        raise RuntimeError("read error")
    

if __name__=="__main__":
    print(plist())