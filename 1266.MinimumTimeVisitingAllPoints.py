def minTimeToVisitAllPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    # I want to check the current coord pair with that of the next
    # Then I want to see if the X positions are further away or if the Y positions are
    # For whichever I find, I want to then add the difference to the rolling total
    # Once we reach the end of the list of coords, return the rolling total

    rollingTotal = 0

    for i in range(len(points)):
        print(points[i])
        try:
            if points[i+1] is not None:
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[i+1][0]
                y2 = points[i+1][1]

                if (abs(x1-x2) > abs(y1-y2)):
                    rollingTotal += abs(x1-x2)
                    continue
                elif (abs(x1-x2) < abs(y1-y2)):
                    rollingTotal += abs(y1-y2)
                    continue
                else:
                    if abs(x1-x2) > 0:
                        rollingTotal += abs(x1-x2)
                        continue
                    elif abs(y1-y2) > 0:
                        rollingTotal += abs(y1-y2)
                        continue
        except:
            return rollingTotal

#minTimeToVisitAllPoints([[1,1], [3,4], [-1,0]])
#minTimeToVisitAllPoints([[3,2], [-2,2]])
print(minTimeToVisitAllPoints([[1,1], [3,4], [-1,0]]))
print(minTimeToVisitAllPoints([[3,2], [-2,2]]))