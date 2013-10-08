complete <- function(directory, id = 1:332) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used
  
  ## Return a data frame of the form:
  ## id nobs
  ## 1  117
  ## 2  1041
  ## ...
  ## where 'id' is the monitor ID number and 'nobs' is the
  ## number of complete cases
  
  df <- data.frame(character(),integer())
  names(df) <- c('id','nobs')
  for (data_id in id) {
    print(id)
    data_filename <- paste(directory,'/',sprintf("%03d",data_id),'.csv',sep="")
    if(!file.exists(data_filename)) {
      stop("directory 'specdata' not found; please change your working directory")
    }
    data <- read.csv(data_filename)
    sdata <- subset(data,TRUE,id)
    row <- data.frame(as.integer(data_id),nrow(sdata))
    names(row) <- c('id','nobs')
    rbind(df,row)
  }
  return (df)
}