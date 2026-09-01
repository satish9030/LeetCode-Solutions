from typing import List
from collections import deque

class Solution:
    def minMoves(self,classroom:List[str],energy:int)->int:
        m=len(classroom)
        n=len(classroom[0])
        sr=sc=0
        lights=[]

        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    sr,sc=i,j
                elif classroom[i][j]=='L':
                    lights.append((i,j))

        if len(lights)==0:
            return 0

        light_id={}
        for i in range(len(lights)):
            light_id[lights[i]]=i

        full=(1<<len(lights))-1

        q=deque()
        q.append((sr,sc,0,energy,0))

        best={}
        best[(sr,sc,0)]=energy

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r,c,mask,e,moves=q.popleft()

            for dr,dc in dirs:
                nr=r+dr
                nc=c+dc

                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue

                if classroom[nr][nc]=='X':
                    continue

                ne=e-1

                if ne<0:
                    continue

                nmask=mask

                if classroom[nr][nc]=='R':
                    ne=energy

                if classroom[nr][nc]=='L':
                    x=light_id[(nr,nc)]
                    nmask=mask|(1<<x)

                if nmask==full:
                    return moves+1

                state=(nr,nc,nmask)

                if state in best and best[state]>=ne:
                    continue

                best[state]=ne
                q.append((nr,nc,nmask,ne,moves+1))

        return -1