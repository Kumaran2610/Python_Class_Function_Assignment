class SubfieldsInAI:
    def Subfields():
        AI = ["Machine Learning","Neural Networks","Vision","Robotics",
          "Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in AI:
            print(field)

  
class OddEven:
    def OddEven():
        num = int(input("Enter a number: "))
        if num % 2 == 1:
            numCategory = "Odd number"
        else:
            numCategory = "Even number"
        return f"{num} is {numCategory}"

class ElegibilityForMarriage:
    def Elegible():
        gender = input("Your Gender :")
        age = int(input("Your Age :"))
        if(gender == "male" and age > 21):
            status = "Elegible"
        elif(gender=="female" and age >18):
            status = "Elegible"
        else:
            status = "Not Elegible"
        return status

class FindPercent:
    def percentage():
        subMark1 = int(input("Subject1 ="))
        subMark2 = int(input("Subject2 ="))
        subMark3 = int(input("Subject3 ="))
        subMark4 = int(input("Subject4 ="))
        subMark5 = int(input("Subject5 ="))
        Total = subMark1 + subMark2 + subMark3 + subMark4 + subMark5
        Percentage = (subMark1 + subMark2 + subMark3 + subMark4 + subMark5)/5
        print("Total :", Total)
        print("Percentage :", repr(Percentage))

class triangle:
    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        area = (height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:", area) 
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        Perimeter = height1+height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", Perimeter)

