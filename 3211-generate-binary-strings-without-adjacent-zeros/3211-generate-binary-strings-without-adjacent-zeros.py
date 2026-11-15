class Solution:
    def solve(self,index, flag,number,result):
        if index >=len(number):
            result.append("".join(number))
            return
        number[index]="1"
        self.solve(index+1,True,number,result)
        if flag==True:
            number[index]="0"
            self.solve(index+1,False,number,result)
            
    def validStrings(self, n: int) -> List[str]:
        number=[""]*n
        result=[]
        self.solve(0,True,number,result)
        return result

        