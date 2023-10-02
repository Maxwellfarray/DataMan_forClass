def monthTempGet():
    monthtemp = []
    monthlist = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
    for i in monthlist:
        monthtemp.append(float(input("Enter the highest tempurature for month of " + i + ": ")))
    return monthtemp , monthlist