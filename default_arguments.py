#Exam results

def status(result = "unknown"):
    if result == "p":
        result = "pass"
    elif result == "f":
        result = "fail"
    return(result)

re1 = status("p")
re2 = status("f")
re3 = status()
print(re1)
print(re2)
print(re3)


