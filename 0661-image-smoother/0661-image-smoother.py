class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        r = len(img)
        c = len(img[0])
        
        output = []
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(0)
            
            output.append(temp)
    
        #print(output)
        for i in range(r):
            for j in range(c):
                count = 1
                summ = img[i][j]
                for direction in directions:
                    if 0 <= i+direction[0] < r and 0 <= j+direction[1] < c:
                        summ += img[i+direction[0]][j+direction[1]]
                        count += 1
                
                output[i][j] = (summ//count)
        
        return output