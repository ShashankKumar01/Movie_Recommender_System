# Abstract
Built a movie recommender system using a content-based filtering approach: used a dataset of 5000 movies with information about genres, actors, directors, and plot summaries; preprocessed the data by converting text data into numerical vectors; calculated similarity between movies based on their vector representations; recommended movies to users based on similarity to movies they have previously watched or liked.

# Description
I developed a movie recommender system using a content-based filtering approach. I started with a dataset of 5,000 movies, which included information about genres, actors, directors, and plot summaries. To prepare the data for analysis, I preprocessed the text data by applying techniques such as tokenization, stopword removal, and stemming using the NLTK PorterStemmer.

Next, I converted the preprocessed text data into numerical vectors using a CountVectorizer from the scikit-learn library. This allowed me to represent each movie as a high-dimensional vector, where each dimension corresponded to a unique word or feature in the dataset.

To calculate the similarity between movies, I employed the cosine similarity metric from the scikit-learn library's pairwise module. Cosine similarity measures the cosine of the angle between two vectors, providing a numerical value that represents the degree of similarity between them. By computing the cosine similarity between the vector representations of all movie pairs, I was able to establish a similarity matrix that captured the relationships between the movies in the dataset.

Finally, to recommend movies to users, I utilized the similarity matrix to identify movies that were most similar to the ones the user had previously watched or liked. This allowed me to provide personalized movie recommendations based on the user's preferences and viewing history.

The combination of text preprocessing, vector representation, and cosine similarity calculations enabled me to build an effective content-based movie recommender system that could suggest relevant and meaningful movie options to users.
