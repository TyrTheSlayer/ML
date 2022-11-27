library(ggplot2)

read.table(text="region  colors
          1   alabama            #f7931e
          2   arizona            #f7931e
          3   arkansas           #4a77bb
          4   california           #787878
          5   colorado            #d3dfbd
          6   connecticut            #f7931e
          7    delaware            #f7931e
          8    florida            #f7931e
          9    georgia            #f7931e
          11    idaho            #f7931e
          12    illinois            #f7931e
          13    indiana            #f7931e
          14    iowa            #f7931e
          15    kansas            #f7931e
          16    kentucky            #f7931e
          17    louisiana           #f7931e
          18    maine            #f7931e
          19    maryland            #f7931e
          20    massachusetts            #f7931e
          21    michigan            #f7931e
          22    minnesota            #f7931e
          23    mississippi            #f7931e
          24    missouri            #f7931e
          25    montana            #f7931e
          26    nebraska            #f7931e
          27    nevada            #f7931e
          28    new hampshire            #f7931e
          29    new jersey          #f7931e
          30    new mexico            #f7931e
          31    new york            #f7931e
          32    north carolina            #f7931e
          33    north dakota            #f7931e
          34    ohio            #f7931e
          35    oklahoma            #f7931e
          36    oregon            #f7931e
          37    pennsylvania            #f7931e
          38    rhode island            #f7931e
          39    south carolina            #f7931e
          40    south dakota            #f7931e
          41    tennessee            #f7931e
          42    texas            #f7931e
          43    utah            #f7931e
          44    vermont            #f7931e
          45    virginia            #f7931e
          46    washington            #f7931e
          47    west virginia            #f7931e
          48    wisconsin            #f7931e
          49    wyoming            #f7931e", 
           stringsAsFactors=FALSE, header=TRUE, comment.char="") -> df

usa_map <- map_data("state")


gg <- ggplot()
gg <- gg + geom_map(data=usa_map, map=usa_map,
                    aes(long, lat, map_id=region),
                    color="#2b2b2b", size=0.15, fill=NA)
gg <- gg + geom_map(data=df, map=usa_map,
                    aes(fill=colors, map_id=region),
                    color="#2b2b2b", size=0.15)
gg <- gg + scale_color_identity()
gg <- gg + coord_map("polyconic")
gg <- gg + ggthemes::theme_map()
gg

