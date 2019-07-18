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

#since the random user API tops out at 500, recommend calling with `repeat 5 {}` in your terminal, where '5' is your preferred multiple

#################### Optional Settings Overrides ####################

anonymize = False
# anonymize = True

# addSensitiveInfo = False
addSensitiveInfo = True

SEGMENT_WRITE_KEY = "" #Optionally, override the write_key here.
#"mZEzm3BGJGP6rw3pT0OcJvE1zT8VyU3S"

NUMBER_OF_USERS = 500 #default

# sendGroupCall = False
sendGroupCall = True

companyData = [(45138, "Segment", "SaaS"), (28152, "Walmart", "Retail"), (61949, "Apple", "Consumer Tech"), (33412, "Amazon", "Retail"), (77874, "Microsoft", "Consumer Tech"), (75531, "Facebook", "Social Media"), (12102, "Google", "Consumer Tech"), (35659, "AT&T", "Telecommunications"), (99565, "Palantir", "Gov Tech"), (33151, "Cisco", "Telecommunications"), (88421, "Samsung", "Telecommunications"), (33287, "Qualcomm", "Manufacturing"), (44541, "Tencent", "Social Media"), (66431, "WeWork", "Real Estate"), (99412, "Slack", "SaaS"), (77412, "Atlassian", "SaaS")]

######################################################################

