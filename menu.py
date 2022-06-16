import inputHelper
import navigation


class Menu:
    def __init__(self) -> None:
        self.__common = 'Enter from above options: '
        self.__inputHelper = inputHelper.InputHelper()
        self.__nav = navigation.Navigation()
        self.__dvdListPage = 1
        self.__customerListPage = 1

    def mainMenu(self):
        nav = self.__nav
        options = [
            # 'Enter 1 to view list of DVDs',
            'Enter 1 to search for DVD',
            'Enter 2 to rent DVD',
            'Enter 3 to return DVD',
            'Enter 4 to access Admin Options',
            'Enter 5 to quit.'
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'Main Menu')

        match option:
            # case 1:
            #     nav.showDvdLists(self.__dvdListPage)
            #     self.dvdMneu()
            case 1:
                searchText = self.searchPrompt()
                results = nav.searchTitle(searchText, self.__dvdListPage)
                if results:
                    self.dvdMneu()
            case 2:
                nav.showDvdLists(self.__dvdListPage)
                self.dvdMneu()
            case 3:
                nav.showCustomerList(self.__customerListPage)
                self.customerMenu('return')
            case 4:
                self.adminMenu()
            case 5:
                return
            
    def transactionMenu(self):
        nav = self.__nav
        self.dvdMneu()
        
   

    def adminMenu(self):
        nav = self.__nav
        options = [
            'Enter 1 to view Customer List',
            'Enter 2 to add new Customer',
            'Enter 3 to update Customer details',
            'Enter 4 to add new DVD',
            'Enter 5 to update DVD',
            'Enter 6 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'Admin Options')
        match option:
            case 1:
                nav.showCustomerList(self.__customerListPage)
                self.customerMenu()
            case 2:
                return
            case 3:
                return
            case 4:
                return
            case 5:
                nav.showDvdLists(self.__dvdListPage)
                self.dvdEditMenu()
            case 6:
                self.mainMenu()

    def dvdEditMenu(self):
        
        def saveConfirmation(check):
            if check == 1:
                nav.saveDetails('update')
            elif check == 2:
                self.mainMenu()
                
        nav = self.__nav
        options = [
            'Enter 1 to check out another page',
            'Enter 2 to view and/or edit DVD details',
            'Enter 3 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'DVD Edit Menu')

        match option:
            case 1:
                pageNum = self.detailsMenu('page')
                if pageNum == 'exit':
                    self.mainMenu()
                else:
                    nav.showDvdLists(pageNum)
                    self.dvdMneu()
            case 2:
                id = self.detailsMenu('ID')
                if id == 'exit':
                    self.mainMenu()
                else:
                    nav.showDvdDetails(id)
                    editOptions = [
                        '1 -> Title',
                        '2 -> Summary',
                        '3 -> Number of Copies in Store',
                        '4 -> Exit to DVD Menu'
                    ]
                    editOptions = self.__inputHelper.menuInput(
                        self.__common, editOptions, 'Select Option')

                    match editOptions:
                        case 1:
                            nav.upateDvdDetails('title')
                            check = self.confirmMenu()
                            saveConfirmation(check)
                        case 2:
                            nav.upateDvdDetails('summary')
                            check = self.confirmMenu()
                            saveConfirmation(check)
                        case 3:
                            nav.upateDvdDetails('copies')
                            check = self.confirmMenu()
                            saveConfirmation(check)
                        case 4:
                            self.dvdEditMenu()
            case 3:
                self.mainMenu()
                
        

    def dvdMneu(self):
        nav = self.__nav
        options = [
            'Enter 1 to check out another page',
            'Enter 2 to view DVD details',
            'Enter 3 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'DVD Options')
        match option:
            case 1:
                pageNum = self.detailsMenu('page')
                if pageNum == 'exit':
                    self.mainMenu()
                else:
                    nav.showDvdLists(pageNum)
                    self.dvdMneu()
            case 2:
                dvdID = self.detailsMenu('ID')
                if dvdID == 'exit':
                    self.mainMenu()
                else:
                    nav.showDvdDetails(dvdID)
                    self.dvdDetailsMenu(dvdID)
            case 3:
                self.mainMenu()

    def dvdDetailsMenu(self, dvdID):
        nav = self.__nav
        options = [
            'Enter 1 to rent this DVD',
            'Enter 2 to continue viewing DVDs',
            'Enter 3 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'DVD Options')
        
        match option:
           case 1:
                options = [
                    'Enter 1 to rent exisiting customer',
                    'Enter 2 to rent for new customer',
                    'Enter 3 for Main Menu',
                ]
                option = self.__inputHelper.menuInput(
                    self.__common, options, 'DVD Options')
                
                match option:
                    case 1:
                        nav.showCustomerList(self.__customerListPage)
                        self.customerMenuForRent(dvdID)
                    case 2:
                        pass
                    case 3:
                        self.mainMenu()
           case 2:
               pass
           case 3:
               self.mainMenu() 

    def checkOut(self):
        nav = self.__nav
        options = [
            'Enter 1 check-out this DVD',
            'Enter 2 to continue viewing more DVDs',
            'Enter 3 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'Check-Out')
        match option:
            case 1:
                return
            case 2:
                nav.showDvdLists(self.__dvdListPage)
                self.dvdMneu()
            case 3:
                self.mainMenu()

    def customerMenuForRent(self, dvdID):
        nav = self.__nav
        options = [
            'Enter 1 to check out another page',
            'Enter 2 to enter customer ID',
            'Enter 3 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'Customer Menu')
        match option:
            case 1:
                pageNum = self.detailsMenu('page')
                if pageNum == 'exit':
                    self.mainMenu()
                else:
                    nav.showCustomerList(pageNum)
                    self.customerMenu()
            case 2:
                id = self.detailsMenu(None, 'DVD ID to rent')
                if id == 'exit':
                    self.mainMenu()
                else:
                    nav.showTransaction(dvdID, id)
                    self.customerMenu()
            case 3:
                self.mainMenu()

    def customerMenu(self, menuType=None):
        nav = self.__nav
        options = [
            'Enter 1 to check out another page',
            'Enter 2 to view Customer details',
            'Enter 3 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'Customer Menu')
        match option:
            case 1:
                pageNum = self.detailsMenu('page')
                if pageNum == 'exit':
                    self.mainMenu()
                else:
                    nav.showCustomerList(pageNum)
                    self.customerMenu()
            case 2:
                cusID = self.detailsMenu('ID')
                if cusID == 'exit':
                    self.mainMenu()
                else:
                    nav.showCustomerDetail(cusID)
                    if menuType == 'return':
                        self.customerMenuForReturn(cusID)
                    else:
                        self.customerMenu()
            case 3:
                self.mainMenu()
                
    def customerMenuForReturn(self, cusID):
        nav = self.__nav
        options = [
            'Enter 1 to enter DVD ID for returing',
            'Enter 3 for Main Menu',
        ]
        option = self.__inputHelper.menuInput(
            self.__common, options, 'Customer Menu')
        match option:
            case 1:
                dvdID = self.detailsMenu(None, 'DVD ID to return')
                if dvdID == 'exit':
                    self.mainMenu()
                else:
                    nav.showTransactionReturn(dvdID, cusID)
                    self.customerMenu()
            case 2:
                self.mainMenu()
                

    def searchPrompt(self):
        msg = f'Enter the Movie Title: '
        return self.__inputHelper.stringInput(msg,'any')
    
    def detailsMenu(self, promptType, promptType2=None):
        if promptType2:
            msg = f'Enter {promptType2} OR \'exit\' for Main Menu: '
        else:
            msg = f'Enter {promptType} number to view details OR \'exit\' for Main Menu: '
        return self.__inputHelper.detailsMenuInput(msg)

    def confirmMenu(self):
        msg = 'Save updated details to file?'
        options = [
            'Enter 1 to save new details to file',
            'Enter 2 cancel and exit to main menu',
        ]
        option = self.__inputHelper.menuInput(
            msg, options, 'Confirmation')
        return option
