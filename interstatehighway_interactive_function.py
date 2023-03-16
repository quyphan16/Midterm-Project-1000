def get_highway_number():
    highway_num = int(input("Enter Highway Number: I-"))
    if (highway_num >= 1 and highway_num <= 99) or (highway_num >= 100 and highway_num <= 999):
        return highway_num
    else:
        serve_num = highway_num % 100
        if serve_num == 0:
            print(highway_num, "is not a valid interstate highway number.")
            return highway_num
            
def print_highway_info(n):
    highway_num = n
    highway_reminder = highway_num % 2
    if highway_num >= 1 and highway_num <= 99:
        if highway_reminder == 0:
            new_hw_num = str(highway_num)
            print("I-"+ new_hw_num, "is primary, going east/west.")
        else:
            new_hw_num = str(highway_num)
            print("I-"+ new_hw_num, "is primary, going north/south.")
    else:
        if highway_num >= 100 and highway_num <= 999:
            serve_num = highway_num % 100
            serve_reminder = serve_num % 2
            if serve_num == 0:
                print(highway_num, "is not a valid interstate highway number.")
            elif serve_reminder == 0:
                new_hw_num = str(highway_num)
                new_serve_num = str(serve_num)
                print("I-"+ new_hw_num, "is auxiliary,", "serving I-"+new_serve_num, "going east/west.")
            else:
                new_hw_num = str(highway_num)
                new_serve_num = str(serve_num)
                print("I-"+ new_hw_num, "is auxiliary,", "serving I-"+ new_serve_num, "going north/south.")

if __name__ == "__main__":
    n = get_highway_number()
    print_highway_info(n)
