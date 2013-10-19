# Digital Tranfer Function Example
# from pages 333 - 337 of Engineering Problem Solving with Matlab
# D.M. Etter, Prentice Hall 1993

# Compute and plot digital transfer functions
library(signal)
data(package="signal") # to see the data sets availale in the package signal
ls("package:signal")   # to list all of the objects in signal
lsf.str("package:signal") # to list all of the functions in signal


# Filter H1(z)
B1 <- c(0.2066,0.4131,0.2066)	# Coefficients of numerator polynomial
A1 <- c(1,-0.3695,0.1958) # Coefficients of denominator polynomial
H1z <- freqz(B1,A1,100)	 # Compute the transfer function

# Filter H2(z)
B2 <- c(0.894,-1.789,0.894)
A2 <- c(1,-1.788,0.799)
H2z <- freqz(B2,A2,100)

# Filter H3(z)
B3 <- c(0.42,0,-0.42)
A3 <- c(1,-0.443,0.159)
H3z <- freqz(B3,A3,100)

# Filter h4(z)
B4 <- c(0.5972,0.4425,0.5972)
A4 <- c(1,0.4425,0.1584)
H4z <- freqz(B4,A4,100)

# Convenience function to draw multiple plots
hPlot <- function(H){
  text <- deparse(substitute(H)) # get the name of the filter for the title
  c <- substr(text,4,4)
  plot(H$f,abs(H$h),
       col="red",
       ylim=c(0,1),
       xlab="Normalized Frequency",
       ylab="Magnitude",
       main=paste("Filter H",c,"(z)",sep="")
  )
}

par(mfrow=c(2,2))
plotList <- list(H1z,H2z,H3z,H4z)
lapply(plotList,hPlot)
#
plot(H4z)	 # Look at the default plot
