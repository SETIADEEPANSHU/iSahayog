from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
def categorizeProb(text):
	X_train = np.array(['smog','air pollution','smoke','fog','air quality','burning fuel','burning','burn','polluted air','automobiles','dust','ash',
		'fumes','water pollution','polluted water','polluted lake','polluted river','river','lake','acid rain','noise','sound','heavy traffic','volumes',
		'noise pollution','water harvesting','water management','rain water management','rain water harvesting','water crisis','save water','drought',
		'soil fertility','soil','soil pH','plant nutrients','soil erosion','soil degardation','soil depletion'])
	y_train_text =[['air pollution'],['air pollution'],['air pollution'],['air pollution'],['air pollution'],
	['air pollution'],['air pollution'],['air pollution'],['air pollution'],['air pollution'],['air pollution'],['air pollution'],['air pollution'],
	['water pollution'],['water pollution'],['water pollution'],['water pollution'],['water pollution'],['water pollution'],['water pollution'],['noise pollution'],['air pollution','noise pollution'],['noise pollution'],['noise pollution'],['noise pollution'],['water harvesting'],['water harvesting'],['water harvesting'],['water harvesting'],['water harvesting'],['water harvesting'],['water harvesting'],['soil fertility'],['soil fertility'],['soil fertility'],['soil fertility'],['soilfertility'],['soil fertility'],['soil fertility']]
	X_test = np.array([text])
	np.char.lower(X_test)
	target_names = ['air pollution','water pollution','water harvesting','soil fertility']
	mlb = MultiLabelBinarizer()
	Y = mlb.fit_transform(y_train_text)
	classifier = Pipeline([
    	('vectorizer', CountVectorizer()),
    	('tfidf', TfidfTransformer()),
    	('clf',OneVsRestClassifier(LinearSVC()))])

	classifier.fit(X_train, Y)
	predicted = classifier.predict(X_test)
	all_labels = mlb.inverse_transform(predicted)

	for item, labels in zip(X_test, all_labels):
		lss=[labels[i] for i in range(0,len(labels))]
        return lss
