library(lpSolve)
f.obj<-c(2,3)
f.con<-matrix(c(2,3, 2,6),nrow=2,byrow=TRUE)
f.dir<-c("<=","<=")
f.rhs<-c(8,18)
opt<-lp("max",f.obj,f.con,f.dir,f.rhs, compute.sens=TRUE) 
optval<-opt$objval
d<-opt$duals

print("DUALS")
cat("RAW MATERIALS 1 :" , d[1] ,"\n")
cat("RAW MATERIALS 2:" , d[2] ,"\n")

from <- opt$duals.from
to <- opt$duals.to

print("Feasibility Range")
cat("RAW MATERIALS 1 :" , from[1] ,"to",to[1] ,"\n")
cat("RAW MATERIALS 2:" , from[2] ,"to",to[2] ,"\n")

d<-d[1]-0.30
if(f.rhs[1] +4 >=from[1]&& f.rhs[1]+4 <=to[1]){
newopt = optval +(d1*4)
if(newopt>optval){
print("Recommended")}
else{
print("Not Recommended")}}

