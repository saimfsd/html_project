doctorAvailable = (input("doctor present or not")) == "yes"
paitentRegisterd = (input("Paitent registerd or not")) == "yes"
pymentDone = (input("Pyment done or not")) == "No"
if doctorAvailable:
    if paitentRegisterd:
        if pymentDone:
            print("Appinment Conform")
        else:
            print("Payment Pending" )
    else:
        print("Patient not register")
else:
    print("docgtor Unavailable")

