#!/usr/bin/env python
import random
from copy import copy

#families = [['Jean', 'Tim'],
#            ['Ben', 'Anna'],
#            ['Paul', 'Melissa'],
#            ['Heidi', 'Zach'],
#            ['Sam']]

families = [['Caleb', 'Cecily'],
            ['Owen'],
            ['Mia', 'Hayden'],
            ['Clara', 'Rex']]

            
class ListMaker:
    def __init__(self, listOfFamilies):
        self.families = listOfFamilies
        self.namePool = [item for sublist in listOfFamilies for item in sublist]
        self.restOfFamilyDict = {}
        for family in listOfFamilies:
            for person in family:
                self.restOfFamilyDict[person] = filter(lambda x: x != person, family)
        self.finalList = {}

    def printList(self):
        recipientNamePool = copy(self.namePool)
        while len(recipientNamePool) > 0:
            recipientIndex = random.randint(0, len(recipientNamePool) - 1)
            recipient = recipientNamePool[recipientIndex]
            found = False
            while not found:
                giverIndex = random.randint(0, len(self.namePool) - 1)
                giver = self.namePool[giverIndex]
                if (not self.finalList.has_key(giver)) and (not giver in self.restOfFamilyDict[recipient]) and ((not self.finalList.has_key(recipient) or (not self.finalList[recipient] == giver))) and giver != recipient:
                    self.finalList[giver] = recipient
                    recipientNamePool.remove(recipient)
                    found = True
        for giver in self.finalList.keys():
            print "%s gives a gift to: %s" % (giver, self.finalList[giver])
                                                         

if __name__ == "__main__":
    l = ListMaker(families)
    l.printList()
