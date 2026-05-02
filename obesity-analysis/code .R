#the variables we need 
imc_level<-women2$imc_level
age<-women2$age
fhcf<-women2$fhcf
pal<-women2$pal

# Get descriptive statistics for each variable
summary(age)
summary(imc_level)
summary(pal)
summary(fhcf)

# Visualize the distribution of these variables 
hist_var <- function(data, main = "Histogram", xlab = "x value", ylab = "Frequency",breaks=10) {
  data <- na.omit(data)
  
  hist(data,
       main   = main,
       xlab   = xlab,
       ylab   = ylab,
       xlim   = range(data),
       breaks = breaks,
       col    = "hotpink3",
       border = "black")
  
  abline(v = mean(data), col = "gray1", lwd = 2)
}

par(mfrow = c(1, 2)) 
hist_var(age,breaks = 10,main="Histogram of age ")
hist_var(pal,breaks = 15,main="Histogram of pal ")


par(mfrow = c(1, 2)) 
# Create a frequency table for the categorical variable 'fhcf' and 'imc_level'
tab_fhcf <- table(women2$fhcf)
tab_imc_level <- table(women2$imc_level)

#barplot for the variable "fhcf" and "imc_level"
barplot(tab_fhcf,
        main = "barplot fhcf",
        xlab = "fhcf",
        ylab = "frequency",
        col    = "hotpink3",
        border = "black")

barplot(tab_imc_level,
        main = "barplot imc level",
        xlab = "imc level",
        ylab = "frequency",
        col    = "hotpink3",
        border = "black")

#the qqplot function , the same we saw in class
my.qqnorm = function(x) {
  scaled = scale(x, center = mean(x))
  sequence = seq(0.01, 0.99, 0.01)
  normal = qnorm(sequence, 0, 1)
  reel = quantile(scaled, sequence)
  # keep the variable name of 'x' for the title
  variablename = deparse(substitute(x))
  
  plot(normal, reel,
       xlim = c(-3, 3),
       ylim = c(-3, 3),
       main = paste("qqplot:", variablename),
       xlab = "Theoretical quantiles",
       ylab = "Sample quantiles",
       pch  = 16,            # filled points
       col  = "hotpink3")    # same color as histogram
  
  abline(0, 1, col = "gray1", lwd = 2)  # similar style to mean line on histogram
}


par(mfrow = c(1, 3)) 
#annexe
my.qqnorm(age)

my.qqnorm(pal)

my.qqnorm(imc_level)



