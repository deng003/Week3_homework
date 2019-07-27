文件说明：
1 线性回归python形式，采用numpy中一维数组进行处理，
  可以避免除了最大迭代次数循环之外的所有循环语句。
  
2 逻辑回归python形式，同样采用numpy中一维数组进行处理
  通过将线性回归的结果代入sigmoid函数中，将函数值位于0-1区间内
  再构建cost function通过梯度下降法求解最小值得出最优模型参数
  
3 游泳问题数学模型
  a 此问题通过过河总时间T可以构建ai相关的约束方程
  b 根据所求h，可以构建目标方程
  c 根据lagrangian multiplier可以 得出满足条件的等式
    gradF(ai)+λ*gradg(ai)=0
	则 cost function= (gradF(ai)+λ*gradg(ai))^2
	当 cost function取最小值即0时，ai可以满足要求
  