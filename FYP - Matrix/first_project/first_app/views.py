from django.shortcuts import render
from . import forms
import numpy as np
import scipy as sp
from scipy import integrate
# Create your views here.
BeamLengthList = []
PinSupLoc = []
RollerSupLoc = []
FixSupLoc = []
PointLoadLoc = []
PointMag = []
PointAngle = []
MomentLoc = []
MomentMag = []
UDLStartLoc = []
UDLEndLoc = []
UDLMag = []
NDLStartLoc = []
NDLEndLoc = []
NDLStartMag = []
NDLEndMag = []

BeamLengthList0 = []
PinSupLoc0 = []
RollerSupLoc0 = []
FixSupLoc0 = []
PointLoadLoc0 = []
PointMag0 = []
PointAngle0 = []
MomentLoc0 = []
MomentMag0 = []
UDLStartLoc0 = []
UDLEndLoc0 = []
UDLMag0 = []
NDLStartLoc0 = []
NDLEndLoc0 = []
NDLStartMag0 = []
NDLEndMag0 = []
def index(request):
    return render(request,'basicapp/index.html')

def myview(request):
    BeamForm = forms.BeamForm()

    if request.method == 'POST':
        BeamForm = forms.BeamForm(request.POST)
#display entered form on command pormpt (feedback)
        if BeamForm.is_valid():
            '''print("NAME: ", BeamForm.cleaned_data['BeamLength'])
            print("NAME: ", BeamForm.cleaned_data['Pin_Support_Location'])
            print("NAME: ", BeamForm.cleaned_data['Roller_Support_Location'])
            print("NAME: ", BeamForm.cleaned_data['Fixed_Support_Location'])
            print("NAME: ", BeamForm.cleaned_data['Point_Load_Location'])
            print("NAME: ", BeamForm.cleaned_data['Point_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['Point_Angle'])
            print("NAME: ", BeamForm.cleaned_data['Moment_Location'])
            print("NAME: ", BeamForm.cleaned_data['Moment_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['UDL_Start_Location'])
            print("NAME: ", BeamForm.cleaned_data['UDL_End_Location'])
            print("NAME: ", BeamForm.cleaned_data['UDL_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['NDL_Start_Location'])
            print("NAME: ", BeamForm.cleaned_data['NDL_End_Location'])
            print("NAME: ", BeamForm.cleaned_data['NDL_Start_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['NDL_End_Magnitude'])'''
#Assign form variable to backend
            BeamLength = BeamForm.cleaned_data['BeamLength']
            Pin_Support_Location = BeamForm.cleaned_data['Pin_Support_Location']
            Roller_Support_Location = BeamForm.cleaned_data['Roller_Support_Location']
            Fixed_Support_Location = BeamForm.cleaned_data['Fixed_Support_Location']
            Point_Load_Location = BeamForm.cleaned_data['Point_Load_Location']
            Point_Magnitude = BeamForm.cleaned_data['Point_Magnitude']
            Point_Angle = BeamForm.cleaned_data['Point_Angle']
            Moment_Location = BeamForm.cleaned_data['Moment_Location']
            Moment_Magnitude = BeamForm.cleaned_data['Moment_Magnitude']
            UDL_Start_Location = BeamForm.cleaned_data['UDL_Start_Location']
            UDL_End_Location = BeamForm.cleaned_data['UDL_End_Location']
            UDL_Magnitude = BeamForm.cleaned_data['UDL_Magnitude']
            NDL_Start_Location = BeamForm.cleaned_data['NDL_Start_Location']
            NDL_End_Location = BeamForm.cleaned_data['NDL_End_Location']
            NDL_Start_Magnitude = BeamForm.cleaned_data['NDL_Start_Magnitude']
            NDL_End_Magnitude = BeamForm.cleaned_data['NDL_End_Magnitude']
#Append further entry into list
            BeamLengthList0.append(BeamLength)
            PinSupLoc0.append(Pin_Support_Location)
            RollerSupLoc0.append(Roller_Support_Location)
            FixSupLoc0.append(Fixed_Support_Location)
            PointLoadLoc0.append(Point_Load_Location)
            PointMag0.append(Point_Magnitude)
            PointAngle0.append(Point_Angle)
            MomentLoc0.append(Moment_Location)
            MomentMag0.append(Moment_Magnitude)
            UDLStartLoc0.append(UDL_Start_Location)
            UDLEndLoc0.append(UDL_End_Location)
            UDLMag0.append(UDL_Magnitude)
            NDLStartLoc0.append(NDL_Start_Location)
            NDLEndLoc0.append(NDL_End_Location)
            NDLStartMag0.append(NDL_Start_Magnitude)
            NDLEndMag0.append(NDL_End_Magnitude)

            BeamLengthList = list(filter(None,BeamLengthList0))
            PinSupLoc = list(filter(None,PinSupLoc0))
            RollerSupLoc = list(filter(None,RollerSupLoc0))
            FixSupLoc = list(filter(None,FixSupLoc0))
            PointLoadLoc = list(filter(None,PointLoadLoc0))
            PointMag = list(filter(None,PointMag0))
            PointAngle = list(filter(None,PointAngle0))
            MomentLoc = list(filter(None,MomentLoc0))
            MomentMag = list(filter(None,MomentMag0))
            UDLStartLoc = list(filter(None,UDLStartLoc0))
            UDLEndLoc = list(filter(None,UDLEndLoc0))
            UDLMag = list(filter(None,UDLMag0))
            NDLStartLoc = list(filter(None,NDLStartLoc0))
            NDLEndLoc = list(filter(None,NDLEndLoc0))
            NDLStartMag = list(filter(None,NDLStartMag0))
            NDLEndMag = list(filter(None,NDLEndMag0))

            #print(BeamLengthList)
            #print(PinSupLoc)
            #print(RollerSupLoc)
            #print(FixSupLoc)
            #print(PointLoadLoc)
            #print(PointMag)
            #print(PointAngle)
            #print(MomentLoc)
            #print(MomentMag)
            #print(UDLStartLoc)
            #print(UDLEndLoc)
            #print(UDLMag)
            #print(NDLStartLoc)
            #print(NDLEndLoc)
            #print("NDLStartMag: ",NDLStartMag)
            #print(NDLEndMag)

#convert list to float
            map(float,BeamLengthList)
            map(float,PinSupLoc)
            map(float,RollerSupLoc)
            map(float,FixSupLoc)
            map(float,PointLoadLoc)
            map(float,PointMag)
            map(float,PointAngle)
            map(float,MomentLoc)
            map(float,MomentMag)
            map(float,UDLStartLoc)
            map(float,UDLEndLoc)
            map(float,UDLMag)
            map(float,NDLStartLoc)
            map(float,NDLEndLoc)
            map(float,NDLStartMag)
            map(float,NDLEndMag)

#elements list consist of Pin sup and Roller sup location
            PinSupLoc1 = list(filter(None,PinSupLoc))
            elements = PinSupLoc + RollerSupLoc
            elements = list(filter(None,elements))

#Append Beam length list for and "0" into elements, these are the features which determines number of elements
            elements.append(float(BeamLengthList[0]))
            elements = list(filter(None,elements))
            elements.append( 0 )
            elements.sort()
            print("Elements list; 0, PinSupLoc, RollerSupLoc and Beam length [elements]:",elements)
            print("Number of elements: ",len(elements) - 1)


