from src.CreateModel import ModelProvider

short_sentence="In 3 bullet points with each bullet point as a separate line and each bullet point has 20 words only, answer the following question: "

def UserInput():
    user_question = input("Please enter your question: ")
    return ModelProvider.generate(short_sentence + user_question)



if __name__ == "__main__":
    UserInput()

