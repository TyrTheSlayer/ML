#Aedan Wells and Samuel nix
#SML and ML
setwd("~/ML/project/")

library("gplots")
require("RColorBrewer")

#read in data
temp = read.csv("data/monthly-mean-temp.csv")
min_temp = read.csv("data/monthly-min-temp.csv")
max_temp = read.csv("data/monthly-max-temp.csv")
greatest_precip = read.csv("data/monthly-greatest-precip.csv")
pressure = read.csv("data/monthly-station-pressure.csv")
snowfall = read.csv("data/monthly-total-snowfall.csv")
total_precip =read.csv("data/monthly-total-liquid-precip.csv")
labels = read.csv("data/labels3.csv")

rownames(total_precip) = total_precip$state

combo.all_temp = merge(labels, combo.all_temp, by= "state")
########## TEST
#Ward Algorithm
rownames(combo.all_temp) = combo.all_temp$state
all_ward = hclust(dist(scale(combo.all_temp[3:37])), method="ward.D")
plot(as.dendrogram(all_ward),  main = "Dendrogram Ward Algo")
rect.hclust(all_ward, k = 7, border = 3:4)
rownames(combo.all_temp) = combo.all_temp$label
all_ward = hclust(dist(scale(combo.all_temp[3:37])), method="ward.D")
plot(as.dendrogram(all_ward),  main = "Dendrogram Ward Algo")
rect.hclust(all_ward, k = 7, border = 3:4)

#combine/merge datasets
#mean temp/greatest precip
combo.temp_precip = merge(temp[,-1], greatest_precip[,-1], by= "state")
#min/max temp
combo.min_max_temp = merge(max_temp[,-1], min_temp[,-1], by= "state")
#all temp values
combo.all_temp = merge(combo.min_max_temp, temp[,-1], by= "state")
#all temp and greatest precip
temp_precip = merge(combo.all_temp, greatest_precip[,-1], by= "state")
#all temp and both precipitates type
temp = merge(temp_precip, total_precip[,-1], by= "state")
twoprecip_temp = merge(labels, temp, by= "state")

all = merge(twoprecip_temp, snowfall[,-1], by="state")
#

################### all things ####################
#average distance between clusters
rownames(all) = all$state
all_ave = hclust(dist(scale(all[3:74])), method="average")
plot(as.dendrogram(all_ave),  main = "Dendrogram Average dist")
rect.hclust(all_ave, k = 14, border = 3:4)
rownames(all) = all$label
all_ave = hclust(dist(scale(all[3:74])), method="average")
plot(as.dendrogram(all_ave),  main = "Dendrogram Average dist")
rect.hclust(all_ave, k = 14, border = 3:4)
#min distance between clusters
rownames(all) = all$state
all_min = hclust(dist(scale(all[3:74])), method="single")
plot(as.dendrogram(all_min),  main = "Dendrogram Min dist")
rect.hclust(all_min, k = 14, border = 3:4)
rownames(all) = all$label
all_min = hclust(dist(scale(all[3:74])), method="single")
plot(as.dendrogram(all_min),  main = "Dendrogram Min dist")
rect.hclust(all_min, k = 14, border = 3:4)
#max distance between clusters
rownames(all) = all$state
all_max = hclust(dist(scale(all[3:74])), method="complete")
plot(as.dendrogram(all_max),  main = "Dendrogram Max dist")
rect.hclust(all_max, k = 14, border = 3:4)
rownames(all) = all$label
all_max = hclust(dist(scale(all[3:74])), method="complete")
plot(as.dendrogram(all_max),  main = "Dendrogram Max dist")
rect.hclust(all_max, k = 14, border = 3:4)
#centroid distance between clusters
rownames(all) = all$state
all_centroid = hclust(dist(scale(all[3:74])), method="centroid")
plot(as.dendrogram(all_centroid),  main = "Dendrogram Centroid dist")
rect.hclust(all_centroid, k = 14, border = 3:4)
rownames(all) = all$label
all_centroid = hclust(dist(scale(all[3:74])), method="centroid")
plot(as.dendrogram(all_centroid),  main = "Dendrogram Centroid dist")
rect.hclust(all_centroid, k = 14, border = 3:4)
#centroid  mediandistance between clusters
rownames(all) = all$state
all_median = hclust(dist(scale(all[3:74])), method="median")
plot(as.dendrogram(all_median),  main = "Dendrogram Median dist")
rect.hclust(all_median, k = 14, border = 3:4)
rownames(all) = all$label
all_median = hclust(dist(scale(all[3:74])), method="median")
plot(as.dendrogram(all_median),  main = "Dendrogram Median dist")
rect.hclust(all_median, k = 14, border = 3:4)
#Ward Algorithm
rownames(all) = all$state
all_ward = hclust(dist(scale(all[3:74])), method="ward.D")
plot(as.dendrogram(all_ward),  main = "Dendrogram Ward Algo")
rect.hclust(all_ward, k = 14, border = 3:4)
rownames(all) = all$label
all_ward = hclust(dist(scale(all[3:74])), method="ward.D")
plot(as.dendrogram(all_ward),  main = "Dendrogram Ward Algo")
rect.hclust(all_ward, k = 14, border = 3:4)

