agecount <- function(age = NULL) {
  ## Check that "age" is non-NULL; else throw error
  if (is.null(age)) {
    stop()
  }
  
  ## Read "homicides.txt" data file
  homicides <- readLines('homicides.txt')

  ## Extract ages of victims; ignore records where no age is
  ## given
  r <- regexec('([1-9][1-9])+ years old',homicides)
  l <- regmatches(homicides,r)
  
  homicide_count_for_age <- 0
  for (h in l) {
    if (!is.na(h[2]) && as.integer(h[2]) == age) {
      homicide_count_for_age <- homicide_count_for_age + 1
    }
  }
  
  ## Return integer containing count of homicides for that age
  return(homicide_count_for_age)
}
