library(lpSolve)
costs <- matrix ( c( 2,2,2,1,10,8,5,4,7,6,6,8), nrow=3,byrow=TRUE)
row.signs <- rep("<=",3)
row.rhs <- c(3,7,5)
col.signs <- rep(">=",4)
col.rhs <- c(4,3,4,4)
lptrams <- lp.transport(costs,"min",row.signs,
 row.rhs, col.signs,col.rhs)
print("quantities transported")
lptrams$solution
print("Total transportation")
lptrams$objval
