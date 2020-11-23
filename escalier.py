def escalier(n):
    for i in range (1,int(n)+1):
        print(((int(n-i)*" ")),(int(i)*"#"))