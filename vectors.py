import math as mt
def vec(i,j,k):
    return [i,j,k]
def kronecker_delta(i,j):
    if i==j:
        return 1
    else:
        return 0
def levi_civita(i,j,k):
    indexorder=str(i)+str(j)+str(k)
    if indexorder in "01201":
        return 1
    elif indexorder in "21021":
        return -1
    else: return 0
def vdot(vector1,vector2):
    sum=0
    for i in range(3):
        for j in range(3):
            sum+=kronecker_delta(i,j)*vector1[i]*vector2[j]
    return sum
def vcrs(vector1,vector2):
    output=[]
    for i in range(3):
        sum=0
        for j in range(3):
            for k in range(3):
                prod=levi_civita(i,j,k)*vector1[j]*vector2[k]
                sum+=prod
        output.append(sum)
    return output
def vscal(constant,vector):
    output=[]
    for i in range(3):
        output.append(constant*vector[i])
    return output
def sign(x):
    return abs(x)/x
def mag(vector):
    sqsum=0
    for i in range(3):
        sqsum+=vector[i]**2
    norm_=mt.sqrt(sqsum)
    return norm_
def sqrmag(vector):
    sqsum=0
    for i in range(3):
        sqsum+=vector[i]**2
    return sqsum
def normalized(vector):
    output=[]
    if mag(vector)==0:
        return [0,0,0]
    for i in range(3):
        n=vector[i]/mag(vector)
        output.append(n)
    return output
def bvec(i):
    bveclist=[[1,0,0],[0,1,0],[0,0,1]]
    return bveclist[i]
def vprj(vector1,vector2):
    if mag(vector2)==0:
        return "Indeterminate"
    k=vdot(vector1,vector2)/(mag(vector2)*mag(vector2))
    output=vscal(k,vector2)
    return output
def vxcl(vector1,vector2):
    output=vminus(vector1,vprj(vector1,vector2))
    return output
def vadd(vector1,vector2):
    output=[]
    for i in range(3):
        n=vector1[i]+vector2[i]
        output.append(n)
    return output
def vminus(vector1,vector2):
    output=[]
    for i in range(3):
        n=vector1[i]-vector2[i]
        output.append(n)
    return output
def vang(vector1,vector2,deg=True):
    if (mag(vector1)*mag(vector2))==0:
        return "Indeterminate"
    m=vdot(vector1,vector2)/(mag(vector1)*mag(vector2))
    if abs(m)>1:
        m=sign(m)*1
    if deg==True:
        return (180/mt.pi)*mt.acos(m)
    return mt.acos(m)
def gramm_schmidt(vector1,vector2,vector3):
    if vang(vector1,vector2)==0 or vang(vector1,vector3)==0 or vang(vector2,vector3)==0:
        return "vectors are parallel"
    vector_a=normalized(vector1)
    vector_b=normalized(vxcl(vector2,vector1))
    vector_c=normalized(vminus(vminus(vector3,vprj(vector3,vector1)),vprj(vector3,vector2)))
    output=[vector_a,vector_b,vector_c]
    return output
v1=vec(2,0,0)
v2=[0,1,2]
v3=[1,34,2]
print(v1)
print(v2)
print(mag(v1))
print(mag(v2))
print(normalized(v1))
print(normalized(v2))
print(vang(v1,v2))
print(vprj(v1,v2))
print(vxcl(v1,v2))
print(vdot(v1,v2))
print(vcrs(v1,v2))