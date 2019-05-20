def calculateMaxLoanTenure(ageFirstApplicant,ageSecondApplicant,remainingLease):
    averageAge=(ageFirstApplicant+ageSecondApplicant)/2
    cover=averageAge+remainingLease
    if cover <80:
        print("not okay")
    else:
        print("max years of loan tenure is",min(25,65-averageAge,remainingLease-20))



def calculateEligibilty(incomeFirstApplicant,incomeSecondApplicant):

        parentsIncome=incomeFirstApplicant+incomeSecondApplicant
        differ=12000-parentsIncome
        if differ<0:
            print("Not eligible for Scheme")
      

        withinLimit=[]
        for i in childrenSalary:
            if i<=differ:
                withinLimit.append(i)
                print("Wihtin",withinLimit)

            if len(withinLimit)==0:
                print("Exceed Income")            
          
        for i in withinLimit:
            childrenSalary.remove(i)
            print("Here",childrenSalary)
            if sum(childrenSalary)<12000:
                if (differ+i+sum(childrenSalary))<18000:
                    print("Eligible")
            childrenSalary.append(i)


#Question 1(i)
numberOfApplicants=int(input("Enter number of applicants, valid values from 1 to 2:"))
if numberOfApplicants !=1 and numberOfApplicants !=2:
    print("Invalid input, valid values are 1 and 2")

#Question 1(ii)
print("Enter whether one least one buyer is Singapore citizenship")
isSingaporeans=(input("Enter either Y for Yes or N for No:")).upper()
if isSingaporeans!="Y":
    print("At least one buyer must be a Singapore citizen")



#Question 1(iii)
numberOfHDBLoans=int(input("Enter number of HDB loans taken previously, valid values from 0:"))
if numberOfHDBLoans>=2:
    print("Exceeded number of permitt loans")

#Question 1(iv)
print("Enter whether last owned property is a private residential property (local or overseas) such as:\n- HUDC flat\n- Property acquired by gift\n- Property inherited as a beneficiary under a will or as a result of the Intestate Succession Act\n- Property owned/ acquired/ disposed of through nominees")

isOwnProperty=input("Enter either Y for Yes or N for No:").upper()
if isOwnProperty =="Y" and numberOfHDBLoans>1:
    print("Not Eligible for loan")


#Question 1(v)
print("Enter which scheme loan is made under")
loanScheme=input("Enter either F for Family or E for Extended family or S for Single:").upper()

#for Extended Family Loan
if loanScheme =="E":
    incomeFirstApplicant=int(input("Enter monthly income of first applicant, valid values from 0.0:"))
    incomeSecondApplicant=int(input("Enter monthly income of Second applicant, valid values from 0.0:"))
    numberOfChildren=int(input("Enter number of children, valid values from 1:"))
    print("Enter whether any child in household is married or applied HDB Fiance/Fiancee Scheme")
    marriedOrFiancee=input("Enter either Y for Yes or N for No:").upper()
    if marriedOrFiancee=="Y":
        incomeMarriedChild=int(input("Enter monthly income of child married or has applied HDB Fiance/Fiancee Scheme,valid values from 0.0"))
        incomeSpouse=int(input("Enter monthly income of fiance/fiancee/spouse of child, valid values from 0.0"))

    incomeSingleChild=int(input("Enter monthly income of any single child, valid values from 0.0:"))

    if marriedOrFiancee=="N":
        childrenSalary=[]
        userInput=int(input("Enter the number of children"))
        def childrenInput(userInput):
            for i in range(numberOfChildren):
                userInputSalary=int(input("Enter the salary of"+str(i+1)+"child"))
                childrenSalary.append(userInputSalary)
        childrenInput(userInput)

   
#Question 1(vii)
print("Enter whether you have owned or have disposed of any private residential property in the 30 months before the date of application for an HDB Loan Eligibility (HLE) letter.\nA private residential property (local or overseas) will include:\n- Property acquired by gift\n-Property inherited as a beneficiary under a will or as a result of the\nIntestate Succession Act\n-Property owned/ acquired/ disposed of through nominees")

isOwnPropertyBefore=input("Enter either Y for Yes or N for No:").upper()
if isOwnPropertyBefore=="Y":
    print("Not Eligible for Loans")
   
#Question 1(viiI)
numberOfIndustrialProperty=int(input("Enter number of market/ hawker stall or commercial/ industrial property you currently owned, valid values from 0:"))
if numberOfIndustrialProperty ==1:
    print("Enter whether operating the business there, and have no other sources of income")
    isOperatingBusiness=input("Enter either Y for Yes or N for No:").upper()
    if isOperatingBusiness =="Y":
        print("Not Eligible for Loan")

ageFirstApplicant=int(input("Enter age of first applicant, valid values from 21.0"))
ageSecondApplicant=int(input("Enter age of second applicant, valid values from 21.0"))

remainingLease=int(input("Enter number of years of remaining lease, valid values from 1 to 99:"))


calculateMaxLoanTenure(ageFirstApplicant,ageSecondApplicant,remainingLease)


    

    
