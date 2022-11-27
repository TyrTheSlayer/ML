#Aedan Wells and Samuel nix
#SML and ML
setwd("~/ML/project/")

temp = read.csv("data/monthly-mean-temp.csv")
min_temp = read.csv("data/monthly-min-temp.csv")
max_temp = read.csv("data/monthly-max-temp.csv")
greatest_precip = read.csv("data/monthly-greatest-precip.csv")
pressure = read.csv("data/monthly-station-pressure.csv")
snowfall = read.csv("data/monthly-total-snowfall.csv")

#heatmaps
h1 <-  heatmap(scale(temp[3:14]), distfun = dist, keep.dendro = T,labRow = temp$state, 
               main="Cluster on Mean Temp", xlab = "Month")
h1 <-  heatmap(scale(min_temp[3:14]), distfun = dist, keep.dendro = T,labRow = temp$state, 
               main="Cluster on Min Temp", xlab = "Month")
h1 <-  heatmap(scale(max_temp[3:14]), distfun = dist, keep.dendro = T,labRow = temp$state, 
               main="Cluster on Max Temp", xlab = "Month")
h1 <-  heatmap(scale(greatest_precip[3:14]), distfun = dist, keep.dendro = T,labRow = temp$state, 
               main="Cluster on Greatest Precip", xlab = "Month")
h1 <-  heatmap(scale(pressure[3:14]), distfun = dist, keep.dendro = T,labRow = temp$state, 
               main="Cluster on Station Pressure", xlab = "Month")
h1 <-  heatmap(scale(snowfall[3:14]), distfun = dist, keep.dendro = T,labRow = temp$state, 
               main="Cluster on Snowfall", xlab = "Month")


#Basic Trees
mean_tree = hclust(dist(scale(temp[3:14])), "ave")
plot(mean_tree, labels = temp$state, main = "Mean Temp Dendrogram")
min_tree = hclust(dist(scale(min_temp[3:14])), "ave")
plot(min_tree, labels = temp$state, main = "Min Temp Dendrogram")
max_tree = hclust(dist(scale(max_temp[3:14])), "ave")
plot(max_tree, labels = temp$state, main = "Max Temp Dendrogram")
precip = hclust(dist(scale(greatest_precip[3:14])), "ave")
plot(precip, labels = temp$state, main = "Greatest Precip. Dendrogram")
pressure_tree = hclust(dist(pressure[3:14]), "ave")
plot(pressure_tree, labels = pressure$state, main = "Pressure Dendrogram")

snowfall_tree = hclust(dist(scale(snowfall[3:14])), "ave")
plot(snowfall_tree, labels = snowfall$state, main = "snowfall Dendrogram")

######################### NY Dataset code ####################
#data = read.csv("Weather.csv")

#plot(data$tempm, data$precipi)
#colnames(data)

#data2 = data[,c("tempm", "dewptm", "hum", "wspdm", "vism", "pressurem", "windchillm", "precipm")]
#data2[is.na(data2)] <- 0
#X = scale(data2)
#h1 <-  heatmap(scale(data2), distfun = dist, keep.dendro = T)
