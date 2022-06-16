import cmd


class PrintHelper:
    def __init__(self) -> None:
        pass

    def printHeader(self, header):
        print('')
        print(f'~~~~~~~~~~~~{header}~~~~~~~~~~~~')

    def printFooter(self, msg):
        print('----------------------------------')
        print(msg)
        print('----------------------------------')

    def printColumn(self, stringList, colWidth, colName):
        cli = cmd.Cmd()
        self.printHeader(colName)
        cli.columnize(stringList, displaywidth=colWidth)
        print('')

    def printMenu(self, options, menuName):
        self.printHeader(menuName)
        for i in options:
            print(i)
        print('------------------------')
        print('')
