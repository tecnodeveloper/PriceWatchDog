# Price WatchDog: Autonomous Multi-Platform E-Commerence Agent
  (Artifical Intelligence / Web Programming / Web Automation)
## Project IDEA
- First User gave our agent single product name, single website link and minimum Price he wanna set for trigger. Then our Chatbot check the provide URL website is live not 404. Then we use library called playwright to extract the semantics of webpage while ignoring sidebars and advertisement information. Then Chatbot checks that item is not out of stocks and item has not multiple variants. if item has multiple variants then asks the user which variant he want to select for price watching and if the product is out of stock then Show message to user that product is out of stocks. Then we extract price, currency and product name, Extracted messy html extracted converted into markdown by using tool called turnDown. if the price drops at the user level price then we give him notification + Email. Else we do scrapping after every 15min and store the price information in database and return the file in the form of JSON.

## Functional Requirements
  **FR1: URL Processing & Validation**
  **FR2: Intelligent Content Extraction** 
  **FR3: Variant Detection** 
  **FR4: Autonomous Comparison Logic**
  **FR5: Availability Monitoring**
  **FR6: Notification Trigger**
  **FR7: History Management**
