This is a page-object-model framework
Please refer to Project_Structure.png in root folder (/Gemini) for project directory structure

There are three tests
1. Launch HomePage (https://exchange.sandbox.gemini.com/)
2. Launch HomePage --> click create new account --> click create business  acc --> navigate to register Institution page (https://exchange.sandbox.gemini.com/register/institution)
3. Launch Institution Registration --> enter Business Name --> click Continue to Fail Test (If we see an error, Pass the Test Case)

How to run project :

Prerequisites: Unix like machine (Mac or Linux OK)
Chrome (Preferably version >= 95)

What to expect :

1. Project will run the automated tests
2. A HTML report will be generated
3. Generated HTML report will automatically open

Navigate to project directory :

1. cd Gemini
2. run command './execute.sh' without apostrophe 
