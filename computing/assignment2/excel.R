library(XLConnect)

# Load workbook (create if not existing)
wb <- loadWorkbook("createSheet.xlsx", create = TRUE)

# Create a worksheet called 'CO2'
createSheet(wb, name = "CO2")

# Save workbook (this actually writes the file to disk)
saveWorkbook(wb)
