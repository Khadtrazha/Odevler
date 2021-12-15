def bubble_sort(dizi):
    for i in range(len(dizi)-1):
        for j in range(len(dizi) -1 -i):
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j+1] = dizi [j+1], dizi[j]
     
                
def selection_sort(dizi):
    for i in range(len(dizi)):
        min_index = i
        for j in range(i+1,len(dizi)):
            if dizi[min_index] > dizi[j]:
                min_index = j
        if min_index != i:
            dizi[min_index],dizi[i] = dizi[i],dizi[min_index]


def insertion_sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j = i -1
        while j >=0 and key < dizi[j]:
            dizi[j+1] = dizi[j]
            j = j -1
        dizi[j+1] = key
        
        
def merge(dizi):
    if len(dizi) > 1:
        orta = len(dizi) // 2
        solDizi = dizi[:orta]
        sagDizi = dizi[orta:]
        merge(solDizi)               
        merge(sagDizi)
        
        mergeSort(dizi, solDizi, sagDizi)

def mergeSort(dizi,solDizi,sagDizi):
    i = 0
    j = 0
    k = 0        
    
    while i < len(solDizi) and j < len(sagDizi):
        if solDizi[i] < sagDizi[j]:
            dizi[k] = solDizi[i]            
            i = i +1
        else:
            dizi[k] = sagDizi[j]
            j =j +1
        k = k +1
    while i < len(solDizi):
        dizi[k] = solDizi[i]
        i = i +1
        k = k +1
    while j < len(sagDizi):
        dizi[k] = sagDizi[j]
        j = j +1
        k = k +1

def partition(arr,low,high):
    i = ( low-1 )        
    pivot = arr[high]     
 
    for j in range(low , high):
 
       
        if   arr[j] <= pivot:
         
      
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
def quickSort(arr,low,high):
    if low < high:
 
      
        pi = partition(arr,low,high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
                
sirasiz_dizi = [3,10,15,2,1,80,55,72,43,102]

bubble_sort(sirasiz_dizi)
print(sirasiz_dizi)

selection_sort(sirasiz_dizi)
print(sirasiz_dizi)

insertion_sort(sirasiz_dizi)
print(sirasiz_dizi)

merge(sirasiz_dizi)
print(sirasiz_dizi)

quickSort(sirasiz_dizi, 0, len(sirasiz_dizi)- 1)
print(sirasiz_dizi)

