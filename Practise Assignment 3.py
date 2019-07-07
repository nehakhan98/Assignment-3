
# coding: utf-8

# # Q1:

# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

# In[6]:


favpizza=['chicken supreme','spicy ranch','bbq buzz']
for a in favpizza:
    print (a)


# # Q2

# Start with your last question , Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.

# In[5]:


favpizza=['i like chicken supreme','i baked spicy ranch today','people love to eat bbq buzz pizza']
for a in favpizza:
    print (a)


# # Q3:

# Use a for loop to print the numbers from 1 to 20,
# inclusive.

# In[4]:


for a in range(1,21):
    print(a)


# # Q4:

# Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

# In[2]:


for a in range (1,21,2):
    print(a)


# # Q5:

# Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

# In[3]:


numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i*3)
    


# # Q6:

# A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube

# In[2]:


numbers=[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i**3)
    
 


# # Q7:

# ###### Make a python program that conatains your nine favourite dishes in a list called foods.
# 
# ###### Print the message, The first three items in the list are:. 
# ###### Then use a slice to print the first three items from that program’s list.
# 
# ###### Print the message, Three items from the middle of the list are:
# ###### Use a slice to print three items from the middle of the list.
# 
# ###### Print the message, The last three items in the list are:
# ###### Use a slice to print the last three items in the list.

# In[13]:


favdishes=['Mutton Karhai','Peshawri Karhai','Green Karahai','White Chicken Handi','Malai Boti','Aghwani Pillaow','Beef Briyani','Chocolate Icecream','Fanta']
print(f"First three dishes:")
for breakfast in favdishes[0:3]:
    print(breakfast)


# In[17]:


favdishes=['Mutton Karhai','Peshawri Karhai','Green Karahai','White Chicken Handi','Malai Boti','Aghwani Pillaow','Beef Briyani','Chocolate Icecream','Fanta']
print(f"Middle three dishes:")
for lunch in favdishes[3:6]:
    print(lunch)


# In[18]:


favdishes=['Mutton Karhai','Peshawri Karhai','Green Karahai','White Chicken Handi','Malai Boti','Aghwani Pillaow','Beef Briyani','Chocolate Icecream','Fanta']
print(f"Last three dishes:")
for dinner in favdishes[6:9]:
    print(dinner)


# # Q8:

# ### Start with your program from your last Question8.
# ###### Make a copy of the list of foods, and call it friend_foods.
# ###### Then, do the following:
# ######    Add a new dish to the original list.
# ######    Add a different dish to the list friend_foodss.
# ######    Prove that you have two separate lists. 
# ###### Print the message, My favorite pizzas are: and then use a for loop to print the first list. 
# ###### Print the message,
# ###### My friend’s favorite foods are:, and then use a for loop to print the second list.
#     
# ##### NOTE: Make sure each new dish is stored in the appropriate list.

# In[14]:


friend_Food=['Mutton Karhai','Peshawri Karhai','Green Karahai','White Chicken Handi','Malai Boti','Aghwani Pillaow','Beef Briyani','Chocolate Icecream','Fanta']
print(f"New dish added:")
friend_Food.append('BBQ')
friend_Food


# In[25]:


friend_Food=['Mutton Karhai','Peshawri Karhai','Green Karahai','White Chicken Handi','Malai Boti','Aghwani Pillaow','Beef Briyani','Chocolate Icecream','Fanta']
friend_foods=friend_Food.copy()


# In[26]:


friend_foods.append('Tea')
friend_foods


# In[35]:


friend_Food=['Mutton Karhai','Peshawri Karhai','Green Karahai','White Chicken Handi','Malai Boti','Aghwani Pillaow','Beef Briyani','Chocolate Icecream','Fanta']
print(f"My fav Pizza",)
for pizzas in friend_Food:
    print(pizzas)
    


# In[36]:


print(f"My Friend's Fav Foods Are :")
for friendfavfood in friend_Food:
    print(friendfavfood)


# In[38]:


print(f"My Fav Foods Are :")
for myfriendfavfood in friend_foods:
    print(myfriendfavfood)


# # Q9:

# Take a user input from console line.Store it in a variable called Alien_color.
# 
# If the alien’s color is red, print a statement that the player just earned 5 points for shooting the alien.
# 
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# 
# If the alien's color isn't red or green , print a statment :, Alien is no more.....

# In[42]:


aliencolor=input("Enter the color of ALIEN ")
if aliencolor=="red":
    print("That the player just earned 5 points for shooting the alien.")
elif aliencolor=="green":
        print("That the player just earned 10 points.")
else:
    print("Alien is no more")


# # Q10:

# Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
#     
# •	 If the person is less than 2 years old, print a message that the person is a baby.
# 
# •	 If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# 
# •	 If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# 
# •	 If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# 
# •	 If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# 
# •	 If the person is age 65 or older, print a message that the person is an elder.

# In[3]:


age=int(input("Enter any age : "))
if age<2:
    print("The person is a Baby")
elif age <=2 or age <4:
    print("The person is a Toddler")
elif age <=4 or age <13:
    print("The person is a Kid")
elif age <=13 or age <20:    
    print("The person is a Teenager")
elif age <=20 or age <65:        
    print("The person is a Adult")
else:
    print("The person is an Elder")
    
    


# # Q11:

# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# 
# •	 Make a list of five or more usernames called current_users.
# 
# •	 Make another list of five usernames called new_users. 
# Make sure one or two of the new usernames are also in the current_users list.
# 
# •	 Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available.
# 
# •	 Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.

# In[15]:


current_user=['Ahmed','Amna','Faheel','Neha','Mariyam']
new_user=['Warda','Usman','Hamza','Ahsan','Neha']


# In[16]:


for i in new_user:
    if i in current_user:
        print(f"{i} username has been already used,You will need to enter a new username")
    else:
          print(f"{i} Username is available")


# # Q12:

# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary

# In[6]:


person_info={}


# In[8]:


person_info["First Name"]="Neha"
person_info["Last Name"]="khan"
person_info["Age"]="21"
person_info["City"]="Karachi"


# In[9]:


person_info


# In[21]:


for keys in person_info:
    print(keys)


# In[24]:


for key,val in person_info.items():
    print(":",val)


# # Q13:

# Starts with your last question 12 , loop through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# dictionary . When you run your program again, these new words and meanings
# should automatically be included in the output.

# In[10]:


for key,val in person_info.items():
    print(key,":",val)


# In[11]:


person_info["Education"]="B.ed"
person_info["Religion"]="Islam"
person_info["Nationality"]="Pakistani"
person_info["Hobby"]="Creativity"
person_info["Profession"]="Teaching"


# In[12]:


for key,val in person_info.items():
    print(key,":",val)


# # Q14:

# Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
#     
#     
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# 
# NOTE: use upper case through keys and values.

# In[7]:


river_name={'Nile':'Ejypt','Lorie':'France','Shinano':'Japan'}


# In[8]:


for river , country in river_name.items():
    print("The " + river.upper() + " runs through " + country .upper())


# # Q15:

# Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

# In[5]:


Candy={"name":"Candy","kind":"Cat","owner":"Mariyam"}
Sandy={"name":"Sandy","kind":"Kitten","owner":"Warda"}
Brolo={"name":"Brolo","kind":"Dog","owner":"Maham"}
pets=[Candy,Sandy,Brolo]
for i in pets:
    print(i["name"], "is a " , i["kind"] , "of " , i["owner"])

