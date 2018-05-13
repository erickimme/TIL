'''
It’s been a few months since Bender solved his famous bending problem. A special request has arrived to Planet Express Inc., the interplanetary courier company where Bender works. Professor Farnsworth (founder, CEO, and chairman of the board) immediately prepared the mission and summoned his crew: Philip J. Fry, Turanga Leela, and Bender. To succeed in the mission, the crew has to make n trips: τ1, τ2, . . ., τn, in the exact order established by Professor Farnsworth. He has also provided the crew with a notebook that specifies how many minutes each trip in the spaceship will take.

image Nibbler is also a member of the crew and a critical element to succeed in the mission. Nibbler’s feces, which it expels every now and then, consist of spheres of dark matter that can be used to increase the speed of the spaceship. In fact, a sphere used during a trip halves its duration. Bender’s role in the mission is to pick up the heavy spheres and put them in the reactor of the spaceship. However, he will never put two spheres during the same trip: the accumulation of dark matter is extremely dangerous and may destroy the spaceship.

In each trip of the mission, Nibbler expels a certain number of dark matter spheres that can be used to decrease the duration of any of the upcoming trips. In other words, a sphere of dark matter produced during the trip τi can be used to duplicate the speed of the spaceship in one of the trips τj , with i < j ≤ n. Fry is responsible for planning how to use the spheres to reduce the total travel time. Your task is to help Fry in determining what is the minimum duration of the mission if he uses Nibbler’s spheres cleverly.

Input Format

The input consists of several test cases. The first line of each case contains an integer n indicating the number of trips. Then, n lines follow describing each of the trips τ1, τ2, …, τn: each line contains two integers ti and bi separated by blanks, where ti indicates the duration in minutes specified by Professor Farnsworth for the trip. τi and bi indicates the number of dark matter spheres that Nibbler will expel during the trip τi. The last test case is followed by a line containing a single ‘0’.

Constraints

1 ≤ n ≤ 100

2 ≤ ti ≤ 1000 (ti is always even)

0 ≤ bi ≤ n

Output Format

For each test case, print a line with an integer number indicating the minimum time required to complete the mission.

Sample Input 0

2
24 1
10 0
2
10 1
24 0
3
10 0
24 0
38 0
3
10 1
24 0
14 0
3
10 1
24 0
38 0
3
10 1
24 1
38 0
3
10 3
24 0
38 1
0

Sample Output 0

29
22
72
36
53
41
41
'''

'''
2
24 1
10 0
2
10 1
24 0
3
10 0
24 0
38 0
3
10 1
24 0
14 0
3
10 1
24 0
38 0
3
10 1
24 1
38 0
3
10 3
24 0
38 1
0
'''


def calc(oneCycleList):
    for i in range(len(oneCycleList)):
        print("i: " + str(i) + " oneCycleList[i]: " + str(oneCycleList[i])) #0
        for i in
        if (type(oneCycleList[i])) == "int":

            for j in range(i):
                print("j: " +  str(j))
    return

def main():

    numTripsLi = []
    minsLi = []
    spheresLi = []
    oneCycleList = []

    while True:
        numTrips = int(input().strip())
        oneCycleList.append(numTrips)
        if numTrips == 0:
            break
        for i in range(numTrips):
            minSphere = input().split()
            oneCycleList.append(minSphere)
    print("oneCycleList: " + str(oneCycleList))
    calc(oneCycleList)


    '''
    while True:
        numTrips = int(input().strip())  # str -> int
        if numTrips == 0:
            break
        numTripsLi.append(numTrips)
        for i in range(numTrips):
            minSphere = input().split()
            minsLi.append(minSphere[0])
            spheresLi.append(minSphere[1])
    print("numTrip list: " + str(numTripsLi))
    print("mins list: " + str(minsLi))
    print("spheres list: " + str(spheresLi))
    '''

main()
