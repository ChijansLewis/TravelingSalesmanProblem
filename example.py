#import the class
from TSP import Tsp
#creat or paste the coordinates 
cities=[[0, 0], [0, 3], [18, 3], [17, 3], [17, 15], [26, 15], [17, 18], [9, 18], [16,
18], [16, 24], [14, 24], [7, 24], [0, 24], [0, 27], [4, 27], [11, 20]]

tsp=Tsp(cities)#claim a class

tsp.main(ploter=True,length=True)#use the main method