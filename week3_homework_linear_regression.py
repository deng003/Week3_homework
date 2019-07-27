import numpy as np
import random

#生成样本，均为一维数组
def get_sample():
    sample_number=100
    x=np.random.uniform(0,10,sample_number)
    w=10+np.random.uniform(0,1,sample_number)
    b=3+np.random.uniform(0,1,sample_number)
    y=b+w*x+random.random()
    return x,y,sample_number

#梯度下降法计算w b值
def cal_step_gradient(w,b,batch_x,batch_y,lr):
    diff=w*batch_x+b-batch_y
    dw=np.sum(diff*batch_x)/len(batch_x)
    db=np.sum(diff)/len(batch_x)
    w=w-lr*dw
    b=b-lr*db
    return w,b

#计算loss值
def loss(w,b,x,y):
    loss_value=np.sum((w*x+b-y)*(w*x+b-y))/len(x)
    return loss_value

#开始训练，迭代
def train():
    w=0
    b=0
    batch_size=10
    max_iter=1000
    lr=0.003
    x,y,sample_number=get_sample()
    for i in range(max_iter):
        batch_id = np.random.choice(sample_number, batch_size,False)
        batch_x=np.array([x[j] for j in batch_id])
        batch_y=np.array([y[j] for j in batch_id])
        w,b=cal_step_gradient(w,b,batch_x,batch_y,lr)
        print ('w=',w ,'b=',b)
        print ('loss=',loss(w,b,x,y))

if __name__ == '__main__':
    train()