all[, c('snow5', 'snow6','snow7', 'snow8', 'snow9')] <- list(NULL)

###################### 7 groups #################
#average distance between clusters
rownames(all) = all$state
all_ave = hclust(dist(scale(all[3:74])), method="average")
plot(as.dendrogram(all_ave),  main = "Dendrogram Average dist")
rect.hclust(all_ave, k = 7, border = 3:4)
rownames(all) = all$label
all_ave = hclust(dist(scale(all[3:74])), method="average")
plot(as.dendrogram(all_ave),  main = "Dendrogram Average dist")
rect.hclust(all_ave, k = 7, border = 3:4)
#min distance between clusters
rownames(all) = all$state
all_min = hclust(dist(scale(all[3:74])), method="single")
plot(as.dendrogram(all_min),  main = "Dendrogram Min dist")
rect.hclust(all_min, k = 7, border = 3:4)
rownames(all) = all$label
all_min = hclust(dist(scale(all[3:74])), method="single")
plot(as.dendrogram(all_min),  main = "Dendrogram Min dist")
rect.hclust(all_min, k = 7, border = 3:4)
#max distance between clusters
rownames(all) = all$state
all_max = hclust(dist(scale(all[3:74])), method="complete")
plot(as.dendrogram(all_max),  main = "Dendrogram Max dist")
rect.hclust(all_max, k = 7, border = 3:4)
rownames(all) = all$label
all_max = hclust(dist(scale(all[3:74])), method="complete")
plot(as.dendrogram(all_max),  main = "Dendrogram Max dist")
rect.hclust(all_max, k = 7, border = 3:4)
#centroid distance between clusters
rownames(all) = all$state
all_centroid = hclust(dist(scale(all[3:74])), method="centroid")
plot(as.dendrogram(all_centroid),  main = "Dendrogram Centroid dist")
rect.hclust(all_centroid, k = 7, border = 3:4)
rownames(all) = all$label
all_centroid = hclust(dist(scale(all[3:74])), method="centroid")
plot(as.dendrogram(all_centroid),  main = "Dendrogram Centroid dist")
rect.hclust(all_centroid, k = 7, border = 3:4)
#centroid  mediandistance between clusters
rownames(all) = all$state
all_median = hclust(dist(scale(all[3:74])), method="median")
plot(as.dendrogram(all_median),  main = "Dendrogram Median dist")
rect.hclust(all_median, k = 7, border = 3:4)
rownames(all) = all$label
all_median = hclust(dist(scale(all[3:74])), method="median")
plot(as.dendrogram(all_median),  main = "Dendrogram Median dist")
rect.hclust(all_median, k = 7, border = 3:4)
#Ward Algorithm
rownames(all) = all$state
all_ward = hclust(dist(scale(all[3:74])), method="ward.D")
plot(as.dendrogram(all_ward),  main = "Dendrogram Ward Algo")
rect.hclust(all_ward, k = 7, border = 3:4)
rownames(all) = all$label
all_ward = hclust(dist(scale(all[3:74])), method="ward.D")
plot(as.dendrogram(all_ward),  main = "Dendrogram Ward Algo")
rect.hclust(all_ward, k = 7, border = 3:4)

###############KMeans#################
K = 7
print(all)

all_temp = kmeans(scale(all[3:69]), K, nstart = 5)
clust=all_temp$cluster
for (i in 1:K) {
  print(i)
  print(all$label[all_temp$cluster == i])
}
##PCA
all_temp_precip.pca = prcomp(scale(all[3:69]))
summary(all_temp_precip.pca)
str(all_temp_precip.pca)
biplot(all_temp_precip.pca)

#Total Precipitation
K = 7
big_precip = kmeans(scale(twoprecip_temp[3:61]), K, nstart = 5)
clust=big_precip$cluster
for (i in 1:K) {
  print(i)
  print(twoprecip_temp$state[big_precip$cluster == i])
}

#2 Precipitation and temp
K = 7
big_precip = kmeans(scale(total_precip[3:14]), K, nstart = 5)
clust=big_precip$cluster
for (i in 1:K) {
  print(i)
  print(total_precip$state[big_precip$cluster == i])
}

#temp + precip
K = 7
temp_precip_kmean = kmeans(scale(temp_precip[2:49]), K, nstart = 5)
clust=temp_precip_kmean$cluster
for (i in 1:K) {
  print(i)
  print(temp_precip$state[temp_precip_kmean$cluster == i])
}
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
km4 = kmeans(scale(greatest_precip[3:14]),K, nstart = 5)
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

################## PCA #################

#All temp and both precipitations
all_temp_precip.pca = prcomp(scale(twoprecip_temp[3:61]))
summary(all_temp_precip.pca)
str(all_temp_precip.pca)
biplot(all_temp_precip.pca)

