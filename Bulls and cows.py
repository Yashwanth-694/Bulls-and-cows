secret=int(input('Enter secret no:'))
guess=int(input('Enter Guess no:'))
print('Sec no=',secret);print('guess no=',guess)
sec_lst=[d for d in str(secret)]
guess_lst=[d for d in str(guess)]
x=0;y=0
for i,d in enumerate(sec_lst):
    if d in guess_lst:
        if sec_lst[i]==guess_lst[i]:
            x+=1
        else:
            y+=1
ans=str(x)+'A'+str(y)+'B'
print(ans)
    
