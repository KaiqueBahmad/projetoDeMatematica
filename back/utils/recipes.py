import json

def readJSON(name="userdata.json"):
    with open('../'+name, 'r') as file:
        return json.loads(file.read())

def saveJSON(data, name="userdata.json"):
    json.dump(data, "./"+name)


def addRecipe(recipeName, recipe):
    try:
        data = readJSON()
        data["recipes"].update(recipe)
        return "sucess"
    except Exception:
        return "fail"
    
def removeRecipe(recipeName):
    data= readJSON()


def increaseBalance(amount):
    pass

def defineBalance(amount):
    pass


if __name__ =='__main__':
    print(readJSON('userdata.json'))

