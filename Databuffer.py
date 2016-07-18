# -*- coding: utf-8 -*-
class Databuffer:
    def __init__(self, Path, BufferSize):    #Konstrukor
        self.Path= Path
        self.BufferSize=BufferSize
        try:
            d=open(self.Path)
        except:
            #Keine Daten -> Erstelle leere Datei
            d=open(self.Path,'w')
            for i in range(self.BufferSize):
                d.write('{0:0.1f},'.format(0))
            d.close()
            print('New File Created')

    def GetBuffer(self,Buffer=[]):
        TempData=[]
        d=open(self.Path)
        data = d.readlines()
        d.close()
        datastr=data[0] 
        for i in range(datastr.count(',')+1): 
                data1=datastr.partition(',') 
                if data1[0]!= "": 
                    TempData.append(float(data1[0])) 
                datastr=data1[2]

        # Falls nötig auf Buffersize auffüllen
        while len(TempData) < self.BufferSize:
             TempData.append(float(0))
             
        Buffer = TempData
        return Buffer
    
    def Get(self):
        TempData=[]
        d=open(self.Path)
        data = d.readlines()
        d.close()
        datastr=data[0] 
        for i in range(datastr.count(',')+1): 
                data1=datastr.partition(',') 
                if data1[0]!= "": 
                    TempData.append(float(data1[0])) 
                datastr=data1[2]

        # Falls nötig auf Buffersize auffüllen
        while len(TempData) < self.BufferSize:
             TempData.append(float(0))
             
        Buffer = TempData
        Data=Buffer[self.BufferSize-1]
        return Data

    def Set(self,Data, Buffer=[]):
        TempData=[]
        d=open(self.Path)
        data = d.readlines()
        d.close()
        datastr=data[0] 
        for i in range(datastr.count(',')+1): 
                data1=datastr.partition(',') 
                if data1[0]!= "": 
                    TempData.append(float(data1[0])) 
                datastr=data1[2]

        # Falls nötig auf Buffersize auffüllen
        while len(TempData) < self.BufferSize:
             TempData.append(float(0))
        TempData.append(float(Data))

        # Alte Werte verwerfen
        s = len(TempData)- self.BufferSize
        Buffer = TempData[s:]
        
        #Daten schreiben
        d=open(self.Path,'w')
        for i in range(self.BufferSize):
            d.write('{0:0.1f},'.format(Buffer[i]))
        d.close()
        
        return Buffer    
