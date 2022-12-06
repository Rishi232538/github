# file = open('text')

#nov = file.readline()

#for i in nov:
 #   print(nov)
  #  nov = file.readline()

print("*********Another Concept**********")

try:
    with open('text', 'r') as reader:
        content = reader.readlines()
        for i in content:
            print(i)
    reversed(content)
    print("******************************")
    with open('text', 'w') as writer:
        for j in reversed(content):
            writer.write(j)
            print(j)

except Exception as e:
    print("Forward-Reverse is not working")





