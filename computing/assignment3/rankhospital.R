library(psych)
rankhospital <- function(state, outcome, num) {
  ## Read outcome data
  data <- read.csv("outcome-of-care-measures.csv")
  states <- read.csv("states.csv")
  ## Check that state and outcome are valid
  if (nrow(subset(states,Abbreviation == state)) == 0) {
    stop("invalid state")
  }
  
  if (outcome == "heart attack" || outcome == "heart failure" || outcome == "pneumonia") {
    
  } else {
    stop("invalid outcome")
  }
  
  # Filter By State
  data <- subset(data,State == state)
  # Remove Not Available
  if (outcome == 'heart attack') {

    outcome <- subset(data,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack != "Not Available",
                           select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack))
  }else if(outcome == 'heart failure') {
    outcome <- subset(data,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure != "Not Available",
                           select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure  ))    
  } else {
    outcome <- subset(data,Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia != "Not Available",
                      select=c(Hospital.Name,Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia))
  }
  
  names(outcome) <- c("hospital","rate")
  outcome$rate <- as.character(outcome$rate)
  outcome$rate <- as.numeric(outcome$rate)
  h <- sort(h, partial=c(2))
  print(h)
  nrows <- nrow(h)
  print(nrows)
  if (num == "best") {
    num <- 1
  } else if (num == "worst") {
    num <- nrow
  }
  if (num > nrows) {
    h <- NA
  } else {
    h <- as.character(h$hospital)
  }
  return(h)
}


