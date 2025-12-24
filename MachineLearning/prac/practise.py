t=["Amber_",")ray"]
th=" ".join(t)
ty=t[0].rstrip("_")
tr=t[1].lstrip(")")
print(th)
print(ty)
print(tr)

t[0]=t[0].rstrip("_")
t[1]=t[1].lstrip(")")
t="".join(t)
print(t)