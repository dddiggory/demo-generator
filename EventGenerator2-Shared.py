import json
import analytics
import uuid
import time
import random
import datetime
import requests
import time
import sys
from colorama import init, Fore, Back, Style

# Shared template for Event Generator. I've removed all
# customer-specific references, and left just a handful
# of industry templates for your reference

# To use:
# python EventGenerator2.py [INDUSTRY] [NUMBER OF USERS]
# e.g., python EventGenerator2.py saas 1000


#################### Config Options ####################

anonymize = False
# anonymize = True

# addSensitiveInfo = False
addSensitiveInfo = True

SEGMENT_WRITE_KEY = "" #Optionally, override the write_key here. Otherwise, the write_key set in the EventData dict will apply.


NUMBER_OF_USERS = 500 #default
DELAY_BETWEEN_USERS = 1 #time.sleep seconds to wait between users (for a 'live' debugger throughout your demo)

# sendGroupCall = False
sendGroupCall = True

companyData = [(45138, "Segment", "SaaS"), (28152, "Walmart", "Retail"), (61949, "Apple", "Consumer Tech"), (33412, "Amazon", "Retail"), (77874, "Microsoft", "Consumer Tech"), (75531, "Facebook", "Social Media"), (12102, "Google", "Consumer Tech"), (35659, "AT&T", "Telecommunications"), (99565, "Palantir", "Gov Tech"), (33151, "Cisco", "Telecommunications"), (88421, "Samsung", "Telecommunications"), (33287, "Qualcomm", "Manufacturing"), (44541, "Tencent", "Social Media"), (66431, "WeWork", "Real Estate"), (99412, "Slack", "SaaS"), (77412, "Atlassian", "SaaS")]

######################################################################

