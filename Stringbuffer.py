# -*- coding: utf-8 -*-
class Stringbuffer:
    def __init__(self, Path, BufferSize):    #Konstrukor
        self.Path= Path
        self.BufferSize=BufferSize
        try:
            d=open(self.Path)
        except:
            #Keine Daten -> Erstelle leere Datei
            d=open(self.Path,'w')
            for i in range(self.BufferSize):
                d.write('nc,')
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
                    TempData.append((data1[0])) 
                datastr=data1[2]

        # Falls nötig auf Buffersize auffüllen
        while len(TempData) < self.BufferSize:
             TempData.append('nc')
             
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
                    TempData.append((data1[0])) 
                datastr=data1[2]

        # Falls nötig auf Buffersize auffüllen
        while len(TempData) < self.BufferSize:
             TempData.append('nc')
             
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
                    TempData.append((data1[0])) 
                datastr=data1[2]

        # Falls nötig auf Buffersize auffüllen
        while len(TempData) < self.BufferSize:
             TempData.append('nc')
        TempData.append((Data))

        # Alte Werte verwerfen
        s = len(TempData)- self.BufferSize
        Buffer = TempData[s:]
        
        #Daten schreiben
        d=open(self.Path,'w')
        for i in range(self.BufferSize):
            d.write(Buffer[i]+',')
        d.close()
        
        return Buffer    
