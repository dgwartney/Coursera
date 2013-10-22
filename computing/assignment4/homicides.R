homicides <- readLines('homicides.txt')

length(grep('iconHomicideShooting',homicides))
length(grep('iconHomicideShooting|icon_homicide_shooting',homicides))
length(grep('Cause: shooting',homicides))
length(grep('Cause: [Ss]hooting',homicides))
length(grep('[Ss]hooting',homicides))

i <- grep('[Cc]ause: [Ss]hooting',homicides)
j <- grep('[Ss]hooting',homicides)

setdiff(i,j)
setdiff(j,i)
       