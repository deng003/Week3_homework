"""
约束条件： T= sum[si/(v*cosai) for i in range(n)]  过河总时间
目标函数：f(ai)=sum[(si/(v*cosai)) * (vi+v*sinai) ]  求目标函数最大值

问题稍微转换：
约束条件：g(ai)=T-sum[si/(v*cosai) for i in range(n)] =0
目标函数F(ai)=-f(ai) 求目标函数最小值

由拉格朗日乘子发可知，当ai满足下式时候，目标函数为最小值
gradF(ai))+λ*gradg(ai)=0
则
cost function = (gradF(ai))+λ*gradg(ai))**2
满足cost function取最小值的ai，即为答案

"""