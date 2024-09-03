user_age = int(input("How old are you?"))

if user_age < 18:
  print("You can't drink.")
elif user_age >= 18 and user_age <= 35:
  print("You drink beer!")
elif user_age>= 36 and user_age <= 59:
  print("You drink soju!")
elif user_age == 60 or user_age == 70:
  print("Congratulations! You are free of charge!")
elif user_age > 60 and user_age < 70:
  print("You drink whatever you want!")
else:
  print("Help yourself!")