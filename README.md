# Compozent_Major_project
Phishing URL detection website using Machine learning + AI chatbot for helping user's (ollama, gemma 2:2b)
## Below are the steps used to make this project
# Step 1: Data collection
first we need a data of latest phishing url for that we've used the opensource platform Phishtank: ,https://phishtank.org/developer_info.php. and dowloaded a big (~90k) data called Blacklist.csv	
then we downloaded legitamate url's from  Majestic Million then we named that file whitelist.csv

# Step 2 : feature extraction
now we will extract the url from blacklist and whitelist and process it using many function's such as :having_ip,having @,url lenght,url depth,redirect(//),prefix/suffix(-) etc 
	referancing from https://archive.ics.uci.edu/dataset/327/phishing+websites
 and the feature extracted and proceesed in Feature.ipynb 
 	after extracting the features we made two new dataset called legit_website.csv and Phishing_website.csv

# Step 3:ML Model Training
all below steps is done in data.ipynb:
FIrst we will comnbine the Legit_website.csv and phishing_website.csv and shuffle/mix them randomly
into one final Dataset called urldataset.csv
now we will use that dataset to train Ml model's using 3 Ml algorithm  : 1)Logestic Regression 2)Decision Tree 3) Random Forest 
		Now we will compare the accuracy of the # ML model and export the one with highest accuracy which in this case is DECISION TREE
	we used Pickle to export the ML model of decision tree xcalled : Cyber_model.pkl

 # Step 4 : Extracting Features from user Input
 we will not make an feature.py to extract features from user input url and convert them into a row type dataset that the Ml model will take it aas input and predict them
# Step 5: Making A phishing website and connecting ML model
now we first make app.py and import flask (for api calls),pickle(for loading ml model) and the feature from feature.py to extract the feature from user input
then we will use flask api to render the homepage in index.html and also make an /predict which will use features and give to ml model which will predict and give output['label'] as 0 or 1 now we will print it is phishing url if output is 0 or its safe if output is 1 


## *Caution: This detection is powered by an ML model and it is not 100% accurate. Please exercise caution and avoid entering sensitive information on websites flagged as phishing or even on seemingly safe websites.
