#install.packages("kernlab")
#install.packages("caret")

library("kernlab")
library("caret")
# spam email library from kernlab
data(spam)
# partition or split the data into training anf testing at 75% and 25%
inTrain <- createDataPartition(y=spam$type,p=0.75,list = FALSE)
#training data 75%
training <- spam[inTrain,]
#testing data 25%
testing <- spam[-inTrain,]
#dimensions of training data
dim(training)

#set seed 
set.seed(32223)

#fit the model, use all the columns of the data represented by type ~., data = training, method to be used glm
modelFit <- train(type ~.,data = training, method="glm")
modelFit$finalModel
#predict the testing data using training model
predictions <- predict(modelFit, newdata = testing)
predictions
# confusion matrix gives the matrix data about predicted and actual data
confusionMatrix(predictions, testing$type)
