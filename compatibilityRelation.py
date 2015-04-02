
class CompatibilityRelations:

    compatibilityRelations = []
    compatibilityInfo = []
    relatedTo = []

    def __init__(self):
        pass

    def organize_relations(self, CR):

        for elements in CR:
            splitter = elements.split(':')
            key = splitter[0]
            self.compatibilityInfo.append(splitter[1:3])
            self.relatedTo.append(splitter[3])

        return self.compatibilityInfo, self.relatedTo




