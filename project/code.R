#Aedan Wells and Samuel nix
#SML and ML
setwd("~/ML/project/")

al_ga = read.csv("data/monthly-al-ga.csv")
hi_md = read.csv("data/monthly-hi-md.csv")
ma_nj = read.csv("data/monthly-ma-nj.csv")
nm_sc = read.csv("data/monthly-nm-sc.csv")
sd_wy = read.csv("data/monthly-sd-wy.csv")


data = rbind(al_ga[-1,], hi_md[-1,])
data = rbind(data, ma_nj[-1,])
data = rbind(data, nm_sc[-1,])
data = rbind(data, sd_wy[-1,])

data2 = data[,c("MonthlyMeanTemperature", "MonthlyStationPressure")]
data2[is.na(data2)] <- 0
h1 <-  heatmap(scale(data2), distfun = dist, keep.dendro = T)


######################### NY Dataset code ####################
#data = read.csv("Weather.csv")

#plot(data$tempm, data$precipi)
#colnames(data)

#data2 = data[,c("tempm", "dewptm", "hum", "wspdm", "vism", "pressurem", "windchillm", "precipm")]
#data2[is.na(data2)] <- 0
#X = scale(data2)
#h1 <-  heatmap(scale(data2), distfun = dist, keep.dendro = T)
