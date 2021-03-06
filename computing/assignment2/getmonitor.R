getmonitor <- function(id, directory, summarize = FALSE) {
  ## 'id' is a vector of length 1 indicating the monitor ID
  ## number. The user can specify 'id' as either an integer, a
  ## character, or a numeric.
  
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'summarize' is a logical indicating whether a summary of
  ## the data should be printed to the console; the default is
  ## FALSE
  
  ## Your code here
  data_id <- as.integer(id)
  data_filename <- paste(directory,'/',sprintf("%03d",data_id),'.csv',sep="")
  if(!file.exists(data_filename))
    stop("directory 'specdata' not found; please change your working directory")
  data <- read.csv(data_filename)
  if (summarize == TRUE) {
    print(summary(data))
  }
  return(data)
}