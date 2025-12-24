import torch as pt 
x=pt.tensor([[2,7,4,8],[6,3,1,0]])
print(x[0,3].item())
print(x.view(4,2))

#tensor to numpy
z=x.numpy()

#numpy to tensor
w=pt.from_numpy(z)