import numpy as np

class DataAnalytics:
    def __init__(self):
        self.current_array = None
        
    @classmethod
    def welcome(cls):
        print("Welcome to the NumPy Analyzer!!")
        print("="*50)

    @staticmethod
    def main_menu():
        print("\nChoose an option:")
        print("1.Create a numpy array.")
        print("2.Perform Mathematical Operation.")
        print("3.Combine or Split array.")
        print("4.Search, Sort, or Filter Array.")
        print("5.Compute Aggregates and Statistics")
        print("6.Exit")
        
    def __indexing(self):
        arr = self.current_array
        print(f"\nCurrent Array: \n{arr}")

        if arr.ndim == 1:
            index = int(input("\nEnter Index Value:"))

            try:
                print(f"\nElement at entered Index {index}: {arr[index]}")

            except:
                print("\nIndex out of range!!")

        elif arr.ndim == 2:
            r = int(input("\nEnter Row Index: "))
            c = int(input("Enter Column Index: "))

            try:
                print(f"\nElement at [{r}][{c}]: {arr[r][c]}") 

            except:
                print("\nIndex out of Range!!")

        elif arr.ndim == 3:
            l = int(input("\nEnter Layer Index: "))
            r = int(input("Enter Row Index: "))
            c = int(input("Enter Column Index: "))

            try:
                print(f"\nElement at [{l}][{r}][{c}]: {arr[l][r][c]}")

            except:
                print("\nIndex Out of Range")

    def __slicing(self):
        arr = self.current_array
        print(f"\nCurrent Array: \n{arr}")

        if arr.ndim == 1:
            start = int(input("\nEnter Start Index: "))
            end = int(input("Enter End Index: "))

            try:
                print(f"\nSliced Array: {arr[start:end]}")

            except:
                print("\nIndex out of range!!")

        elif arr.ndim == 2:
            print(f"\nArray shape: {arr.shape[0]} rows x {arr.shape[1]} columns")

            r_start = int(input("\nEnter start Row Index: "))
            r_end = int(input("Enter end Row Index: "))
            c_start = int(input("\nEnter start Column Index: "))
            c_end = int(input("Enter end Column Index: "))

            try:
                print(f"\nSliced Array: \n{arr[r_start:r_end, c_start:c_end]}")

            except:
                print("\nIndex out of Range!!")

        elif arr.ndim == 3:
            print(f"\nArray shape: {arr.shape[0]} layers x {arr.shape[1]} rows x {arr.shape[2]} columns")

            l_start = int(input("\nEnter start Layer Index: "))
            l_end = int(input("Enter end Layer Index: "))
            r_start = int(input("\nEnter start Row Index: "))
            r_end = int(input("Enter end Row Index: "))
            c_start = int(input("\nEnter start Column Index: "))
            c_end = int(input("Enter end Column Index: "))

            try:
                sliced = arr[l_start:l_end, r_start:r_end, c_start:c_end]

            except:
                print("\nIndex out of Range!!")

            else:
                print(f"\nSliced Array: \n{sliced}")

    def create_array(self):
        while True:
            print("\nSelect the type of array to create:")
            print("1.1D Array")
            print("2.2D Array")
            print("3.3D Array")
            print("4.Go Back")

            option = int(input("\nEnter your choice:"))

            match option:
                case 1:
                    ele = input("\nEnter your elements as space separated(1D Array): ")
                    elements = [int(i) for i in ele.split()]
                    arr = np.array(elements)
                    print(f"\nCreated 1D Array: \n{arr}")

                case 2:
                    row = int(input("\nEnter number of Rows: "))
                    col = int(input("Enter number of columns: "))
                    ele = input(f"\nEnter total {row*col} Elemnts as space separated: ")
                    elements = [int(i) for i in ele.split()]
                    arr = np.array(elements).reshape(row, col)
                    print(f"\nCreated 2D Array: \n{arr}")

                case 3:
                    layer = int(input("\nEnter depth of the array: "))
                    row = int(input("Enter number of Rows: "))
                    col = int(input("Enter number of columns: "))
                    ele = input(f"\nEnter total {layer*row*col} Elemnts as space separated: ")
                    elements = [int(i) for i in ele.split()] 
                    arr = np.array(elements).reshape(layer, row, col)
                    print(f"\nCreated 3D Array: \n{arr}")
                
                case 4:
                    print("\nGoing to main menu...")
                    break
                
                case _:
                    print("\nInvalid Input!!")

            print("\nChoose an operation(You can perform this operation only after creating array...):")
            print("1.Indexing")
            print("2.Slicing")
            print("3.Go Back")

            operation = int(input("\nEnter your choice:"))
    
            match operation:
                case 1:
                    self.__indexing()
                    
                case 2:
                    self.__slicing()
                    
                case 3:
                    print("\nGoing to main menu...")
                    break
                
                case _:
                    print("\nInvalid Input!!")

    def math_operation(self):
        while True:
            print("\nChoose a Mathematical Operation:")
            print("1.Element-Wise Addition")
            print("2.Element-Wise Subtraction")
            print("3.Element-Wise Multiplication")
            print("4.Element-Wise Division")
            print("5.Dot Product")
            print("6.Matrix Multiplication")
            print("7.Retun to Main Menu")

            math_op = int(input("\nEnter your choice:"))
            
            if math_op == 7:
                print("\nGoing into main menu...")
                break
            
            row = int(input("\nEnter the number of rows: "))
            col = int(input("Enter the number of columns: "))
        
            ele1 = input(f"\nEnter total {row*col} Elemnts as space separated: ")
            elements = [int(i) for i in ele1.split()]
            array1 = np.array(elements).reshape(row, col)
            print(f"\nFirst Array: \n{array1}")
        
            ele2 = input(f"\nEnter total {row*col} Elemnts as space separated: ")
            elements2 = [int(i) for i in ele2.split()]
            array2 = np.array(elements2).reshape(row, col)
            print(f"\nSecond Array: \n{array2}")
                    
            match math_op:
                case 1:
                    print(f"\nAddition of both array: \n{np.add(array1, array2)}")
            
                case 2:
                    print(f"\nSubtraction of both array: \n{np.subtract(array1, array2)}")
                    
                case 3:
                    print(f"\nMultiplication both array: \n{np.multiply(array1, array2)}")
                    
                case 4:
                    print(f"\nDivision of both array: \n{np.divide(array1, array2)}")
                    
                case 5:
                    if row == col:
                        print(f"\nDot Product of Array: \n{np.dot(array1, array2)}")
                        
                    else:
                        print("\nDot Product is not possible!!")
                
                case 6:
                    if row == col:
                        print(f"\nMatrix Multiplication: \n{np.matmul(array1, array2)}")
                        
                    else:
                        print("\nMatrix Multiplication not Possible!!")
                
                
                case _:
                    print("\nInvalid Input!!")
    
    def __combine_arr(self):
        print("\nHow would you like to combine Array?")
        print("1.Side by Side(Horizontally)")
        print("2.One on to another(Vertical)")
        
        com_choice = int(input("\nEnter your Choice:"))
        
        row = int(input("\nEnter the number of rows: "))
        col = int(input("Enter the number of columns: "))
    
        ele1 = input(f"\nEnter total {row*col} Elemnts as space separated(array1): ")
        elements = [int(i) for i in ele1.split()]
        array1 = np.array(elements).reshape(row, col)
        print(f"\nFirst Array: \n{array1}")
    
        ele2 = input(f"\nEnter total {row*col} Elemnts as space separated(array2): ")
        elements2 = [int(i) for i in ele2.split()]
        array2 = np.array(elements2).reshape(row, col)
        print(f"\nSecond Array: \n{array2}")
        
        match com_choice:
            case 1:
                com_h = np.hstack((array1, array2))
                print(f"\nHorizontally Combined Array: \n{com_h}")
                
            case 2:
                com_v = np.vstack((array1, array2))
                print(f"\nVertically Combined Array: \n{com_v}")
                
            case _:
                print("\nInvalid Input!!")
                
    def __split_arr(self):
        arr = self.current_array
        print("\nHow would you like to split array?")
        print("1.Horizontal split")
        print("2.Vertical split")

        split_choice = int(input("\nEnter your Choice:"))
        print(f"\nOriginal Array: \n{arr}")

        parts = int(input("\nEnter number of parts you want to split into: "))

        match split_choice:
            case 1:
                if arr.ndim == 1 or arr.ndim == 2:
                    try:
                        split_h = np.hsplit(arr, parts)
                    except:
                        print("\nCannot Split into equal parts!!")
                    else:
                        print(f"\nSplited Array Horizontally: \n{split_h}")

                elif arr.ndim == 3:
                    if arr.shape[2] % parts == 0:
                        split_h = np.hsplit(arr, parts)
                        print(f"\nSplited Array Horizontally: \n{split_h}")

                    else:
                        print("\nCannot Split into equal parts!!")

            case 2:
                if arr.ndim == 1:
                    print("\nVertical split is not applicable for 1D array!")

                elif arr.ndim == 2:
                    try:
                        split_v = np.vsplit(arr, parts)
                    except:
                        print("\nCannot Split into equal parts!!")
                    else:
                        print(f"\nSplited Array Vertically: \n{split_v}")

                elif arr.ndim == 3:
                    if arr.shape[0] % parts == 0:
                        split_v = np.vsplit(arr, parts)
                        print(f"\nSplited Array Vertically: \n{split_v}")

                    else:
                        print("\nCannot Split into equal parts!!")

            case _:
                print("\nInvalid Input!!")

    def combine_split(self):
        while True:
            print("\nChoose an Option: ")
            print("1.Combine arrays")
            print("2.Split Arrays")
            print("3.Return to Main Menu")
            
            option1 = int(input("Enter your option: "))
            
            match option1:
                case 1:
                    self.__combine_arr()

                case 2:
                    self.__split_arr()
                    
                case 3:
                    print("Going to main menu...")
                    break
                
                case _:
                    print("Invalid Input!!")
    
    def __search(self):
        arr = self.current_array
        print(f"\nOriginal Array: \n{arr}")
        value = int(input("\nEnter value to search: "))
        result = np.where(arr == value)
        
        if len(result[0]) == 0:
            print("\nValue not found!!")
            
        else:
            if arr.ndim == 1:
                for i in result[0]:
                    print(f"\nValue found at Index: {i}")
                    
            elif arr.ndim == 2:
                for r, c in zip(result[0], result[1]):
                    print(f"\nValue found at Row: {r}, Column: {c}")
                    
            elif arr.ndim == 3:
                for l, r, c in zip(result[0], result[1], result[2]):
                    print(f"\nValue found at Layer: {l}, Row: {r}, Column: {c}")
    
    def __sort(self):
        arr = self.current_array
        print(f"\nOriginal Array: \n{arr}")
        print("\nChoose sort order:")
        print("1.Ascending Order")
        print("2.Descending Order")
        
        order = int(input("\nEnter your choice:"))
        if arr.ndim ==1:
            match order:
                case 1:
                    sort_arr = np.sort(arr)
                    print(f"\nSorted Array in Ascending Order: \n{sort_arr}")
                    
                case 2:
                    sort_arr = np.sort(arr)[::-1]
                    print(f"\nSorted Array in Descendind Order: \n{sort_arr}")
                    
                case _:
                    print("\nInvalid Input!!")
                    
        else:
            print("\nChoose sort axis:")
            print("1.Row-Wise")
            print("2.Column-Wise")
            axis = int(input("\nEnter your choice: "))
            
            if axis == 1:
                match order:
                    case 1:
                        sort_arr = np.sort(arr, axis=1)
                        print(f"\nSorted Array in Ascending Order (Row-Wise): \n{sort_arr}")
                        
                    case 2:
                        sort_arr = np.sort(arr, axis=1)[:, ::-1]
                        print(f"\nSorted Array in Descending Order (Row-Wise): \n{sort_arr}")
                        
                    case _:
                        print("\nInvalid Input!!")
                        
            elif axis == 2:
                match order:
                    case 1:
                        sort_arr = np.sort(arr, axis=0)
                        print(f"\nSorted Array in Ascending Order (Column-Wise): \n{sort_arr}")
                        
                    case 2:
                        sort_arr = np.sort(arr, axis=0)[::-1, :]
                        print(f"\nSorted Array in Descending Order (Column-Wise): \n{sort_arr}")
                        
                    case _:
                        print("\nInvalid Input!!")
                    
            else:
                print("\nInvalid Input!!")
    
    def __filter(self):
        arr = self.current_array
        print(f"\nOriginal Array: \n{arr}")
        print("\nChoose filter condition: ")
        print("1.Greater than a value")
        print("2.Less than a value")
        print("3.Equal to a value")
        
        filter = int(input("\nEnter your choice: "))
        val = int(input("\nEnter a value: "))
        
        match filter:
            case 1:
                filtered = arr[arr > val]
                print(f"\nElements greater than {val}: \n{filtered}")
                
            case 2:
                filtered = arr[arr < val]
                print(f"\nElements less than {val}: \n{filtered}")
                
            case 3:
                filtered = arr[arr == val]
                print(f"\nElements equal to {val}: \n{filtered}")
                
            case _:
                print("\nInvalid Input!!")
    
    def search_sort_filter(self):
        while True:
            print("\nChoose an Option: ")
            print("1.Search a value")
            print("2.Sort the Array")
            print("3.Filter values")
            print("4.Return to Main Menu")
            
            option2 = int(input("\nEnter your option: "))
            
            match option2:
                case 1:
                    self.__search()
                    
                case 2:
                    self.__sort()
                    
                case 3:
                    self.__filter()
                    
                case 4:
                    print("\nGoing to main menu...")
                    break
                
                case _:
                    print("\nInvalid Input!!")
    
    def __aggregation(self):
        arr = self.current_array
        print("\nChoose an Aggregation Operation: ")
        print("1.Sum")
        print("2.Mean")
        print("3.Meadian")
        print("4.Standard Deviation")
        print("5.Variance")
        
        op1 = int(input("\nChoose operation:"))
        print(f"\nOriginal Array: \n{arr}")
        
        match op1:
            case 1:
                print(f"\nSum of Array: {np.sum(arr)}")
                
            case 2:
                print(f"\nMean of Array: {np.mean(arr)}")
                
            case 3:
                print(f"\nMedian of Array: {np.median(arr)}")

            case 4:
                print(f"\nStandard Deviation of Array: {np.std(arr)}")
                
            case 5:
                print(f"\nVariance of Array: {np.var(arr)}")
            
            case _:
                print("\nInvalid Input!!")

    def __statistical(self):
        arr = self.current_array
        print("\nChoose Statistical Operation:")
        print("1.Maximum value")
        print("2.Minimum value")
        print("3.Percentiles")
        print("4.Corelation co-efficient")
        
        op2 = int(input("\nChoose operation:"))
        match op2:
            case 1:
                print(f"\nMaximum of Array: {np.max(arr)}")
            
            case 2:
                print(f"\nMinimum of Array: {np.min(arr)}")
            
            case 3:
                p = int(input("\nEnter percentile value: "))
                print(f"\nPercentile of Array: {np.percentile(arr, p)}")
            
            case 4:
                if arr.ndim == 2:
                    print(f"\nCorelation co-efficient of Array: \n{np.corrcoef(arr)}")
                    
                else:
                    print("\nCorelation Co-efficient onlt applicable for 2D array.")
            
            case _:
                print("\nInvalid Input!!")
                
    def aggregation_statistical(self):
            while True:
                print("\nChoose an operation:")
                print("1.Aggregation")
                print("2.Statistical")
                print("3.Return to main menu")
                
                operation1 = int(input("\nChoose operation:"))
                match operation1:
                    case 1:
                        self.__aggregation()
                        
                    case 2:
                        self.__statistical()
                        
                    case 3:
                        print("\nGoing to main menu...")
                        break
                    
                    case _:
                        print("\nInvalid Input!!")
        
    def run(self):
        DataAnalytics.welcome()
        
        while True:
            DataAnalytics.main_menu()
            choice = int(input("\nEnter your choice: "))
            
            match choice:
                case 1:
                    self.create_array()
                    
                case 2:
                    self.math_operation()
                    
                case 3:
                    self.combine_split()
                    
                case 4:
                    self.search_sort_filter()
                    
                case 5:
                    self.aggregation_statistical()
                    
                case 6:
                    print("\nThank you for using the NumPy Analyzer!! \nGood Bye!!")
                    break
                
                case _:
                    print("\nInvalid Input!!")
                
analyzer = DataAnalytics()
analyzer.run() 