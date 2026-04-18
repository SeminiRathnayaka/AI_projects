# Patient Info Collector - Ai mini project

name = input(" Enter Your Name : ")
age = input (" Enter Your Age : ")
concern = input("What is Your Main Health Concern : ")
 
patient = {
  "name": name,
  "age":age,
  "concern":concern
 }

print(" --- Patinet Summery --- ")
print("Name     :", patient["name"])
print("Age      :", patient["age"])
print("Concern  :", patient["concern"])
print(" ------------------------ ")
