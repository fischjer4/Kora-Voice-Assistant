from Mongo import mongoSetUp as mongoSetUp
from Services import interactionService as interLogger

def main():
    mongoSetUp.globalInit()
data1= {
		"user"			:	"Jeremy",
		"userCommand"	:	"rotate ninety degrees left",
		"commandIntent"	:	"rotate",
		"context"		:	{
								"units"		: "degrees",
								"quantity"	: "ninety",
								"direction"	: "left"
							},
		"chosenAPICall"	:	"fusion.endpoint.rotate('ninety','degrees','left')",
		"fusionResponse": 	{
								"code" : 200,
								"response" : ""
							},
		"execTime"		:	2.32
	}
data2 = {
		"user" 			 :	"James",
		"userCommand"    :	"extrude 2 milimeters",
		"commandIntent"  :	"extrude",
		"context"        :	{
								"units"    : "milimeters",
								"quantity" : "2"
							},
		"chosenAPICall"  :	"fusion.endpoint.extrude('2','milimeters')",
		"fusionResponse" : 	{
								"code" : 200,
								"response" : ""
							},
		"execTime"       :  1.56
	}
data3 = {
		"user" 			 :	"Austin",
		"userCommand"    :	"save design as myDesgin",
		"commandIntent"  :	"save",
		"context"        :	{
								"name"    : "myDesign"
							},
		"chosenAPICall"  :	"fusion.endpoint.save('myDesign')",
		"fusionResponse" : 	{
								"code" : 504,
								"response" : "you are not authorized"
							},
		"execTime"       :  1.73
	}

interLogger.logInteraction(data1)
print("After call 1")
# interLogger.logInteraction(data2)
# print("After call 2")
# interLogger.logInteraction(data3)
# print("After call 3")

# jeremyFound = interLogger.findUserInserts('Jeremy')
# if(jeremyFound):
# 	for i in jeremyFound:
# 		print(i)
	
if __name__ == '__main__':
    main()