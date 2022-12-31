library(ReppHungarian)
a<- matrix(c(80,55,45,45,58,35,70,50,70,50,80,65,90,70,40,80),nrow=4,byrow=TRUE)
cost <- matrix (0,nrow(a) , ncol(a))
maxi <- max(a)
for (i in 1:nrow(a))
{
	for(j in 1:ncol(a))
	{
		cost[i,j] <- max(a) - a[i,j]
	}
}
print("Assignmnet")
soln <- HungarianSolver(cost)$pairs
print(soln)
score <- 0
for(i in 1:nrow(soln)){
score <- score+a[i,soln[i,2]]}
cat ("max :" , score)

