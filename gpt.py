from transformers import pipeline, Conversation
import os

def get_conv(model = "conversational"):
    return pipeline(model)

def predict_conv(conv_pipeline, conv):
    return conv_pipeline(conv)

def create_conv(msg:str, conv=None):
    if conv:
        conv.add_user_input(msg)
        return conv
    return Conversation(msg)

def main():
    print("Downloading the model")
    conv_pipeline = get_conv()
    print("Downloading complete")
    msg = input("Start a conv: ")
    conv = create_conv(msg)
    out = predict_conv(conv_pipeline, conv)
    exit = False
    while not exit:
        os.system('cls')
        print(out)
        msg = input('--> ')
        conv = create_conv(msg, conv)
        out = predict_conv(conv_pipeline, conv)

if __name__ == "__main__":
    main()


    