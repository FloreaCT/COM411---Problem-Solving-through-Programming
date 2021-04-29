#Defining the function
def escape_by(plan):
  if plan == "jumping over":
    print("We cannot escape that way! The boulder is to big!")
  elif plan == "running around":
    print("We cannot escape that way! The boulder is moving to fast")
  elif plan == "going deeper":
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")

#Calling the function
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")  
escape_by("Destroying the boulder with our laser guns!")