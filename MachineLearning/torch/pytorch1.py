import torch

r=[[4,2],[6,9]]
x=torch.ones(2,4,3,dtype=torch.float16)
y=torch.tensor([[2,4],[6,8]])
R=torch.tensor(r)

z=torch.tensor([[4,7,9],[7,3,5]])
Mean=torch.mean(x)
print(Mean)

sum=torch.sum(z)
print(sum)

mal=torch.matmul(y,z) #row*column
print(mal)

add=torch.subtract(mal,z)
print(add)

min=torch.min(z)
print(min)

slice=z[0,0:3] #slice
print(f"Slice: {slice}")

row=z[1, :]
print(f"Row:{row}")

col=z[:,1]
print(f"column: {col}")

w=torch.rand(5,3)
step=w[::2] #split  at intervals
print(f"steps: {step}")

mask=z>5 #apply condition to tensor
print(z[mask])