#Segmentize elements
            p2 = 0
            elements1 = []
            #Formula for number of element
            z1 = len(elements) - 1
            #Taking 2nd point in beam - first point in beam to get local beamlength
            while z1> 0:
                elements2 = float(elements[p2+1]) - float(elements[p2])
                p2 += 1
                z1 -= 1
                elements1.append(elements2)

            #elements1 is list of local beamlength
            print("Interval between elements [elements1]: ",elements1)

            #matrix elements#
            z = len(elements) - 1
            x = 1
            p = 0
            CounterA = 0
            Currentcount = 0
            StoreA = []
            Mlist = []

            while z> 0:
                A = np.array([
                [12/float(elements1[p])**3,6/float(elements1[p])**2,-12/float(elements1[p])**3,6/float(elements1[p])**2],
                [6/float(elements1[p])**2,4/float(elements1[p]),-6/float(elements1[p])**2,2/float(elements1[p])],
                [-12/float(elements1[p])**3,-6/float(elements1[p])**2,12/float(elements1[p])**3,-6/float(elements1[p])**2],
                [6/float(elements1[p])**2,2/float(elements1[p]),-6/float(elements1[p])**2,4/float(elements1[p])]
                ])
                CounterA += 1
                StoreA.append(CounterA)
                Currentcount = StoreA[-1]
                print("Current count is:", Currentcount)
                Mlist.append(A)
                print("Local stiffness matrix of element",x ,"\n",A)
                print("current element length: ",elements1[p])
                z = z - 1
                x = x + 1
                p = p + 1
                print("List of Local stiffness matrix are:\n",Mlist,"\n")
            #Global matrix
            A1 = 2
            A2 = Currentcount
            A3 = Currentcount*2
            A4 = 1
            A5 = 6
            A6 = 2
            A7 = 3

            GlobalM = np.zeros(shape=((A3)+2,(A3)+2))

            GlobalM1 = GlobalM
            #Assigning first matrix into emty matrix of 0
            GlobalM1[:4,:4] = Mlist[0][:4,:4]
            #adding the rest of matrix into global matrix
            '''Changed here\/'''
            if Currentcount == 1:
                GlobalM1 = Mlist[0]
                print("GlobalM1 = Mlist[0]")
            else:

                while 1:
                    #[2:5,2:5]
                    GlobalM1[A1:A5,A1:A5] = Mlist[A4][:4,:4]
                    #3,3
                    GlobalM1[A6,A6] = Mlist[A4][0,0] + Mlist[A4-1][2,2]
                    #3,4,2,3
                    GlobalM1[A6,A7] = Mlist[A4][0,1] + Mlist[A4-1][2,3]
                    #4,3

                    GlobalM1[A7,A6] = Mlist[A4][1,0] + Mlist[A4-1][3,2]
                    #4,4
                    GlobalM1[A7,A7] = Mlist[A4][1,1] + Mlist[A4-1][3,3]
                    A1 += 2
                    A5 += 2
                    A4 += 1
                    A6 += 2
                    A7 += 2

                    if A4 == A2:
                        break
            #to here /\
            print("The global matrix is:\n",GlobalM1)
            print("===================================== GLOBAL MATRIX SOLVED============================ \n\n")




            print("Point load to Moment A calculation\n")
            """print("Separate pointLoad locations into individual elements list\n")"""
            #Pointload location seperate into list
            PointMag2 = PointMag
            PointMag2 = list(filter(None,PointMag2))
            CountPointMag = len(PointMag2)
            NumElements = len(elements) - 1
            Pointelements2 = elements
            PointElementList = []
            PointIndicator1 = 0
            PointIndicator2 = 1
            PointLoadIndicator = 0
            CounterPointList = 1
            CountListOfList = 0
            PointLoadLoc1 = PointLoadLoc
            PointLoadLoc1 = list(filter(None,PointLoadLoc1))
            AscendingPointLoadLoc = sorted(PointLoadLoc1)
            AscendingPointLoadLoc = list(filter(None,AscendingPointLoadLoc))
            UltimateMomentA = [[] for i in range(NumElements)]
            UltimateMomentB = [[] for i in range(NumElements)]
            UltimateForceA = [[] for i in range(NumElements)]
            UltimateForceB = [[] for i in range(NumElements)]

            print('No.elements [NumElements]: ',NumElements,"| Elements locations [Pointelements2]: ",Pointelements2,"|Elements interval [elements1]: ",elements1)
            print("No.Point loads [CountPointMag]: ",CountPointMag," | Point load Magnitude [PointMag2]: ",PointMag2," @ Point load location [AscendingPointLoadLoc]: ",AscendingPointLoadLoc)
            print("Creating same number of list as elements [ListOflist]")
            #Create list of list based on number of elements
            ListOfList = [[] for i in range(NumElements)]
            if len(AscendingPointLoadLoc) > 0:
                while CountPointMag > 0:
                    if Pointelements2[PointIndicator1] < AscendingPointLoadLoc[PointLoadIndicator] < Pointelements2[PointIndicator2]:
                        ListOfList[CountListOfList].append(AscendingPointLoadLoc[PointLoadIndicator])
                        PointLoadIndicator += 1
                        CountPointMag -=1
                    elif AscendingPointLoadLoc[PointLoadIndicator] > elements[PointIndicator2]:
                        CountListOfList += 1
                        PointIndicator1 += 1
                        PointIndicator2 += 1
                    elif AscendingPointLoadLoc[PointLoadIndicator] <elements[PointIndicator1]:
                        PointIndicator1 -= 1
                        PointIndicator2 -= 1
                    else:
                        pass
                print("Number of element lists [ListOfList]: ",ListOfList)
            else:
                pass

            #==============convert point load into fixed end Moment (Ma)===================
            #rename so can use in while loop locally
            PointMag1 = PointMag
            PointMag1 = list(filter(None,PointMag1))
            Pointelements = elements
            PointLoadLoc1 = list(filter(None,PointLoadLoc))
            #align force and location after sorting with zip
            PointSortedZip = sorted(zip(PointLoadLoc1,PointMag1))
            PointListOfList = [list(t) for t in zip(*PointSortedZip)]
            #list for point load @ Ma for each element
            PointMa = [[] for i in range(NumElements)]
            PointLoada = [[] for i in range(NumElements)]
            PointLoadb = [[] for i in range(NumElements)]

            #counters for while loop sA
            sA = 0
            sB = 1
            PointForce = 0
            CountPointMag1A = len(PointMag1)

            #print("PointSortedZip:" ,PointSortedZip)
            #print("len(PointLoadLoc1): ",len(PointLoadLoc1))
            #print("PointListOfList: ", PointListOfList)

            if len(PointLoadLoc1) > 0:
                while CountPointMag1A > 0:
                    if Pointelements[sA] < PointListOfList[0][PointForce] < Pointelements[sB] and len(PointLoadLoc) > 0:
                        #print("PointLoadLoc[sA]: ",PointLoadLoc[PointForce])
                        #print("PointListOfList[1][PointForce]: ",PointListOfList[1][PointForce])
                        #print("Point Ma = (",PointListOfList[1][PointForce],"*(",Pointelements[sB],"-",PointListOfList[0][PointForce],")^2(",PointListOfList[0][PointForce],"-",Pointelements[sA],"))/(",Pointelements[sB],"-",Pointelements[sA],")^2")
                        #b = (Pointelements[sB]-PointListOfList[0][PointForce])
                        #a = (PointListOfList[0][PointForce]-Pointelements[sA])
                        #L = (Pointelements[sB]-Pointelements[sA])
                        PointMAformula = (PointListOfList[1][PointForce]*(Pointelements[sB]-PointListOfList[0][PointForce])**2*(PointListOfList[0][PointForce]-Pointelements[sA]))/((Pointelements[sB]-Pointelements[sA])**2)
                        PointMa[sA].append(PointMAformula)
                        UltimateMomentA[sA].append(PointMAformula)
                        PointLoadBFormula = (PointListOfList[1][PointForce]*(PointListOfList[0][PointForce]-Pointelements[sA])**2*((3*(Pointelements[sB]-Pointelements[sA]))-(2*(PointListOfList[0][PointForce]-Pointelements[sA]))))/((Pointelements[sB]-Pointelements[sA])**3)
                        PointLoadAFormula = (PointListOfList[1][PointForce]*(Pointelements[sB]-PointListOfList[0][PointForce])**2*((3*(Pointelements[sB]-Pointelements[sA]))-(2*(Pointelements[sB]-PointListOfList[0][PointForce]))))/((Pointelements[sB]-Pointelements[sA])**3)
                        PointLoada[sA].append(PointLoadAFormula)
                        PointLoadb[sA].append(PointLoadBFormula)
                        UltimateForceA[sA].append(PointLoadAFormula)
                        UltimateForceB[sA].append(PointLoadBFormula)
                        CountPointMag1A -= 1
                        PointForce += 1

                    elif PointListOfList[0][PointForce] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif PointListOfList[0][PointForce] < Pointelements[sA]: #sB changed to sA
                        sA -= 1
                        sB -= 1
                    else:
                        pass
                    #print("PointMa: ",PointMa)
                    #print("PointLoada: ",PointLoada)
                    #print("PointLoadb: ",PointLoadb)
                    #print("====================================== Point Ma solved =============================================\n\n")
            else:
                pass

            #==============convert point load into fixed end Moment (Mb)===================
            #rename so can use in while loop locally
            PointMag1 = PointMag
            PointMag1 = list(filter(None,PointMag1))
            Pointelements = elements
            PointLoadLoc1 = list(filter(None,PointLoadLoc))
            #align force and location after sorting with zip
            PointSortedZip = sorted(zip(PointLoadLoc1,PointMag1))
            PointListOfList = [list(t) for t in zip(*PointSortedZip)]
            #list for point load @ Ma for each element
            PointMb = [[] for i in range(NumElements)]

            #counters for while loop sA
            sA = 0
            sB = 1
            PointForce = 0
            CountPointMag1A = len(PointMag1)

            #print("PointSortedZip:" ,PointSortedZip)
            #print("len(PointLoadLoc1): ",len(PointLoadLoc1))
            #print("PointListOfList: ", PointListOfList)

            if len(PointLoadLoc1) > 0:
                while CountPointMag1A > 0:
                    if Pointelements[sA] < PointListOfList[0][PointForce] < Pointelements[sB] and len(PointLoadLoc) > 0:
                        #print("PointLoadLoc[sA]: ",PointLoadLoc[PointForce])
                        #print("PointListOfList[1][PointForce]: ",PointListOfList[1][PointForce])
                        #print("Point Mb = (",PointListOfList[1][PointForce],"*(",Pointelements[sB],"-",PointListOfList[0][PointForce],")*(",PointListOfList[0][PointForce],"-",Pointelements[sA],")^2)/(",Pointelements[sB],"-",Pointelements[sA],")^2")

                        PointMAformula = -(PointListOfList[1][PointForce]*(Pointelements[sB]-PointListOfList[0][PointForce])*(PointListOfList[0][PointForce]-Pointelements[sA])**2)/((Pointelements[sB]-Pointelements[sA])**2)
                        PointMb[sA].append(PointMAformula)
                        UltimateMomentB[sA].append(PointMAformula)
                        CountPointMag1A -= 1
                        PointForce += 1

                    elif PointListOfList[0][PointForce] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif PointListOfList[0][PointForce] < Pointelements[sB]:
                        sA -= 1
                        sB -= 1
                    else:
                        pass
                    #print("PointMb: ",PointMb)
                    #print("========================================== Mb solved ========================================\n\n")
            else:
                pass



            #============================convert UDL and NDL to PointLoad============
            #convert UDL to point load (UDLpoint)
            CountUDLPointLen = len(UDLMag)
            UDLindicator = 0
            UDLpointformulamaglist = []
            UDLpointformulaloclist = []
            UDLpointmag = []
            UDLpointloc = []
            UDLsA = 0
            UDLsB = 1
            PointelementsUDL = elements

            if CountUDLPointLen > 0:
                while CountUDLPointLen > 0:
                    if PointelementsUDL[UDLsA] <= UDLEndLoc[UDLindicator] and UDLStartLoc[UDLindicator] <= PointelementsUDL[UDLsB]:
                        UDLpointformulamag = (UDLEndLoc[UDLindicator] - UDLStartLoc[UDLindicator])*UDLMag[UDLindicator]
                        UDLpointformulamaglist.append(UDLpointformulamag)
                        UDLpointformulaloc = ((UDLEndLoc[UDLindicator] - UDLStartLoc[UDLindicator])/2)+UDLStartLoc[UDLindicator]
                        UDLpointformulaloclist.append(UDLpointformulaloc)
                        CountUDLPointLen -= 1
                        UDLindicator += 1
                        UDLpointmag.append(UDLpointformulamaglist[-1])
                        UDLpointloc.append(UDLpointformulaloclist[-1])
                    elif UDLEndLoc[UDLindicator] and UDLStartLoc[UDLindicator] > PointelementsUDL[UDLsB]:
                        UDLsA += 1
                        UDLsB += 1
                    elif UDLEndLoc[UDLindicator] and UDLStartLoc[UDLindicator] < PointelementsUDL[UDLsA]:
                        UDLsA -= 1
                        UDLsB -= 1
                    else:
                        pass
                #print("UDLpointformulaList: ",UDLpointformulamaglist)
                #print("UDLpointmag: ",UDLpointmag)
                #print("UDLpointloc: ",UDLpointloc)
            else:
                pass

            UDLPointMa = [[] for i in range(NumElements)]
            UDLsortedzip = sorted(zip(UDLpointloc,UDLpointmag))
            #print("UDLsortedzip: ",UDLsortedzip)
            UDLsortedunzip = [list(t) for t in zip(*UDLsortedzip)]
            #print("UDL to pointload locations(left) & magnitude(right) [UDLsortedunzip]: ", UDLsortedunzip)

            #UDLtoPoint Ma calculation
            PointForce = 0
            sA = 0
            sB = 1
            '''print("Pointelements[sB]: ",Pointelements[sB])
            print("UDLsortedunzip[0][PointForce]",UDLsortedunzip[0][PointForce])'''
            CountUDLPointLen1 = len(UDLMag)
            if CountUDLPointLen1 > 0:
                while CountUDLPointLen1 > 0:
                    if Pointelements[sA] <= UDLsortedunzip[0][PointForce] <= Pointelements[sB]:

                        #print("Point Ma = (",UDLsortedunzip[1][PointForce],"*(",Pointelements[sB],"-",UDLsortedunzip[0][PointForce],")^2(",UDLsortedunzip[0][PointForce],"-",Pointelements[sA],"))/(",Pointelements[sB],"-",Pointelements[sA],")^2")

                        UDLPointMAformula = (UDLsortedunzip[1][PointForce]*(Pointelements[sB]-UDLsortedunzip[0][PointForce])**2*(UDLsortedunzip[0][PointForce]-Pointelements[sA]))/((Pointelements[sB]-Pointelements[sA])**2)
                        UDLPointMa[sA].append(UDLPointMAformula)
                        CountUDLPointLen1 -= 1
                        PointForce += 1

                    elif UDLsortedunzip[0][PointForce] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif UDLsortedunzip[0][PointForce] < Pointelements[sA]: #sB changed to sA
                        sA -= 1
                        sB -= 1
                    else:
                        pass
                    #print("UDLPointMa: ",UDLPointMa)
                    #print("====================================== UDL Ma solved =============================================\n\n")
            else:
                pass
            #UDL Mb
            UDLPointMb = [[] for i in range(NumElements)]
            PointForce = 0
            sA = 0
            sB = 1
            '''print("Pointelements[sB]: ",Pointelements[sB])
            print("UDLsortedunzip[0][PointForce]",UDLsortedunzip[0][PointForce])'''
            CountUDLPointLen1 = len(UDLMag)
            if CountUDLPointLen1 > 0:
                while CountUDLPointLen1 > 0:
                    if Pointelements[sA] <= UDLsortedunzip[0][PointForce] <= Pointelements[sB]:
                        #print("PointLoadLoc[sA]: ",PointLoadLoc[PointForce])
                        #print("PointListOfList[1][PointForce]: ",PointListOfList[1][PointForce])
                        #print("Point Ma = (",UDLsortedunzip[1][PointForce],"*(",Pointelements[sB],"-",UDLsortedunzip[0][PointForce],")*(",UDLsortedunzip[0][PointForce],"-",Pointelements[sA],")^2)/(",Pointelements[sB],"-",Pointelements[sA],")^2")

                        UDLPointMbformula = (UDLsortedunzip[1][PointForce]*(Pointelements[sB]-UDLsortedunzip[0][PointForce])*(UDLsortedunzip[0][PointForce]-Pointelements[sA])**2)/((Pointelements[sB]-Pointelements[sA])**2)
                        UDLPointMb[sA].append(UDLPointMbformula)
                        CountUDLPointLen1 -= 1
                        PointForce += 1

                    elif UDLsortedunzip[0][PointForce] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif UDLsortedunzip[0][PointForce] < Pointelements[sA]: #sB changed to sA
                        sA -= 1
                        sB -= 1
                    else:
                        pass
                    #print("UDLPointMb: ",UDLPointMb)
                    #print("====================================== UDL Mb solved =============================================\n\n")
            else:
                pass
            #++++++++++++++++++++++++UDL MOMENT into Ma and Mb [start]+++++++++++++++++++++
            UDLLoada = [[] for i in range(NumElements)]
            UDLLoadb = [[] for i in range(NumElements)]
            UDLMomenta = [[] for i in range(NumElements)]
            UDLMomentb = [[] for i in range(NumElements)]
            NumP1Column = (NumElements + 1)*2
            P1Array = np.zeros((NumP1Column,1))
            UDLMaEmpty1 = np.array([])
            UDLMaEmpty = []
            UDLMbEmpty = []
            #print("P1 Array : ", P1Array)

            UDLArrayMagIndicator = 0
            UDLsA = 0
            UDLsB = 1
            UDLindicator = 0
            CountUDLPointLen3 = len(UDLMag)

            #UDL Moment
            if CountUDLPointLen3 > 0:
                #print("\n\n +++++++++++++++++++++++++++++UDL MOMENT+++++++++++++++++++++++++++++\n\n")
                #print("Check1 Good")
                while CountUDLPointLen3 > 0:
                    #print("if PointelementsUDL[UDLsA] (",PointelementsUDL[UDLsA], ") < UDLEndLoc[UDLindicator] (", UDLEndLoc[UDLindicator], ") and UDLStartLoc[UDLindicator](" ,UDLStartLoc[UDLindicator], ") < PointelementsUDL[UDLsB](",PointelementsUDL[UDLsB],")")

                    if PointelementsUDL[UDLsA] <= UDLEndLoc[UDLindicator] and UDLStartLoc[UDLindicator] <= PointelementsUDL[UDLsB]:
                        #print("Check 2 Good")
                        UDLArrayFormulax = lambda x: (UDLMag[UDLindicator]*x*(elements1[UDLsA]-x)**2)/elements1[UDLsA]**2
                        #print((UDLMag[UDLArrayMagIndicator],"*x*",(elements1[UDLsA],"-x)**2)/",elements1[UDLsA],"**2")))
                        UDLArrayFormulaxb = lambda y: ((UDLMag[UDLArrayMagIndicator]*(y**2))*(elements1[UDLsA]-y))/elements1[UDLsA]**2
                        # a = (UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        # b = (UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        # W = UDLMag[UDLindicator]
                        # L = elements1[UDLsA]
                        UDLa =(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        UDLb = (UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        UDLw = UDLMag[UDLindicator]
                        UDLL = elements1[UDLsA]
                        UDLLoadaFormula = (UDLw/UDLL)*( ((UDLb**2-UDLa**2)/2)-((UDLb**3-UDLa**3)/UDLL)+((UDLb**4-UDLa**4)/(2*UDLL**2)) ) + UDLw*(UDLb-UDLa) - (UDLw/(2*UDLL))*(UDLb**2-UDLa**2)

                        '''(UDLMag[UDLindicator]/elements1[UDLsA])*( (((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**2-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**2)/2) - (((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**3-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**3)/elements1[UDLsA])
                        +(((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**4-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**4)/(2*elements1[UDLsA]**2)))
                        + (UDLMag[UDLindicator]*((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])))-((UDLMag[UDLindicator]/(2*elements1[UDLsA]))*((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**2-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**2))'''

                        UDLLoadbFormula = (UDLw/UDLL)*( -((UDLb**2-UDLa**2)/2)+((UDLb**3-UDLa**3)/UDLL)-((UDLb**4-UDLa**4)/(2*UDLL**2)) ) + (UDLw/(2*UDLL))*(UDLb**2-UDLa**2)

                        '''(UDLMag[UDLindicator]/elements1[UDLsA])*( (((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**2-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**2)/2) - (((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**3-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**3)/elements1[UDLsA])
                        +(((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**4-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**4)/(2*elements1[UDLsA]**2)))
                        +((UDLMag[UDLindicator]/(2*elements1[UDLsA]))*((UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**2-(UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**2))'''
                        '''!UDLLoada and B same answer, maybe wrong!'''
                        UDLLoada[UDLsA].append(UDLLoadaFormula)
                        UDLLoadb[UDLsA].append(UDLLoadbFormula)
                        UltimateForceA[UDLsA].append(UDLLoadaFormula)
                        UltimateForceB[UDLsA].append(UDLLoadbFormula)
                        #print("UDLLoada[UDLsA]: ",UDLLoada[UDLsA])
                        #print("UDLLoadb[UDLsA]: ",UDLLoadb[UDLsA])

                        if PointelementsUDL[0] <= UDLEndLoc[UDLindicator] and UDLStartLoc[UDLindicator] <= PointelementsUDL[1]:
                            #print("if ",PointelementsUDL[0], "<" ,UDLEndLoc[UDLindicator], " and ", UDLStartLoc[UDLindicator] ,"<", PointelementsUDL[1])
                            UDLMaFormula1 = integrate.quad(UDLArrayFormulax, 0, (UDLEndLoc[UDLsA]-PointelementsUDL[UDLsA]))
                            UDLMbFormula1 = integrate.quad(UDLArrayFormulaxb, 0, (UDLEndLoc[UDLsA]-PointelementsUDL[UDLsA]))
                            #print("From 0, integrate over 0 and ",elements1[0])
                            #print("elements1[0]: ",elements1[0])
                            UDLMaEmpty.append(UDLMaFormula1[0])
                            UDLMomenta[0].append(UDLMaFormula1[0])
                            UDLMbEmpty.append(-UDLMbFormula1[0])
                            UDLMomentb[0].append(-UDLMbFormula1[0])
                            UltimateMomentA[0].append(UDLMaFormula1[0])
                            UltimateMomentB[0].append(-UDLMbFormula1[0])

                        else:
                            #print("check 3 Good")
                            UDLMaFormula = integrate.quad(UDLArrayFormulax, (UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA]), (UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA]))
                            UDLMbFormula = integrate.quad(UDLArrayFormulaxb, (UDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA]), (UDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA]))

                            #print("From not 0, integrate over ",UDLStartLoc[UDLindicator], "-", PointelementsUDL[UDLsA], " and ", UDLEndLoc[UDLindicator],"-",PointelementsUDL[UDLsA])
                            UDLMaEmpty.append(UDLMaFormula[0])
                            UDLMomenta[UDLsA].append(UDLMaFormula[0])
                            UDLMbEmpty.append(-UDLMbFormula[0])
                            UDLMomentb[UDLsA].append(-UDLMbFormula[0])
                            UltimateMomentA[UDLsA].append(UDLMaFormula[0])
                            UltimateMomentB[UDLsA].append(-UDLMbFormula[0])

                        '''print("UDLMaEmpty: ",UDLMaEmpty)
                        print("UDLMbEmpty: ",UDLMbEmpty)
                        print("UDLMomenta: ",UDLMomenta)
                        print("UDLMomentb: ",UDLMomentb)
                        print("UDLLoada: ",UDLLoada)
                        print("UDLLoadb: ",UDLLoadb)'''

                        UDLArrayMagIndicator += 1
                        CountUDLPointLen3 -= 1
                        UDLindicator += 1
                        print("UDL moment & force SOLVED +++++++++++++++++++++++++++++++++++++++++++++++ \n")

                    elif UDLEndLoc[UDLindicator] and UDLStartLoc[UDLindicator] > PointelementsUDL[UDLsB]:
                        UDLsA += 1
                        UDLsB += 1
                    elif UDLEndLoc[UDLindicator] and UDLStartLoc[UDLindicator] < PointelementsUDL[UDLsA]:
                        UDLsA -= 1
                        UDLsB -= 1
                    else:
                        pass

