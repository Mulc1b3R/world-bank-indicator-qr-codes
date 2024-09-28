

# World Bank Indicator QR Codes

QR codes for all 1488 world bank indicators returning indicator code (id) and description.

----------------------------------------------------------------------------------------------------------------------------------------

Data Mining, Cleaning, and QR Code Generation Process

This repository contains a process for extracting World Bank indicators from World Bank Data Portal, 
cleaning the data, transforming it into different formats, converting it, and generating QR codes based on the indicator information.
-----------------------------------------------------------------------------------------------------------------------------------------

#Process Overview

    Data Mining (Extraction):
	
        Extracted data from World Bank Data Portal by parsing <a href> tags.
		URL: https://data.worldbank.org/indicator?tab=all
        Retrieved the indicator "id" and description.
		'wb-indicators.txt'
        Comma-separated the indicator and description to create a CSV file.
        
    Data Cleaning (Scrubbing):
	
        Added .indicator and .description as columns to the CSV file.
		'wb-indicators.csv'

    Data Transformation:
	
        Converted the CSV file to JSON format to represent key-value pairs.
		'wb-indicators.json'

    Data Conversion and QR Code Generation:
	
        Generated QR codes using the JSON data containing the indicator and description.
		'qr.py'
        The QR code format allows easy reconversion back to JSON format.

    Data Source Clarification:
	
        Opted for direct extraction from the page rather than the World Bank API 
		(https://api.worldbank.org/v2/indicator/?format=json), as the API would have resulted in different formats for the indicators.
        Focused on 1488 indicators in a consistent format (AG.CON.FERT.PT.ZS) for clarity and ease of processing.

    Naming convention:

        The format of Wold Bank indicators uses a '.' as a seperator ,eg 'AG.CON.FERT.PT.ZS' but filenames are confused by the use of'.' 
	so the naming process transforms '.' to '-' . 
        AG.CON.FERT.PT.ZS (wb indicator) thus becomes AG_CON_FERT_PT_ZS.png when converted to a qr code.
	(See code for'qr.py').

    Returned data:

       Reading or scanning an indicator qr code returns data in the followning format.
       Indicator = AG.CON.FERT.PT.ZS  Qr code = AG_CON_FERT_PT_ZS.png  Returned data = AG.CON.FERT.PT.ZS : Fertilizer consumption (% of fertilizer production)
		
    Data Reader:
        Use the drag and drop qr code reader provided.
        All generic QR code scanners and readers. ie https://qrscanner.net/
        	
---------------------------------------------------------------------------------------------------------------------------------------------------------	



#Additional Notes:

    
    pip install -r requirements.txt
	
    The 'wb-indicators-list.txt' can be utilized for programmatic tasks.

    The process ensures a structured approach to data handling, transformation, and visualization through QR codes.
    The QR codes enable quick access to indicator information and can be reconverted back to JSON if required.
	
#Credits:
     
	The Data mining and qr code creation was performed by 
    Psico Communications and Blockchain Development.

    England , Yorkshire . (28/09/2024).	

