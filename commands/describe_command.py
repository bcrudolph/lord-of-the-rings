#!/usr/bin/python

from command import Command
from space import Space
from player import Player

class DescribeCommand(Command):
    """
    Describes the current space.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new describe command.

        @param name:         The name of player.
        @param explanation:  Explanation of player.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)
        
        self._player = player

    def execute(self):
        """
        Runs Describe command.
        """
        location = self._player.getLocation()
        locationName = location.getName()
        description = location.getDescription()
        items = location.getItems()
        itemsList = items.getItems()
        
        #Give space name and description
        print "%s: %s" % (locationName, description)

        #If space has a city
        if location.getCity():
            city = location.getCity()
            cityName = city.getName()
            print "\n%s is contained in %s." % (cityName, locationName)
            
            #If city has buildings
            if city.getBuildings():
                buildings = city.getBuildings()
                print "\nBuildings in %s:" % cityName
                for building in buildings:
                    buildingName = building.getName()
                    buildingDescription = building.getDescription()
                    print "\t%s: %s." % (buildingName, buildingDescription)
     
        #If space has one or more uniquePlace objects
        uniquePlaces = location.getUniquePlaces()
        for uniquePlace in uniquePlaces:
            uniquePlaceName = uniquePlace.getName()
            print "\n%s is contained in %s." %(uniquePlaceName, locationName)
   
   
        #If space has items
        if len(itemsList) > 0:
            print "\nItems contained in %s:" % locationName
            for item in itemsList:
                print "\t%s" % item.getName()
