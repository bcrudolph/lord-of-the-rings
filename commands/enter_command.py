#!/usr/bin/python

from command import Command

class EnterCommand(Command):
    """
    Allows player to enter a building.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new enter command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Allows player to enter a building.
        """
        name = self._player.getName()
        space = self._player.getLocation()
        city = space.getCity()
        cityName = city.getName()
        buildings = city.getBuildings()
        uniquePlaces = space.getUniquePlaces()

        #Display places player may enter
        print "%s may enter the following in %s:" % (name, cityName)
        for building in buildings:
            print "\t%s" % building.getName()
        print ""
        
        print "Also, you may enter: \n"
        
        for uniquePlace in uniquePlaces:
            print "\t %s" %uniquePlace.getName()

        placeToEnter = raw_input("Where would you like to go? ")
        building = city.getBuildingString(placeToEnter)
        
        if building:
            building.enter(self._player)
        else:
            print "Building does not exist."
        
        for uniquePlace in uniquePlaces:
            if uniquePlace.getName() == placeToEnter:
                uniquePlace.enterUniquePlace()