#+++++++++++++++++++++++++++++++++++++++++++++UDL into ma and mb [end]


#+++++++++++++++++++++++++++++++++++++++++++++++moment into moment a and b [Start]
            sA = 0
            sB = 1
            PointForce = 0
            CountMomentMag1A = len(MomentLoc)
            MomentMomenta = [[] for i in range(NumElements)]
            MomentMomentb = [[] for i in range(NumElements)]
            MomentLoada = [[] for i in range(NumElements)]
            MomentLoadb = [[] for i in range(NumElements)]
            MomentMaList = []
            MomentMbList = []
            MomentForceMaList = []
            MomentForceMbList = []
            #print("MomentLoc0: ",MomentLoc)

            if len(MomentLoc) > 0:
                while CountMomentMag1A > 0:
                    if Pointelements[sA] <= MomentLoc[PointForce] <= Pointelements[sB]:
                        #print("MomentMAformula = -(",MomentMag[PointForce],"*(",Pointelements[sB],"-",MomentLoc[PointForce],")*((2*(",elements1[sA],"-(",Pointelements[sB]-MomentLoc[PointForce],"))-(",Pointelements[sB],"-",MomentLoc[PointForce],")))/(",elements1[sA],")**2")
                        #print("MomentMBformula = -((",MomentMag[PointForce],"*(",elements1[sA],")-(",Pointelements[sB],"-",MomentLoc[PointForce],"))*((2*(",Pointelements[sB],"-",MomentLoc[PointForce],")-(",elements1[sA],")-(",Pointelements[sB],"-",MomentLoc[PointForce],"))))/(",elements1[sA],")**2")
                        MomentMAformula = -(MomentMag[PointForce]*(Pointelements[sB]-MomentLoc[PointForce])*(2*((elements1[sA])-(Pointelements[sB]-MomentLoc[PointForce]))-(Pointelements[sB]-MomentLoc[PointForce])))/(elements1[sA])**2
                        MomentMBformula = -((MomentMag[PointForce]*((elements1[sA])-(Pointelements[sB]-MomentLoc[PointForce])))*((2*(Pointelements[sB]-MomentLoc[PointForce])-(elements1[sA]-(Pointelements[sB]-MomentLoc[PointForce])))))/(elements1[sA])**2
                        Vaformula = -(6*MomentMag[PointForce]*((elements1[sA])-(Pointelements[sB]-MomentLoc[PointForce]))*(Pointelements[sB]-MomentLoc[PointForce]))/(elements1[sA])**3
                        Vbformula = (6*MomentMag[PointForce]*((elements1[sA])-(Pointelements[sB]-MomentLoc[PointForce]))*(Pointelements[sB]-MomentLoc[PointForce]))/(elements1[sA])**3
                        MomentMaList.append(MomentMAformula)
                        MomentMbList.append(MomentMBformula)
                        MomentMomenta[sA].append(MomentMAformula)
                        MomentMomentb[sA].append(MomentMBformula)
                        MomentForceMaList.append(Vaformula)
                        MomentForceMbList.append(Vbformula)
                        MomentLoada[sA].append(Vaformula)
                        MomentLoadb[sA].append(Vbformula)
                        UltimateForceA[sA].append(Vaformula)
                        UltimateForceB[sA].append(Vbformula)
                        UltimateMomentA[sA].append(MomentMAformula)
                        UltimateMomentB[sA].append(MomentMBformula)
                        CountMomentMag1A -= 1
                        PointForce += 1

                    elif MomentLoc[PointForce] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif MomentLoc[PointForce] < Pointelements[sA]: #sB changed to sA
                        sA -= 1
                        sB -= 1
                    else:
                        pass
                    #print("MomentMaList: ",MomentMaList)
                    #print("MomentMbList: ",MomentMbList)
                    #print("MomentForceMaList: ",MomentForceMaList)
                    #print("MomentForceMbList: ",MomentForceMbList)
                    #print("====================================== MomentList =============================================\n\n")
            else:
                pass

            #++++++++++++++++++++++++++++++++++++++++Moment into Mb and Mb [End]

            #++++++++++++++++++++++++UDL MOMENT into Ma and Mb [start]+++++++++++++++++++++
            NumP1Column = (NumElements + 1)*2
            P1Array = np.zeros((NumP1Column,1))
            UDLMaEmpty1 = np.array([])
            NDLMaEmpty = []
            NDLMbEmpty = []
            #print("P1 Array : ", P1Array)

            UDLArrayMagIndicator = 0
            UDLsA = 0
            UDLsB = 1
            UDLindicator = 0
            CountNDLPointLen3 = len(NDLStartMag)
            NDLWo = []
            NDLWo1 = []
            NDLForceaEmpty = []
            NDLForcebEmpty = []
            #UDL Moment
            if CountNDLPointLen3 > 0:
                #print("\n\n +++++++++++++++++++++++++++++NDL MOMENT+++++++++++++++++++++++++++++\n\n")
                #print("Check1 Good")
                while CountNDLPointLen3 > 0:

                    if PointelementsUDL[UDLsA] <= NDLEndLoc[UDLindicator] and NDLStartLoc[UDLindicator] <= PointelementsUDL[UDLsB]:
                        #print("Check 2 Good")
                        '''print("\n\n")
                        print("NDLStartMag[UDLindicator]: ",NDLStartMag[UDLindicator])
                        print("NDLEndLoc[UDLindicator]: ",NDLEndLoc[UDLindicator])
                        print("PointelementsUDL[UDLsA]: ",PointelementsUDL[UDLsA])
                        print("NDLEndMag[UDLindicator]: ", NDLEndMag[UDLindicator])
                        print("NDLStartLoc[UDLindicator]: ",NDLStartLoc[UDLindicator])
                        print("elements1[UDLindicator]:", elements1[UDLindicator])
                        print("\n\n")'''
                        NDLa = (NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        NDLb = (NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        NDLL = elements1[UDLindicator]
                        NDLw2 = NDLEndMag[UDLindicator]
                        NDLw1 = NDLStartMag[UDLindicator]
                        #print("NDLWoFormula = ((",NDLStartMag[UDLindicator],"*",(NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA]),")-(",NDLEndMag[UDLindicator],"*",(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA]),")/(",(NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA]),"-",(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA]),")")
                        NDLWoFormula1 = ((NDLw1*NDLb)-(NDLw2*NDLa))/(NDLb-NDLa)
                        NDLWoFormula = ( (NDLStartMag[UDLindicator]*(NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])) -( NDLEndMag[UDLindicator]*(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA]) ) / ((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])))

                        #a = NDLa = (NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        #b = NDLb = (NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])
                        #L = NDLL = elements1[UDLindicator]
                        #Wo = NDLWo1= NDLWo1[UDLindicator]
                        #w1 = NDLw1 = NDLStartMag[UDLindicator]
                        #w2 = NDLw2 = NDLEndMag[UDLindicator]

                        NDLWo1.append(NDLWoFormula1)
                        NDLWo.append(NDLWoFormula)
                        #Wo = NDLWo1 = NDLWo1[UDLindicator]
                        NDLWo1 = NDLWo1[UDLindicator]

                        '''print("NDLWo1: ",NDLWo1)
                        print("NDLa: ",NDLa)
                        print("NDLb: ",NDLb)
                        print("NDLL: ",NDLL)
                        print("NDLw1: ",NDLw1)
                        print("NDLw2: ",NDLw2)
                        print("NDLWo1: ",NDLWo1)
                        print("\n\n")'''


                        NDLMaMomentFormula=(((NDLw2-NDLWo1)/NDLb)*( ((NDLb**3-NDLa**3)/3) - ((NDLb**4-NDLa**4)/(2*NDLL)) + ((NDLb**5-NDLa**5)/(5*NDLL**2)) )
                         + NDLWo1*( ((NDLb**2-NDLa**2)/2) - 2*((NDLb**3)-NDLa**3)/(3*NDLL) + ((NDLb**4-NDLa**4)/(4*NDLL**2)) ))

                        '''NDLMaFormula=((NDLEndMag[UDLindicator]-NDLWo1[UDLindicator])/(NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA]))*(((((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**3)-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**3)/3)
                        -(((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**4
                        -(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**4)
                        /(2*elements1[UDLindicator]))
                        +
                        (NDLWo1[UDLindicator]*(((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**2
                        -(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**2)/2-2*((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**3-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**3)/(3*elements1[UDLindicator])
                        +((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**4-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**4)/(4*elements1[UDLindicator]**2))))'''
                        '''thiseeror'''
                        '''Haven't do forceA and force B for NDL'''
                        NDLMaEmpty.append(NDLMaMomentFormula)
                        UltimateMomentA[UDLindicator].append(NDLMaMomentFormula)

                        NDLMbMomentFormula = ( -((NDLw2-NDLWo1)/NDLb)*(((NDLb**4-NDLa**4)/(4*NDLL))-((NDLb**5-NDLa**5)/(5*NDLL**2))) - NDLWo1*(((NDLb**3-NDLa**3)/(3*NDLL))-((NDLb**4-NDLa**4)/(4*NDLL**2))) )
                        '''NDLMbFormula = -((NDLEndMag[UDLindicator]-NDLWo1[UDLindicator])/(NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA]))*(
                        (((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**4-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**4)/(4*elements1[UDLindicator]))
                        -( ((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**5-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**5)/(5*elements1[UDLindicator]**2)))
                        -NDLWo1[UDLindicator]*(((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**3-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**3)/(3*elements1[UDLindicator])
                        - ((NDLEndLoc[UDLindicator]-PointelementsUDL[UDLsA])**4-(NDLStartLoc[UDLindicator]-PointelementsUDL[UDLsA])**4)/(4*elements1[UDLindicator]**2))'''
                        print("NDLMbMomentFormula: ",NDLMbMomentFormula)
                        NDLMbEmpty.append(NDLMbMomentFormula)
                        UltimateMomentB[UDLindicator].append(NDLMbMomentFormula)

                        NDLMaForceFormula = (((NDLw2-NDLWo1)/(NDLb*NDLL))*( ((NDLb**3-NDLa**3)/3) - (3*(NDLb**4-NDLa**4)/(4*NDLL)) + (2*(NDLb**5-NDLa**5)/(5*NDLL**2)) )
                         + (NDLWo1/NDLL)*( ((NDLb**2-NDLa**2)/2) - ((NDLb**3)-NDLa**3)/(NDLL) + ((NDLb**4-NDLa**4)/(2*NDLL**2)) )
                         + ( (((NDLb-NDLa)/2)*(1-(NDLa/NDLL))*(NDLw1+NDLw2)) - ((((NDLb-NDLa)**2)/(6*NDLL))*(NDLw1+2*NDLw2)) ) )

                        '''print((NDLw2-NDLWo1)/(NDLb*NDLL))
                        print(-((NDLb**3-NDLa**3)/3))
                        print((3*(NDLb**4-NDLa**4)/(4*NDLL)))
                        print((2*(NDLb**5-NDLa**5)/(5*NDLL**2)))
                        print((NDLWo1/NDLL))
                        print(-((NDLb**2-NDLa**2)/2))
                        print(((NDLb**3)-NDLa**3)/(NDLL))
                        print(((NDLb**4-NDLa**4)/(2*NDLL**2)))
                        print((((NDLb-NDLa)*NDLa)/(2*NDLL)))
                        print((NDLw1+NDLw2))
                        print((((NDLb-NDLa)**2)/(6*NDLL)))
                        print((NDLw1+(2*NDLw2)))'''
                        NDLMbForceFormula = (((NDLw2-NDLWo1)/(NDLb*NDLL))*( -((NDLb**3-NDLa**3)/3) + (3*(NDLb**4-NDLa**4)/(4*NDLL)) - (2*(NDLb**5-NDLa**5)/(5*NDLL**2)) )
                         + (NDLWo1/NDLL)*( -((NDLb**2-NDLa**2)/2) + ((NDLb**3)-NDLa**3)/(NDLL) - ((NDLb**4-NDLa**4)/(2*NDLL**2)) )
                         + ( ((((NDLb-NDLa)*NDLa)/(2*NDLL))*(NDLw1+NDLw2)) + ((((NDLb-NDLa)**2)/(6*NDLL))*(NDLw1+(2*NDLw2))) ) )

                        NDLForceaEmpty.append(NDLMaForceFormula)
                        NDLForcebEmpty.append(NDLMbForceFormula)
                        UltimateForceA[UDLsA].append(NDLMaForceFormula)
                        UltimateForceB[UDLsA].append(NDLMbForceFormula)
                        #print("NDLMaEmpty: ",NDLMaEmpty)
                        #print("NDLMbEmpty: ",NDLMbEmpty)
                        UDLArrayMagIndicator += 1
                        CountNDLPointLen3 -= 1
                        UDLindicator += 1
                        #print("NDL moment SOLVED +++++++++++++++++++++++++++++++++++++++++++++++ \n")

                    elif NDLEndLoc[UDLindicator] and NDLStartLoc[UDLindicator] > PointelementsUDL[UDLsB]:
                        UDLsA += 1
                        UDLsB += 1
                    elif NDLEndLoc[UDLindicator] and NDLStartLoc[UDLindicator] < PointelementsUDL[UDLsA]:
                        UDLsA -= 1
                        UDLsB -= 1
                    else:
                        pass

            UltimateForceA1 = []
            UltimateForceB1 = []
            UltimateMomentA1 = []
            UltimateMomentB1 = []
            print("-Point force")
            print("PointMa: ",PointMa)
            print("PointMb: ",PointMb)
            print("PointLoada: ",PointLoada)
            print("PointLoadb: ",PointLoadb)
            print("\n")
            print("-Moment force")
            print("MomentMaList: ",MomentMaList)
            print("MomentMbList: ",MomentMbList)
            print("MomentForceMaList: ",MomentForceMaList)
            print("MomentForceMbList: ",MomentForceMbList)
            print("\n")

            print("-UDL force")
            print("UDLMbEmpty: ",UDLMbEmpty)
            print("UDLMomenta: ",UDLMomenta)
            print("UDLMomentb: ",UDLMomentb)
            print("UDLMaEmpty: ",UDLMaEmpty)
            print("UDLLoada: ",UDLLoada)
            print("UDLLoadb: ",UDLLoadb)
            print("\n")

            print("-NDL force")
            print("NDLMaEmpty: ",NDLMaEmpty)
            print("NDLMbEmpty: ",NDLMbEmpty)
            print("NDLForceaEmpty: ",NDLForceaEmpty)
            print("NDLForcebEmpty: ",NDLForcebEmpty)
            print("\n")

            print("Ultimate list (haven't add tgt)")
            print("UltimateMomentA: ",UltimateMomentA)
            print("UltimateMomentB: ",UltimateMomentB)
            print("UltimateForceA: ",UltimateForceA)
            print("UltimateForceB: ",UltimateForceB)
            print("\n")

            #for adding up Ultimate List - start
            for l in UltimateForceA:
                UltimateForceA1.append(sum(l))

            for l in UltimateForceB:
                UltimateForceB1.append(sum(l))

            for l in UltimateMomentA:
                UltimateMomentA1.append(sum(l))

            for l in UltimateMomentB:
                UltimateMomentB1.append(sum(l))
            # Adding up ultimate list -end

            UltimateABForce = []
            UltimateABMoment = []
            UltiCount = len(UltimateForceA1)
            sAult = 0

            #summing up A to B - start
            #summing up Force A to Force B
            if (len(UltimateForceA1) > 0):
                while UltiCount > 1:
                    UltimateABForceFormula = (UltimateForceA1[sAult+1]+UltimateForceB1[sAult])
                    UltimateABForce.append(UltimateABForceFormula)
                    UltiCount -= 1
            else:
                pass
            if (len(UltimateForceA1) > 0):
                UltimateABForce.insert(0,UltimateForceA1[0])
            if (len(UltimateForceB1) > 0):
                UltimateABForce.append(UltimateForceB1[-1])
            #Summing up Moment A to Moment B
            UltiCount1 = len(UltimateMomentA1)
            if (len(UltimateMomentA1) > 0):
                while UltiCount1 > 1:
                    UltimateABMomentFormula = (UltimateMomentA1[sAult+1]+UltimateMomentB1[sAult])
                    UltimateABMoment.append(UltimateABMomentFormula)
                    UltiCount1 -= 1
            else:
                pass
            if (len(UltimateMomentA1) > 0):
                UltimateABMoment.insert(0,UltimateMomentA1[0])
            if (len(UltimateMomentB1) > 0):
                UltimateABMoment.append(UltimateMomentB1[-1])
            #sum up A to B - end

            PprimeCount = len(UltimateABForce)
            PprimeCount1 = (len(UltimateABForce)+len(UltimateABMoment))
            Pprime = np.zeros(shape =( PprimeCount1 , 1)) #column, row
            PsA = 0
            PsA1 = 0
            PsB = 1
            PsB1 = 0
            while (PprimeCount > 0):
                Pprime[PsA,0] = UltimateABForce[PsA1]
                PsA += 2
                PsA1 += 1
                #print("Pprime1: ",Pprime)
                Pprime[PsB,0] = UltimateABMoment[PsB1]
                PsB += 2
                PsB1 += 1
                PprimeCount -= 1
                #print("Pprime2: ",Pprime)

            CutPprime = Pprime
            CutPsA = 2
            PinCutCount = len(PinSupLoc)+len(RollerSupLoc)

            while PinCutCount > 0:
                CutPprime = np.delete(CutPprime,CutPsA,0)
                CutPsA += 2
                PinCutCount -= 1
            CutFix1 = len(FixSupLoc)
            CutFix = FixSupLoc
            if CutFix1 > 0:
                if CutFix1 > 1:
                    CutPprime = np.delete(CutPprime,0,0)
                    CutPprime = np.delete(CutPprime,1,0)
                else:
                    pass
            else:
                pass


            #CutPprime = np.delete(CutPprime,-1,0)
            CutPprime = np.delete(CutPprime,-1,0)
            CutPprime = np.delete(CutPprime,-1,0)

            CutGlobalM = GlobalM1

            PinCutCount2 = len(PinSupLoc)+len(RollerSupLoc)
            CutPsAM = 2
            while PinCutCount2 > 0:
                CutGlobalM = np.delete(CutGlobalM,CutPsAM,0)
                CutGlobalM = np.delete(CutGlobalM,CutPsAM,1)
                #print("CutGlobalMT: \n",CutGlobalM)
                '''CutPsAM += 2'''
                PinCutCount2 -= 1

            CutGlobalM = np.delete(CutGlobalM,-1,0)
            CutGlobalM = np.delete(CutGlobalM,-1,0)
            CutGlobalM = np.delete(CutGlobalM,-1,1)
            CutGlobalM = np.delete(CutGlobalM,-1,1)

            CutGlobalMInv = np.linalg.inv(CutGlobalM)
            PprimeCount3 = len(PinSupLoc)+len(RollerSupLoc)
            ColumnCountGlobalM1 = np.size(GlobalM1,0)
            ReverseCutGlobal = np.empty((0,ColumnCountGlobalM1),float)
            PsA = 2

            while (PprimeCount3 > 0):
                #print("adding",[GlobalM1[PsA,:]])
                ReverseCutGlobal = np.append(ReverseCutGlobal,([GlobalM1[:,PsA]]),axis = 0)
                PsA += 2
                PprimeCount3 -= 1
            ReverseCutGlobal = np.append(ReverseCutGlobal,([GlobalM1[:,-2]]),axis = 0)
            ReverseCutGlobal = np.append(ReverseCutGlobal,([GlobalM1[:,-1]]),axis = 0)

            PprimeCount4 = len(PinSupLoc)+len(RollerSupLoc)
            PsA = 2
            while (PprimeCount4 >0):
                ReverseCutGlobal = np.delete(ReverseCutGlobal,2,1)
                PprimeCount4 -= 1
            ReverseCutGlobal = np.delete(ReverseCutGlobal,-1,1)
            ReverseCutGlobal = np.delete(ReverseCutGlobal,-1,1)

            Funknown1 = np.matmul(CutGlobalMInv,CutPprime)
            Funknown = np.matmul(ReverseCutGlobal,Funknown1)
            CutPprimeFinal = CutPprime

            '''while PprimeCount5 > 0:
                CutPprimeFinal = np.insert(CutPprimeFinal,PsA,Funknown[PsB,0])
                PsA += 2
                PsB+=1
                PprimeCount5 -= 1'''
            print("Summing up list within list")
            print("UltimateMomentA1: ",UltimateMomentA1)
            print("UltimateMomentB1: ",UltimateMomentB1)
            print("UltimateForceA1: ",UltimateForceA1)
            print("UltimateForceB1: ",UltimateForceB1)
            print("\n")

            print("Summing up A to B ")
            print("UltimateABForce: ",UltimateABForce)
            print("UltimateABMoment: ",UltimateABMoment)
            print("\n")

            #print("PprimeCount: ",PprimeCount)
            print("Pprime: ",Pprime)
            print("\n")
            print("CutPprime: ",CutPprime)
            print("GlobalM1 (B4 Cut): \n", GlobalM1)
            print('\n')
            print("CutGlobalM (Aft Cut): \n",CutGlobalM)
            print("CutGlobalMInv: \n",CutGlobalMInv)
            print("ReverseCutGlobal: \n",ReverseCutGlobal)
            print("Funknown: \n",Funknown)
            print("Funknown1: \n",Funknown1)
            print("CutPprimeFinal: \n",CutPprimeFinal)
            FunknownList = []
            FunknownListFormula = Funknown.tolist()
            CutPprimeList = []
            CutPprimeListFormula = CutPprime.tolist()
            PprimeList = []
            PprimeListFormula = Pprime.tolist()

            for sublist in FunknownListFormula:
                for item in sublist:
                    FunknownList.append(item)
            print("FunknownList: ",FunknownList)
            for sublist in CutPprimeListFormula:
                for item in sublist:
                    CutPprimeList.append(item)
            print("CutPprimeList: ", CutPprimeList)
            for sublist in PprimeListFormula:
                for item in sublist:
                    PprimeList.append(item)
            print("PprimeList: ", PprimeList)
            PsA = 2
            PsB = 0
            PprimeCount5 = len(PinSupLoc)+len(RollerSupLoc)
            PprimeAdd = CutPprimeList
            while PprimeCount5 > 0:
                PprimeAdd.insert(PsA,FunknownList[PsB])
                PsB += 1
                PsA += 2
                PprimeCount5 -= 1

            PprimeAdd.append(FunknownList[-2])
            PprimeAdd.append(FunknownList[-1])

            UltimateP = []
            UltimateP = [sum(x) for x in zip(PprimeAdd,-Pprime)]


            print("PprimeAdd: ",PprimeAdd)
            print("PprimeList: ",PprimeList)
            print("UltimateP: ",UltimateP)








            print("\n")
