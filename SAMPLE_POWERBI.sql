
IF OBJECT_ID('gdp_raw_data') IS NOT NULL DROP TABLE Raw_Data_GDP
--CREATE THE TABLE

CREATE TABLE Raw_Data_GDP
(DEMO_IND NVARCHAR(200),
Indicator NVARCHAR(200),
[Location] NVARCHAR(200),
Country NVARCHAR(200),
[Time] NVARCHAR(200),
[Value] FLOAT,
[Flag Codes] NVARCHAR(200),
FLAGS NVARCHAR(200),	
)

--SELECT FROM CSV

BULK INSERT Raw_Data_GDP
FROM 'C:\Users\prdator\Downloads\gdp_raw_data.csv'
WITH (FORMAT='CSV');

--SELECT * FROM Raw_Data_GDP