import sys
#sys.stdin=open("input.txt","rt")

if __name__ =="__main__":
    n,m=map(int,input().split())
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        score,time=map(int,input().split())
        if time > m:
            break
        for k in range(time,m+1):
            dp[i][k]=max(dp[i-1][k-time]+score,dp[i-1][k])
	#for k in range(m+1,time-1,-1)
	#    dp[k]=max(dp[k-time]+score,dp[k])

print(dp[n][m])
#2차원으로 하는 방법 > 메모리 낭비
#중복을 허용하지 않는 경우 DP
#DP Table을 새로 갱신해야함(기존 것에서 X)

#1차원 > 훨씬 효율적
#뒤에서 부터 계산하면서 앞으로 오면 중복 계산이 안됨