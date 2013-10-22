reg <- '^([a-z]+) +\1 +[a-z]+ [0-9]'
s <-c('night night at 8','going up and up and up','bye bye from up high','heading, heading by 9')
s
i <- grep('^([a-z]+) +\1 +[a-z]+ [0-9]',s)

reg2 <- '^s(.*?)r'
regexec(reg2,'she likes rum raisin after running hard')