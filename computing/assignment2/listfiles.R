corr <- function(directory,threshold=0) {
  files <- list.files(path=directory,pattern=".*.csv")
  df <- data.frame(numeric(),numeric())
  names(df) <- c('sulfate','nitrate')
  v <- numeric()
  for (file in files) {
    data_filename <- paste(directory,'/',file,sep="")
    if(!file.exists(data_filename)) {
      stop(paste("File: ",data_files," not found!",sep=""))
    }
    data <- read.csv(data_filename)
    ndata <- subset(data,!is.na(sulfate),select=c(sulfate,nitrate))
    sdata <- subset(ndata,!is.na(nitrate),select=c(sulfate,nitrate))
    names(sdata) <- c('sulfate','nitrate')
    v <- c(v,corr(sdata))
  }
  return(v)
}