eventData = {
	"media": {
		"write_key": "6f4pcfvQXv60D3gWgB1YUAW8N5A82Tu8",
		"eventsWithProps": ["Playlist Generated", "Song Played", "Connect Spotify", "Search Query", "Page Viewed", "Video Playback Started", "Video Playback Paused", "Video Playback Interrupted", "Video Playback Buffer Completed", "Video Playback Seek Started", "Video Playback Seek Completed", "Video Playback Resumed", "Video Playback Completed", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing", "Video Content Playing"],
		"eventsNoProps": ["Application Installed", "Application Opened", "Application Updated", "Application Backgrounded", "Application Crashed", "Application Uninstalled", "Push Notification Received"],

		"strings": {
			"title": ["Seinfeld", "Game of Thrones", "New Girl", "The Americans", "Breaking Bad", "Better Call Saul", "Big Little Lies", "The Good Place", "One Day at a Time", "Killing Eve", "Insecure", "Riverdale", "Atlanta", "Stranger Things", "Westworld", "Curb Your Enthusiasm", "Fargo", "Mr. Robot", "Twin Peaks"],
			"genre": ["Comedy", "Drama", "Reality", "Action", "Family", "Kids 3-8", "Kids 9-12", "Kids 12+",],
			"music_genre": ["R&B", "Rap", "Indie Rock", "Dream Pop", "Pop Rock", "Pop"],
			"show": ["La Reina Soy Yo", "Por Amar Sin Ley", "Despierta America"],
			"artist": ["Dua Lipa", "Ed Sheeran", "Jason Derulo", "Madonna", "Wiz Khalifa", "Camila Cabello", "Metallica", "Rihanna", "The Mountain Goats", "Vampire Weekend", "Jay-Z", "Kanye West", "Taylor Swift", "HAIM", "Car Seat Headrest", "Shania Twain", "John Mayer", "Bleachers"],
			"full episode": [True, False],
			"ad_type": ["pre-roll", "mid-roll", "post-roll"]
		},
		"ints": {
			"season": 10,
			"episode": 26,
			"total_length": 3600,
			"framerate": 60,
			"position": 3600,
			"percentage_completed": 100,
			"search_results": 20
		}
	},
	"saas": {
		"write_key": "mUFv8S1qOc7q8cbfpdbMZvnKonZPCEfd",
		"eventsWithProps": ["Dashboard Element Added", "Dashboard Element Removed", "Marketing Page Viewed", "Trial Page Viewed", "Trial Started", "Invite User", "View Dashboard", "Launch App", "Trial Expired", "Plans Viewed", "Plan Selected", "Billing Run", "Cancellation Initiated", "Cancellation Completed", "Support Request", "Request Quote", "Content Viewed", "Alert Sent", "Alert Received", "Alert Forwarded", "Request Demo", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Hit Paywall", ],
		# "Browse Course Category", "View Course", "Course Signup", "Course Started", "Course Completed"
		"eventsNoProps": [],

		"strings": {
			"current_product": ["PROTECT", "OPTICS", "ThreatZERO", "Smart Antivirus"],
			"current_trial_status": ["Pre-Trial", "Active Trial", "Lapsed", "Subscribed"],
			"current_plan": ["Basic", "Standard", "Advanced", "Lite", "Plus"],
			# "current_topic": ["Computer & Mobile Forensics", "Security+", "Ethical Hacking", "CISA"],
			# "current_certification": ["CISSP", "CEH", "CISA", "PMP", "CCNA"],
			# "current_feature": ["Support", "Sales Channels", "Manual Order Creation", "Abandoned Cart Recovery", "Gift Cards", "Advanced Report Builder", "Shipping", "Fraud Analysis", "POS App"],
			"current_feature": ["Malware Prevention", "Script Management", "Application Control", "Device Usage Reports", "Console Reporting", "Antivirus"],
			"premium_feature?": [True, False],
			"current_role": ["Admin", "User", "Analytics Viewer"],
			# "shop_type": ["Dropshipping", "Standard Store", "Facebook Messenger Store", "Brick-and-Mortar"]
		},
		"ints": {
			"ARR": 100000,
			# "course_level": (0,10)
		}
	},
	"redhat": {
		"write_key": "mUFv8S1qOc7q8cbfpdbMZvnKonZPCEfd",
		"eventsWithProps": ["Dashboard Element Added", "Dashboard Element Removed", "Marketing Page Viewed", "Trial Page Viewed", "Trial Started", "Invite User", "View Dashboard", "Launch App", "Trial Expired", "Plans Viewed", "Plan Selected", "Billing Run", "Cancellation Initiated", "Cancellation Completed", "Support Request", "Hit Paywall", "Request Quote", "Content Viewed", "Alert Sent", "Alert Received", "Alert Forwarded", "Request Demo", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Hit Paywall", "Browse Course Category", "View Course", "Course Signup", "Course Started", "Course Completed"],
		"eventsNoProps": [],

		"strings": {
			"current_product": ["OpenShift Application Runtimes", "OpenShift Container Platform", "OpenStack Platform", "Ceph Storage", "Cloud Suite", "Cloud Infrastructure", "CloudForms", "Insights", "Enterprise Linux", "Ansible Automation", "Satellite", "Virtualization", "Gluster Storage", "Data Grid", "Red Hat Learning Subscription"],
			"current_feature": ["Hands-On Labs", "Expert Seminars", "Course E-Books", "Instructor Videos", "Certification Exams"],
			"current_trial_status": ["Pre-Trial", "Active Trial", "Lapsed", "Subscribed"],
			"renewal_date": ["06-01-2019", "07-01-2019", "08-01-2019"],
			"current_plan": ["Basic", "Standard", "Advanced", "Lite", "Plus"],
			"paywall_type": ["Education Resource", "Usage Cap", "Feature Gate"],
			# "current_feature": ["Support", "Sales Channels", "Manual Order Creation", "Abandoned Cart Recovery", "Gift Cards", "Advanced Report Builder", "Shipping", "Fraud Analysis", "POS App"],
			"premium_feature?": [True, False],
			"current_role": ["Admin", "User", "Analytics Viewer"],
			"learning_subscription": ["None", "Basic Individual", "Standard Individual", "Developer Individual", "Basic Enterprise", "Standard Enterprise", "Developer Enterprise"]
			# "shop_type": ["Dropshipping", "Standard Store", "Facebook Messenger Store", "Brick-and-Mortar"]
		},
		"ints": {
			"ARR": 100000,
			"course_level": (0,10)
		}
	},
	"shopify": {
		"write_key": "bvMWDN7wP0mqQbmNFr7ks7VEZsQqYd0m",
		"eventsWithProps": ["Dashboard Element Added", "Dashboard Element Removed", "Marketing Page Viewed", "Trial Page Viewed", "Trial Started", "Invite User", "View Dashboard", "Launch App", "Trial Expired", "Plans Viewed", "Plan Selected", "Billing Run", "Cancellation Initiated", "Cancellation Completed", "Support Request", "Request Quote", "Content Viewed", "Alert Sent", "Alert Received", "Alert Forwarded", "Request Demo", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Feature Usage", "Hit Paywall"],
		"eventsNoProps": [],

		"strings": {
			# "current_product": ["PROTECT", "OPTICS", "ThreatZERO", "Smart Antivirus"],
			"current_trial_status": ["Pre-Trial", "Active Trial", "Lapsed", "Subscribed"],
			"current_plan": ["Basic", "Standard", "Advanced", "Lite", "Plus"],
			"current_feature": ["Support", "Sales Channels", "Manual Order Creation", "Abandoned Cart Recovery", "Gift Cards", "Advanced Report Builder", "Shipping", "Fraud Analysis", "POS App"],
			"premium_feature?": [True, False],
			"current_role": ["Admin", "User", "Analytics Viewer"],
			"shop_type": ["Dropshipping", "Standard Store", "Facebook Messenger Store", "Brick-and-Mortar"]
		},
		"ints": {
			"ARR": 100000
		}
	},
	"education": {
		"write_key": "mUFv8S1qOc7q8cbfpdbMZvnKonZPCEfd",
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
			"degree_progress": (0,100)
		}
	},
	"retail": {
		"write_key": "0QOx6XUUIM1kokYyAHdEelDIsg1z2M20",
		"eventsWithProps": ["In-Store Visit", "Appointment Set", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "Loyalty Signup Started", "Loyalty Signup Completed", "Catalog Signup", "Return Initiated", "Return Complete", "Gift Card Purchased", "Store Locator Activated","View Today's Offers", "Store Finder Launched", "Size Guide Launched", "App Launched", "Cart Abandoned", "Nutritional Info Viewed", "Delivery Order Started","Delivery Order Completed", "MyBK Launched", "View Coupon", "Receive Coupon", "Use Coupon"],
		"eventsNoProps": [],

		"strings": {
			# "category": ["Electronics", "Shirts", "T-Shirts", "Shoes", "Dresses", "Jewelry"],
			# "occasion": ["Mother's Day", "Birthday", "Sympathy", "Get Well", "Housewarming", "New Baby", "Retirement"],
			# "flower_type": ["Carnations", "Daisies", "Lilies", "Mixed Bouquets", "Orchids", "Roses","Sunflowers","Tulips"],
			# "category": ["Pants","Jeans","Sweaters","Tees and Knits","Blouses and Shirts","Jackets and Outerwear","Dresses","Skirts","Suiting","Lounge","Shorts","Sun & Swim","Intimates"],
			# "product_name": ["Cutout Racerback Tank", "Fallon Printed Wide-Leg Pants", "Santa Maria Maxi Dress", "Lucy Overalls", "Carmen Top", "High Tides Mini", "City of Angels Cami", "Under the Moonlight Maxi Dress"],
			"product_name": ["Impossible Whopper","Rodeo King", "Triple Stacker King", "Double Stacker King", "Single Stacker King"],
			"product_category": ["Burgers","Chicken & More","Salads & Veggies","Beverages", "Breakfast","Coffee","Sides"],
			"coupon_code": ["FRIENDS30","BKNOW","SUMMERTIME"],
			"day_of_week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
			"time_of_day": ["Early Morning","Morning","Afternoon","Late Afternoon","Evening"],
			# "partner_brand": ["Keds", "Sperry", "Superga"],
			# "product_tags": ["New Arrivals", "T By Talbots", "Work Shop", "Linen Shop", "Petite", "Keds", "Sperry", "Superga"],
			# "brand": ["Altra", "Icebreaker", "Smartwool", "The North Face", "Timberland", "Eagle Creek", "Eastpak", "JanSport", "Kipling", "Napapijri", "Vans", "Terra", "Lee", "Wrangler"],
			# "brand_category": ["Outdoor", "Active", "Work", "Jeans"],
			# "brands": ["Nike", "Outdoor Voices", "Urban Outfitters", "Anthropologie", "ASOS", "Supreme", "Sephora", "Bonobos"],
			"current_platform": ["Web", "In-Store", "Mobile Web", "Mobile Native"],
			"messaging_preferences": ["Push", "Email", "Text"],
			"messaging_status": ["Opt-In"],
			"loyalty_status": ["None", "Active", "Premium"],
			# "credit_card_member": [True,False],
			"subscriptions": ["Back-in-Stock Notification"],
			"social_channel": ["Instagram", "Facebook", "Pinterest", "Twitter", "YouTube"],
			"utm_campaign": ["summer-2019"]
			# "current_brand": ["1-800-Flowers", "Harry & David", "1-800 Baskets", "Simply Chocolate", "Cheryl's Cookies", "Personalization Universe", "The Popcorn Factory", "Wolferman's", "Stock Yards", "Goodsey"]
		},
		"ints": {
			"price": 300,
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
	"freepeople": {
		"write_key": "1NVSv2OEBHE77kWCfueMC9JPfLgVgIHa", #lone dataset
		# "write_key": "0QOx6XUUIM1kokYyAHdEelDIsg1z2M20", #diggory01
		"eventsWithProps": ["In-Store Visit", "Appointment Set", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed","Order Completed","Order Completed","Order Completed","Order Completed","Order Completed","Order Completed","Order Completed","Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "Loyalty Signup Started", "Loyalty Signup Completed", "Catalog Signup", "Return Initiated", "Return Complete", "Gift Card Purchased", "Store Locator Activated","View Today's Offers", "Store Finder Launched", "Size Guide Launched", "App Launched", "Cart Abandoned", "Message Viewed"],
		"eventsNoProps": [],

		"strings": {
			# "category": ["Electronics", "Shirts", "T-Shirts", "Shoes", "Dresses", "Jewelry"],
			# "occasion": ["Mother's Day", "Birthday", "Sympathy", "Get Well", "Housewarming", "New Baby", "Retirement"],
			# "flower_type": ["Carnations", "Daisies", "Lilies", "Mixed Bouquets", "Orchids", "Roses","Sunflowers","Tulips"],
			"category": ["Pants","Jeans","Sweaters","Tees and Knits","Blouses and Shirts","Jackets and Outerwear","Dresses","Skirts","Suiting","Lounge","Shorts","Sun & Swim","Intimates"],
			"message_channel": ["Mobile Push","Email"],
			"product_name": ["Cutout Racerback Tank", "Fallon Printed Wide-Leg Pants", "Santa Maria Maxi Dress", "Lucy Overalls", "Carmen Top", "High Tides Mini", "City of Angels Cami", "Under the Moonlight Maxi Dress"],
			"coupon_code": ["FRIENDS30"],
			"product_tags": ["FP Beach","Customer Favorites","Back in Stock"],
			"day_of_week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
			# "partner_brand": ["Keds", "Sperry", "Superga"],
			# "product_tags": ["New Arrivals", "T By Talbots", "Work Shop", "Linen Shop", "Petite", "Keds", "Sperry", "Superga"],
			# "brand": ["Altra", "Icebreaker", "Smartwool", "The North Face", "Timberland", "Eagle Creek", "Eastpak", "JanSport", "Kipling", "Napapijri", "Vans", "Terra", "Lee", "Wrangler"],
			# "brand_category": ["Outdoor", "Active", "Work", "Jeans"],
			# "brands": ["Nike", "Outdoor Voices", "Urban Outfitters", "Anthropologie", "ASOS", "Supreme", "Sephora", "Bonobos"],
			"current_platform": ["Web", "In-Store", "Mobile Web", "Mobile Native"],
			"messaging_preferences": ["Push", "Email", "Text"],
			"messaging_status": ["Opt-In"],
			"loyalty_status": ["None", "Active", "Premium"],
			# "credit_card_member": [True,False],
			"subscriptions": ["Back-in-Stock Notification"],
			"social_channel": ["Instagram", "Facebook", "Pinterest", "Twitter", "YouTube"],
			"currency": ["USD"],
			# "current_brand": ["1-800-Flowers", "Harry & David", "1-800 Baskets", "Simply Chocolate", "Cheryl's Cookies", "Personalization Universe", "The Popcorn Factory", "Wolferman's", "Stock Yards", "Goodsey"]
		},
		"ints": {
			"price": 300,
			"revenue": 300,
			"discount_%": 30,
			"search_results": (0,25),
			"hour_of_day": (6,23),
			"quantity": (1,5),
			"store_id": (1111,9999),
			"region_id": (111,999),
			"items_in_cart": (1,5),
			"color_options": (1,5)

		}
	},
	"kimberlyclark": {
		"write_key": "0QOx6XUUIM1kokYyAHdEelDIsg1z2M20",
		"eventsWithProps": ["In-Store Visit", "Appointment Set", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "Loyalty Signup Started", "Loyalty Signup Completed", "Catalog Signup", "Return Initiated", "Return Complete", "Gift Card Purchased", "Store Locator Activated","View Today's Offers", "Store Finder Launched", "Size Guide Launched", "App Launched", "Cart Abandoned"],
		"eventsNoProps": [],

		"strings": {
			"product_segment": ["Adult Care", "Baby and Child Care", "Feminine Care", "Family Care", "Kimberly-Clark Professional"],
			"day_of_week": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
			# "product_tags": ["New Arrivals", "T By Talbots", "Work Shop", "Linen Shop", "Petite", "Keds", "Sperry", "Superga"],
			"brand": ["Kleenex", "Andrex", "Hakle","Cottonelle","Scottex","Page","Neve","Petals","Wondersoft","Tela","Scott","Viva"],
			# "brand_category": ["Outdoor", "Active", "Work", "Jeans"],
			# "brands": ["Nike", "Outdoor Voices", "Urban Outfitters", "Anthropologie", "ASOS", "Supreme", "Sephora", "Bonobos"],
			"current_platform": ["Web", "In-Store", "Mobile Web", "Mobile Native"],
			"messaging_preferences": ["Push", "Email", "Text"],
			"messaging_status": ["Opt-In"],
			"loyalty_status": ["None", "Active", "Premium"],
			# "credit_card_member": [True,False],
			"subscriptions": ["Back-in-Stock Notification"],
			"social_channel": ["Instagram", "Facebook", "Pinterest", "Twitter", "YouTube"],
			# "current_brand": ["1-800-Flowers", "Harry & David", "1-800 Baskets", "Simply Chocolate", "Cheryl's Cookies", "Personalization Universe", "The Popcorn Factory", "Wolferman's", "Stock Yards", "Goodsey"]
		},
		"ints": {
			"price": 300,
			"discount_%": 30,
			"search_results": (0,25),
			"hour_of_day": (6,23),
			"quantity": (1,5),
			"store_id": (1111,9999),
			"region_id": (111,999),
			"items_in_cart": (1,5)
		}
	},
	"sears": {
		"write_key": "0QOx6XUUIM1kokYyAHdEelDIsg1z2M20",
		"eventsWithProps": ["In-Store Visit", "Add to Cart", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "Newsletter Signup"],
		"eventsNoProps": [],

		"strings": {
			"category": ["Refrigerators & Freezers","Washers & Dryers","Cooking Appliances","Mattresses","Dishwashers & Disposals", "Lawn & Garden", "Tools & Tool Storage", "Outdoor Living", "Furniture Collections", "Fitness & Sports", "Electronics", "Home"],
			"brand": ["Kenmore", "LG", "Whirlpool", "Samsung", "GE", "Amana", "Maytag", "Bosch", "Frigidaire", "KitchenAid"],
			"current_platform": ["Web", "In-Store", "Mobile"],
			"navigation_source": ["Top Deals", "Search", "Direct Link", "Weekly Ad", "Deal of the Day"],
			"nearest_store": ["West Orange, NJ", "Watchung, NJ", "Newton, NJ", "Philadelphia, PA", "Voorhees, NJ", "Norristown, PA", "Newark, DE"],
			"current_store": ["West Orange, NJ", "Watchung, NJ", "Newton, NJ", "Philadelphia, PA", "Voorhees, NJ", "Norristown, PA", "Newark, DE"]
		},
		"ints": {
			"price": 300,
			"quantity": 25,
			"store_id": (1111,9999),
			"region_id": (111,999)
		}
	},
	"paybyphone": {
		"write_key": "0QOx6XUUIM1kokYyAHdEelDIsg1z2M20",
		"eventsWithProps": ["Alert Viewed", "Top-Up Started", "Top-Up Completed", "Meter Status Checked", "App Launched", "Onboarding Started", "Onboarding Completed", "Location Code Entered", "Parking Duration Entered", "Parking Extended", "Error", "Payment Method Added"],
		"eventsNoProps": [],

		"strings": {
			"interaction_method": ["Phone Call", "Web", "Mobile Web", "Mobile App"],
			"payment_method": ["Credit Card"],
			"user_type": ["Consumer", "Business", "Parking Operator"],
			"current_platform": ["Web", "Mobile Web", "iOS", "Android", "Blackberry"],
			"current_location": ["Anchorage, AK","Ann Arbor, MI", "Miami,FL", "Aspen, CO", "Nashua, NH", "New Castle, NY", "New Hope, PA", "Oakland, CA", "Boston, MA",  "Bellevue, WA", "Portland, OR", "Las Vegas, NV", "Kirkland, WA", "Montreal, QC", "Ottawa, ON", "University of Texas", "Yale University", "Duke University", "Toronto, ON"],
			"error_type": ["Invalid location code.", "Insufficient funds.", "Payment method declined.", ]
		},
		"ints": {
			"parking_duration": 60,
			"max_parking_duration": (60,120),
			"location_id": (1111,9999),
			"region_id": (111,999)
		}
	},
	"theShadeStore": {
		"write_key": "0QOx6XUUIM1kokYyAHdEelDIsg1z2M20",
		"eventsWithProps": ["In-Store Visit", "Appointment Set", "Order Swatches", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "Catalog Ordered"],
		"eventsNoProps": [],

		"strings": {
			"shade_category": ["Roller Shades", "Solar Shades", "Roman Shades", "Woven Wood Shades", "Cellular Shades", "Wood Blinds", "Vertical Blinds", "Metal Blinds", "Custmo Drapes", "Drapery Hardware", "Valances & Cornices"],
			"shade_features": ["Light Filtering", "Blackout", "Double Roller", "Zen Roller", "Sunbrella", "Cascade", "Pleated"],
			# "brands": ["Nike", "Outdoor Voices", "Urban Outfitters", "Anthropologie", "ASOS", "Supreme", "Sephora", "Bonobos"],
			"current_platform": ["Web", "In-Store", "Mobile Web", "Mobile Native"],
		},
		"ints": {
			"price": (200,800),
			"quantity": 25,
			"store_id": (1111,9999),
			"region_id": (111,999)
		}
	},
	"consumer": {
		"eventsWithProps": [],
		"eventsNoProps": [],

		"strings": {

		},
		"ints": {

		}
	},
	"finserv": {
		"write_key": "nRiCwhsHA8H3pJ1D5dm70wZmRTpNX1qA",
		# "eventsWithProps": ["App Launched", "Account Closure Options Viewed", "Account Closure Requested", "Account Closed", "Screen Viewed", "Balance Checked", "P2P Payment Started", "P2P Payment Completed", "Support Request Opened", "Support Request Completed", "Financial Advisor Message Sent", "Account Balance Viewed", "Password Reset", "Credit Increase Requested", "Payment Submitted"],
		"eventsWithProps": ["Home Screen Viewed", "Savings Account Viewed", "Savings Account Opened", "Auto-Deposit Completed", "Credit Score Viewed", "App Launched", "Spending Report Viewed", "Cancellation Page Viewed", "Cancellation Requested", "Account Canceled", "Screen Viewed", "Balance Checked", "Budget Checked", "View Subscriptions", "Support Request Opened", "Support Request Completed", "Account Balance Viewed", "Password Reset", "Saving Goal Set", "Cancel Subscription", "Trade Initiated", "Trade Confirmed", "Fund Viewed", "Customer Contact", "Content Viewed", "401k Deposit Completed", "401k Withdrawal Completed"],
		"eventsNoProps": [],

		"strings": {
			"current_feature": ["Budget", "Auto-Deposit", "Saving Goals", "Subscription Manager", "Credit Score", "Savings Account"],
			"current_offering": ["FA Portal","Education","Institutional Investments","Wealth Management Portal"],
			"service_level": ["Self-Serve", "Managed", "Top Tier"],
			"symbol": ["BEL", "BVN", "AU", "YORW","GOL","NRG","GRVY","SPA","SCG","EIDX","AVGO","AMSC","CWT","NTEC","TRCO","CJJD","NTRI","MITK","LION"],
			"contact_channel": ["Salesforce", "Qualtrics", "Yext", "Twilio", "Adobe"],
			"contact_type": ["push","email","survey","in-app message","SMS"],
			"content_topic": ["Institutional Investments", "Oil & Gas", "Mortage & Real Estate", "Global Emerging Markets", "Domestic Markets", "Personal Finance", "General Investnig"]
		},
		"ints": {
			"credit_score": 800,
			"monthly_expenses": 2000,
			"percentage_cash": 40,
			"percentage_debt": 10,
			"percentage_investments": 50,
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
	"fidelity": {
		"write_key": "nRiCwhsHA8H3pJ1D5dm70wZmRTpNX1qA",
		# "eventsWithProps": ["App Launched", "Account Closure Options Viewed", "Account Closure Requested", "Account Closed", "Screen Viewed", "Balance Checked", "P2P Payment Started", "P2P Payment Completed", "Support Request Opened", "Support Request Completed", "Financial Advisor Message Sent", "Account Balance Viewed", "Password Reset", "Credit Increase Requested", "Payment Submitted"],
		"eventsWithProps": ["PSW Launched", "Participant Searched", "Participant Record Viewed", "Notification Viewed", "Notification Opened", "Notification Response Sent", "File Manager Launched", "File Created", "File Uploaded", "File Manager Error", "Support Portal Launched", "Support Session Started", "Support Session Completed"],
		"eventsNoProps": [],

		"strings": {
			"File Context": ["Benefits Records", "Company Demographics", "Fund Information"],
			"File Type": ["CSV", "XLSX", "TXT", "DOC", "PNG", "PDF"],
			"Error Type": ["Filesize exceeds limits.", "Incorrect filetype.", "Insufficient permissions."]
		},
		"ints": {
			"File Size (MB)": (1,100)
		},
		"traits":{
		}
	},
	"zendesk": {
		"eventsWithProps": ["Order Completed", "Recurring Order Canceled", "Ticket Solved", "Ticket Escalated", "Ticket Created", "Ticket Assigned", "Ticket Viewed", "Ticket Status Changed", "Ticket Priority Decrease", "Ticket Comment Added", "NPS Survey Submitted"],
		"eventsNoProps": [],

		"strings": {
			"subject": ["Unable to Access Our Account", "Optimizely Data File", "Replay Request - 2", "Zendesk Source", "Connecting Hubspot x Segment", "SFMC UUID scheme", "Stripe cards table in Redshift", "Bigquery setup question", "Return request #0351xx0", "Replay request", "Proxy server setup", "In-store coupon question"],
			"status": ["open", "pending", "hold", "solved", "closed"],
			"priority": ["urgent", "high", "normal", "low"],
			"type": ["problem", "incident", "question", "task"],
			"tags": ["warehouses", "billing", "site", "app", "in-store", "infra", "libraries", "GDPR", "security", "partner request"],
		},
		"ints": {
			"requester_id": 99999999,
			"organization_id": 99999,
			"group_id": 99999,
			"ticket_age": 100,
			"ticket_id": 99999,
			"agent_id": 99999,
			"nps_score": 10
		}
	},
	"draftkings": {
		"write_key": "IOON1YsCfPGiXBeWC6JlFK45OJewxJJi",
		"eventsWithProps": ["App Launch", "Place Bet", "Start Roster", "Confirm Roster", "QuickBet", "League Page", "Event Detail", "Content Viewed", "Signup Started", "Signup Completed", "View Team", "Play"],
		"eventsNoProps": [],

		"strings": {
			"current_app": ["Sportsbook", "Daily Fantasy Sports", "DK Live"],
			"app_id": ["sbios", "sbandroid", "dkios", "dkandroid", "dkweb", "sbweb", "dkliveandroid", "dkliveios", "dkliveweb"],
			"league": ["NFL","NBA","MLB","GOLF","NHL","NAS","MMA","SOC","CFL","CFB","LOL","EL","TEN"],
			"team": ["Patriots", "Rams", "Giants", "Packers", "Jets", "Eagles", "Falcons", "Vikings", "Steelers", "Panthers", "49ers", "Jaguars", "Texans", "Raiders", "Cowboys"],
			"stake_level": ["low", "medium", "high", "high+"],
			"state/region": ["Non-US", "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

		},
		"ints": {
			"bet_amount": 1000
		}
	},
	"thomsonreuters": {
		"write_key": "iDpmmWYMrliCyH1nIQoPjYs1hAqfWJ3h",
		"eventsWithProps": ["Content Viewed", "Content Saved", "Product Launched", "Saved Stories Viewed", "Feed Viewed", "Social Share"],
		"eventsNoProps": ["App Launch", "App Backgrounded"],

		"strings": {
			"sector": ["Legal", "Financial", "News & Media", "Risk Management", "Tax & Accounting", "Thomson Reuters Corporate", "Government Solutions", "Technology", "Energy", "Automotive"],
			"topic": ["Artificial intelligence", "Big data", "Blockchain", "Brexit", "Data privacy & GDPR", "Global trade", "Regulatory intelligence"],
			"report_name": ["Hanson Robotics founder: Caring about AI that cares about us", "WEF's head of AI: Bringing leaders together around socially responsible AI", "8 legal experts weigh in on some of the industry's top trends in 2018", "UK's AI Council chair: Humanizing the business of artificial intelligence", "Who are the most influential people in your company?", "Are there more twists to come in the online sales tax saga?", "Cryptoeconomics: Can blockchain reinvent justice systems?", "Why we shouldn't be afraid of artificial intelligence"],
			"current_product": ["Eikon", "Eikon Messenger", "Datastream", "FXall", "REDI", "Elektron Data Platform"],
			"content_type": ["Special Report", "Article"],
			"platform": ["ios", "android", "web"]
		},
		"ints": {
			"read_time": 30,
			"account_id": 9999
		}
	},
	"wework": {
		"write_key": "UvHbEuWygeDIYOCaKn33ooTMsrd4vNux",
		"eventsWithProps": ["Visit Scheduled", "Visit Completed", "Building Viewed", "Labs Flow Entered", "Labs Flow Completed", "Card Swipe", "Support Request Opened", "Support Request Completed", "Quote Requested", "Membership Meeting Scheduled", "Membership Meeting Completed", "Community Post Viewed", "Community Post Commented", "Community Post Started", "Community Post Created", "Program RSVP", "Program Attended"],
		"eventsNoProps": [],

		"strings": {
			"platform": ["ios", "android", "web", "offline"],
			"program_type": ["e-commerce", "programming", "enterpreneurship", "networking", "misc"],
			"user_type": ["prospect", "has_toured", "wework_member", "labs_member"],
			"wework_city": ["Atlanta","Austin","Baltimore","Boston","Boulder","Charlotte","Chicago","College Park, MD","Dallas - Fort Worth","Denver","Detroit","Houston","Kansas City","Las Vegas","Los Angeles","Miami","Minneapolis","Nashville","New York City","Orange County","Philadelphia","Phoenix","Pittsburgh","Portland","Raleigh-Durham","SF Bay Area","Salt Lake City","San Antonio","San Diego","Seattle","Washington, D.C."],
			"wework_bldg": ["750 Lexington","154 W 14th", "880 3rd Ave", "408 Broadway","609 Greenwich", "1619 Broadway", "460 Park Ave S", "21 Penn Plaza", "214 W 29th", "130 5th", "Dock 72", "One Gotham Ctr", "3537 36th", "27-01 Queens Plaza N", "South Williamsburg", "134 N 4th", "115 Broadway"],
			"member_type": ["Private Office", "Dedicated Desk", "Hot Desk"],

		},
		"ints": {
		},
		"traits": {
			"user_type": ["prospect", "has_toured", "wework_member", "labs_member"],
			"wework_city": ["Atlanta","Austin","Baltimore","Boston","Boulder","Charlotte","Chicago","College Park, MD","Dallas - Fort Worth","Denver","Detroit","Houston","Kansas City","Las Vegas","Los Angeles","Miami","Minneapolis","Nashville","New York City","Orange County","Philadelphia","Phoenix","Pittsburgh","Portland","Raleigh-Durham","SF Bay Area","Salt Lake City","San Antonio","San Diego","Seattle","Washington, D.C."],
			"wework_bldg": ["750 Lexington","154 W 14th", "880 3rd Ave", "408 Broadway","609 Greenwich", "1619 Broadway", "460 Park Ave S", "21 Penn Plaza", "214 W 29th", "130 5th", "Dock 72", "One Gotham Ctr", "3537 36th", "27-01 Queens Plaza N", "South Williamsburg", "134 N 4th", "115 Broadway"],
			"member_type": ["Private Office", "Dedicated Desk", "Hot Desk"]
		}
	},
	"healthcare": {
		"write_key": "1cllWiQDgAcDQX8QCVzOoN93aXWaHXV9",
		"eventsWithProps": ["Set Reminder", "Feature Usage", "View Calendar", "Support Request Started", "Search Started", "Search Result Clicked", "App Launched", "App Installed", "First App Launch", "Appointment Booked", "Appointment Rescheduled", "Appointment Cancelled", "Reviews Viewed", "Practitioner Viewed", "Review Submitted", "Review Started", "App Link Texted"],
		"eventsNoProps": [],

		"strings": {
			"platform": ["ios", "android", "web"],
			"specialization": ["Acupuncturists","Allergists","Audiologists","Cardiologists","Chiropractors","Dentists","Dermatologists","Dietitians","Ear, Nose & Throat Doctors","Emergency Medicine Physicians","Endocrinologists","Endodontists","Eye Doctors","Family Physicians","Gastroenterologists","Hand Surgeons","Hearing Specialists","Hematologists","Infectious Disease Specialists","Infertility Specialists","Internists","Naturopathic Doctors","Nephrologists","Neurologists","Neurosurgeons","Nurse Practitioners","Nutritionists","OB-GYNs","Oncologists","Ophthalmologists","Optometrists","Oral Surgeons","Orthodontists","Orthopedic Surgeons","Pain Management Specialists","Pediatric Dentists","Pediatric Urgent Care Specialists","Pediatricians","Periodontists","Physiatrists","Physical Therapists","Plastic Surgeons","Podiatrists","Doctors","Prosthodontists","Psychiatrists","Psychologists","Psychotherapists","Pulmonologists","Radiologists","Rheumatologists","Sleep Medicine Specialists","Sports Medicine Specialists","Surgeons","Therapists / Counselors","Travel Medicine Specialists","Urgent Care Specialists","Urologists"],
			"changed_by": ["Patient", "Practitioner"],
			"current_feature": ["Calendar", "Tracker", "Reminders", "Health Guides", "Live Help"],
			"insurance_provider": ["Aetna", "Blue Cross Blue Shield", "Cigna", "EmblemHealth", "UnitedHealthcare", "None", "Banner Health", "Avera Health", "Assurant Health", "Medicare", "Medicaid", "MetroHealth", "MetLife"]

		},
		"ints": {
			"search_results": 100,
			"lifetime_appointments": 50,
			"lifetime_cancellations": 10,
			"days_in_advance": 30,
			"average_rating": 5,
			"total_reviews": 500,
			"distance_miles": 10
		},
		"traits": {
			"current_feature": ["Calendar", "Tracker", "Reminders", "Health Guides", "Live Help"],	
			"insurance_provider": ["Aetna", "Blue Cross Blue Shield", "Cigna", "EmblemHealth", "UnitedHealthcare", "None", "Banner Health", "Avera Health", "Assurant Health", "Medicare", "Medicaid", "MetroHealth", "MetLife"]
		}
	},
	"healthfirst": {
		"write_key": "1cllWiQDgAcDQX8QCVzOoN93aXWaHXV9",
		"eventsWithProps": ["Set Reminder", "Feature Usage", "View Calendar", "Support Request Started", "Search Started", "Search Result Clicked", "App Launched", "App Installed", "First App Launch", "Appointment Booked", "Appointment Rescheduled", "Appointment Cancelled", "Reviews Viewed", "Provider Viewed", "Review Submitted", "Review Started", "App Link Texted", "Plan Viewed", "Plan Selected", "Claim Form Started", "Claim Form Submitted", "Claim Response Viewed", "Plan-Finder Started", "Plan Renewed", "Message Viewed", "Message Sent", "App Crash", "Login", "Home Service", "Eligibility Viewed", "Bill Viewed", "Bill Paid", "Caremark Accessed", "OTC Benefits Viewed", "Account Creation Started", "Anonymous Visit", "Account Creation Completed"],
		"eventsNoProps": [],

		"strings": {
			"platform": ["ios", "android", "web", "IVR/phone"],
			"messaging_channel": ["Email", "Message Center", "Push Notification", "Phone Call/IVR", "Livechat"],
			"user_type": ["Employer", "Member", "Provider", "Broker", "Member", "Member", "Member", "Member", "Member", "Member"],
			"provider_type": ["Acupuncturists","Allergists","Audiologists","Cardiologists","Chiropractors","Dentists","Dermatologists","Dietitians","Ear, Nose & Throat Doctors","Emergency Medicine Physicians","Endocrinologists","Endodontists","Eye Doctors","Family Physicians","Gastroenterologists","Hand Surgeons","Hearing Specialists","Hematologists","Infectious Disease Specialists","Infertility Specialists","Internists","Naturopathic Doctors","Nephrologists","Neurologists","Neurosurgeons","Nurse Practitioners","Nutritionists","OB-GYNs","Oncologists","Ophthalmologists","Optometrists","Oral Surgeons","Orthodontists","Orthopedic Surgeons","Pain Management Specialists","Pediatric Dentists","Pediatric Urgent Care Specialists","Pediatricians","Periodontists","Physiatrists","Physical Therapists","Plastic Surgeons","Podiatrists","Doctors","Prosthodontists","Psychiatrists","Psychologists","Psychotherapists","Pulmonologists","Radiologists","Rheumatologists","Sleep Medicine Specialists","Sports Medicine Specialists","Surgeons","Therapists / Counselors","Travel Medicine Specialists","Urgent Care Specialists","Urologists"],
			"changed_by": ["Patient", "Practitioner"],
			"support_type": ["Claim Support", "Tech Support", "Find a Practice"],
			"current_feature": ["Calendar", "Tracker", "Reminders", "Health Guides", "Live Help"],
			"renewal_date": ["2019-04-01", "2019-05-01", "2019-06-01"],
			"plan_category": ["Healthfirst Leaf", "Medicaid Managed Care", "Healthfirst Essential", "Medicare", "Managed Long Term Care", "Healthfirst AbsoluteCare FIDA", "Child Health Plus", "Personasl Wellness", "Healthfirst Pro & Pro Plus EPO"],
			"most_recent_activity": ["Set Reminder", "Feature Usage", "View Calendar", "Support Request Started", "Search Started", "Search Result Clicked", "App Launched", "App Installed", "First App Launch", "Appointment Booked", "Appointment Rescheduled", "Appointment Cancelled", "Reviews Viewed", "Provider Viewed", "Review Submitted", "Review Started", "App Link Texted", "Plan Viewed", "Plan Selected", "Claim Form Started", "Claim Form Submitted", "Claim Response Viewed", "Plan-Finder Started", "Plan Renewed", "Message Viewed", "Message Sent", "App Crash", "Login", "Home Service", "Eligibility Viewed", "Bill Viewed", "Bill Paid", "Caremark Accessed", "OTC Benefits Viewed", "Account Creation Started", "Anonymous Visit", "Account Creation Completed"],
			# "insurance_provider": ["Aetna", "Blue Cross Blue Shield", "Cigna", "EmblemHealth", "UnitedHealthcare", "None", "Banner Health", "Avera Health", "Assurant Health", "Medicare", "Medicaid", "MetroHealth", "MetLife"]

		},
		"ints": {
			"search_results": 100,
			"age": (18,65),
			"lifetime_appointments": 50,
			"lifetime_cancellations": 10,
			"days_in_advance": 30,
			"average_rating": 5,
			"total_reviews": 500,
			"distance_miles": 10,
			"deductible": (0,5000),
			"monthly_cost": (0,5000)
		}
	},
	"guardian": {
		"write_key": "1cllWiQDgAcDQX8QCVzOoN93aXWaHXV9",
		"eventsWithProps": ["Advisor Viewed", "Advisor Meeting Scheduled", "Advisor Meeting Completed", "Advisor Message Opened", "Set Reminder", "Feature Usage", "View Calendar", "Support Request Started", "Search Started", "Search Result Clicked", "App Launched", "App Installed", "First App Launch", "Appointment Booked", "Appointment Rescheduled", "Appointment Cancelled", "Reviews Viewed", "Provider Viewed", "Review Submitted", "Review Started", "App Link Texted", "Plan Viewed", "Plan Selected", "Claim Form Started", "Claim Form Submitted", "Claim Response Viewed", "Plan-Finder Started", "Plan Renewed", "Message Viewed", "Message Sent", "App Crash", "Login", "Home Service", "Eligibility Viewed", "Bill Viewed", "Bill Paid", "OTC Benefits Viewed", "Account Creation Started", "Anonymous Visit", "Account Creation Completed", "401k Contribution Changed", "401k Balance Viewed", "401k Withdrawal Started","Provider Saved", "Provider Viewed", "Page Viewed"],
		"eventsNoProps": [],

		"strings": {
			"platform": ["ios", "android", "web", "IVR/phone"],
			"state": ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"],
			"messaging_channel": ["Email", "Message Center", "Push Notification", "Phone Call/IVR", "Livechat"],
			"user_type": ["Employer", "Member", "Provider", "Broker", "Member", "Member", "Member", "Member", "Member", "Member"],
			"care_type": ["Dentist", "Orthodontist", "Ophthalmologist", "Optometrist"],
			"support_type": ["Claim Support", "Tech Support", "Find a Practice"],
			"current_feature": ["Calendar", "Tracker", "Reminders", "Health Guides", "Live Help"],
			"renewal_date": ["2019-06-01", "2019-07-01", "2019-08-01"],
			"plan_type": ["PPO", "DHMO"],
			"plan_manager": ["Individual", "Employer-Sponsored"],
			"plan_name": ["Managed DentalGuard", "Managed DentalGuard Child Essentials", "Guardian Family Essentials", "Guardian Pediatric Essentials"],
			"active_products": ["Disability Income Insurance", "Annuities", "Investments", "Individual Dental", "Health Exchange Dental", "401k"],
			"current_product": ["Disability Income Insurance", "Annuities", "Investments", "Individual Dental", "Health Exchange Dental", "401k"],
			"most_recent_activity": ["Set Reminder", "Feature Usage", "View Calendar", "Support Request Started", "Search Started", "Search Result Clicked", "App Launched", "App Installed", "First App Launch", "Appointment Booked", "Appointment Rescheduled", "Appointment Cancelled", "Reviews Viewed", "Provider Viewed", "Review Submitted", "Review Started", "App Link Texted", "Plan Viewed", "Plan Selected", "Claim Form Started", "Claim Form Submitted", "Claim Response Viewed", "Plan-Finder Started", "Plan Renewed", "Message Viewed", "Message Sent", "App Crash", "Login", "Home Service", "Eligibility Viewed", "Bill Viewed", "Bill Paid", "OTC Benefits Viewed", "Account Creation Started", "Anonymous Visit", "Account Creation Completed"],
			"current_domain": ["GuardianOnline","NetxInvestor","GuardianAnytime"],
			# "insurance_provider": ["Aetna", "Blue Cross Blue Shield", "Cigna", "EmblemHealth", "UnitedHealthcare", "None", "Banner Health", "Avera Health", "Assurant Health", "Medicare", "Medicaid", "MetroHealth", "MetLife"]

		},
		"ints": {
			"search_results": 100,
			"age": (18,65),
			"lifetime_appointments": 50,
			"lifetime_cancellations": 10,
			"days_in_advance": 30,
			"average_rating": 5,
			"total_reviews": 500,
			"distance_miles": 10,
			"deductible": (0,5000),
			"broker_id": (1111,9999),
			"nearby_search_results": (5,50),
			"broker_clients": (10,500),
			"monthly_cost": (0,5000),
			"savings_goal_status_%": (0,100),
			"annual_maximum_%_remaining": (0,100)
		}
	},
	"ibm_cloud": {
		"write_key": "Xw07eALQqvBVjHaJemyZIyeePXwQHtqW",
		"eventsWithProps": ["Start Trial", "Marketing Page Viewed", "Trial Page Viewed", "Trial Requested", "Invite User", "View Dashboard", "Launch App", "Trial Expired", "Plans Viewed", "Plan Selected", "Billing Run", "Cancellation Initiated", "Cancellation Completed", "Support Request", "Request Quote", "Request Demo"],
		"eventsNoProps": [],

		"strings": {
			"current_feature": ["Dashboard", "Invite Users", "Audit Logs", "Technical Support", "Reporting UI", "Reporting API", "IAM & Permissions"],
			"current_product_category": ["Compute", "Containers", "Networking", "Storage", "AI", "Analytics", "Databases", "Developer Tools", "Integration", "Internet of Things", "Security and Identity", "Starter Kits", "Web and Mobile", "Web and Application"],
			"current_product": ["Liberty for Java", "SDK for Node.js", "ASP.NET Core", "Runtime for Swift", "XPages", "Go", "PHP", "Python", "Ruby", "Tomcat", "Container Registry", "Object Storage", "Watson Assistant", "AI OpenScale", "Compare Comply", "Discovery", "Knowledge Catalog", "Knowledge Studio", "Language Translator", "Machine Learning", "Natural Language Understanding", "Personality Insights", "Speech to Text", "Text to Speech", "Tone Analyzer", "Visual Recognition", "Watson Studio", "Analytics Engine", "IBM Cognos Dashboard Embedded", "SQL Query", "Streaming Analytics", "Cloudant", "Db2", "SQL Query"]
		},
		"ints": {
			"active_offering_count": (0,15)
		}
	},
	"spirit": {
		"write_key": "v7USqyjHoN4xqi00rO97oMQXWHBGPVIn",
		"eventsWithProps": ["App Launched", "Kiosk Login", "View Itinerary", "Search", "Search Results Viewed", "Flight Selected", "Check-In Started", "Check-In Completed", "Kiosk Session Aborted", "Kiosk Help Requested", "Checkout Started", "Checkout Completed", "$9 Fare Club Application Started", "$9 Fare Club Application Completed", "Newsletter Signup", "Free Spirit Account View", "Miles Checked", "Miles Redeemed", "Baggage Fee Paid", "Flight Cancelled", "Flight Boarded"],
		"eventsNoProps": [],

		"strings": {
			"$9 Fare Club Member": [True, False],
			"Spirit Airlines World Mastercard Member": [True, False],
			"flight_type": ["Round trip", "One way", "Multi-city"],
			"check-in method": ["Kiosk", "Electronic", "Manual"],
			"current_platform": ["Kiosk", "Web", "Mobile Web", "Native Mobile", "iOS", "Android"],
			"search_type": ["Flight", "Vacation", "Car", "Hotel", "Cruise"],
			"origin": ["BQN","CAK","AXM","AUA","AVL","ATL","ACY","AUS","BWI","BOG","BOS","IAG","SJD","CLO","CUN","FLL","PHX","MCO","OAK","GSO","LAX","DEN","DFW","LAS","PHL"],
			"destination": ["BQN","CAK","AXM","AUA","AVL","ATL","ACY","AUS","BWI","BOG","BOS","IAG","SJD","CLO","CUN","FLL","PHX","MCO","OAK","GSO","LAX","DEN","DFW","LAS","PHL"],
			"fare_class": ["Big Front Seat", "$9 Fare Club", "Standard"],
			"flight_timing": ["Early Morning", "Afternoon", "Midday", "Overnight", "Evening"],
			"services_purchased": ["Baggage", "Seat Assignments", "Big Front Seat"]

		},
		"ints": {
			"available_itineraries": 50,
			"miles": 20000,
			"adults": 4,
			"children": 4,
			"amount": 1000,
			"days_in_advance": 30,
			"stops": 2
		}
	},
	"hospitality": {
		"write_key": "bUPdxB7pZr7nnSDiDIcfaNynxUXmZN7b",
		"eventsWithProps": ["Reservation Started", "Reservation Confirmed", "Reservation Canceled", "Landing Page Loaded", "Rewards Login", "Rewards Signup Started", "Rewards Signup Completed", "Rewards Dashboard Viewed", "Points Redeemed", "Hotel Viewed", "Search Initiated", "Search Results Viewed", "Search Result Clicked", "Checkout Started", "Checkout Completed", "Check-In Started", "Check-In Completed", "Review Started", "Review Submitted", "Payment Complete", "App Launched", "Call Logged"],
		"eventsNoProps": [],

		"strings": {
			"current_platform":["iOS","Android","Web","Check-In Kiosk"],
			"booking_source": ["First-Party", "hotels.com", "kayak.com", "expedia.com"],
			"category_l1": ["Luxury", "Premium", "Select", "Longer Stays"],
			"flexible_dates": [True, False],
			"wyndham_rewards_member?": [True,False],
			"current_channel": ["Call Center", "Web"],
			"category": ["Classic Luxury", "Distinctive Luxury", "Classic Premium", "Distinctive Premium", "Classic Select", "Distinctive Select", "Classic Select Longer Stays", "Distinctive Select Longer Stays"],
			# "current_brand": ["The Ritz-Carlton", "St. Regis", "JW Marriott", "The Luxury Collection", "W Hotels", "Edition", "Marriott", "Sheraton", "Marriott Vacation Club", "Delta Hotels", "Le Meridien", "Westin", "Autograph Collection", "Design Hotels", "Renaissance Hotels", "Tribute Portfolio", "Courtyard by Marriott", "Four Points", "Springhill Suites", "Protea Hotels", "Fairfield by Marriott", "AC Hotels", "Aloft", "Moxy", "Marriott Executive Apartments", "Residence Inn", "Towneplace Suites", "Element"],
			"room_type": ["Standard King", "City View King", "Oceanfront King", "Standard Double", "City View Double", "Oceanfront Double", "Oceanfront Suite", "Bungalow Loft Suite", "Penthouse"],
			"package": ["Hotel Only", "Hotel+Flight", "Hotel+Experience", "Hotel+Flight+Experience"],
			"location": ["Dove Mountain","Paradise Valley ","Half Moon Bay","Laguna Niguel","Lake Tahoe","Los Angeles","Marina del Rey","Rancho Mirage","San Francisco","Santa Barbara","Bachelor Gulch","Denver","Vail","Amelia Island","Bal Harbour, Miami","Coconut Grove, Miami","Fort Lauderdale","Key Biscayne, Miami","Naples","Naples Golf","Orlando","Sarasota","South Beach","Atlanta","Reynolds, Lake Oconee","Kapalua","Waikiki Beach ","Chicago","New Orleans","Boston","St. Louis","New York, Central Park","New York, Westchester","Charlotte","Cleveland","Ontario","Toronto","Pennsylvania","Philadelphia","Dallas","Georgetown, Washington, D.C.","Pentagon City","Tysons Corner","Washington, D.C.", "Vienna","Berlin","Barcelona","Tenerife","Geneva","Istanbul","Moscow","Aruba","San Juan","Montreal"]
		},
		"ints": {
			"price": (200,5000),
			"days_in_advance": (0,30),
			"review_score": (2,5),
			"resort_credit": (0,100),
			"lifetime_value": (0,5000),
			"points": (0,10000)
		}
	},
	"tripadvisor": {
		"write_key": "TK2pc58JqkRPzgLSdRr32ifsCx5OtIOQ",
		"eventsWithProps": ["View Partner Content", "View VRBO Destiantion", "View VRBO Listing", "VRBO Booking Started", "VRBO Booking Completed", "View Travel Feed", "Reservation Started", "Reservation Confirmed", "Reservation Canceled", "Landing Page Loaded", "Rewards Login", "Rewards Signup Started", "Rewards Signup Completed", "Rewards Dashboard Viewed", "Points Redeemed", "Hotel Viewed", "Search Initiated", "Search Results Viewed", "Search Result Clicked", "Checkout Started", "Checkout Completed", "Check-In Started", "Check-In Completed", "Review Started", "Review Submitted", "Payment Complete", "App Launched", "Feature Usage", "Item Viewed", "Item Saved", "Item Shared", "Item Viewed", "Item Saved", "Item Shared", "Item Viewed", "Item Saved", "Item Shared", "Item Viewed", "Item Saved", "Item Shared", "Item Viewed", "Item Saved", "Item Shared", "Item Viewed", "Item Saved", "Item Shared", "Item Viewed", "Item Saved", "Item Shared", "Support Request Started", "Support Request Completed"],
		"eventsNoProps": [],

		"strings": {
			"current_platform":["iOS","Android","Web","Mobile Web","Apple TV"],
			"current_domain": ["AirfareWatchdog", "BookingBuddy","CityMaps","CruiseCritic", "FamilyVacationCritic", "FlipKey", "GateGuru", "HolidayLettings.co.uk","HolidayWatchdog", "Housetrip", "IndependentTraveler","JetSetter", "TheFork", "LaFourchette", "ElTenedor", "Iens.nl", "BestTables", "Dimmi", "Niumba", "OneTime", "Viator","Oyster","SeatGuru", "SmarterTravel", "Tingo","TravelPod","TripBod","VacationHomeRentals","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor","TripAdvisor"],
			"content_creator": ["Thrillist", "Insider", "Travel + Leisure", "Business Insider", "The Points Guy", "PopSugar"],
			"item_type": ["VRBO", "Hotel", "Restaurant", "Attraction", "City Guide", "Partner Content", "Forum Post"],
			"category": ["Classic Luxury", "Distinctive Luxury", "Classic Premium", "Distinctive Premium", "Classic Select", "Distinctive Select", "Classic Select Longer Stays", "Distinctive Select Longer Stays"],
			"current_brand": ["The Ritz-Carlton", "St. Regis", "JW Marriott", "The Luxury Collection", "W Hotels", "Edition", "Marriott", "Sheraton", "Marriott Vacation Club", "Delta Hotels", "Le Meridien", "Westin", "Autograph Collection", "Design Hotels", "Renaissance Hotels", "Tribute Portfolio", "Courtyard by Marriott", "Four Points", "Springhill Suites", "Protea Hotels", "Fairfield by Marriott", "AC Hotels", "Aloft", "Moxy", "Marriott Executive Apartments", "Residence Inn", "Towneplace Suites", "Element"],
			"room_type": ["Standard King", "City View King", "Oceanfront King", "Standard Double", "City View Double", "Oceanfront Double", "Oceanfront Suite", "Bungalow Loft Suite", "Penthouse"],
			"package": ["Hotel Only", "Hotel+Flight", "Hotel+Experience", "Hotel+Flight+Experience"],
			"location": ["Dove Mountain","Paradise Valley ","Half Moon Bay","Laguna Niguel","Lake Tahoe","Los Angeles","Marina del Rey","Rancho Mirage","San Francisco","Santa Barbara","Bachelor Gulch","Denver","Vail","Amelia Island","Bal Harbour, Miami","Coconut Grove, Miami","Fort Lauderdale","Key Biscayne, Miami","Naples","Naples Golf","Orlando","Sarasota","South Beach","Atlanta","Reynolds, Lake Oconee","Kapalua","Waikiki Beach ","Chicago","New Orleans","Boston","St. Louis","New York, Central Park","New York, Westchester","Charlotte","Cleveland","Ontario","Toronto","Pennsylvania","Philadelphia","Dallas","Georgetown, Washington, D.C.","Pentagon City","Tysons Corner","Washington, D.C.", "Vienna","Berlin","Barcelona","Tenerife","Geneva","Istanbul","Moscow","Aruba","San Juan","Montreal"]
		},
		"ints": {
			"price": (200,5000),
			"days_in_advance": (0,30),
			"review_score": (2,5),
			"resort_credit": (0,100),
			"points": (0,10000),
			"support_NPS": (0,10)
		}
	},
	"carrefour": {
		"write_key": "UZkyREjOpT7a5LqJIbjVbNsLRSXRD88K",
		"eventsWithProps": ["Digital Checkout", "POS Checkout", "1-Hour Delivery Started", "Feedback Submitted", "In-Store Visit", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "In-Store", "Mobile"],
			"category": ["Misc Electronics", "Grocery", "Fresh Food", "Health & Fitness", "Babies", "Smartphones", "Laptops/IT/Gaming"],
			"MyCLUB_member": [True, False]
		},
		"ints": {
			"price": 300,
			"quantity": 25,
			"store_id": (1111,9999),
			"region_id": (1111,9999)
		}
	},
	"agropur": {
		"write_key": "YW5zhfzjODgPX0SFalOeSzTU1XyDwXzw",
		"eventsWithProps": ["Page Viewed", "Products Searched", "Category Viewed", "Products Filtered", "Promotion Viewed", "Ad Impression", "Email Clickthrough", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Saved", "Product Removed", "Support Contact Started","Support Contact Completed","Message Viewed","Content Viewed","Bulk Sales Uploaded","Catalog Viewed","Catalog Ordered","Feedback Submitted","Newsletter Signup"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "Mobile Web", "Social", "Back-End"],
			"cheese_type": ["Blue", "Brie", "Camembert", "Cheddar", "Cream", "Emmental", "Feta", "Parmigiano Reggiano", "Swiss"],
			"inquiry_type": ["Consumer","Business Customer","Supplier","International Export"],
			"user_type": ["Consumer","Business Customer","Supplier","International Export"],
			"content_type": ["Preparation Guide", "Product Detail", "Recipe", "News"],
			"ad_utm_campaign": ["Facebook-Spring2019", "Facebook-LactoseFree", "Facebook"],
			"ad_utm_source": ["Facebook", "Adwords", "Organic"],
			"user_demographics": ["Homemaker", "Lactose-Free","Single","City-Dweller","Suburb-Dweller"],
			"user_locale": ["Toronto","Montreal","Calgary","Ottawa","Edmonton","Mississauga","Winnipeg","Vancouver","Brampton","Hamilton","Quebec City","Surrey","Laval","Halifax","Markham"],
			"communication_channel": ["Email","Social","Livechat"],
			"current_domain": ["Agropur.com","Natrel.ca","AgropurSolutions.ca","CheeseBar.ca","ObviouslyGoodMilk.ca","IslandFarms.com","QueBon.ca","CentralDairies.com","NorthumberlandDairy.ca","Sealtest.ca","FarmersDairy.ca","Iogo.ca","OlympicDairy","biProCA.com","Scotsburn","Dairy Town"],
			"current_brand": ["OKA","Le Rustique","Champfleury","Agropur Grand Cheddar","L'Extra", "Chevre des Alpes","Jarlsberg","Cambozola","Saint Agur","Saint-Paulin"],
			"recipe_name":["5-year-old Agropur Grand Cheddar with quick pickles", "Agropur Grand Cheddar with smoky spice","Agropur Grand Cheddar with sweet spice","Asparagus-Prosciutto Rolls with OKA Cheese","Baked pear with OKA cheese","Blue beef carpaccio","Crispy Harvest Melts","Fried Mac & Cheese balls with Agropur Grand Cheddar and Jarlsberg","Brie Agropur Import Collection with gingerbread and caramel"],
			"recipe_type": ["Breakfast","Lunch","Dinner","Dessert"],
			"content_title": ["Where to find Natrel Ice Cream Mochis?","Mochi: A treat at your fingertips!","Natrel invites you to its Bistro","Best New Product Award : Natrel Whipped Dip & Spread","A new lactose free ice cream flavour, with a Canadian touch!","Natrel chocolate milk now organic","Taste the possibilities with Natrel"],
			"product_category": ["Milks","Creams","Flavoured Milks","Cheeses","Yoghurts","Lactose-Free","Ice Creams","Sour Creams","Cottage Cheeses","Cream Cheeses"],
			"product_name":["Eggnog","Chocolate Milk","Buttermilk","1% Partly Skimmed Milk","Homogenized Milk","2% Partly Skimmed Milk","Skim Milk","Island Farms by Natrel 33% Whipping Cream", "Island Farms by Natrel 18% Table Cream", "Island Farms by Natrel 10% Half & Half Cream","1% Cottage Cheese"],
			"campaign_variant": ["Updated Images", "Larger CTA", "Control Group"],
			"consent_status": ["opt-out-marketing", "opt-out-emails", "opt-out-push", "opt-out-all", "subscribed"],
			"consent_email": [True, False],
			"consent_push": [True, False],
			"consent_mktg": [True, False],
			"consent_transactional": [True, False],
			"consent_productupdates": [True, False]
		},
		"ints": {
			"campaign_id": (111,999),
			"email_id": (111,999),
			"quantity": 25,
			"account_id": (1111,9999),
			"region_id": (1111,9999)
		}
	},
	"pepsico": {
		"write_key": "NENlMui3I560s9ISDtTGvIBAsXiPBdFU",
		"eventsWithProps": ["Page Viewed", "Products Searched", "Category Viewed", "Products Filtered", "Promotion Viewed", "Ad Impression", "Email Clickthrough", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Saved", "Product Removed", "Support Contact Started","Support Contact Completed","Message Viewed","Content Viewed","Catalog Viewed","Catalog Ordered","Feedback Submitted","Newsletter Signup", "Recipe Viewed", "Recipe Saved", "Recipe Shared", "Store Finder Launched", "Nutrition Facts Viewed","Nutrition Facts Viewed","Nutrition Facts Viewed","Nutrition Facts Viewed","Nutrition Facts Viewed","Social Clickthrough","Distributor Clickthrough", "Coupon Viewed", "Content Viewed", "Coupon Redeemed"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "Mobile Web", "Social", "Back-End"],
			"inquiry_type": ["Consumer","Business Customer","Supplier","International Export"],
			"user_type": ["Consumer","Business Customer","Supplier","International Export"],
			"ad_utm_campaign": ["Facebook-Spring2019", "Facebook-Tostitos", "Facebook"],
			"ad_utm_source": ["Facebook", "Adwords", "Organic"],
			"user_demographics": ["Homemaker", "Single","City-Dweller","Suburb-Dweller", "Active", "Classic"],
			"user_locale": ["New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Philadelphia, PA", "Phoenix, AZ", "San Diego, CA", "Dallas, TX"],
			"communication_channel": ["Email","Social","Livechat"],
			"current_domain": ["Sabra.com", "QuakerOats.com", "Izze.com", "AMPEnergy.com", "OneCoconutWater.com", "SodaStream.com","NakedJuice.com","PureLeaf.com","FritoLay.com", "Pepsi.com","OffTheEatenPathSnacks.com"],
			"current_brand": ["Sabra", "Quaker Oats", "IZZE", "AMP ENERGY", "O.N.E. Coconut Water", "SodaStream","Naked Juice","Pure Leaf","Frito Lay", "Pepsi","Off the Eaten Path", "Tropicana","Bare","Imagine", "Sun Chips", "Propel", "Maker", "Aquafina","KeVita","LifeWTR"],
			"active_subscriptions": ["Sabra", "Quaker Oats", "Izze", "AMP ENERGY", "O.N.E. Coconut Water", "SodaStream","Naked Juice","Pure Leaf","Frito Lay", "Pepsi","Off the Eaten Path", "Tropicana","Bare","Imagine", "Sun Chips", "Propel", "Maker", "Aquafina","KeVita","LifeWTR"],
			"content_title": ["Sabra's Pearl Center of Excellence", "Food Safety", "FAQ", "Our Story", ],
			"product_category": ["Savory Snack", "Beverage", "Health Food", "Zero-Calorie Beverage", "Dessert", "Grocery/Preparation Required", "Ready-to-Eat"],
			"product_name":["Caramelized Onion Hummus", "Classic Hummus", "Classic Hummus Singles", "Classic Hummus with Pita Chips", "Classic Hummus with Pretzels", "Greek Inspired Hummus", "Jalapeno Hummus","Lemon Twist Hummus"," Olive Tapenade Hummus", "Organic Simply Roasted Garlic Hummus", "Organic Simply Roasted Pine Nut Hummus", "Organic Simply Traditional Hummus"],
			"social_channel": ["Instagram", "Facebook", "Twitter", "Pinterest", "YouTube"],
			"product_tags": ["Health Food", "Zero-Calorie", "On-The-Go", "Home Prep", "Active", "Caffeinated", "Premium", "Limited Edition", "Parties"],
			"distributor_clicked": ["Amazon", "Local Store"],
			"campaign_variant": ["Updated Images", "Larger CTA", "Control Group"],
			"online_purchase_enabled": [True, False],
			"consent_status": ["opt-out-marketing", "opt-out-emails", "opt-out-push", "opt-out-all", "subscribed"],
			"consent_email": [True, False],
			"consent_push": [True, False],
			"consent_mktg": [True, False],
			"consent_transactional": [True, False],
			"consent_productupdates": [True, False]
		},
		"ints": {
			"campaign_id": (111,999),
			"nearby_stores": (1,50),
			"email_id": (111,999),
			"quantity": 25,
			"account_id": (1111,9999),
			"region_id": (1111,9999)
		}
	},
	"giant_eagle": {
		"write_key": "UZkyREjOpT7a5LqJIbjVbNsLRSXRD88K",
		"eventsWithProps": ["Digital Checkout", "POS Checkout", "1-Hour Delivery Started", "Feedback Submitted", "In-Store Visit", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "View eCoupon", "Clip eCoupon", "Screen Viewed", "Feature Used", "Circular Delivered"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "In-Store", "Mobile"],
			"category": ["On Sale", "Grocery", "Produce", "Meat & Seafood", "Deli & Cheese", "Bakery & Bread", "Prepared Foods", "Dairy & Eggs", "Frozen", "Beverages", "Household Essentials", "Health & Beauty", "Floral", "Pharmacy"],
			"current_feature": ["eCoupon", "Free Pickup", "Delivery", "Order Online", "Weekly Ad", "Shopping History", "eAdvantage Offer of the Week", "Catering", "Cake Ordering"],
			"current_brand": ["Giant Eagle", "Giant Eagle", "Giant Eagle", "Giant Eagle", "Giant Eagle", "Giant Eagle", "Market District", "GetGo Cafe + Market"],
			"advantageClub_member": [True, False],
			"fuelperks_member": [True,False],
			"circular_pause_experiment": [True,False],
		},
		"ints": {
			"price": 300,
			"quantity": 25,
			"fuelperks_points": 10000,
			"store_id": (1111,9999),
			"region_id": (1111,9999)
		}
	},	
	"underarmour": {
		"write_key": "8vABethNNe8D69MaxikXB0rlIQCKyAYy", #Final Demo
		# "write_key": "UFQwYG7POPFE3Xfab4CXkHjCcUDhuGpn", #POC Source
		# "write_key": "6RU8FkqKYTNxZsjN2LedDP99AnktZEto", #Demo Source
		"eventsWithProps": ["New User Registered", "Password Changed", "Email Verified", "Cancellation Page Viewed", "Trial Started", "Trial Expired", "A/B Experiment Started", "In-Store Visit", "Page Viewed", "Products Searched", "Product List Viewed", "Product List Filtered", "Promotion Viewed", "Promotion Clicked", "Product Clicked", "Product Viewed", "Product Added", "Product Removed", "Cart Viewed", "Checkout Started", "Checkout Step Viewed", "Checkout Step Completed", "Payment Info Entered", "Order Completed", "Order Updated", "Order Refunded", "Order Cancelled", "Workout Logged", "Route Viewed", "Connect Shoes", "View Run Data", "Training Plan Viewed", "Training Plan Subscribed", "MVP Info Viewed", "MVP Subscription Flow Started", "MVP Subscription Confirmed", "MVP Cancellation Page Viewed", "MVP Canceled", "Premium Info Viewed", "Premium Subscription Started", "Premium Cancellation Page Viewed", "Premium Canceled", "Add to Cart", "App Launch", "Audience Entered", "Audience Exited", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "In-Store", "Mobile Web", "Native App", "Apple Watch"],
			"race_type": ["Half Marathon","5K","Marathon","10K","4M","1M"],
			"current_feature": ["Map Route", "Goal Tracking", "Splits", "Heart Rate Analysis", "Route Genius", "Power Analysis", "Cadence Analysis", "Training Plans", "Mobile Coaching", "Live Tracking", "Advanced Leaderboards", "Custom Splits", "Advanced Maps", "Export Workout", "Interval Training"],
			"premium_feature?": [True,False],
			"premium_status": ["Canceled", "Free", "Active"],
			"mvp_status": ["Canceled", "Free", "Paid"],
			"workout_type": ["Hike", "Run", "Walk", "Strength Training", "Bike"],
			"shoes_connected?": [True, False],
			"shoe_model": ["HOVR Phantom", "HOVR Infinite", "HOVR Sonic 2", "HOVR Guardian", "ICON Curry 6", "Curry 6", "HOVR SLK EVO Print Midsole", "HOVR SLK", "HOVR SLK EVO", "HOVR Lace Up Mid PRM", "HOVR Phantom Connected", "HOVR Havoc", "HOVR Havoc Mid", "HOVR Havoc Low", "HOVR Phantom Reflective"],
			"item_subcategory": ["Basketball", "Boots", "Cleats & Spikes", "Custom", "Golf", "Hiking & Trail", "Running", "Slides & Sandals", "Sportstyle", "Training", "Graphic Ts", "Hoodies & Sweatshirts", "Jackets & Vests", "Long Sleeves", "Polo Shirts", "Short Sleeves", "Backpacks & Bags"],
			"connected_device": ["Apple Watch", "Garmin", "Fitbit", "Jawbone"],
			"[Amplitude] Cohorts": ["Churn Risks", "Slow Onboarding Funnel", "Upsell Cluster A", "Upsell Cluster B", "New Users with Garmin", "Connected Newest Garmin Device", "UA HOVR Connected"],
			"consent_status": ["opt-out-marketing", "opt-out-emails", "opt-out-push", "opt-out-all", "subscribed"],
			"consent_email": [True, False],
			"consent_push": [True, False],
			"consent_mktg": [True, False],
			"consent_transactional": [True, False],
			"consent_productupdates": [True, False],
			"mvp_payment_type": ["monthly","yearly","free"],
			"audience": ["Churn Risks", "Premium Upsell Likely", "New Users with Garmin", "Connected Newest Garmin Device", "UA HOVR Connected"],
			"current_app": ["Under Armour Mobile", "UA Play", "UnderArmour.com", "Map My Run", "Map My Walk", "Map My Ride", "Record by Under Armour", "Map My Fitness", "Map My Hike", "UA Shop"],
		},
		"ints": {
			"run_distance": 20.0,
			"run_distance_mi": 20.0,
			"run_duration": 60.0,
			"price": 300,
			"quantity": 25,
			"store_id": (1111,9999),
			"region_id": (1111,9999)
		}
	},
	"equinox": {
		"write_key": "8NQd1D3WifE9EAaLCniyLVNm1C6zxlp4",
		"eventsWithProps": ["Set Appointment", "Class List Browsed", "Clubs Searched", "Class Waitlist Viewed", "Class Waitlist Joined", "Class Search Filtered", "Class Added to Favorites", 'Trial Pass Requested', 'Member Login', 'Support Ticket Opened', 'Support Ticket Completed', 'Shop Purchase Completed', 'Membership Advisor Meeting Completed', 'Plan Purchased', 'Payment Completed', 'Live Chat Started', 'Tour Completed', 'Live Chat Completed', 'Day Pass Generated', 'Day Pass Used', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Class Check-In', 'Activity Completed', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Club Check-In', 'Class Check-In'],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "In-Club", "Mobile Web", "Native App", "Apple Watch", "Phone/IVR"],
			"purchase_channel": ["In-Person", "Online", "Phone Call", "Mobile"],
			"purchase_type": ["Self-Serve", "Membership Consultant"],
			"class_timerange": ["Early Morning", "Mid-Morning", "Late Morning", "Noon", "Early Afternoon", "Afternoon", "Late Afternoon", "Evening", "Late Night"],
			"member_since": ["2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012"],
			"class_timeslot": ["6:30-7:15AM", "6:45-7:40AM", "7:15-8:00AM", "8:15-9:00AM", "10:00-11:00AM","12:00-12:45PM"],
			"class_instructor": ["James Ervin", "Lindsay Carson", "Danny Byrd", "Alicia Archer", "Jackie Ochoa-Mendez", "Grace Twesigye", "Miriam Shestack"],
			"membership_advisor": ["James Ervin", "Lindsay Carson", "Danny Byrd", "Alicia Archer", "Jackie Ochoa-Mendez", "Grace Twesigye", "Miriam Shestack"],
			"current_service": ["Standard Workout", "EquiFit", "Personal Training", "Spa Treatment", "Workout Class", "Hotel Stay", "Pilates Class"],
			"plan_type": ["All Access", "One Club", "Free Trial"],
			"class_name": ["Pure Strength", "Precision Run", "Anthem", "Power Yoga", "True Athlete: Strong", "Deep Extreme", "Metcon3", "Tai Sculpt", "EQX Barre Burn", "Vinyasa Yoga", "Cardio Dance Club", "Stacked!", "Tabata"],
			"class_category": ["Active Regeneration", 'Athletic Training', 'Barre', 'Boxing + Material Arts', 'Cycling', 'Dance', 'Long + Lean', 'Pilates', 'Pool', 'Running', 'Yoga'],
			"member_status": ["Free Trial", "Member Guest", "Lead", "Lapsed"],
			"workout_type": ["Spinning", "Yoga", "Run", "Strength"],
			"connected_device": ["Apple Watch", "Garmin", "Fitbit", "Jawbone"],
			"consent_status": ["opt-out-marketing", "opt-out-all", "subscribed"],
			"current_region": ["Boston", "Canada", "Chicago", "Connecticut", "Florida", "London", "Michigan", "New Jersey", "New York", "Northern California", "Southern California", "Texas", "Washington DC"],
			"home_region": ["Boston", "Canada", "Chicago", "Connecticut", "Florida", "London", "Michigan", "New Jersey", "New York", "Northern California", "Southern California", "Texas", "Washington DC"],
			"current_club": ["Columbus Circle", "E Madison Avenue", "East 61st Street", "East 63rd Street", "East 74th Street", "East 85th Street", "East 92nd Street", "Sports Club New York", "West 76th Street", "West 92nd Street", "Bryant Park", "East 43rd Street", "East 44th Street", "East 53rd Street", "East 54th Street", "Park Avenue", "Rockefeller Center", "West 50th Street", "Bond St.", "Brookfield Place", "Flatiron", "Gramercy", "Greenwich Ave", "High Line", "Orchard St", "Printing House", "SoHo", "Tribeca", "Wall Street", "Brooklyn Heights", "DUMBO", "Williamsburg", "Great Neck", "Roslyn", "Woodbury", "Armonk", "Mamaroneck", "Scarsdale"],
			"home_club": ["Columbus Circle", "E Madison Avenue", "East 61st Street", "East 63rd Street", "East 74th Street", "East 85th Street", "East 92nd Street", "Sports Club New York", "West 76th Street", "West 92nd Street", "Bryant Park", "East 43rd Street", "East 44th Street", "East 53rd Street", "East 54th Street", "Park Avenue", "Rockefeller Center", "West 50th Street", "Bond St.", "Brookfield Place", "Flatiron", "Gramercy", "Greenwich Ave", "High Line", "Orchard St", "Printing House", "SoHo", "Tribeca", "Wall Street", "Brooklyn Heights", "DUMBO", "Williamsburg", "Great Neck", "Roslyn", "Woodbury", "Armonk", "Mamaroneck", "Scarsdale"],
			"membership_conversation_in_progress": [True,False],
			"former_cancellation?": [True,False],
			"former_cancellation_reason": ["Moving (Non-Equinox City)", "Moving (Equinox Available in City)", "Price", "Too Far", "Not Using Enough"]			
		},
		"ints": {
			"run_distance": 20,
			"run_duration": 60,
			"price": 300,
			"quantity": 25,
			"club_id": (1111,9999),
			"region_id": (1111,9999),
			"lifetime_PT_sessions": (0,100),
			"membership_advisor_id": (1111,9999)
		}
	},
	"glamsquad": {
		"write_key": "MFKZ5jQtiaFNrc96eCVQa0mvYUUQ1ajE",
		"eventsWithProps": ["Booking Request", "Product Added", "Product Viewed", "Checkout Started", "Order Completed", "Content Read", "Wedding Request Submitted"],
		"eventsNoProps": ["Account Login", "Account Created"],

		"strings": {
				"category": ["blowout", "makeup", "nail", "annual", "beauty product", "electronics", "wedding", "photo-shoot & events"],
				"variant": ["events", "wedding day makeup", "blowout", "updo", "nail art", "pedicure", "makeup"],
				"add-ons": ["eye patch", "spa", "pedi", "lashes"],
				"location": ["New York", "Southern California", "DC", "Boston"],
				"type": ["single", "package"],
				"product": ["gift card", "electonics", "service", "	 product"],
				"in_package": [ True, False ]
		},
		"ints": {
			"total": 300,
			"price": 100,
			"quantity": 5
		},
		"traits": {
		}
	},
	"tidal": {
		"write_key": "V95mNxWLrkzB60HWRBFQTGIBNYJonFDW", #ios
		# "write_key": "qiCqbTATYCCLwb1DC3ZcYjTtxQMqSNWj", #web
		# "write_key": "V95mNxWLrkzB60HWRBFQTGIBNYJonFDW", #android
		"eventsWithProps": ["Block Artist", "Block Song", "Trial Started", "Session Ended", "Video Played", "Playlist Imported", "App Install", "Signup Started", "Signup Completed", "Trial Started", "Trial Completed", "Billing Added", "Renewal", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "App Launched"],
		# "eventsWithProps": ["Trial Started", "Session Ended", "Signup Started", "Signup Completed", "Trial Started", "Trial Completed", "Billing Added", "Renewal", "songplayed", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "Song Played", "App Launched"], #web
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "Mobile Web", "Native iOS", "Native Android", "PS4", "XboxOne", "Nintendo Switch", "CarPlay"],
			"current_artist": ["Drake", "Ariana Grande", "Meek Mill", "Future", "21 Savage", "A Boogie Wit Da Hoodie", "Travis Scott", "Cardi B", "Lil Baby", "Ella Mai", "Solange", "T-Pain", "JuiceWRLD", "Kanye West", "Jay-Z", "Beyonce", "Gesaffelstein", "Dave", "Foals", "Dido", "Sigrid", "Fuse ODG", "BAMSAVAGE", "Giggs", "Lil Pump", "Offset"],
			"current_genre": ["Hip-Hop", "Electronic", "Classical", "Pop", "Pop Rock", "Indie"],
			# "tidal_exclusive?": [True, False],
			"hifi_audio?": [True, False],
			"current_playlist": ["Thoro Hip Hop", "Pop Life", "Real Love", "Dimelo Flow", "Indie Circus", "Hot Rocks", "Big Dance Energy", "Viral Hype", "Dale Reggaeton", "Rhythm & Groove", "Fresco", "Rap Bars & Melodies", "Pop Art", "Future Proof", "Weekend Waves", "Conversion Rave", "Rinsed", "Retroactive Classic Rock"],
			"features_used": ["Concert Livestream", "Exclusive Content", "HiFi Audio", "Playlist Share", "Playlist Import"],
			"features_used": ["Exclusive Content", "HiFi Audio", "Playlist Share", "Flow"],
			"account_status": ["Installed", "Trial", "Paid", "Trial Expired", "Canceled"],
			# "plan_type": ["Free", "Premium", "HiFi", "Family Premium", "Family HiFi", "Student Premium", "Student HiFi", "Military Premium", "Military HiFi", "Tidal X"],
			"plan_type": ["Free", "Premium", "Family Premium", "HiFi", "Student Premium"],
			"monthly_payment": [9.99, 19.99, 14.99, 29.99, 4.99, 9.99, 5.99, 11.99],
			"utm_source": ["Sprint"]
		},
		"traits": {},
		"ints": {
			"content_age_(days)": (0,300),
			"completion_percentage": (1,100),
			"trial_days_remaining": (0,30),
			"song_length": (60, 300)
		}
	},
	"navient": {
		"write_key": "0XtlULesfknbWHM4m5HSD1sDx0H2I1WR",
		"eventsWithProps": ["Signup Started", "Signup Completed", "Account Summary Viewed", "Payment Started", "Payment Completed", "Recent Payments Viewed", "Repayment Options Viewed", "Repayment Plan Selected", "Payment Pause Requested", "Loan Forgiveness Options Viewed", "Payment Scheduled", "Help Center Viewed", "Help Center Item Viewed", "Loan Refinance Viewed", "Loan Refinance Requested"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "Mobile Web", "iOS", "Android", "Windows Phone", "Phone/IVR"],
			"help_center_question": ["Can I pay more than my monthly payment amount?", "How do I pay with special instructions?", "How do I qualify for a repayment plan based on my income?", "How do I know whether to request a deferment or forbearance?", "As a military service member, what are my benefits and how do I request them?"],
			"help_center_topic": ["Payments", "Auto Pay", "Payment Options", "Technical Support"],
			"current_feature": ["Scheduled Payments", "Live Chat", "Repayment Planner", "Help Center"],
			"plan_type": ["Revised Pay-As-You-Earn", "Pay-As-You-Earn", "Income-Based Repayment", "Income-Contingent Repayment", "Income-Sensitive Repayment", "Direct Consolidation"],
			"loan_status": ["Active Payments", "Deferment", "Forbearance"]

		},
		"traits": {},
		"ints": {
			"loan_repayment_progress(%)": (30,100),
			"loan_total": (50000,100000),
			"loan_amount_remaining": (100,30000),
			"loan_count": (1,10)
		}
	},	
	"vimeo": {
		"write_key": "g9Ym0DRWYjy5M4zPBxUVXTRv2rWon4gH",
		"eventsWithProps": ["Signup Started", "Signup Completed", "Video Uploaded", "Plans Viewed", "Plan Selected", "Storage Limit Reached", "Teammate Added", "Link Shared", "Video Details Edited", "Video Published", "Video Deleted", "Stock Video Search", "Stock Video Viewed", "Stock Video Added to Cart", "Stock Video Purchase Started", "Stock Video Purchase Completed", "Stock Collection Browsed", "Support Chat Started", "Support Chat Completed", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Feature Used", "Analytics Report Viewed","Analytics Report Viewed","Analytics Report Viewed","Analytics Report Viewed","Analytics Report Shared"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "Mobile Web", "iOS", "Android", "Windows Phone", "Phone/IVR"],
			"current_plan": ["Free", "Plus", "Pro", "Business", "Premium"],
			"current_feature": ["Customized Player", "Private Links", "Playback Speed Control", "Liva Q&A", "Audience Chat", "Live Stream", "Advanced Analytics", "VimeoStock", "Basic Analytics"],
			"monthly_payment": [7,20,50,75],
			"monetized_videos": [True,False],
			"current_analytics_report": ["Basic Analytics", "Play Count", "Finish Count", "Comment Count", "Region Report", "Engagement Curve", "Realtime View", "Custom Reports"],
			"publish_method": ["Facebook","Linkedin","Twitter","YouTube"],
			"stock_collection": ["Vimeo Essentials", "Timelapse", "City of angels", "Solo traveler", "Technology", "Drone", "Animation", "Families", "Cities"," Space", "Business"]

		},
		"traits": {},
		"ints": {
			"video_version": (1,20),
			"product_NPS": (1,5),
			"stock_video_price": (64,200),
			"viewer_count": (1000,50000)
		}
	},	
	"carshare": {
		"write_key": "lm9pNUCZQvBbVRB84eR81iLQ4bP5rBiZ",
		"eventsWithProps": ["Signup Started", "Signup Completed", "App Launched", "Map View Opened", "Searched for Cars", "Park-and-Return", "Damage Report Started", "Damage Report Completed", "Car Locked", "Car Unlocked", "HomeZone Entered", "HomeZone Left", "Ride Started", "Ride Completed", "Friend Invited", "Coupon Unlocked", "Feedback Submitted", "AAA Assistance Called", "AAA Assistance Completed"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["Web", "Mobile Web", "iOS", "Android", "Windows Phone", "Phone/IVR"],
			"current_plan": ["Free", "Plus", "Pro", "Business", "Premium"],
			"currently_in_homezone?": [True,False],
			"car_make": ["Ford", "Volkswagen", "Toyota", "Hyundai", "Chevrolet", "Honda", "Kia", "Mazda", "Mercedes", "Audi", "Nissan", "Dodge"],
			"car_model": ["Mustang Bullitt", "Veloster", "XC40", "Range Rover", "Stinger", "8 Series", "ZR1", "A6", "Camry", "Altima", "Sentra", "Sonata", "Elantra", "Cruze"],
		},
		"traits": {},
		"ints": {
			"nearby_cars": (1,50),
			"nearest_car_distance": (0,10),
			"product_NPS": (1,5),
			"last_ride_distance": (1,100),
			"last_ride_duration": (1,100),
			"current_ride_distance": (1,100),
			"current_ride_duration": (1,100),
			"lifetime_rides": (0,50)
		}
	},	
	"apalon": {
		"write_key": "Qhm2bMQvMEdO8TfWW7PdFdpjjXfO6NIS",
		"eventsWithProps": ["App Launched", "Scan Started", "Signup Started", "Signup Completed", "Egg Hatched", "Weather Checked", "Forecast Viewed", "Horoscope Viewed", "Alarm Set", "Print Confirmed", "Feature Used", "Note Saved", "Note Deleted", "Note Started", "Reminder Set", "Paywall Hit", "Premium Details Viewed", "In-App Purchase Completed","Friend Invited","App Installed","Social Clickthrough", "App Feedback Submitted"],
		"eventsNoProps": [],

		"strings": {
			"current_platform": ["iOS", "Android"],
			"current_plan": ["Free", "Pro"],
			"current_app": ["Calculator Pro", 'Zodiask','Sleepzy','Coloring Book for Me','Notepad+','Alarm Clock for Me','Planes Live','Booster Kit', 'Live Wallpapers for Me', 'Wallpapers for Me', 'Speak and Translate', 'Fontmania','Kazki','Paloma','Jigsaw Puzzles for Me','Clipomatic','Snap & Translate','Productive','#VPN','Warmlight','Snapcalc','Weather Live','Eggzy','NOAA Weather Live'],
			"current_feature": ["Calculator","Weather Forecast","Horoscopes","Print/Scan","Notetaking"],
			"product_category": ["Calculator","Weather Forecast","Horoscopes","Print/Scan","Notetaking",'Productivity','Clocks','Wallpapers']
		},
		"traits": {},
		"ints": {
			"lifetime_value": (0,500),
			"product_NPS": (1,5)
			}
	}
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
	time.sleep(0.8)
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

	if industry == "ibm_cloud": #generate fake emails for ~20%
		if random.randint(0,100) < 20:
			fakeWord = "+"+random.choice(["1", "2", "3", "demo", "abcd", "qwerty", "again", "999", "9999", "newtrial", "trial"])+"@"
			userEmail = userEmail.replace("@", fakeWord)
			print "fake email generated: "+userEmail


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
	userLTV = random.randint(0, 3000)
	userCity = location['city']
	userState = location['state']

	userTraits = {
		"name": userName, "email": userEmail, "birthday": userDOB,
		"age": userAge, "phone": userPhone, "lifetime_value": userLTV ,
		"address": {"city": userCity, "state": userState}
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
	analytics.identify(random_user, userTraits, {"externalIds": [
		{"id": userPhone, "type": "phone", "collection": "users", "encoding": "none"},
		{"id": str(uuid.uuid4()), "type": "mobile_device_id", "collection": "users", "encoding": "none"},
		{"id": str(uuid.uuid4()), "type": "cookie_id", "collection": "users", "encoding": "none"},
		{"id": str(uuid.uuid4()), "type": "cross_domain_id", "collection": "users", "encoding": "none"},
		]}, anonymous_id=anonId)

	groupProps = False
	if sendGroupCall:
		userGroup = random.choice(companyData)
		groupProps = {'company_id': userGroup[0], 'company_name': userGroup[1], 'industry': userGroup[2], "client_ARR": random.randint(0,500000), "client_DAU": random.randint(0,50)}
		analytics.group(random_user, userGroup[0], groupProps)



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
		analytics.identify(random_user, eventProperties, anonymous_id=anonId)

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



		