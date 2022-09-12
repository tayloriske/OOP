import InsectClass as i

def main():
    fly = i.Insect(2,4)
    mosquito = i.Insect(4,4)

    fly.lengthofflight()
    mosquito.lengthofflight()

    print ("The fly can fly", fly.get_miles(), "miles.")
    print ("The mosquito can fly", mosquito.get_miles(), "miles.")

main()