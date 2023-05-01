There are 3 main files, described below - 

(in R you can use "R.matlab" to load the .mat files)

1. Network Data (Adjacency Matrices) : RFENetwork.mat 

	- This has network data for 70 villages, across 7 dimensions. 
	- The sequence of the dimensions within each village is as follows -
		- 1. (borrow) If you urgently needed Kerosene, rice, other groceries or money, who do you borrow them from?
		- 2. (lend) Who comes to your house if they needed Kerosene, rice, other groceries or money?
		- 3. (coming free time) Who comes to your house in their free time?
		- 4. (going free time) Whose house do you go to in your free time?
		- 5. (seek advise) Who do you ask for advise on matters  pertaining to health/finance/farming? 
		- 6. (give advise) Who asks you for advise on matters  pertaining to health/finance/farming?
		- 7. (relative) relatives in the village, besides people in the household?

2. Matching key from network data to covariates : vertex_key.mat

	- This is used to map vertex to hhid for each village

3. Covariate data : covariates_combined.csv

	- 1. villageid
	- 2. hh_id (same as hhid in key data)
	- 3. leader (If anyone in the HH is a current/former leader)
	- 4. caste_category (Caste)
	- 5. subcaste (Subcaste)
	- 6. hh_owned (house ownership status)
	- 7. roof_type (1 = Thatch, 2 = Tile, 3 = Stone, 4 = Sheet, 5 = Rcc, -333 = Others, -888 = Refuse to say, -999 = Do not know)
	- 8. num_rooms (Number of rooms in the house)
	- 9. electricity (1 = Yes, Regular own connection, 2 = Yes, under govt. scheme, 3 = No, -888 = Refuse to say, -999 = Do not know)
	- 10. Occupation type