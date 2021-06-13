def main():

    print("Inici")

    from IAPract2 import solve_card
    from IAPract2 import printTable
    
    printTable()
    print()

    if (solve_card()):
        printTable()
    else:
        print("No existeix solució")


if __name__ == "__main__":
    main()