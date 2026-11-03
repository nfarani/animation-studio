import sys
from PIL import Image, ImageDraw
out=sys.argv[1]; cols=int(sys.argv[2]); files=sys.argv[3:]; W=800; ims=[]
for f in files:
    im=Image.open(f).convert('RGB'); im=im.resize((W,int(im.height*W/im.width)))
    d=ImageDraw.Draw(im); lab=f.split('/')[-1].rsplit('.',1)[0]; d.rectangle([0,0,10+8*len(lab),18],fill=(0,0,0)); d.text((4,3),lab,fill=(255,255,255)); ims.append(im)
rows=(len(ims)+cols-1)//cols; H=max(i.height for i in ims); sheet=Image.new('RGB',(W*cols,H*rows),(30,30,30))
for n,im in enumerate(ims): sheet.paste(im,((n%cols)*W,(n//cols)*H))
sheet.save(out,quality=82)
