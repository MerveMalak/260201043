right_email = "ceng113@example.com"
email = input("Enter a email: ")
email_at_index = email.index("@")
email_at_before = email[:email_at_index]
email_at_after = email[email_at_index+1:]
email = email_at_before.replace(".","").lower()+"@"+email_at_after.lower()
if email == right_email:
    print("Valid email")
else:
    print("Invalid email")