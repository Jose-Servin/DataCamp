-- Import Master Data file to Master_Data table
CREATE TABLE master_data (
	Customer_ID serial PRIMARY KEY,
	Year_Birth int,
	Education varchar(50),
	Marial_Status varchar(50),
	Income int,
	KidHome int,
	TeenHome int, 
	Dt_Customer timestamp,
	Recency int,
	MntWines int, 
	MntFruits int, 
	MntMeatProducts int,
	MntFishProducts int, 
	MntSweetProducts int, 
	MntGoldProds int,
	NumDealsPurchases int,
	NumWebPuchases int,
	NumCatalogPurchases int, 
	NumStorePurchases int,
	NumWebVisitsMonth int,
	AcceptedCmp3 int,
	AcceptedCmp4 int,
	AcceptedCmp5 int,
	AcceptedCmp1 int, 
	AcceptedCmp2 int, 
	Complain int,
	Z_CostContact int,
	Z_Revenue int,
	Response int
);

-- DROP TABLE master_data; (used to fix mistakes made when creating master data table)

COPY master_data
FROM '/Users/joseservin/DataCamp/Projects/Customer_Personality_Analysis/marketing_campaign.csv'
WITH (FORMAT CSV, HEADER, DELIMITER ';');

SELECT * FROM master_data;