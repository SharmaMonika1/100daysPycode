#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Nesting :{Key: [List],Key2:{dict},}
capitals= {"France":"Paris","Germany":"Berlin"}
travel_log = {"France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
           "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}}

travel_log = [
   {"country":"France",
    "cities_visited":["Paris","Lille","Dijon"],
    "total_visits":12
   },
   {"country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits":5
   }
]


# In[9]:


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades={}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  if 91 <= student_scores[student] <= 100:       
     student_grades[student]= "Outstanding"
  elif 81 <= student_scores[student] <= 90:       
     student_grades[student]= "Exceeds Expectations"
  elif 71 <= student_scores[student] <= 80:       
     student_grades[student]= "Acceptable"
  else:
    student_grades[student]= "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)


# In[8]:


programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}
print(programming_dictionary)
programming_dictionary["Loop"]= "The action of doing something over and over again."
print(programming_dictionary)

empty_dictionary = {}
print(empty_dictionary)

program_dictionary =programming_dictionary
print(program_dictionary)

program_dictionary = {}
print(program_dictionary)

programming_dictionary["Bug"]= "A moth in your computer"
print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# In[32]:


from art import logo_auction
from IPython.display import clear_output

print(logo_auction)
print("Welcome to the secret auction program.")
is_bid= True
bid_dictionary={}

while is_bid:
    name = input("What is your name?: ")
    bid = int(input("What is you bid?$"))
    new_bidder= input("Are there any other bidders? Type 'yes' or 'no'.\n")
    bid_dictionary[name]=bid
    if new_bidder == 'yes':
        clear_output(wait=False)
        is_bid=True
    elif new_bidder == 'no':        
        is_bid=False
        find_highest_bidder(bid_dictionary)
        print(f"The highest bidder is {is_highest_bidder} with bid amount ${is_highest_bid}")
def find_highest_bidder(dictionary):
    is_highest_bid = 0
    is_highest_bidder = ''
    for bidder in dictionary:
        if diction[key] > is_highest_bid:
            is_highest_bid =  dictionary[key]
            is_highest_bidder =  bidder


# In[ ]:





# In[ ]:




