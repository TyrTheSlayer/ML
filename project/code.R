#Aedan Wells and Samuel nix
#SML and ML
setwd("~/ML/project/")

data = read.csv("Weather.csv")

plot(data$tempm, data$precipi)
colnames(data)

data2 = data[,c("tempm", "dewptm", "hum", "wspdm", "vism", "pressurem", "windchillm", "precipm")]
data2[is.na(data2)] <- 0
X = scale(data2)
h1 <-  heatmap(scale(data2), distfun = dist, keep.dendro = T)
