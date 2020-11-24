def escalier(n):
    for i in range (1,int(n)+1):
        print(f'{int(n-i)*"-"}{int(i)*"#"}')