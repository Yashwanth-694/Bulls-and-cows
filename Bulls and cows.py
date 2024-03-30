secret=int(input('Enter secret no:'))
guess=int(input('Enter Guess no:'))
sec_lst=[d for d in str(secret)]
guess_lst=[d for d in str(guess)]
x=0;y=0
sset=set();gset=set()
for i,d in enumerate(sec_lst):
    sset.add((i,d))
for i,d in enumerate(guess_lst):
    gset.add((i,d))
res=sset.intersection(gset)
x=len(res)
for item in res:
    sec_lst[item[0]]=-1
    guess_lst[item[0]]=-1

bctr,cctr=0,0
for i,d in enumerate(sec_lst):
    if d in guess_lst:
        if sec_lst[i]==guess_lst[i]:
            bctr+=1
        else:
            cctr+=1
            ind=guess_lst.index(d)
            guess_lst[ind]=-2
            sec_lst[i]=-2
ans=str(bctr)+'A'+str(cctr)+'B'
print(ans)
    
