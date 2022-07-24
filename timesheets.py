import datetime
def timesheets(filenumber, date):
    # import file as a single string
    fname = 'timesheets (' + filenumber + ').csv'
    csv = open(fname)

    # set function variables
    stores = {}
    timesheets = []

    # take the read csv and store it as a matrix w rows and columns
    for timesheet in csv:
        timesheets.append(timesheet.strip().split(','))

    # remove the column titles row
    timesheets.pop(0)

    # loop through the rows (timesheets) in the matrix
    for timesheet in timesheets:
        # define suspicious durations
        sus = float(timesheet[11]) < 0.07 or float(timesheet[11]) >= 10.0
        # access timesheet pieces
        labor = int(float(timesheet[12][1:]))
        tsday = int(timesheet[3][8:])
        employee = timesheet[0]
        clockin = timesheet[4]
        clockout = timesheet[5]
        store = timesheet[7]
        hours = timesheet[11]

        # filter for day of interest
        if tsday == date:
            # sum labor costs for a store
            if store in stores:
                stores[store] = stores[store] + labor
            # create a key for the store if it's not there yet
            else:
                stores[store] = labor

            # print timesheets of suspicious duration
            if sus:
                print(clockin, "|", clockout, "|", hours, "|", store, "|", employee)

    # loop through the stores of the srg dictionary printing the labor totals
    for store in stores:
        print(store + ': ' + str(stores[store]))


# set function call variables
num = input("Enter CSV file number: ")
standard = input("Standard run? (y/n): ")
default = int(str(datetime.datetime.today())[8:10]) - 1
pa = num
va = str(int(num) + 1)
nc = str(int(num) + 2)

# single call or full call
if standard == "y":
    print('-------------------PA LABOR-------------------')
    timesheets(pa, default)
    print('-------------------VA LABOR-------------------')
    timesheets(va, default)
    print('-------------------NC LABOR-------------------')
    timesheets(nc, default)
else:
    while True:
        try:
            date = int(input("Enter date to review: "))
        except:
            break
        print('---------------------' + str(date) + '---------------------')
        timesheets(num, date)
