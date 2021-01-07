file_name = "pancakes.txt"

f = open(file_name)

count=0
total_thickness=0
total_parameter=0

for number in f:
    number = number.strip("\n") #to separate record line
    #print("number=",type(number)) #to check number data type
    value = number.split(",") #to split each record into fields (thickness and parameter)
    #print("value=",type(value)) #to check value data type
    print("Thickness: ",value[0],"\tParameters: ",value[1])

    total_thickness+=float(value[0]) # total_thickness = total_thickness + float(value[0])
    total_parameter+=float(value[1])
        
    count+=1

print("\nTotal pancakes:",count)
print("Average thickness:",total_thickness/count)
print("Average parameter:",total_parameter/count)

f.close()
