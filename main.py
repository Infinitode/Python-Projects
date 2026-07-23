import os, shutil
sz = shutil.get_terminal_size().columns

def numput(prompt, default=0, do=int, use=input):
    try:
        d = do(use(prompt))
    except:
        print(f"Non-numeric value - defaulting to {default}")
        d = default
    return d

def fnh(ls):
    rt = {}
    for f in ls:
        n, _ = os.path.splitext(f)
        c = n.split("_")
        v = c[0]
        del c[0]
        rt[int(v)] = (" ".join(c).title(), f)

ip = fnh([os.path.join(os.path.join(os.getcwd(), "Intermediate"), z) for z in os.listdir("Intermediate/")])
bp = fnh([os.path.join(os.path.join(os.getcwd(), "Beginner/"), z) for z in os.listdir("Beginner/")])
def m():
    print("Welcome to projects browser!")
    print("Projects available:")
    print("="*sz)
    print("\033[1m\033[94mBeginner:")
    for q, w in bp.items():
        print(f"#{q}. {w}")
    print("-"*sz)
    print("\033[1m\033[93mIntermediate:")
    for q, w in ip.items():
        print(f"#{q}. {w}")
    print("\033[0m="*sz)
    
    
