



rankall <- function(outcome, num = "best") {
  results <- data.frame(hospital=character(0),state=character(0))
  states <- read.csv("states.csv",stringsAsFactors=FALSE)
  ## For each state, find the hospital of the given rank
  for (state in states$Abbreviation) {
    hospital <- rankhospital(state,outcome,num)
    r <- data.frame(hospital,state)
    results <- rbind(results,r)
  }
  #rownames(results) <- states
  return(results)
}
