# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.locations = []
        for htile in range(self.height):
            for wtile in range(self.width):
                #print wtile
                #print htile
                self.locations.append((wtile,htile))
        self.tileStatus = {}
        for loc in range(len(self.locations)):
            self.tileStatus[self.locations[loc]] = False


    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        rounded = (math.floor(pos.getX()),math.floor(pos.getY()))
        if rounded in self.tileStatus:
            self.tileStatus[rounded] = True
            



    def isTileCleaned(self, m,n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        tile = (m,n)
        return self.tileStatus[tile] 

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        numCleaned = 0        
        a = self.tileStatus.values()
        for item in a:
            if item == True:
                numCleaned += 1
        #print numCleaned
        return numCleaned

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        rOne = random.choice(self.locations)[0]
        rTwo = random.choice(self.locations)[1]
        return Position(rOne,rTwo)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return (math.floor(pos.getX()), math.floor(pos.getY())) in self.locations


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        randpos = room.getRandomPosition()
        self.position = randpos
        self.angle = random.randrange(0,360)
        self.room = room
        self.speed = speed
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.angle

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position


    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.angle = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
       # self.room.cleanTileAtPosition()
        raise NotImplementedError # don't change this!

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.room.cleanTileAtPosition(self.position)
        #print "Sweep sweep sweep"
        a = self.position.getNewPosition(self.angle, self.speed)
        if self.room.isPositionInRoom(a):
            self.position = a
        else:
            if a.getX() > self.room.width:
                #print self.position.getX()
                self.angle = random.randrange(180,360)
                #print "Right"
            if a.getX() < 0:
                #print "left"
                self.angle = random.randrange(0,180)
            if a.getY() < 0:
                angle1 = random.randrange(270, 360)
                angle2 = random.randrange(0,90)
                self.angle =random.choice([angle1,angle2])
                #print "Down"
            if a.getY() > self.room.height:
                self.angle = random.randrange(90, 270)
                #print "Up"


# === Problem 3
def runSimulation1(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    stepsTaken = 0
    simRoom = RectangularRoom(width,height)
    robots = []
    perTrial = []
    for robos in range(num_robots):
        rob = robot_type(simRoom,speed)
        robots.append(rob)
    print len(robots)
    for trials in range(num_trials):
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        simRoom = RectangularRoom(width,height)            
        print "New Room!"
        while True:
            #print 100 * float(simRoom.getNumCleanedTiles())/float(simRoom.getNumTiles())
            for rob in robots:
                #anim.update(simRoom, robots)
                stepsTaken +=1
                print type(rob)
                rob.updatePositionAndClean()
                print simRoom.getNumCleanedTiles()
                #print stepsTaken
                print simRoom.getNumCleanedTiles()
            if 100 * (float(simRoom.getNumCleanedTiles())/float(simRoom.getNumTiles())) < float(min_coverage)*100:
                #for rob in robots:
                    #print "Move"
                    #anim.update(simRoom, robots)
                    #rob.updatePositionAndClean()
                #print float(min_coverage)*100
                #print 100 * float(simRoom.getNumCleanedTiles())/float(simRoom.getNumTiles())
                #print stepsTaken
                print "end trial"
                #anim.done()
                #print stepsTaken
                #print simRoom.getNumTiles()
                #print simRoom.getNumCleanedTiles()
                #print float(simRoom.getNumTiles())/float(simRoom.getNumCleanedTiles()) *100
                perTrial.append(stepsTaken)
                print "new trial appended"
                print "STEPS TAKEN AFTER TRIAL!"+str(stepsTaken)
                stepsTaken = 0
                #print perTrial
                #print len(perTrial)
                #print stepsTaken
                break
            
        
        

    return float(sum(perTrial)/len(perTrial))
            
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    simRoom = RectangularRoom(width,height)
    perTrial = []
    robots = []
    for trials in range(num_trials):
        #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        stepsTaken = 0
        robots = []
        simRoom = RectangularRoom(width,height)
        for robs in range(num_robots):
            robo = robot_type(simRoom, speed)
            robots.append(robo)
        ##count = 0
        while True:
            ##print count
            for rob in robots:
                rob.updatePositionAndClean()
                #anim.update(simRoom, robots)
            stepsTaken+=1
            if 100 * float(simRoom.getNumCleanedTiles())/float(simRoom.getNumTiles()) >= float(min_coverage*100):
                perTrial.append(stepsTaken)
                stepsTaken = 0
                robots=[]
                #anim.done()
                #print stepsTaken
                #print "End Trial"
                break
        #print sum(perTrial)
        #print num_trials
    return float(sum(perTrial)/num_trials)




# Uncomment this line to see how much your simulation takes on average
#print  runSimulation(1, 1, 5, 5, 0.75, 1, StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.room.cleanTileAtPosition(self.position)
        self.angle = random.randrange(0,360)
        #print "Sweep sweep sweep"
        a = self.position.getNewPosition(self.angle, self.speed)
        if self.room.isPositionInRoom(a):
            self.position = a
        else:
            if a.getX() > self.room.width:
                self.angle = random.randrange(180,360)#right
            if a.getX() < 0:
                #print "left"
                self.angle = random.randrange(0,180)
            if a.getY() < 0:
                angle1 = random.randrange(270, 360)
                angle2 = random.randrange(0,90)
                self.angle =random.choice([angle1,angle2])
                #print "Down"
            if a.getY() > self.room.height:
                self.angle = random.randrange(90, 270)
                #print "Up"
            if x+dx > leftEdge and x+dx < rightEdge:
                x += dx
            if  a.getY > bottomEdge and a.getY < topEdge:
                y += dy        



def showPlot1(title, x_label, y_label):
    """
    informational plot for pset2
    """
    num_robot_range = range(1, 5)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 5, 5, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 5, 5, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    informational plot for pset2
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        print aspect_ratios
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
        print times1,times2
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

def test1():
    room = RectangularRoom(5,5)
    if room.getNumTiles() == 25:
        print "Success number of tiles is correct"
    else:
        print "FAIL!"
        print room.getNumTiles()

#test1()

global troom
troom = RectangularRoom(5,5)
def test2():
    room = RectangularRoom(5,5)
    #print len(room.locations)
    #print "hells yea"
    return False==room.isTileCleaned(2,3)
    #print room.tileStatus.values()
#test2()

def test4():
    room = RectangularRoom(5,5)
    print "NUMBER OF TILES CLEANED SHOULD BE 1 "+ str(room.getNumCleanedTiles())

def test5():
    """
    tests getRandomPosition method
    """
    print troom.getRandomPosition()
def test6():
    """
    tests isPositionInRoom method
    """
    print troom.isPositionInRoom(Position(0,0))
    print troom.isPositionInRoom(Position(6,9))
    #print troom.isPositionInRoom((1.1,0))
    print troom.isPositionInRoom(Position(34,0.1143))
    print "Should return True,False,False"

def test7():
    print troom.isTileCleaned(0,0)
    troom.cleanTileAtPosition(Position(0.6, 0.3))
    print troom.isTileCleaned(0, 0)
    print "END TEST"
#
#test7()
#test5()
#test6()

def rozot1():
    rob = Robot(troom,2)
    print rob.getRobotPosition()
    rob.setRobotPosition((2,4))
    print rob.getRobotPosition()
#rozot1()
#runSimulation(num_robots, speed, width, height, min_coverage, num_trials,robot_type)
#print runSimulation(5, 1, 12, 10, 1.0, 1,
#                 RandomWalkRobot)
title = "title"
x_label = "bottom label"
y_label = "side label"
#showPlot2(title, x_label, y_label)

def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())



testRobotMovement(StandardRobot, RectangularRoom)