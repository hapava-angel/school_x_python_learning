class Matrix:  
    def __init__(self, rows, columns):  
        self.rows = rows  
        self.columns = columns  
        self.data = [[0 for x in range(columns)] for y in range(rows)]  
    def add(self, other):  
        if self.rows != other.rows or self.columns != other.columns:  
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")  
        result = Matrix(self.rows, self.columns)  
        for i in range(self.rows):  
            for j in range(self.columns):  
                result.data[i][j] = self.data[i][j] + other.data[i][j]  
        return result  
    def subtract(self, other):  
        if self.rows != other.rows or self.columns != other.columns:  
            raise ValueError("Матрицы должны быть одинакового размера для вычитания.")  
        result = Matrix(self.rows, self.columns)  
        for i in range(self.rows):  
            for j in range(self.columns):  
                result.data[i][j] = self.data[i][j] - other.data[i][j]  
        return result  
    def multiply(self, other):  
        if self.columns != other.rows:  
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")  
        result = Matrix(self.rows, other.columns)  
        for i in range(self.rows):  
            for j in range(other.columns):  
                for k in range(self.columns):  
                    result.data[i][j] += self.data[i][k] * other.data[k][j]  
        return result  
    def transpose(self):  
        result = Matrix(self.columns, self.rows)  
        for i in range(self.rows):  
            for j in range(self.columns):  
                result.data[j][i] = self.data[i][j]  
        return result 
    def __str__(self):  
        output = ""  
        for row in self.data:  
            output += "\t".join(str(element) for element in row)  
            output += "\n"  
        return output  