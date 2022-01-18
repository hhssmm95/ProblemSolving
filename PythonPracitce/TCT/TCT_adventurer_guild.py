def solution(guild):
  answer = 0

  guild.sort()
  count = 0

  for i in guild:
    count += 1
    if count >= i:
      answer+=1
      count = 0
  return answer

print(solution([4,4,2,1,4,5,6,1,2,1,2,3,1]))