def print_operation_table (operation, num_rows, num_columns):

   for x in range(1,num_rows+1):
    if x==1:
        print (x,'\t','\t'.join(str(y) for y in range(1,num_columns+1)))   
    else:
        print (x,'\t','\t'.join(str(operation(x,y)) for y in range(1,num_columns+1)))

print("Таблица умножения")
print_operation_table(lambda x,y:x*y, 10, 10)
print("Таблица степеней")
print_operation_table(lambda x,y:x**y, 5, 5)
print("Таблица сложения")
print_operation_table(lambda x,y:x+y, 10, 10)



