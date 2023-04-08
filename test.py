
from datetime import date, timedelta


def weekdayNumberToText(weekdayNumber):
    data = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
            3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    return data[weekdayNumber]


subjectName = "Software_Engineering"
subjectWeekChart = {
    # day : timeAlloted in minutes
    "Monday": 120,
    "Tuesday": 150,
    "Wednesday": 0,
    "Thursday": 90,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0,
}
taskName = "DummyTask"
estimatedTime = 500
startDate = date.today() + timedelta(days=1)
bufferPercentage = 0.5

print(startDate)


def SingleSubjectSingleTask(subjectName: str, subjectWeekChart: dict, taskName: str, estimatedTime: int, startDate: date, bufferPercentage: float):
    outputFile = open(f"Outputs\{subjectName}.csv", "w")
    outputFile.write("Date,Day,Task Name,Time Alloted(in minutes)\n")

    totalTimeRequired = estimatedTime + (bufferPercentage*estimatedTime)

    currentDate = startDate
    currentDayNo = currentDate.weekday()
    currentDayText = weekdayNumberToText(currentDayNo)
    taskPartNumber = 1
    while totalTimeRequired > 0:
        currentDayMaxTimeAlloted = subjectWeekChart[currentDayText]
        if currentDayMaxTimeAlloted != 0:
            dataToWrite = f"{currentDate},{currentDayText},{taskName}(Part{taskPartNumber}),{currentDayMaxTimeAlloted}\n"
            outputFile.write(dataToWrite)
            print(dataToWrite)
            taskPartNumber += 1

        totalTimeRequired -= currentDayMaxTimeAlloted
        currentDate = currentDate + timedelta(days=1)
        currentDayNo = currentDate.weekday()
        currentDayText = weekdayNumberToText(currentDayNo)


SingleSubjectSingleTask(subjectName, subjectWeekChart,
                        taskName, estimatedTime, startDate, bufferPercentage)
