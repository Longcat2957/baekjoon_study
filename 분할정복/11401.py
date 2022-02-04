import sys
from math import comb
input = sys.stdin.readline
N, K = map(int, input().split())
p = 1000000007
# 경의롭게도 1000000007은 소수이다.
# 문제의 조건에 의해 N은 4000000이하의 자연수 이므로 1 <= a <= N을 만족하는
# 임의의 자연수 a에 대해서 다음의 페르마 소정리를 만족한다.
# a^(1000000007 - 1) ≡ 1 (mod 1000000007)
# a^(1000000006) ≡ 1 (mod 1000000007)
