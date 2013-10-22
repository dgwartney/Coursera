count <- function(cause = NULL) {
  ## Check that "cause" is non-NULL; else throw error
  if (is.null(cause)) {
    stop()
  }
  
  ## Check that specific "cause" is allowed; else throw error
  acceptable_causes = c('asphyxiation','blunt force','other','shooting', 'stabbing','unknown')
  if (any(acceptable_causes == cause))
  ## Read "homicides.txt" data file
  homicides <- readLines('homicides.txt')
  ## Extract causes of death
  homicide_count <- 0
  if (cause == 'asphyxiation') {
    homicide_count <- length(grep('Cause: [Aa]sphyxiation',homicides))
  } else if (cause == 'blunt force') {
    
  } else if (cause == 'other') {
    
  } else if (cause == 'shooting') {
    homicide_count <- length(grep('Cause: [Ss]hooting',homicides))
  } else if (cause == 'stabbing') {
    homicide_count <- length(grep('Cause: [Ss]tabbing',homicides))
  } else if (cause == 'unknown') {
    
  }
  else {
    stop()
  }

  ## Return integer containing count of homicides for that cause
  return(homicide_count)
}