import os

for f in os.listdir():
    if f.lower().startswith('sparky'):

        nf = f.replace(" ",'-')
        print(f,nf)
        os.rename(f,nf)
