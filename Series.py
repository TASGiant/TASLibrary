class FromTo:

    @staticmethod
    def add(firstnum, addnum, lastnum):

        try:
            while firstnum <= lastnum:
                addnum = addnum + firstnum
                firstnum = firstnum + 1
        except TypeError:
            print("Plese input 3 integer number!")
        finally:
            return addnum

    class Print:
        @staticmethod
        def add(firstnum, addnum, lastnum):
            try:
                while firstnum <= lastnum:
                    addnum = addnum + firstnum
                    firstnum = firstnum + 1
            except TypeError:
                print("Plese input 3 integer number!")
            finally:
                print(addnum)