#just total precipitation
total_precip.pca = prcomp(scale(total_precip[3:14]))
summary(total_precip.pca)
str(total_precip.pca)
biplot(total_precip.pca, main = "Total precipitation")

#total temp
temp.pca = prcomp(scale(combo.all_temp[2:37]))
summary(temp.pca)
str(temp.pca)
biplot(temp.pca, main = "All Temp")



############## Depricated code no longer wanted to use ##########

#make the indices state names

rownames(combo.all_temp) = combo.all_temp$state
rownames(temp_precip) = temp_precip$state

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

##Tree Exploration, all temp
par(mar=c(7,5,4,2)+0.1,mgp=c(5,1,0))
#average distance between clusters
all_temp_ave = hclust(dist(scale(combo.all_temp[2:37])), method="average")
plot(as.dendrogram(all_temp_ave),  main = "All Temp Dendrogram Average dist")
rect.hclust(all_temp_ave, k = 7, border = 3:4)
#min distance between clusters
all_temp_min = hclust(dist(scale(combo.all_temp[2:37])), method="single")
plot(as.dendrogram(all_temp_min),  main = "All Temp Dendrogram Min Cluster Dist")
rect.hclust(all_temp_min, k = 7, border = 3:4)
#max distance between clusters
all_temp_max = hclust(dist(scale(combo.all_temp[2:37])), method="complete")
plot(as.dendrogram(all_temp_max),  main = "All Temp Dendrogram Max Cluster Dist")
rect.hclust(all_temp_max, k = 7, border = 3:4)
#centroid distance between clusters
all_temp_centroid = hclust(dist(scale(combo.all_temp[2:37])), method="centroid")
plot(as.dendrogram(all_temp_centroid),  main = "All Temp Dendrogram Centroid Dist")
rect.hclust(all_temp_centroid, k = 7, border = 3:4)
#median centroid distance between clusters
all_temp_median = hclust(dist(scale(combo.all_temp[2:37])), method="median")
plot(as.dendrogram(all_temp_median),  main = "All Temp Dendrogram median Centroid Dist")
rect.hclust(all_temp_median, k = 7, border = 3:4)
#ward distance between clusters
all_temp_ward = hclust(dist(scale(combo.all_temp[2:37])), method="ward.D")
plot(as.dendrogram(all_temp_ward),  main = "All Temp Dendrogram Ward Dist")
rect.hclust(all_temp_ward, k = 7, border = 3:4)
#ward distance2 between clusters
all_temp_ward2 = hclust(dist(scale(combo.all_temp[2:37])), method="ward.D2")
plot(as.dendrogram(all_temp_ward2),  main = "All Temp Dendrogram Ward Dist2")
rect.hclust(all_temp_ward2, k = 7, border = 3:4)

#All temp plus precipitation
#ward distance between clusters
temp_precip_tree = hclust(dist(scale(temp_precip[2:49])), method="ward.D")
plot(as.dendrogram(temp_precip_tree),  main = "Temp and Precipitation")
rect.hclust(temp_precip_tree, k = 7, border = 3:4)
#Ward2
temp_precip_tree = hclust(dist(scale(temp_precip[2:49])), method="ward.D2")
plot(as.dendrogram(temp_precip_tree),  main = "Temp and Precipitation Ward 2")
rect.hclust(temp_precip_tree, k = 7, border = 3:4)

#Just precipitation
rownames(greatest_precip) <- greatest_precip$state
precip_tree = hclust(dist(scale(greatest_precip[3:14])), method="ward.D")
plot(as.dendrogram(precip_tree),  main = "Precipitation")
rect.hclust(precip_tree, k = 7, border = 3:4)

#total Precip
rownames(total_precip) <-total_precip$state
total_precip_tree = hclust(dist(scale(total_precip[3:14])), method="ward.D")
plot(as.dendrogram(total_precip_tree),  main = "Total Precipitation")
rect.hclust(total_precip_tree, k = 7, border = 3:4)

#2 precips and all temps
rownames(twoprecip_temp) = twoprecip_temp$state
total_precip_tree = hclust(dist(scale(twoprecip_temp[3:62])), method="ward.D")
plot(as.dendrogram(total_precip_tree),  main = "Total/greatest Precip and Temp")
rect.hclust(total_precip_tree, k = 14, border = 3:4)
#cluster with labels to see what is there or not there
rownames(twoprecip_temp) = twoprecip_temp$label
total_precip_tree = hclust(dist(scale(twoprecip_temp[3:62])), method="ward.D")
plot(as.dendrogram(total_precip_tree),  main = "Total/greatest Precip and Temp")
rect.hclust(total_precip_tree, k = 14, border = 3:4)

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
######################### NY Dataset code ####################
#data = read.csv("Weather.csv")

#plot(data$tempm, data$precipi)
#colnames(data)

#data2 = data[,c("tempm", "dewptm", "hum", "wspdm", "vism", "pressurem", "windchillm", "precipm")]
#data2[is.na(data2)] <- 0
#X = scale(data2)
#h1 <-  heatmap(scale(data2), distfun = dist, keep.dendro = T)
