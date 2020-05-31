require(ggplot2)
require(reshape2)
require(dplyr)


df18 <- read.csv("2018.csv")
df19 <- read.csv("2019.csv")

head(df18)
head(df19)

names(df18)
names(df19)

str(df18)
str(df19)

subset(df18,is.na(Perceptions.of.corruption))

# Difference between ranks in 2018 and 2019 between coutnires
df1<-merge(df18[,c(1,2)],
           df19[,c(1,2)],
           by.x = "Country",
           by.y = "Country")

df1


# Top 10 countries in 2019 by Happiness Score
data_Top_10 <- df19[with(df19,order(-Score)),]

data_Top_10 <- data_Top_10[1:10, 1:4]

data_Top_10



# Average Happiness Score by Region in 2019
my.summary <- with(df19, aggregate(list(Score), by = list(Region), 
                                      FUN = function(x) { mon.mean = mean(x, na.rm = TRUE) } ))

my.summary <- do.call(data.frame, my.summary)
colnames(my.summary) <- c("Region", "Score")
my.summary

my.data <- merge(df19, my.summary, by = "Region")
my.data


ggplot(my.summary, aes(reorder(x = Region, -Score), y = Score, fill = Region)) +
  geom_col() + 
  ggtitle("Average Happiness Score by Region in 2019") +
  geom_bar(stat = "identity") +
  theme( axis.text.x=element_blank()) +
  geom_text(aes(label = sprintf("%1.2f", Score)), vjust = -0.2) +
  ylim(0, max(my.summary$Score) * 1.05) 



# Overall Rank vs Happiness Score in 2019
ggplot(df19,aes(x=Overall.rank,y=Score,color=Region)) + geom_point() + 
  ggtitle("Overall Rank vs Happiness Score in 2019")



# Regions with their Perceptions of Coruption in 2019
ggplot(df19,aes(x = GDP.per.capita, y = Perceptions.of.corruption, color = Region)) + geom_point() +
  facet_wrap(~Region, shrink = TRUE) +
  ggtitle("Perception of Corruption by Region in 2019") +
  theme(strip.text = element_text(size = 8)) 



# Regression of Life Expectancy Vs Happiness Score by Region in 2019
ggplot(df19,aes(x = Healthy.life.expectancy,y = Score)) + geom_point(aes(color=Region), size = 2, alpha = 0.5) +
  geom_smooth(aes(color = Country,fill = Region), method="lm", fullrange = T) + 
  facet_wrap(Region~.) + 
  ggtitle("Regression of Life Expectancy Vs Happiness Score by Region in 2019") +
  theme(strip.text = element_text(size = 8)) 



# Countries with highest and lowest Economy GDP per capita in 2018
maxGdp <- max(df18$GDP.per.capita)
subset(df18[c(2,5)], GDP.per.capita == maxGdp) 


minGdp <- min(df18$GDP.per.capita)
subset(df18[c(2,5)], GDP.per.capita == minGdp)


# Countries with highest and lowest Economy GDP per capita in 2019
maxGdp <- max(df19$GDP.per.capita)
subset(df19[c(2,5)], GDP.per.capita == maxGdp) 


minGdp <- min(df19$GDP.per.capita)
subset(df19[c(2,5)], GDP.per.capita == minGdp) 



# Countries with highest and lowest Social Support in 2018
maxFamily <- max(df18$Social.support)
subset(df18[c(2,6)],Social.support == maxFamily) 

minFamily <- min(df18$Social.support)
subset(df18[c(2,6)],Social.support == minFamily) 



## Countries with highest and lowest Social Support in 2019
maxFamily <- max(df19$Social.support)
subset(df19[c(2,6)],Social.support == maxFamily)

minFamily <- min(df19$Social.support)
subset(df19[c(2,6)],Social.support == minFamily) 



# Is there is a correlation between Region and Freedom to make life choices? - No
head(subset(df19[,c("Region", "Freedom.to.make.life.choices")])) 

# We have multiple Regions which are same. so we need to take average of the regions that are same (using aggregate function)
dfRegFre <- aggregate(df19[,c("Freedom.to.make.life.choices")], list(df19$Region), mean)

names(dfRegFre) <- c("Region","Freedom.to.make.life.choices") 
dfRegFre



# Is there is correlation between Happiness score and GDP per capita of the countries?
dfHapp_vs_Gdp <- (subset(df19[,c("Country","Score","GDP.per.capita")])) 
names(dfHapp_vs_Gdp) <- c("Country","Score","GDP.per.capita")
head(dfHapp_vs_Gdp)


