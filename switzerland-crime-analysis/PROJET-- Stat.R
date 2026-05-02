#moyenne et variance du nombre d'habitants par canton



moyenne.habitant=mean(Data2$nombre.d.habitants)
variance.habitant = var(Data2$nombre.d.habitants)

hist(Data2$nombre.d.habitants,
     main="Fréquence des cantons selon le nombre d'habitants",
     xlab="Nombre d'habitants", 
     ylab ="Fréquence des cantons")
boxplot(Data2$nombre.d.habitants,main="Distribution du nombre d'habitants",
        ylab = "Nombre d'habitants")
boxplot(Data2$nombre.d.infractions.habitants, main ="Nombre d'infractions par habitant") # il y a 2 valeurs extremes: ligne 8 et 5

boxplot(Data2$Proportion.de.personnes.dans.le.processus.d.asile, 
        main ="Répartition de la proportion de personnes dans le processus d'asile", 
        ylab ="Proportion de personnes dans le processus d'asile")
boxplot(Data2$PIB.reel..en.milliers.de.CHF..habitants, 
        main= "Distribution du PIB réel en millier de CHF par canton",
        ylab = "PIB réel (en milliers de CHF par habitant)")
boxplot(jeunes$Proportion.des.jeunes.entre.15.et.24.ans)

#moyenne et variance des infractions par canton
moyenne.infraction=mean(Data2$nombre.d.infractions.habitants)
variance.infraction = var(Data2$nombre.d.infractions.habitants)


#nuage de points entre le nombre d'infractions par canton et la 
#proportion des personnes dans le processus d'asiles par canton

plot( Data2$nombre.d.infractions.habitants,Data2$Proportion.de.personnes.dans.le.processus.d.asil, 
      main = "Relation entre la proportion de personnes en processus d'asile et le nombre d'infractions", 
      ylab= "Proportion de personnes en processus d'asile (en %) ", 
      xlab ="Nombre d'infractions par cantons")


#correction du graphe selon l'avis du groupe (nombre d'infraction en fct des proportions de personnes )
plot(Data2$Proportion.de.personnes.dans.le.processus.d.asile , Data2$nombre.d.infractions, 
     main = "Régression linéaire entre le nombre d'infractions et la proportion de personnes en processus d'asile", 
     ylab = "Nombre d'infractions", 
     xlab = "Proportion de personnes en processus d'asile")
regression = lm( Data2$nombre.d.infractions~ Data2$Proportion.de.personnes.dans.le.processus.d.asile)
abline(regression, col ="red")

#nuage de points entre le nombre d'infractions/hab par canton et le PIB/hab. Ce qui est surprenant
# c'est que plus le PIB/hab est grand plus il y a d'infractions/hab

plot(Data2$PIB.reel..en.milliers.de.CHF..habitants, Data2$nombre.d.infractions.habitants, 
     main = "Relation entre le PIB et le nombre d'infraction par habitant", 
     ylab = "Nombre d'infractions par habitant", 
     xlab = "PIB réel en milliers de CHF par habitant")

# régression linéaire entre le nombre d'infractions/hab par canton et le PIB/hab
regression.PIB = lm(Data2$nombre.d.infractions.habitants ~ Data2$PIB.reel..en.milliers.de.CHF..habitants)
plot(Data2$PIB.reel..en.milliers.de.CHF..habitants, Data2$nombre.d.infractions.habitants, 
     main = "Régression linéaire entre le nombre d'infractions par habitants et le PIB par habitants", 
     ylab = "Nombre d'infractions par habitant", 
     xlab = "PIB réel en milliers de CHF par habitants")
abline(regression.PIB, col ="red")

# grande corrélation entre le nombre d'infractions/hab par canton et le PIB/hab
cor.infraction.PIB=cor(Data2$nombre.d.infractions.habitants,Data2$PIB.reel..en.milliers.de.CHF..habitants)

# corrélation entre le nombre d'infractions/hab par canton et la 
#proportion des personnes dans le processus d'asiles par canton

cor.infraction.asile=cor(Data2$Proportion.de.personnes.dans.le.processus.d.asile,Data2$nombre.d.infractions.habitants)
cor.infraction.asile # la corrélation est faible : environ -0.03

#nuage de points entre le nombre d'infractions et proportion asile

plot(Data2$Proportion.de.personnes.dans.le.processus.d.asile, Data2$nombre.d.infractions, 
     main = "Relation entre la proportion de personnes en processus d'asile et le nombre d'infraction", 
     xlab = "Proportion de personnes en processus d'asile", 
     ylab = "Nombre d'infractions")

# corrélation entre le nombre d'infractions par canton et la 
#proportion des personnes dans le processus d'asiles par canton

cor.infraction.asile2=cor(Data2$nombre.d.infractions,Data2$Proportion.de.personnes.dans.le.processus.d.asile)
cor.infraction.asile2 # la corrélation est faible : environ 0.11


#petits cantons 
petits_cantons = Data2[Data2$nombre.d.habitants < 100000,]
petits_cantons
infractions_moyennes_par_hab=mean(petits_cantons$nombre.d.infractions.habitants)
infractions_moyennes_par_hab
moyenne.infraction

grand_cantons = Data2[Data2$nombre.d.habitants >= 100000,]
infractions_moyennes_par_hab_grand_canton=mean(grand_cantons$nombre.d.infractions.habitants)
infractions_moyennes_par_hab_grand_canton

#jeunes et infractions

cor.jeune_infractions = cor(jeunes$nombre.d.infractions.habitants,jeunes$Proportion.des.jeunes.entre.15.et.24.ans)
cor.jeune_infractions # surprenant
plot(jeunes$nombre.d.infractions.habitants,jeunes$Proportion.des.jeunes.entre.15.et.24.ans)

#correction selon le groupe (nbre d'infraction par habitant en fct de la proportion des jeunes )
plot(jeunes$Proportion.des.jeunes.entre.15.et.24.ans ,jeunes$nombre.d.infractions.habitants)
regression = lm( jeunes$nombre.d.infractions.habitants~ jeunes$Proportion.des.jeunes.entre.15.et.24.ans )
abline(regression, col ="red")

# régression linéaire pour jeunes et infraction
regression = lm(jeunes$Proportion.des.jeunes.entre.15.et.24.ans ~ jeunes$nombre.d.infractions.habitants)
plot(jeunes$nombre.d.infractions.habitants, jeunes$Proportion.des.jeunes.entre.15.et.24.ans)
abline(regression, col ="red")

