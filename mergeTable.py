import csv

from csv import writer

with open("Table1.csv", "r+") as T1:
    table1 = csv.reader(T1)

    with open("Table2.csv", "r+") as T2:
        table2 = csv.reader(T2)

        with open("Table3.csv", "r+") as T3:
            table3 = csv.reader(T3)

            with open("combineTable.csv", "a", newline='') as Tmerge:
                Tmerge.writelines("START OF DOC")
                Tmerge.writelines('\n')
                Tmerge.writelines("Table1")
                Tmerge.writelines('\n')

                writer_object = writer(Tmerge)
                for table1_row in table1:
                    writer_object.writerow(table1_row)

                Tmerge.writelines('\n')
                Tmerge.writelines("Evaluate")
                Tmerge.writelines('\n')
                Tmerge.writelines('\n')
                Tmerge.writelines('\n')
                Tmerge.writelines("Table2")
                Tmerge.writelines('\n')

                writer_object2 = writer(Tmerge)
                for table2_row in table2:
                    writer_object2.writerow(table2_row)

                Tmerge.writelines('\n')
                Tmerge.writelines("Cred=Oauth")
                Tmerge.writelines('\n')
                Tmerge.writelines("ID=202365")
                Tmerge.writelines('\n')
                Tmerge.writelines('\n')

                writer_object3 = writer(Tmerge)
                for table3_row in table3:
                    writer_object2.writerow(table3_row)

                Tmerge.writelines('\n')
                Tmerge.writelines('\n')
                Tmerge.writelines("upload=True")
                Tmerge.writelines('\n')
                Tmerge.writelines("END")
                Tmerge.close()
        T3.close()
    T2.close()
T1.close()