plot(dfHapp_vs_Gdp)


# Correlation between Happiness score and GDP per capita in 2019
plot(df19$Score, df19$GDP.per.capita, col ="red", type = "p", pch = 8, 
     main = "Correlation between Happiness score and GDP per capita in 2019", las = 1, 
     xlab = "Score", ylab = "GDP per capita") # This shows positive correlation


# Linear regression model 
simple.Regresssion <- lm(df19$GDP.per.capita ~ df19$Score)
summary(simple.Regresssion) 
# R-square = 0.63, p <0.05 shows there is significant correlation between both happiness and economy of the country

# Adding regression line
abline(lm(df19$GDP.per.capita~df19$Score), col = "blue", lwd = 2) 



# Multiple Regression
df <- df19[c("Score","GDP.per.capita","Generosity")]
head(df)

plot(df)

multiple.Regresssion <- lm(df19$GDP.per.capita ~ df19$Score + df19$Generosity)
summary(multiple.Regresssion)


# Since pvalue < 0.05 and adjusted R-Square is 0.65. it means that GPD per capita and Happiness score, Generosity have 
# direct linear relationship between them


generosity_vs_happiness <- df19[c("Region", "Score", "Generosity")]

ggplot(generosity_vs_happiness, 
       aes(x = Score, 
           y = Generosity)) +
  geom_point(aes(colour = Region),
             size = 2) +
  geom_smooth(method="lm") +
  labs(x = "Score",
       y = "Generosity",
       title = "Are happier countries more generous?",
       subtitle = "Generosity and Happiness Score by Region in 2019")


# Graph shows that Western Europe countries are happy and are more Generous, on the other 
# hand Sub-saharan people are less happy and less generous.




# Correlation matrix
selected.table = df19[,c(4:9)]
head(selected.table)

cor.matrix = cor(selected.table)                                                                                                                    
cor.matrix.rotate = apply(cor.matrix, 2, rev)  
print(cor.matrix.rotate)

expand.cor = cbind(expand.grid(rownames(cor.matrix.rotate),                                                                                                   
                               colnames(cor.matrix.rotate)),                                                                                                  
                   value = matrix(cor.matrix.rotate, ncol=1))
print(head(expand.cor))


p.cor = ggplot(data=expand.cor, aes(x = Var1, y = Var2, fill = value)) +                                                                                            
  geom_tile() + scale_x_discrete(position = "top") +                                                                                                      
  xlab(NULL) + ylab(NULL) +                                                                                                                             
  scale_fill_gradient2(low = "blue", high = "red", mid = "white",                                                                                       
                       midpoint = 0, limit = c(-1,1), space = "Lab",                                                                                    
                       name = "correlation")

p.cor

# Finding 1: Social Support and GDP per capita have the highest correlation with happiness score and generosity 
# has the least correaltion with the score.
#  2: There are correlations between variables which may lead to collinearity problem. 



# Boxplot
boxplot(df18$Score ~ df18$Region, xlab = "Region", ylab = "Happiness Score", main = "Boxplot of Happiness Score by Region for 2018")

boxplot(df19$Score ~ df19$Region, xlab = "Region", ylab = "Happiness Score", main = "Boxplot of Happiness Score by Region for 2019")



# Croatia and Ireland rank and score 2018 vs 2019
df2 <-merge(df18[,],
           df19[,],
           by.x = "Country",
           by.y = "Country")

df2


b <- df2 %>% 
  filter(Country %in% c("Croatia","Ireland")) %>% 
  select(Country, Region.x, Score.x, Region.y, Overall.rank.x, Year.x, Score.y, Overall.rank.y, Year.y)

b


# Happiness Score in Croatia and Ireland in 2018
ggplot(b, aes(x = Country, y = Score.x, fill = Year.x)) +
  geom_col(width = 0.5, position = "dodge") + 
  ggtitle("Happiness Score in Croatia and Ireland in 2018") +
  geom_text(aes(label = Score.x), vjust = -0.2) +
  ylim(0, max(b$Score.x) * 1.05) 



# Happiness Score in Croatia and Ireland in 2019
ggplot(b, aes(x = Country, y = Score.y, fill = Year.y)) +
  geom_col(width = 0.5, position = "dodge") + 
  ggtitle("Happiness Score in Croatia and Ireland in 2019") +
  geom_text(aes(label = Score.y), vjust = -0.2) +
  ylim(0, max(b$Score.y) * 1.05) 




