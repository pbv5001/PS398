#Peter Vining
#PLSC 318 HW7
#11/8/11

#Globals#
setwd("C:\\Users\\Peter\\Desktop\\Duke Coursework\\Spring 2012\\Python\\week3\\assignment")

install.packages("foreign")  #For reading dta
install.packages("ggplot2")  #For better plots
install.packages("pastecs")  #For producing tables of descriptive stats
install.packages("xtable")   #For creating tables and exportable LaTeX code thereof
install.packages("directlabels") #For labeling lines in ggplot
install.packages("apsrtable")
install.packages("car")
install.packages("Zelig")
install.packages("sandwich")
install.packages("arm")
install.packages("lmtest")
install.packages("MASS")
library(foreign)
library(ggplot2)
library(directlabels)
library(pastecs)
library(xtable)
library(apsrtable)
library(car)
library(Zelig)
library(sandwich)
library(arm)
library(lmtest)
library(MASS)



data <- read.csv(file="times.csv",head=FALSE,sep=",")


png(file="test.png",width=800,height=400)
plot((data$V1), (data$V2), type="o", xlim=c(1,1000), ylim=c(0,0.200000), main="Figure 1: Sort Times Per List Length of Three Sorting Algorithms", xlab="List length", ylab="Time(Seconds)", col="blue", pch=19, tck=0.025) #plots scaled variables 
par(new=T) #allows overlay  of additional data points
plot((data$V1), (data$V3), type="o",xlim=c(1,1000), ylim=c(0,0.200000), main="Figure 1: Sort Times Per List Length of Three Sorting Algorithms", xlab="List length", ylab="Time(Seconds)", col="red", pch=19, tck=0.025)
par(new=T) 
plot((data$V1), (data$V4), type="o", xlim=c(1,1000), ylim=c(0,0.200000), main="Figure 1: Sort Times Per List Length of Three Sorting Algorithms", xlab="List length", ylab="Time(Seconds)", col="black", pch=19, tck=0.025)
legend(x=15,y=0.15,c("Stooge Sort","Comb Sort","Quick Sort"), lwd=c(1,2,1,2), col=c("blue","red","black"))
dev.off()

png(file="test2.png",width=800,height=400)
plot((data$V1), (data$V3), type="o",xlim=c(1,1000), ylim=c(0,0.00500), main="Figure 2: Comparing Comb Sort to Quick Sort", xlab="List length", ylab="Time(Seconds)", col="red", pch=19, tck=0.025)
par(new=T) 
plot((data$V1), (data$V4), type="o", xlim=c(1,1000), ylim=c(0,0.00500), main="Figure 2: Comparing Comb Sort to Quick Sort", xlab="List length", ylab="Time(Seconds)", col="black", pch=19, tck=0.025)
legend(x=15,y=0.004,c("Comb Sort","Quick Sort"), lwd=c(1,2,1,2), col=c("red","black"))
dev.off()



