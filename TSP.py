class Tsp:
    path=[]
    def __init__(self,cpoints) -> None:
        self.copypoints=cpoints
    @property
    def plength(self)->float:
        sum=0
        for i in range(len(self.copypoints)-1):
            sum+=Tsp.dist(self.copypoints[i],self.copypoints[i+1])
        return sum
    @classmethod
    def dist(cls,p:list,q:list)->float:
        a=((p[0]-q[0])*(p[0]-q[0])+(p[1]-q[1])*(p[1]-q[1]))**0.5
        b=float(str(a).split('.')[0] + '.' + str(a).split('.')[1][:4])
        return b
    @classmethod
    def pathlength(cls,path:list)->float:
        sum=0
        for i in range(len(path)-1):
            sum+=Tsp.dist(path[i],path[i+1])
        return sum
    @classmethod
    def insert(cls,presentpath:list,point:list)->None:
        inter=presentpath[1:]
        dicts=[]
        disten=[]
        for i,_ in enumerate(inter):
            dict={}
            inter.insert(i,point)
            dict['sortedpath']=[presentpath[0],*inter]
            dict['length']=(Tsp.pathlength([presentpath[0],*inter]))
            dicts.append(dict)
            inter.pop(i)
        for dic in dicts:
            disten.append(dic['length'])
        for dic in dicts:
            if dic['length']==min(disten):
                Tsp.path=dic['sortedpath']

    def main(self,ploter=False,length=False)->None:

        points=sorted(self.copypoints)

        origen=points.pop(0)
        p1,p2=points.pop(),points.pop()
        Tsp.path=[origen,p1,p2,origen]

        for point in points:
            Tsp.insert(Tsp.path,point)
        path0=Tsp.path[:]
        len0=Tsp.pathlength(path0)
        for _ in range(5):
            for point in path0[1:-1]:
                Tsp.path.remove(point)
                Tsp.insert(Tsp.path,point)
                if Tsp.pathlength(Tsp.path)<=len0:
                    path1=Tsp.path[:]
                    len0=Tsp.pathlength(path0)
        print(path1)

        for indx,point in enumerate(Tsp.path):
            indx=self.copypoints.index(point)+1
            print(indx,end=',')
        if length:
            print(Tsp.pathlength(path1))
        if ploter:
            import matplotlib.pyplot as plt
            x=[]
            y=[]
            for i,point in enumerate(Tsp.path[:-1]):
                x1,y1=point
                x.append(x1)
                y.append(y1)
                plt.scatter(x1,y1,marker='*',s=30)
            plt.xlabel("x - axis")
            plt.ylabel("y - axis")
            plt.axis("equal")
            plt.plot(x,y,color='r')
            plt.plot([x[0],x[-1]],[y[0],y[-1]],color='r')
            for i,point in enumerate(self.copypoints):
                x1,y1=point
                plt.annotate(f'{i+1}',xy=(x1,y1),xytext=(x1+0.2,y1+0.2))
            plt.show()
