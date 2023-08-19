def solution(S, C):
  """
  Returns the minimum number of insertions after which there will be a '$' character
  between every two occurrences of the same letter in the string S.

  Args:
    S: The string.
    C: The array of insertion positions.

  Returns:
    The minimum number of insertions, or -1 if the condition is not met after all
    the insertions have been made.
  """

  n = len(S)
  ins = 0
  seen = set()
  for i in range(n):
    if S[i] in seen:
      if ins < len(C) and i <= C[ins]:
        ins += 1
      else:
        return -1
    else:
      seen.add(S[i])
  return ins
print(solution("aabcba", [1, 3, 2]))

print(solution("aaa", [1, 2]))