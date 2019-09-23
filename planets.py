def weight_on_planets():
    weight = float(input("What do you weigh on earth? \n"))
    weight_on_mars = weight * 0.38
    weight_on_jupiter = weight * 2.34
    # set the different weights

    print("On Mars you would weigh", weight_on_mars, "pounds.\nOn Jupiter you would weigh", weight_on_jupiter,
          "pounds. ")



if __name__ == '__main__':
    weight_on_planets()
