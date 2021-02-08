# Informal_Response_1_with_2_features

## Model using bedrooms and square footage to predict price

Once again the 3 bedroom house hudgins offers the best deal overall. However newptcomfort and mobjack seem like much better deals now than before now that we have factored square footage into the model. This tells us that the omittance of essential variables can greatly skew our model predictions.

| Number of Bedrooms with sq. footage       | Actual House Price  |	Predicted House Price |	Savings/(Overpayment) |
| -------------------                       | --------------------| ----------------------| ----------------------|
|2_Bedroom(moon) 1479 sqft                  |250000	              |170406	                |($79,594.00)           |
|<mark>3_Bedroom(hudgins) 1238 sqft </mark>	|<mark>97000 </mark>  |<mark>154831 </mark>   |<mark>	$57,831.00 </mark> |
|3_Bedroom(newptcomfort) 2840 sqft          |229000               |	282819                |	$53,819.00             | 
|4_Bedroom(church) 3680 sqft	              |399000               |	353608	              |($45,392.00)           |
|4_Bedroom(mobjack) 3524 sq ft              |	289000	            |341144	                |$51,144.00             |
|5_Bedroom(mathews) 3051 sqft               |	347500              |	307035	              |($40,465.00             | 



## Model using total number of rooms and square footage to predict price

| Number of Rooms with sq. footage       | Actual House Price  |	Predicted House Price |	Savings/(Overpayment) |
| -------------------                       | --------------------| ----------------------| ----------------------|
|3_Rooms(moon) 1479 sqft                  |250000	              |165949	                |($84,051.00)           |
|<mark>4_Rooms(hudgins) 1238 sqft </mark>	|<mark>97000 </mark>  |<mark>161532 </mark>   |<mark>	$64,532.00 </mark> |
|5_Rooms(newptcomfort) 2840 sqft          |229000               |	278262                |	$49,262.00             | 
|7_Rooms(church) 3680 sqft	              |399000               |	356330	              |($42,670.00)           |
|6_Rooms(mobjack) 3524 sq ft              |	289000	            |334650	                |$45,650.00             |
|7_Rooms(mathews) 3051 sqft               |	347500              |	314983	              |($32,517.00             | 


This time using square footage and the total number of rooms instead of just bedrooms, the predicted house prices are different but the results are virtually the same. 