#+++++++++++++++++++++++++++++++++++++++++++++UDL into ma and mb [end]

            '''#Reaction force A and B of element for local stiffness matrix
            #Fb using sumation Fa = 0 with positive moment = +
            UDLReactCounter1 = len(UDLpointmag)
            UDLReactCounter2 = 0
            UDLFb = []
            PointForce1 = 0
            FaUDLListOfList = [[] for i in range(NumElements)]
            FbUDLListOfList = [[] for i in range(NumElements)] #List of List storing moment of UDLFb
            sA1 = 0
            sB1 = 1
            CountUDLPointLen2 = len(UDLMag)
            #sort Pudl force using moment into respective elements
            if CountUDLPointLen2 > 0:
                while CountUDLPointLen2 > 0:
                    if Pointelements[sA1] < UDLsortedunzip[0][PointForce1] < Pointelements[sB1]:
                        #force Fa
                        FaUDLmomentformula = -UDLsortedunzip[1][PointForce1]
                        FaUDLListOfList[sA1].append(float(FaUDLmomentformula))
                        #force Fb
                        FbUDLmomentformula = float(-UDLsortedunzip[1][PointForce1]*(UDLsortedunzip[0][PointForce1]-Pointelements[sA1]))
                        FbUDLListOfList[sA1].append(float(FbUDLmomentformula))
                        CountUDLPointLen2 -= 1
                        PointForce1 += 1

                    elif UDLsortedunzip[0][PointForce1] > Pointelements[sB1]:
                        sA1 += 1
                        sB1 += 1
                    elif UDLsortedunzip[0][PointForce1] < Pointelements[sA1]:
                        sA1 -= 1
                        sB1 -= 1
                    else:
                        pass
                    #print("FbUDLListOfList: ",FbUDLListOfList)
                    #print(">>>>>>>>>>>>>>>>>>>>>>>>>>> FbUDLListOfList =============================================\n\n")
            else:
                pass
            #sort Ppoint force using sumation moment into respective elements
            PointForce1 = 0
            sA = 0
            sB = 1
            PointLoadLoc2 = len(PointLoadLoc0)
            FaPointListOfList = [[] for i in range(NumElements)]
            FbPointListOfList = [[] for i in range(NumElements)]
            CountPointMag2A = len(PointMag1)

            print("PointListOfList: ",PointListOfList)

            if len(PointMag2) > 0:
                while CountPointMag2A > 0:
                    if Pointelements[sA] < PointListOfList[0][PointForce1] < Pointelements[sB] and len(PointLoadLoc) > 0:
                        #force Fa
                        PointFaFormula = -PointListOfList[1][PointForce1]
                        FaPointListOfList[sA].append(PointFaFormula)
                        #force Fb
                        PointFbFormula = float(-PointListOfList[1][PointForce1]*(PointListOfList[0][PointForce1]-Pointelements[sA]))
                        print("PointFbFormula = -",PointListOfList[1][PointForce1],"*(",PointListOfList[0][PointForce1],"-",Pointelements[sA],")")
                        FbPointListOfList[sA].append(float(PointFbFormula))
                        CountPointMag2A -= 1
                        PointForce1 += 1

                    elif PointListOfList[0][PointForce1] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif PointListOfList[0][PointForce1] < Pointelements[sA]: #sB changed to sA
                        sA -= 1
                        sB -= 1
                    else:
                        pass

                    #print("FbPointListOfList: ",FbPointListOfList)
                    #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FbPointListOfList solved =============================================\n\n")
            else:
                pass
            print("\n")
            print("FbPointListOfList: ",FbPointListOfList)
            print("FbUDLListOfList: ",FbUDLListOfList)
            print("\n")
            print("FaPointListOfList: ",FbPointListOfList)
            print("FaUDLListOfList: ",FaUDLListOfList)
            print("\n")
#tester\/


            aaa1 = FbPointListOfList[1][0]+FbUDLListOfList[1][0]
            print("aaa1",aaa1)
            FbListOfList = sorted(zip(FbPointListOfList,FbUDLListOfList))
#tester\/
            result = [sum(b) for b in FbListOfList[2]]
            print("result: ",result)
            print(type(FbPointListOfList[2]))
#tester\/
            redundantCounter = 0
            newFbPointListOfList = []
            newFbPointListOfList1 = []
            while(redundantCounter < len(FbListOfList)):
                print("redundantCounter: ", redundantCounter)
                print("FbListOfList[redundantCounter][0]: ", FbListOfList[redundantCounter][0])
                print("FbListOfList[redundantCounter][1]: ", FbListOfList[redundantCounter][1])
                print(FbListOfList[redundantCounter][0]+FbListOfList[redundantCounter][1])

                print(sum(FbListOfList[redundantCounter][0]+FbListOfList[redundantCounter][1]))

                newFbPointListOfList.append(FbListOfList[redundantCounter][0]+FbListOfList[redundantCounter][1])
                newFbPointListOfList1.append(FbListOfList[redundantCounter][0]+FbListOfList[redundantCounter][1])
                print(newFbPointListOfList1)

                print(np.array(FbListOfList[redundantCounter][1],float))

                redundantCounter += 1

            print (type(newFbPointListOfList))
            print(newFbPointListOfList)
            print("newFbPointListOfList: ", newFbPointListOfList)

            #++++++++++++++++add them and divide as per formula,moment and NDL not yet added in
            #force fa using summation Fy=0
            FaListOfList = sorted(zip(FaPointListOfList,FaUDLListOfList))
            print("FaListOfList: ", FaListOfList)'''
            #for force<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<




            '''
            #convert NDL to pointload (NDLpoint)
            NDLpoint = []
            CountNDLlen = len(NDLStartMag)
            #NDL net increase
            CountPLDistance = len(NDLStartLoc)
            CountNDLSign = 0
            NDLCentroidDistanceList = []
            NDLsharpload = []
            NDLflatload = []
            #distance from 0,0 to point load for Sharp NDL
            ===> cut this off>while CountPLDistance > 0:
                if (NDLStartMag[CountNDLSign] - NDLEndMag[CountNDLSign]) > 0:
                    NDLStartPositiveCentroidFormula = (((NDLEndLoc[CountNDLSign]-NDLStartLoc[CountNDLSign])/3) + NDLStartLoc[CountNDLSign])
                    NDLCentroidDistanceList.Append(NDLStartPositiveCentroidFormula)
                else:
                    NDLNegCentroidFormula = ((((NDLEndLoc[CountNDLSign]- NDLStartLoc[CountNDLSign])*2)/3)+NDLStartLoc[CountNDLSign])
                    NDLCentroidDistanceList.Append(NDLNegCentroidFormula)
                CountPLDistance -= 1
                CountNDLSign += 1 <cut this off<===

            #Point load for UDL and NDL
            NDLcounter = 0
            NDLtotalmag = []
            NDLEndMag1 = NDLEndMag
            NDLStartMag1 = NDLStartMag
            NDLEndLoc1 = NDLEndLoc
            NDLStartLoc1 = NDLStartLoc

            print("NDL conditions: ",NDLStartMag1[NDLcounter]," and ",NDLEndMag1[NDLcounter] )

            if CountNDLlen > 0:
                while CountNDLlen > 0:
                    #NDL without base
                    if float(NDLStartMag1[NDLcounter]) == 0 or float(NDLEndMag1[NDLcounter]) == 0:
                        NDLsharploadFormula1 = (abs((NDLStartMag1[NDLcounter] - NDLEndMag1[NDLcounter])*(NDLEndLoc1[NDLcounter] - NDLStartLoc1[NDLcounter])/2))
                        NDLsharpload.append(NDLsharploadFormula1)
                        print("NDL without base is read.")
                    #NDL with base
                    else:
                        NDLsharploadFormula = (abs((NDLStartMag1[NDLcounter] - NDLEndMag1[NDLcounter])*(NDLEndLoc1[NDLcounter] - NDLStartLoc1[NDLcounter])/2))
                        NDLsharpload.append(NDLsharploadFormula)
                        if NDLStartMag1[NDLcounter] > NDLEndMag1[NDLcounter]:
                            NDLflatloadFormula = (NDLEndMag1[NDLcounter]*(NDLEndLoc1[NDLcounter] - NDLStartLoc1[NDLcounter]))
                            NDLflatload.append(NDLflatloadFormula)
                        elif NDLStartMag1[NDLcounter] < NDLEndMag1[NDLcounter]:
                            NDLflatloadFormula = (NDLStartMag1[NDLcounter]*(NDLEndLoc1[NDLcounter] - NDLStartLoc1[NDLcounter]))
                            NDLflatload.append(NDLflatloadFormula)
                        else:
                            pass
                    CountNDLlen -= 1
                    NDLcounter += 1
                    print("NDLsharpload: ",NDLsharpload)
                    print("NDLflatload: ",NDLflatload)
                    '''