eventData = {
	"media": {
		"write_key": "YOUR_WRITE_KEY",
		"eventsWithProps": ["Playlist Generated", "Song Played", "Connect Spotify", "Search Query", "Page Viewed", "Video Playback Started", "Video Playback Paused", "Video Playback Interrupted", "Video Playback Buffer Completed", "Video Playback Seek Started", "Video Playback Seek Completed", "Video Playback Resumed", "Video Playback Completed", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Subscription Completed", "Comment Posted", "Subscription Canceled", "Article Viewed"],
		"eventsNoProps": ["Application Installed", "Application Opened", "Application Updated", "Application Backgrounded", "Application Crashed", "Application Uninstalled", "Push Notification Received"],

		"strings": {
			# "title": ["Seinfeld", "Game of Thrones", "New Girl", "The Americans", "Breaking Bad", "Better Call Saul", "Big Little Lies", "The Good Place", "One Day at a Time", "Killing Eve", "Insecure", "Riverdale", "Atlanta", "Stranger Things", "Westworld", "Curb Your Enthusiasm", "Fargo", "Mr. Robot", "Twin Peaks"],
			# "genre": ["Comedy", "Drama", "Reality", "Action", "Family", "Kids 3-8", "Kids 9-12", "Kids 12+",],
			"content_section": ["News","Sports","Entertainment","Life","Money","Tech","Travel","Opinion","Weather","Op/Ed"],
			"content_tags": ["environment","trump","parenting","food","celebrities","travel","stocks","personal finance", "mma","nfl","college","china","trade war"],
			"article_title": ['Millennials "kill" food? They just eat differently', 'Disney names new ship, second private island',"Bachelorette's Jojo, Jordan Rogers engaged again","US banana imports on alert as disease hits Colombia","Luck retirement reminder of football's human toll", "Starbucks' new Pumpkin Cream Cold Brew hits Tuesday", "Your home made simple","Tourists on scooters end up on busy highway", "21-year-old MLB star could become all-time great"],
			"article_format": ["text","video","multimedia","interactive"],
			# "music_genre": ["R&B", "Rap", "Indie Rock", "Dream Pop", "Pop Rock", "Pop"],
			# "show": ["La Reina Soy Yo", "Por Amar Sin Ley", "Despierta America"],
			# "artist": ["Dua Lipa", "Ed Sheeran", "Jason Derulo", "Madonna", "Wiz Khalifa", "Camila Cabello", "Metallica", "Rihanna", "The Mountain Goats", "Vampire Weekend", "Jay-Z", "Kanye West", "Taylor Swift", "HAIM", "Car Seat Headrest", "Shania Twain", "John Mayer", "Bleachers"],
			"full episode": [True, False],
			"ad_type": ["pre-roll", "mid-roll", "post-roll"]
		},
		"ints": {
			# "season": 10,
			# "episode": 26,
			"total_length": 3600,
			"framerate": 60,
			"position": 3600,
			"percentage_completed": 100,
			"search_results": 20
		}
	},
	"saas": {
		"write_key": "YOUR_WRITE_KEY",
		"eventsWithProps": ["Dashboard Element Added", "Dashboard Element Removed", "Marketing Page Viewed", "Trial Page Viewed", "Trial Started", "Invite User", "View Dashboard", "Launch App", "Trial Expired", "Plans Viewed", "Plan Selected", "Billing Run", "Cancellation Initiated", "Cancellation Completed", "Support Request", "Request Quote", "Content Viewed", "Alert Sent", "Alert Received", "Alert Forwarded", "Request Demo", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Hit Paywall", "Expert Session Started", "Content Viewed"],
		# "Browse Course Category", "View Course", "Course Signup", "Course Started", "Course Completed"
		"eventsNoProps": [],

		"strings": {
			# "current_product": ["PROTECT", "OPTICS", "ThreatZERO", "Smart Antivirus"],
			"acquisition_campaign": ["IP Backbone CTA Winter 2019","Organic"],
			"current_trial_status": ["Pre-Trial", "Active Trial", "Lapsed", "Subscribed"],
			"current_channel": ["SMS","Email","Livechat"],
			"current_plan": ["Basic", "Standard", "Advanced", "Lite", "Plus"],
			# "current_feature_type": ["Data Management","Governance","News & Insight","Research & Analytics","Trading & Investing"],
			# "current_product_line": ["CEM","Digital Process Automation","Business Network","ECM","Discovery","Security","AI & Analytics"],
			"current_product": ["EtherVision","My Services","Matrix"],
			# "current_feature": ["Eikon","World-Check","Eikon Messenger","AutoAudit","Transaction Monitoring","Country Risk Ranking","Enhanced Due Diligence","Verified Entity Data as a Service"],
			# "current_topic": ["Computer & Mobile Forensics", "Security+", "Ethical Hacking", "CISA"],
			# "current_certification": ["CISSP", "CEH", "CISA", "PMP", "CCNA"],
			# "current_feature": ["Support", "Sales Channels", "Manual Order Creation", "Abandoned Cart Recovery", "Gift Cards", "Advanced Report Builder", "Shipping", "Fraud Analysis", "POS App"],
			# "current_feature": ["Malware Prevention", "Script Management", "Application Control", "Device Usage Reports", "Console Reporting", "Antivirus"],
			"premium_feature?": [True, False],
			# "content_vertical": ["Automotive","Energy","Engineering","Legal","insurance","Public Sector","Utilities","Media","Life sciences","Healthcare","Financial Services"],
			# "content_topic": ["ECM","SAP","Oracle","eDOCS","Connectivity","Information security and privacy","Corporate social responsibility","GDPR","Industry regulatory compliance"],
			# "content_title": ["Top 7 benefits of supply chain optimization","The lawyer's growing role in cybersecurity","Creative collaboration for industry-leading enterprise DAM","Realizing the benefits of EIM managed services"],
			# "online_security_status": ["Compromised","Secure"],
			# "device_software_status": ["Up-to-date", "Outdated","At Risk"],
			# "online_presence_status": ["Review needed"],
			"current_role": ["Admin", "User", "Analytics Viewer"],
			# "shop_type": ["Dropshipping", "Standard Store", "Facebook Messenger Store", "Brick-and-Mortar"]
		},
		"ints": {
			"ARR": 100000,
			# "course_level": (0,10)
		}
	},
	"education": {
		"write_key": "YOUR_WRITE_KEY",
		"eventsWithProps": ["Marketing Page Viewed", "Trial Page Viewed", "Trial Requested", "Invite User", "View Dashboard", "Launch App", "Trial Expired", "Plans Viewed", "Plan Selected", "Billing Run", "Cancellation Initiated", "Cancellation Completed", "Support Request Initiated", "Request Quote", "Request Demo", "Lesson Started", "Lesson Completed", "Lesson Paused", "Lesson Signup", "Class Attended", "Program Completed", "Feature Usage", "Enrollment Started", "Enrollment Completed", "Application Started","Application Completed", "Course Dropped", "Student Portal Launched", "Message Sent", "Message Opened", "Blackboard Login", "Blackboard Home Viewed", "Support Page Viewed"],
		"eventsNoProps": [],

		"strings": {
			"institution": ["Walden University", "NewSchool of Architecture & Design", "Torrens University Australia","THINK Education","Laureate Mecca Female College of Excellence","Laureate Jeddah College of Excellence","Istanbul Bilgi University","Universidade Potiguar (UnP)"],
			"current_program": ["Business and Management","Communication and New Media", "Criminal Justice", "Education", "Health Sciences", "Information Technology","Nursing"],
			"current_degree": ["Doctoral", "Master's","Bachelor's","Certificates"],
			"message_channel": ["Student Portal", "Phone","Email"],
			"highest_education_level": ["High School Diploma", "GED","Some College", "Bachelor's Degree","Master's Degree", "Doctoral"],
			"last_login": ["2019-07-01","2019-07-05","2019-07-07","2019-07-09","2019-07-17"],
			# "current_topic": ["Cloudlets API v2", "CloudTest Provisioning API v2", "CloudTest Test Results API v1", "Content Control Utility API v2", "DataStream API v1"]
		},
		"ints": {
			"class_level": (1,50),
			"days_since_login": (0,20),
			"class_id": 9999,
			"degree_progress_%": (0,100)
		}
	},
	"retail": {
		"write_key": "YOUR_WRITE_KEY",
		"eventsWithProps": ["In-Store Visit", "Appointment Set", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "Loyalty Signup Started", "Loyalty Signup Completed", "Catalog Signup", "Return Initiated", "Return Complete", "Gift Card Purchased", "Store Locator Activated","View Today's Offers", "Store Finder Launched", "Size Guide Launched", "App Installed", "App Downloaded", "App Launched", "Cart Abandoned", "View Coupon", "Receive Coupon", "Use Coupon", "Return Initiated","Return Completed"],
		"eventsNoProps": [],

		"strings": {
			# General
			"coupon_code": ["FRIENDS30","SUMMERTIME"],
			"day_of_week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
			"time_of_day": ["Early Morning","Morning","Afternoon","Late Afternoon","Evening"],
			"current_platform": ["Web", "In-Store", "Mobile Web", "Mobile Native"],
			"messaging_preferences": ["Push", "Email", "Text"],
			"messaging_status": ["Opt-In"],
			"loyalty_status": ["None", "Active", "Premium"],
			"subscriptions": ["Back-in-Stock Notification"],
			"social_channel": ["Instagram", "Facebook", "Pinterest", "Twitter", "YouTube"],
			"utm_campaign": ["summer-sale"],
			#Custom
			"product_category": ["Jackets","Jeans","Sweatshirts","Tees"],
			"product_subcategory": ["Vintage","Cropped","High-Rise","Destructed"],
			"product_tags": ["Vintage","Cropped","High-Rise","Destructed","Apres Ski","Slim","Cropped","Flare","Acid Wash","Retro"],
			"product_promotion": ["Free Shipping","Clearance","Lookbook"],
			"search_filters": ["Size","Color","Type"],
		},
		"ints": {
			"price": (70,250),
			"discount_%": 30,
			"coupon_%": 30,
			"search_results": (0,25),
			"hour_of_day": (6,23),
			"quantity": (1,5),
			"store_id": (1111,9999),
			"region_id": (111,999),
			"items_in_cart": (1,5),
			"color_options": (1,5)

		}
	},
	"finserv": {
		"write_key": "YOUR_WRITE_KEY",
		# "eventsWithProps": ["Content Viewed","Lead Form Submitted","Search","Content Saved","Content Saved","Page Viewed","Partner Clickthrough","Affiliate Clickthrough", "Questionnaire Started","Questionnaire Completed"],
		"eventsWithProps": ["Home Screen Viewed", "Savings Account Viewed", "Savings Account Opened", "Auto-Deposit Completed", "Credit Score Viewed", "App Launched", "Spending Report Viewed", "Cancellation Page Viewed", "Cancellation Requested", "Account Canceled", "Screen Viewed", "Balance Checked", "Budget Checked", "View Subscriptions", "Support Request Opened", "Support Request Completed", "Account Balance Viewed", "Password Reset", "Saving Goal Set", "Cancel Subscription", "Trade Initiated", "Trade Confirmed", "Fund Viewed", "Customer Contact", "Content Viewed", "401k Deposit Completed", "401k Withdrawal Completed", "View Loan Status", "Application Started","Application Completed","Application Approved","Balance Viewed","Payment Started","Payment Completed", "Product Page Viewed","Marketing Page Viewed","Lead Form Submitted","CTA Clicked", "Research Content Viewed", "Research Content Shared"],
		"eventsNoProps": [],

		"strings": {
			"current_feature": ["Research","Trading Platform","Wealth Management","Institutional"],
			"current_account_type": ["Savings","Checking","Investment"],
			"current_offering": ["FA Portal","Education","Institutional Investments","Wealth Management Portal"],
			# "current_product": ["Credit Services","CareCredit","Loyalty","Synchrony Connect","MySynchrony"],
			# "current_offering": ["Retail Financing","Healthcare Financing","Online Savings","Business","Connect"],
			# "account_type":["Consumer","Business"],
			# "payment_type":["Current Balance","Current Due","Custom"],
			# "credit_card_partner": ["ABC Warehouse","Abt Electronics","Amazon","American Eagle Outfitters","Dick's Sporting Goods","Discount Tire","Crutchfield","Daltile","Midas","Men's Wearhouse","Mohawk","Musician's Friend"],
			# "content_topic": ["Home Buying","Taxes","Retirement","Banking","Credit Cards","Investing","SmartReads"],
			# "content_category": ["Home Buying","Taxes","Retirement","Banking","Credit Cards","Investing","SmartReads"],
			# "content_subtopic": ["Bank Reviews","Robo-Advisor Reviews","Financial Advisors","Card Reviews","Compare Cards","Calculators","Helpful Guides"],
			# "partner":["Acorns","Ally","Betterment","Wealthfront","Chase"],
			"service_level": ["Self-Serve", "Managed", "Top Tier"],
			"symbol": ["BEL", "BVN", "AU", "YORW","GOL","NRG","GRVY","SPA","SCG","EIDX","AVGO","AMSC","CWT","NTEC","TRCO","CJJD","NTRI","MITK","LION"],
			"contact_channel": ["Salesforce", "Qualtrics", "Yext", "Twilio", "Adobe"],
			"contact_type": ["push","email","survey","in-app message","SMS"],
			"partner_type": ["Bank","Card","Financial Advisor", "Tax Software"],
			"user_type": ["Trader","Analyst","Wealth Manager","Investment Banker"],
			"user_role": ["Trader","Analyst","Wealth Manager","Investment Banker"],
			"access_method": ["Web","Mobile App","Messenger","Desktop"],
			"content_topic": ["Institutional Investments", "Oil & Gas", "Mortage & Real Estate", "Global Emerging Markets", "Domestic Markets", "Personal Finance", "General Investing"]
		},
		"ints": {
			"credit_score": 800,
			"monthly_expenses": 2000,
			"percentage_cash": 40,
			"percentage_debt": 10,
			"percentage_investments": 50,
			"days_in_advance": (0,20),
			"amount": 1000,
			"%_change": 40,
			"age": 65,
			"dependents": 4
		},
		"traits":{
			"budget_goal": ["Trip", "Retirement", "House", "Large Purchase", "Emergency Fund", "Loans"],
			# "current_subscriptions": ["NYTimes", "Pandora", "Netflix", "Hulu", "HBONow", "The New Yorker", "NYMag", "Forbes"],
			"savings_status": ["On-Track", "Off-Track"]
		}
	},	
	"loanadmin": {
		"write_key": "YOUR_WRITE_KEY",
		"eventsWithProps": ["Signup Started", "Signup Completed", "Account Summary Viewed", "Payment Started", "Payment Completed", "Recent Payments Viewed", "Repayment Options Viewed", "Repayment Plan Selected", "Payment Pause Requested", "Loan Forgiveness Options Viewed", "Payment Scheduled", "Help Center Viewed", "Help Center Item Viewed", "Loan Refinance Viewed", "Loan Refinance Requested", "Rate Calculator Launched","Rate Calculator - Get Quote", "Quote Viewed","Quote Accepted","Skip Payment"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "Mobile Web", "iOS", "Android", "Windows Phone", "Phone/IVR"],
			"help_center_question": ["Can I pay more than my monthly payment amount?", "How do I pay with special instructions?", "How do I qualify for a repayment plan based on my income?", "How do I know whether to request a deferment or forbearance?", "As a military service member, what are my benefits and how do I request them?"],
			"help_center_topic": ["Payments", "Auto Pay", "Payment Options", "Technical Support"],
			"current_feature": ["Scheduled Payments", "Live Chat", "Repayment Planner", "Help Center"],
			"loan_type": ["Refinance","Private Loan","Personal Loan"],
			"loan_repayment": ["Revised Pay-As-You-Earn", "Pay-As-You-Earn", "Income-Based Repayment", "Income-Contingent Repayment", "Income-Sensitive Repayment", "Direct Consolidation"],
			"resource_category": ["Student Loan Refinancing","Private Student Loans","Personal Loans","Calculator","Guide"],
			"resource_title": ["Student Loan Consolidation","Fixed Rates vs Variable Rates","What is a 10-Day Payoff?","What is Precision Pricing?","Loan Application Tips","How Much Does College Cost?","8 Ways to Pay for College","How to Read Your Financial Aid Award Letter","When to Refinance Credit Card Debt","Home Equity Loan or Personal Loan?","How to Pay for Graduate Education","How to Refinance Student Loans","Decision Making Guide"],
			"content_category": ["Student Loan Refinancing","Private Student Loans","Personal Loans","Calculator","Guide"],
			"content_title": ["Student Loan Consolidation","Fixed Rates vs Variable Rates","What is a 10-Day Payoff?","What is Precision Pricing?","Loan Application Tips","How Much Does College Cost?","8 Ways to Pay for College","How to Read Your Financial Aid Award Letter","When to Refinance Credit Card Debt","Home Equity Loan or Personal Loan?","How to Pay for Graduate Education","How to Refinance Student Loans","Decision Making Guide"],
			"blog_title": ["Paying Off Student Loans? Try the 20% Rule","What's The Difference Between a Hard Credit Check and Soft Credit Check?","How to Build Credit in 6 Easy, Smart Steps"],
			"loan_status": ["Active Payments", "Deferment", "Forbearance"],
			"loan_rate": [2.05,3.45],
			"loan_rate_type": ["fixed","variable"]
		},
		"traits": {},
		"ints": {
			"loan_repayment_progress(%)": (30,100),
			"loan_total": (50000,100000),
			"loan_amount_remaining": (100,30000),
			"loan_count": (1,10)
		}
	},	
}


####Error handling for missing inputs.
try:
	industry = sys.argv[1].replace(' ','')
except:
	print "Please", Fore.GREEN+"enter a number or industry name", Fore.RESET+"for your generated data. Options below:\n", Style.BRIGHT
	for key in range(0, len(eventData.keys())):
		print str(key) + ' - ' + eventData.keys()[key]
	print Style.RESET_ALL+"\nAlternatively, include an Industry as arg1 when running the script \n(e.g., `python EventGenerator2.py media`)"
	
	industry = raw_input("\nindustry choice:  ")
	try:
		industry = eventData.keys()[int(industry)]
		print industry
	except (IndexError, ValueError): #it's out of range
		print Fore.RED+"\nBad input, exiting script.", "Valid choices are numbers 0 - "+str(len(eventData.keys())-1)+" or one of the following text strings: "
		print eventData.keys()
		quit()

if industry not in eventData.keys():
		print "Please try again. Valid industry choices are: "+str(eventData.keys())
		print "Format example: `python EventGenerator2.py media`"
		quit()

try:
	NUMBER_OF_USERS = int(sys.argv[2])
except:
	print "Bad input on arg 2 (number_of_users). Defaulting to "+str(NUMBER_OF_USERS)
####

def randomDate(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

def reformat(userStr):
	try:
		return ((userStr.decode('utf-8')).replace("\"",""))
	except:
		return userStr

if SEGMENT_WRITE_KEY == "":
	if eventData[industry].get("write_key"):
		SEGMENT_WRITE_KEY = eventData[industry]["write_key"]
		print "Using write key "+eventData[industry]["write_key"]
	else:
		SEGMENT_WRITE_KEY = raw_input("Insert your Segment write key (or hardcode in the script's header):  ")
analytics.write_key = SEGMENT_WRITE_KEY

if NUMBER_OF_USERS == None:
	NUMBER_OF_USERS = raw_input("\nHow many users to generate? Enter an integer:  ")
	try:
		NUMBER_OF_USERS = int(NUMBER_OF_USERS)
	except:
		print "\nBad input; defaulting to 500."
		NUMBER_OF_USERS = 500

	if NUMBER_OF_USERS > 500:
		NUMBER_OF_USERS = 500

print "\n\nGenerating " + str(NUMBER_OF_USERS) + " users. You may hardcode this in the script's header."
start_time = time.time()


d1 = datetime.datetime.now() - datetime.timedelta(days=5)
d2 = datetime.datetime.now()

# userRequest = requests.get("https://uinames.com/api/?ext&region=united+states&amount="+str(NUMBER_OF_USERS))
# try:
# 	randomUserList = json.loads(userRequest.text)
# except:
# 	print userRequest.text
# 	quit()
# ^ former reliance on API. removed 7/15/2019

randomUserList = json.loads(open('demodata.json', 'rU').read()) #read from local file instead

for iteration in range(NUMBER_OF_USERS):
	time.sleep(DELAY_BETWEEN_USERS)
	random_user = str(uuid.uuid4())

	firstName = random.choice(randomUserList['firstNames'])
	lastName = random.choice(randomUserList['lastNames'])
	location = random.choice(randomUserList['cities'])


	# try:
	# 	currentUser = randomUserList[iteration]
	# except KeyError: # if only 1 user is requested, API will return a Dict, not a List.
	# 	currentUser = randomUserList

	contextProperties = {}

	anonId = str(uuid.uuid4())
	userName = reformat(firstName + " " + lastName + " DEMO")
	userEmail = reformat(firstName.lower()+'.'+lastName.lower()+'.DEMO@example.com')

	# if industry == "ibm_cloud": #generate fake emails for ~20%
	# 	if random.randint(0,100) < 20:
	# 		fakeWord = "+"+random.choice(["1", "2", "3", "demo", "abcd", "qwerty", "again", "999", "9999", "newtrial", "trial"])+"@"
	# 		userEmail = userEmail.replace("@", fakeWord)
	# 		print "fake email generated: "+userEmail


	if anonymize == True:
		userName = uuid.uuid4().hex
		userEmail = uuid.uuid4().hex
	
	# userRegion = reformat(currentUser["region"])
	# userDOB = reformat(currentUser["birthday"]["mdy"])
	dobMonth = random.randint(1,12)
	dobDay = random.randint(1,30)
	dobYear = random.randint(1950,2001)
	today = datetime.date.today()
	
	userDOB = str(dobMonth).zfill(2)+'/'+str(dobDay).zfill(2)+'/'+str(dobYear)
	userAge = today.year - dobYear - ((today.month, today.day) < (dobMonth, dobYear))
	userPhone = '('+str(random.randint(111,999))+') '+str(random.randint(111,999))+'-'+str(random.randint(1111,9999))
	businessPhone = '('+str(random.randint(111,999))+') '+str(random.randint(111,999))+'-'+str(random.randint(1111,9999))
	userLTV = random.randint(0, 3000)
	userCity = location['city']
	userState = location['state']
	userConsentStatus = random.choice(["opt-out-marketing", "opt-out-emails", "opt-out-push", "opt-out-all", "subscribed"])
	consent_email = random.choice([True, False])
	consent_push = random.choice([True, False])
	consent_mktg = random.choice([True, False])
	consent_transactional = random.choice([True, False])

	homeAddress = str(random.randint(10,100)) + ' ' + random.choice(randomUserList['lastNames']) + ' St, ' + userCity + ', ' + userState 
	businessAddress = str(random.randint(10,100)) + ' ' + random.choice(randomUserList['lastNames']) + ' St, ' + userCity + ', ' + userState 

	# print homeAddress
	# print businessAddress


	userTraits = {
		"name": userName, "email": userEmail, "birthday": userDOB,
		"age": userAge, "phone": userPhone, "phone_business": businessPhone, "lifetime_value": userLTV ,
		"address": {"address_home": homeAddress, "address_business": businessAddress,
		"city": userCity, "state": userState}, 
		"address_home": homeAddress,
		"address_business": businessAddress,
		"consent_status": userConsentStatus, "consent_email": consent_email,
		"consent_push": consent_push, "consent_mktg": consent_mktg,
		"consent_transactional": consent_transactional
	}

	if addSensitiveInfo:
		sensitiveProps = {}
		SSN = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+'-'+str(random.randint(0,9))+str(random.randint(0,9))+'-'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
		# sensitiveProps.update({"SSN": SSN})
		sensitiveProps.update({"Privacy Test Prop": SSN})

		userTraits.update(sensitiveProps)

	if eventData[industry].get("traits"):
		for customTrait in eventData[industry]["traits"]:
			userTraits[customTrait] = random.choice(eventData[industry]["traits"][customTrait])
			print customTrait, userTraits[customTrait]
	userTraits.update(contextProperties)

	userExternalIds = [
		{
			"id": userPhone, 
			"type": "personal_phone", 
			"collection": "users", "encoding":"none"},
		{
			"id": businessPhone, 
			"type": "business_phone", 
			"collection": "users", "encoding":"none"},
		{
			"id": str(uuid.uuid4()), 
			"type": "member_id", 
			"collection": "users", "encoding":"none"},
		{
			"id": str(uuid.uuid4()), 
			"type": "individual_id", 
			"collection": "users","encoding":"none"},
		{
			"id": str(uuid.uuid4()), 
			"type": "mobile_device_id", 
			"collection": "users","encoding":"none"}
		]

	analytics.identify(random_user, userTraits, context={"externalIds": userExternalIds}, anonymous_id=anonId)

	groupProps = False
	if sendGroupCall:
		userGroup = random.choice(companyData)
		groupProps = {'company_id': userGroup[0], 'company_name': userGroup[1], 'industry': userGroup[2], "client_ARR": random.randint(0,500000), "client_DAU": random.randint(0,50)}
		analytics.group(random_user, userGroup[0], groupProps)

	hospitalityOwnerships = []
	if industry=="wyndham":
		hospitalityMembershipId = random.randint(1111,9999)
		hospitalityMembershipName = userName.split(' ')[1]+'-'+str(hospitalityMembershipId)
		analytics.group(random_user, hospitalityMembershipId, {"name": hospitalityMembershipName})
		analytics.group(random_user, "121", {"name": "Reinhardt-121"})

		# hospitalityOwnerships = []
		for i in xrange(0,random.randint(2,8)):
			ownershipLocation = random.choice(eventData[industry]["strings"]["location"])
			ownershipNightlyPrice = random.randint(100,3000)
			ownershipAssetId = random.randint(11111,99999)
			ownershipObj = {"Location": ownershipLocation, "Exchange Fee": ownershipNightlyPrice, "Property ID": ownershipAssetId}
			hospitalityOwnerships.append(ownershipObj)
		analytics.identify(random_user, {"Ownerships": hospitalityOwnerships})

	NUMBER_OF_EVENTS = random.randint(5, 50)
	elapsed_seconds = time.time() - start_time
	elapsed = (datetime.datetime(1,1,1) + datetime.timedelta(seconds=elapsed_seconds))



	print "("+str(elapsed.minute) + ":" + str(elapsed.second).zfill(2) + ") " + str(iteration) + ": " + userName + ", " + str(NUMBER_OF_EVENTS+(NUMBER_OF_EVENTS/2)) + " events."
	print 'Born '+userDOB+' (age '+str(userAge)+'). Lives in '+userCity+', '+userState+'.\n'
	analytics.track(random_user, "First Launch", contextProperties, anonymous_id=anonId, timestamp=datetime.datetime.now() - datetime.timedelta(days=5))
	analytics.track(random_user, "Signup Started", contextProperties, anonymous_id=anonId, timestamp=datetime.datetime.now() - datetime.timedelta(days=5))
	analytics.track(random_user, "Signup Completed", contextProperties, anonymous_id=anonId, timestamp=datetime.datetime.now() - datetime.timedelta(days=5))
	for subiteration in range(NUMBER_OF_EVENTS):
		eventName = random.choice(eventData[industry]["eventsWithProps"])
		randomTimestamp = randomDate(d1, d2)
		eventProperties = {}
		if hospitalityOwnerships:
			eventProperties.update({'Ownerships': hospitalityOwnerships})

		for stringProp in eventData[industry]["strings"]:
			stringPropValue = random.choice(eventData[industry]["strings"][stringProp])
			# analytics.identify(random_user, {stringProp: stringPropValue})
			eventProperties.update({stringProp: stringPropValue})
		
		for intProp in eventData[industry]["ints"]:
			if type(eventData[industry]["ints"][intProp]) == int or type(eventData[industry]["ints"][intProp]) == float:
				intPropValue = random.randint(eventData[industry]["ints"][intProp]/10, eventData[industry]["ints"][intProp])
			elif type(eventData[industry]["ints"][intProp]) == tuple:
				intPropValue = random.randint(eventData[industry]["ints"][intProp][0], eventData[industry]["ints"][intProp][1])
			else:
				print "'ints' properties must be ints or, optionally, tuples. Skipping "+intProp+"."
				print type(json.dumps(intProp))
				quit()
			intPropValue = float(intPropValue)
			eventProperties.update({intProp: intPropValue})

		eventProperties.update({"email": userEmail}) #including email on all calls per Mailchimp requirement
		analytics.identify(random_user, eventProperties, anonymous_id=anonId, context={"externalIds": userExternalIds})
		
		

		if groupProps:
			eventProperties.update(groupProps)	
		
		if (eventName == "Order Completed") and eventData[industry]["strings"].get("product_name"):
			productsObject = {"products": [
				{
					"product_id": random.choice(eventData[industry]["strings"]["product_name"]),
					"price": random.randint(eventData[industry]["ints"]["price"]/10,eventData[industry]["ints"]["price"]),
					"revenue": random.randint(eventData[industry]["ints"]["price"]/10,eventData[industry]["ints"]["price"]),
					"currency": "USD"
				}
			]}
			eventProperties.update(productsObject)

		analytics.track(random_user, eventName, eventProperties, timestamp=randomTimestamp, anonymous_id=anonId)


	for subiteration in range(NUMBER_OF_EVENTS/2):
		if not len(eventData[industry]["eventsNoProps"]):
			break
		eventName = random.choice(eventData[industry]["eventsNoProps"])
		randomTimestamp = randomDate(d1, d2)
		eventProperties = {}
		analytics.track(random_user, eventName, eventProperties,  anonymous_id=anonId, timestamp=randomTimestamp)



		