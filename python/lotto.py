#https://programmers.co.kr/learn/courses/30/lessons/77484
  
def solution(lottos,win_nums):
    count=0
    countz=0
    
    countz=lottos.count(0)      
    for i in lottos:
        for j in win_nums:
            if i==j:
                count+=1
                win_nums.remove(j)
    
    maxi=7-count-countz
    mini=7-count
    
    if mini>6: mini=6
    if maxi<1: maxi=1
    elif maxi>6: maxi=6
    answer=[maxi,mini]
    return answer