#!!!!!!!!!!!!!!!!!!!!!!problem when either startmag = 0 or endmag = 0, the whole loop passes.


    return render(request,'first_app/index.html',{'BeamView':BeamForm})



'''            print("CountNDLlen",CountNDLlen)
            print("NDLStartMag1: ",NDLStartMag1)
            if CountNDLlen > 0:
                if NDLStartMag1[NDLcounter] != 0 and NDLEndMag1[NDLcounter] != 0:
                    while CountNDLlen > 0:
                        #Calculation of sharp NDL
                        #print("Hello",NDLStartLoc1[NDLcounter])
                        print("NDLsharploadFormula =",NDLEndMag1[NDLcounter], "-",NDLStartMag1[NDLcounter], "*(",NDLEndLoc1[NDLcounter], "-",NDLStartLoc1[NDLcounter],")/2")
                        NDLsharploadFormula = (abs(NDLEndMag1[NDLcounter] - NDLStartMag1[NDLcounter])*(NDLEndLoc1[NDLcounter]-NDLStartLoc1[NDLcounter]))/2
                        NDLsharpload.append(NDLsharploadFormula)
                        print("NDLsharpload: ",NDLsharpload)
                        #only for flat UDL
                        if NDLEndMag[NDLcounter] > NDLStartMag[NDLcounter]:
                            NDLflatloadFormula = NDLStartMag[NDLcounter]*(NDLEndLoc[NDLcounter] - NDLStartLoc[NDLcounter])
                            NDLflatload.append(NDLflatloadFormula)
                        else:
                            NDLflatloadFormula2 = NDLEndMag[NDLcounter]*(NDLEndLoc[NDLcounter] - NDLStartLoc[NDLcounter])
                            NDLflatload.append(NDLflatloadFormula2)
                        NDLcounter += 1
                        CountNDLlen -= 1


                else:
                    while CountNDLlen > 0:
                        print("NDLsharploadFormula =",NDLEndMag1[NDLcounter], "-",NDLStartMag1[NDLcounter], "*(",NDLEndLoc1[NDLcounter], "-",NDLStartLoc1[NDLcounter],")/2")
                        NDLsharploadFormula = (abs(NDLEndMag1[NDLcounter] - NDLStartMag1[NDLcounter])*(NDLEndLoc1[NDLcounter]-NDLStartLoc1[NDLcounter]))/2
                        NDLsharpload.append(NDLsharploadFormula)
                        print("NDLsharpload: ",NDLsharpload)
                        NDLcounter += 1
                        CountNDLlen -= 1


                print("NDLflatload:",NDLflatload)
                print("NDLsharpload:", NDLsharpload)

            else:
                pass'''
