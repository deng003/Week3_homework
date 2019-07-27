import numpy as np
import math

#生成样本，均为一维数组
def get_sample():
    sample_number=100
    x=np.random.uniform(-2,2,sample_number)
    w=10+np.random.uniform(0,1,sample_number)
    y=1/(math.e**(x*(-w))+1)
    return x,y,sample_number

#梯度下降法计算w值
def cal_step_gradient(w,batch_x,batch_y,lr):
    diff=1/(math.e**(batch_x*(-w))+1)-batch_y
    dw=np.sum(diff*batch_x)/len(batch_x)
    w=w-lr*dw
    return w

#计算loss值
def loss(w,x,y):
    y1=1/(math.e**(x*(-w))+1)
    loss_value=np.sum(y*np.log(y1)+(1-y)*np.log(1-y1))/(-len(x))
    return loss_value

#开始训练，迭代
def train():
    w=0
    batch_size=50
    max_iter=1000
    lr=10
    x,y,sample_number=get_sample()
    for i in range(max_iter):
        batch_id = np.random.choice(sample_number, batch_size,False)
        batch_x=np.array([x[j] for j in batch_id])
        batch_y=np.array([y[j] for j in batch_id])
        w=cal_step_gradient(w,batch_x,batch_y,lr)
        print ('w=',w)
        print ('loss=',loss(w,x,y))

if __name__ == '__main__':
    train()