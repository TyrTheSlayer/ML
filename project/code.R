#Aedan Wells and Samuel nix
#SML and ML
setwd("~/ML/project/")

temp = read.csv("data/monthly-mean-temp.csv")
min_temp = read.csv("data/monthly-min-temp.csv")
max_temp = read.csv("data/monthly-max-temp.csv")
greatest_precip = read.csv("data/monthly-greatest-precip.csv")
pressure = read.csv("data/monthly-station-pressure.csv")
snowfall = read.csv("data/monthly-total-snowfall.csv")

combo.temp_precip = merge(temp[,-1], greatest_precip[,-1], by= "state")
combo.min_max_temp = merge(max_temp[,-1], min_temp[,-1], by= "state")
combo.all_temp = merge(combo.min_max_temp, temp[,-1], by= "state")
print(combo.all_temp[2:37])

print(combo.temp_precip[2:25])

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

h2 <- heatmap(scale(combo.temp_precip[2:25]), distfun = dist, keep.dendro = T,labRow = temp$state, 
              main="Cluster on mean/precipitation", xlab = "Month")
h3 <- heatmap(scale(combo.all_temp[2:37]), distfun = dist, keep.dendro = T,labRow = combo.all_temp$state, 
              main="Cluster on all temp", xlab = "Month")

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

mean_precip_tree = hclust(dist(scale(combo.temp_precip[2:25])), "ave")
plot(mean_precip_tree, labels = combo.temp_precip$state, main = "Mean temp/precipitation Dendrogram")

all_temp_tree = hclust(dist(scale(combo.all_temp[2:37])), "ave")
plot(all_temp_tree, labels = combo.all_temp$state, main = "All Temp Dendrogram")
###############KMeans#################
K = 5

#temp
km1 = kmeans(scale(temp[3:14]), K, nstart = 5)
clust=km1$cluster
for (i in 1:K) {
  print(i)
  print(temp$state[km1$cluster == i])
}
#table(temp$state, clust)

#min temp
km2 = kmeans(scale(min_temp[3:14]),K, nstart = 10)
clust=km2$cluster
#table(temp$state, clust)
for (i in 1:K) {
  print(i)
  print(min_temp$state[km2$cluster == i])
}

#max temp
km3 = kmeans(scale(max_temp[3:14]),K, nstart = 10)
clust=km3$cluster
#table(temp$state, clust)
for (i in 1:K) {
  print(i)
  print(max_temp$state[km3$cluster == i])
}

#greatest precip
km4 = kmeans(scale(greatest_precip[3:14]),K, nstart = 10)
clust=km4$cluster
#table(temp$state, clust)
for (i in 1:K) {
  print(i)
  print(greatest_precip$state[km4$cluster == i])
}

#pressure
km5 = kmeans(scale(pressure[3:14]),K, nstart = 10)
clust=km5$cluster
#table(temp$state, clust)
for (i in 1:K) {
  print(i)
  print(pressure$state[km5$cluster == i])
}

#snowfall
km6 = kmeans(scale(min_temp[3:14]),K, nstart = 10)
clust=km6$cluster
#table(temp$state, clust)
for (i in 1:K) {
  print(i)
  print(pressure$state[km6$cluster == i])
}

######################### NY Dataset code ####################
#data = read.csv("Weather.csv")

#plot(data$tempm, data$precipi)
#colnames(data)

#data2 = data[,c("tempm", "dewptm", "hum", "wspdm", "vism", "pressurem", "windchillm", "precipm")]
#data2[is.na(data2)] <- 0
#X = scale(data2)
#h1 <-  heatmap(scale(data2), distfun = dist, keep.dendro = T)
